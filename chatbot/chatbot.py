print("Student Assignment Chatbot")

question = input("Ask your question: ")

if "pending" in question.lower():
    print("Your pending assignments are:")
    print("1. DSA Lab - Data Structures - Due: 2026-09-25")
    print("2. AI Report - Artificial Intelligence - Due: 2026-09-28")
else:
    print("I can help with your assignments.")