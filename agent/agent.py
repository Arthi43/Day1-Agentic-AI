import json

def read_assignments():
    with open("student_data.json", "r") as file:
        return json.load(file)


def agent(question):
    print("AI Agent")

    # Tool selection
    if "pending" in question.lower():
        print("Agent selected tool: read_assignments")

        # Tool execution
        assignments = read_assignments()

        # Observe result
        pending = []

        for item in assignments:
            if item["status"] == "pending":
                pending.append(item)

        # Final response
        print("Your pending assignments are:")

        for item in pending:
            print(
                item["assignment"],
                "-",
                item["subject"],
                "- Due:",
                item["due_date"]
            )
    else:
        print("Agent could not identify the required task.")


question = input("Ask the agent: ")
agent(question)