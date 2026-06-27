Chapter 2 – Software Design Before AI
Why do we design before coding?
Large software projects become difficult to maintain if developers start coding without a clear plan.
Designing first helps us:
•	Understand the problem. 
•	Divide the project into modules. 
•	Reduce future bugs. 
•	Improve scalability. 
•	Make the project easier to maintain. 
 
Functional Requirements
Functional requirements describe what the system should do.
Examples:
•	User login 
•	Explain AI concepts 
•	Generate quizzes 
•	Track learning progress 
 
Non-Functional Requirements
Non-functional requirements describe how well the system should work.
Examples:
•	Performance 
•	Security 
•	Reliability 
•	Scalability 
•	Maintainability 
•	Usability 
 
Interview Question
Q: What is the difference between Functional and Non-Functional Requirements?
Answer:
Functional requirements define the features or functions of the system.
Non-functional requirements define quality attributes such as performance, security, and scalability.






 
AI Notes 


Now let's answer a fundamental question:
What is an AI System?
Many people think:
User
   ↓
ChatGPT
   ↓
Answer
That's not how production AI systems work.
A real AI system looks more like this:
             User
               │
               ▼
        Application/UI
               │
               ▼
      AI Orchestrator
               │
      ┌────────┼────────┐
      ▼        ▼        ▼
   LLM      Database   Memory
      │        │        │
      └────────┼────────┘
               ▼
            Response
This is a key insight:
The LLM is just one component of the system.
The application is responsible for deciding:
•	What to ask the LLM. 
•	What data to retrieve. 
•	What context to include. 
•	How to format the response. 
This is why AI engineering is much more than calling an API.
 

