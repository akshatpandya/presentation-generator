from textwrap import dedent
from crewai import Agent, Crew
from agents import PresentationGeneratorAgents
from tasks import PresentationGeneratorTasks

tasks = PresentationGeneratorTasks()
agents = PresentationGeneratorAgents()

# Create agents
document_review_agent = agents.document_review_agent()
# outline_agent = agents.outline_agent()
content_extraction_task_and_summarization_agent = agents.content_extraction_task_and_summarization_agent()
slide_design_agent = agents.slide_design_agent()

# Create tasks
document_review_task = tasks.document_review_task(document_review_agent, "document.pdf")
# outline_task = tasks.outline_task(outline_agent, "document.pdf")
content_extraction_task_and_summarization_task = tasks.content_extraction_task_and_summarization(content_extraction_task_and_summarization_agent, "document.pdf")
slide_design_task = tasks.slide_design_task(slide_design_agent, "document.pdf")

# Create Crew
crew = Crew(
    agents=[
        document_review_agent,
        # outline_agent,
        content_extraction_task_and_summarization_agent,
        slide_design_agent
    ],
    tasks=[
        document_review_task,
        # outline_task,
        content_extraction_task_and_summarization_task,
        slide_design_task
    ],
    verbose=True
)

slide_design_result = crew.kickoff()

print(slide_design_result.raw)