# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

The chosen private-data scenario is a Student Assignment Tracker. The private data contains assignment names, subjects, due dates, and completion status. The example user request is: "What are my pending assignments?"

## 2. Explanation of Each Approach

### Plain Chatbot

The plain chatbot mainly uses an LLM to provide a response to the user's request. It does not use a separate tool or a predefined workflow. In this scenario, the chatbot responds to the user's question about pending assignments. Its main limitation is that its access to the private assignment data depends on what information is provided to it. It is mainly suitable for generating responses rather than performing a sequence of tool-based actions.

### Rule-Based Workflow

The rule-based workflow follows predefined steps and conditions and does not involve an LLM. In this scenario, the workflow reads the student assignment data and checks the status of each assignment. If the status is "pending", the assignment is displayed to the user. This approach is predictable because the conditions are predefined, but it is less flexible when the user's request changes or becomes more complex.

### AI Agent

The AI agent combines an LLM, tools, and a loop. It can reason about the task, select and use a tool, observe the result, and continue actions until the task is completed. In this scenario, the agent selects the assignment-reading tool, obtains the private assignment data, identifies the pending assignments, and provides the result to the user. This makes the approach suitable for tasks that require multiple steps and tool usage.

## 3. Comparison Table

| Basis | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | Higher for natural-language responses | Limited by predefined rules | Higher because it can reason and select actions |
| Decision-making | Mainly response generation | Predefined conditions | Can reason and select tools |
| Tool usage | No separate tool | Uses predefined processing steps | Uses tools as required |
| Private-data access | Depends on available information | Can directly process the stored data | Can access private data through tools |
| Multi-step task handling | Limited | Fixed sequence of steps | Can continue through multiple steps |
| Automation | Limited | High for predefined tasks | High for dynamic tasks |
| Reliability | Depends on the response | Predictable for defined conditions | Depends on reasoning and tool execution |

## 4. Suitability Analysis

For the Student Assignment Tracker scenario, the three approaches demonstrate different ways of handling the same request. The plain chatbot is useful for providing a simple response. The rule-based workflow is useful when the required steps and conditions are already known. The AI agent is suitable when the task requires reasoning, tool selection, private-data access, and multiple steps. Therefore, the suitability depends on the requirements of the task and the amount of flexibility and automation needed.

## 5. Conclusion

A plain chatbot is appropriate for tasks mainly requiring responses from an LLM. A rule-based workflow is appropriate when the steps and conditions are known in advance and predictable execution is required. An AI agent is appropriate for tasks that require an LLM together with tools, reasoning, observation, and multiple actions. The comparison shows that the three approaches solve problems differently, and the appropriate approach depends on the type and complexity of the problem.