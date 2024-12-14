import os
from textwrap import dedent
from crewai import Crew, Process
from agents import PresentationGeneratorAgents
from tasks import PresentationGeneratorTasks
from tools import Tools
from langchain_openai import OpenAI

llm = OpenAI(temperature=0.1, openai_api_key=os.getenv("OPENAI_API_KEY"))

tasks = PresentationGeneratorTasks()
agents = PresentationGeneratorAgents()
tools = Tools("/home/akshat/presentation-generator/document.pdf")

# Tools
pdf_rag_tool = tools.rag_tool(llm)

# Create agents
document_review_agent = agents.document_review_agent(llm, pdf_rag_tool)
content_extraction_task_and_summarization_agent = agents.content_extraction_task_and_summarization_agent(llm, pdf_rag_tool)
slide_design_agent = agents.slide_design_agent(llm)
manager_agent = agents.manager()

# Create tasks
document_review_task = tasks.document_review_task(document_review_agent, "document.pdf")
content_extraction_task_and_summarization_task = tasks.content_extraction_task_and_summarization(content_extraction_task_and_summarization_agent, "document.pdf")
slide_design_task = tasks.slide_design_task(slide_design_agent, "document.pdf")

# Create Crew
crew = Crew(
    agents=[
        document_review_agent,
        content_extraction_task_and_summarization_agent,
        slide_design_agent
    ],
    tasks=[
        document_review_task,
        content_extraction_task_and_summarization_task,
        slide_design_task
    ],
    manager_agent=manager_agent,
    process=Process.hierarchical,
    verbose=True
)

slide_design_result = crew.kickoff()

print(slide_design_result.raw)