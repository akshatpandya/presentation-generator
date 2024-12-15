import os
from textwrap import dedent
from crewai import Crew, Process
from agents import PresentationGeneratorAgents
from tasks import PresentationGeneratorTasks
from tools.pdf_content_extractor_tool import PDFContentExtractorTool
from tools.summarize_content_tool import SummarizeContentTool
from langchain_openai import OpenAI

llm = OpenAI(temperature=0.1, openai_api_key=os.getenv("OPENAI_API_KEY"))
pdf_path = "/home/akshat/presentation-generator/document.pdf"

tasks = PresentationGeneratorTasks()
agents = PresentationGeneratorAgents()

# Tools
pdf_content_extractor_tool = PDFContentExtractorTool()
summarize_content_tool = SummarizeContentTool()

# Create agents
content_extractor_agent = agents.content_extractor_agent(pdf_content_extractor_tool, str(pdf_path))
content_summarizer_agent = agents.content_summarizer_agent()
slide_creator_agent = agents.slide_creator_agent()

# Create tasks
content_extraction_task = tasks.content_extraction_task(content_extractor_agent)
content_summarization_task = tasks.content_summarization_task(content_summarizer_agent, summarize_content_tool, [content_extraction_task])
slide_creator_task = tasks.slide_creator_task(slide_creator_agent, [content_summarization_task])

# Create Crew
crew = Crew(
    agents=[
        content_extractor_agent,
        content_summarizer_agent,
        slide_creator_agent,
    ],
    tasks=[
        content_extraction_task,
        content_summarization_task,
        slide_creator_task
    ],
    process=Process.sequential,
    verbose=True
)

slide_design_result = crew.kickoff()

print(slide_design_result.raw)

# print("Task output")
# print(slide_design_result.tasks[0].raw)