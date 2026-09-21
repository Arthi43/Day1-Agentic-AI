import json

with open("student_data.json", "r") as file:
    assignments = json.load(file)

print("Student Assignment Workflow")

question = input("Ask your question: ")

if "pending" in question.lower():
    print("Your pending assignments are:")

    for item in assignments:
        if item["status"] == "pending":
            print(
                item["assignment"],
                "-",
                item["subject"],
                "- Due:",
                item["due_date"]
            )
else:
    print("Sorry, this workflow only handles pending assignments.")