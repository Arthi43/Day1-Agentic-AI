# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

The chosen private-data scenario is a Student Assignment Tracker. The private data contains assignment names, subjects, due dates, and completion status. The example user request is: "What are my pending assignments?"

## 2. Explanation of Each Approach

### Plain Chatbot

The plain chatbot sends the user's question directly to an LLM. It does not access the student's private assignment data and does not use any external tool. When asked about pending assignments, the chatbot explains that it cannot access the student's personal assignment list. This shows that an LLM alone does not automatically have access to private data.

### Rule-Based Workflow

The rule-based workflow does not use an LLM. It reads the private assignment data from the JSON file and follows predefined conditions. When the user asks about pending assignments, the workflow checks each assignment and displays the assignments whose status is "pending". This approach is predictable and reliable for tasks that have clearly defined rules.

### AI Agent

The AI agent combines an LLM, a tool, and a loop. The LLM receives the user's request and decides that it needs the assignment-reading tool. The tool reads the private assignment data from the JSON file and returns the result to the LLM. The agent then uses the tool result to generate the final response. This approach can handle tasks that require reasoning and tool usage.

## 3. Comparison Table

| Basis | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | High for natural-language responses | Limited by predefined rules | High because the LLM can decide actions |
| Decision-making | Generates a response | Uses fixed conditions | LLM decides when to use a tool |
| Tool usage | No tool | No LLM tool | Uses assignment-reading tool |
| Private-data access | No | Yes, directly from JSON | Yes, through the tool |
| Multi-step task handling | Limited | Fixed steps | Can perform tool-based steps |
| Automation | Limited | High for predefined tasks | High for dynamic tasks |
| Reliability | Depends on LLM response | Predictable for defined rules | Depends on LLM reasoning and tool execution |

## 4. Suitability Analysis

The plain chatbot is useful when the task mainly requires a natural-language response from an LLM and private data is not required. The rule-based workflow is useful when the required conditions and processing steps are already known. The AI agent is useful when the task requires an LLM to reason about a request, use a tool to access private data, observe the tool result, and produce a final response.

For the Student Assignment Tracker, each approach demonstrates a different way of solving the same type of request. The chatbot does not have access to the private assignment data, the workflow directly processes the data using fixed rules, and the agent uses an LLM together with a tool to access and process the data.

## 5. Conclusion

A plain chatbot is appropriate for tasks that mainly require LLM-based responses. A rule-based workflow is appropriate when the steps and conditions are known in advance. An AI agent is appropriate when a task requires an LLM, tools, reasoning, and multiple steps. The three approaches demonstrate different levels of data access, decision-making, tool usage, and automation.