# Day 1 - Agentic AI

## Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

### Scenario

This project demonstrates three approaches for handling a **Student Assignment Tracker** scenario.

The private data contains:

- Assignment name
- Subject
- Due date
- Assignment status

Example user request:

> What are my pending assignments?

---

## 1. Plain Chatbot

The plain chatbot sends the user's question directly to an LLM.

It does not have access to the student's private assignment data and does not use any separate tool.

---

## 2. Rule-Based Workflow

The rule-based workflow uses predefined Python conditions.

It reads the private assignment data from `student_data.json` and checks the status of each assignment.

If an assignment has the status `pending`, it is displayed to the user.

---

## 3. AI Agent

The AI agent combines:

**LLM + Tool + Loop**

The agent receives the user's request and decides when to use the `read_assignments` tool.

The tool reads the private assignment data from `student_data.json`.

The result is then returned to the LLM, which generates the final response.

---

## Project Structure

```text
DAY1 Agentic AI
│
├── Output
│   ├── chatbot_output.png
│   ├── workflow_output.png
│   └── agent_output.png
│
├── chatbot
│   └── chatbot.py
│
├── workflow
│   └── workflow.py
│
├── agent
│   └── agent.py
│
├── analysis.md
├── student_data.json
├── config.py
├── check_setup.py
├── requirements.txt
├── .gitignore
└── README.md
Technologies Used
Python
OpenAI-compatible API
Groq
LLM
Tool Calling
JSON
python-dotenv
Output

The Output folder contains screenshots showing the three systems running on the same Student Assignment Tracker scenario.

Plain Chatbot

The chatbot receives the user's question directly and does not have access to the private assignment data.

Rule-Based Workflow

The workflow reads the private assignment data and uses predefined rules to identify pending assignments.

AI Agent

The agent uses the LLM together with the read_assignments tool to access the private assignment data and generate the response.

Analysis

A detailed comparison of the plain chatbot, rule-based workflow, and AI agent is available in analysis.md.

The analysis covers:

Flexibility
Decision-making
Tool usage
Private-data access
Multi-step task handling
Automation
Reliability
Suitability of each approach
Purpose

The purpose of this project is to understand the difference between a plain chatbot, a rule-based workflow, and an AI agent that can use tools to access private data.
