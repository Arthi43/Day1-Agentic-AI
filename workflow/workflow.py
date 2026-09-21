import json

with open("student_data.json", "r") as file:
    assignments = json.load(file)

print("Student Assignment Workflow")

question = input("Ask your question: ")

if "pending" in question.lower():
    print("\nYour pending assignments:")

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
    print("\nSorry, this workflow only handles pending assignments.")