import sys
import os
import json
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from config import GROQ_API_KEY, MODEL

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


# Tool
def read_assignments():
    with open("student_data.json", "r") as file:
        return json.load(file)


tools = [
    {
        "type": "function",
        "function": {
            "name": "read_assignments",
            "description": "Read the student's private assignment data.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]


messages = [
    {
        "role": "system",
        "content": "You are a student assignment assistant. Use the read_assignments tool when the user asks about their assignments."
    }
]

question = input("Ask the AI Agent: ")
messages.append({"role": "user", "content": question})


# Agent loop
while True:

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if not message.tool_calls:
        print("\nAI Agent response:")
        print(message.content)
        break

    messages.append(message)

    for tool_call in message.tool_calls:

        if tool_call.function.name == "read_assignments":

            assignments = read_assignments()

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(assignments)
            })