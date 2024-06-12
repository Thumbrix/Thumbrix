import os
from crewai import Agent, Task, Crew, Process
os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-70b-8192'  # Adjust based on available model
os.environ["OPENAI_API_KEY"] ='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'

def Thumbrix_AI(message):
    Thumbrix_Agent = Agent(
        role="Thumbrix_Agent",
        goal=f"to promote in short messege a design company called Thumbrix that sells: thumbnails, animations, logos, profile pictures(pfp), banners' video editing etc",
        backstory="you need to promote in short a messege for a design company called Thumbrix, Thumbrix may be a small company but it has a great crew and amazing sales, Thumbrix makes mostly Gorilla Tag designs. You Can Buy Our Products From Our Shop In Discord!. Try to make the messege very short and catchy",
        verbose=True,
        allow_delegation=False,
    )


    THUMBRIX_ANSWER2 = Task(
        description=f"Promote a design company called Thumbrix that sells: thumbnails, animations, logos, etc",
        input_type=str,
        agent=Thumbrix_Agent,
        expected_output=f"ANSWER to the question: {message}",
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