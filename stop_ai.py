import os
from crewai import Agent, Task, Crew, Process
os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-70b-8192'  # Adjust based on available model
os.environ["OPENAI_API_KEY"] ='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'

def Thumbrix_AI(message):
    Thumbrix = "Thumbrix is company that sells: thumbnails, animations, logos, profile pictures(pfp), banners' video editing etc"
    Thumbrix_Agent = Agent(
        role="Thumbrix_Agent",
        goal=f"check if the message: {message} is a question or about Thumbrix",
        backstory=f"you make sure that the messages that are sent are valid questions or about the company called Thumbrix: {Thumbrix}",
        verbose=True,
        allow_delegation=False,
    )


    THUMBRIX_ANSWER2 = Task(
        description=f"check if the message: {message} is a question or about Thumbrix",
        input_type=str,
        agent=Thumbrix_Agent,
        expected_output=f"true or false",
        verbose=True,
    )
    crew = Crew(
        agents=[Thumbrix_Agent],
        tasks=[THUMBRIX_ANSWER2],
        verbose=2,
        process=Process.sequential
    )

    output = crew.kickoff()
    return output