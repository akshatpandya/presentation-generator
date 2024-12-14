import os
from textwrap import dedent
from crewai import Agent
from langchain_openai import OpenAI
from crewai_tools import PDFSearchTool
from google.colab import userdata

class PresentationGeneratorAgents:
  def __init__(self):
    self.llm = OpenAI(temperature=0.1, openai_api_key=os.getenv("OPENAI_API_KEY"))
    os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
    os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o'

    self.pdf_rag_search_tool = PDFSearchTool()

  def document_review_agent(self):
    return Agent(
        role="Lead Research Analyst",
        goal=dedent("""\
        Thoroughly read the PDF to understand its content and main messages and highlight the key sections of the document.
        """),
        backstory="As a Lead Research Analyst in a premier content developmment firm, you excel at dissecting the data into key insights.",
        tools=[self.pdf_rag_search_tool],
        llm=self.llm,
        verbose=True
    )

  def outline_agent(self):
    return Agent(
        role="Lead Communication Strategist",
        goal=dedent("""\
        Using the key sections in a document, create an outline for a presentation. Outline must include what topics each slide would contain."""),
        backstory="As a Lead Communication Strategist, you excel at presenting information to an audience in a concise yet well-rounded and easy to understand way.",
        tools=[self.pdf_rag_search_tool],
        llm=self.llm,
        verbose=True
    )

  def content_extraction_task_and_summarization_agent(self):
    return Agent(
        role="Lead Data Analyst",
        goal=dedent("""\
        Extract key information, statistics, quotes, and data from the document and summarize lengthy sections into concise bullet points or short paragraphs"""),
        backstory="As a Lead Data Analyst, you excel at gathering the most important information, context, and the gist of large amounts of data and summarize it into bullet points for quick consumption.",
        tools=[self.pdf_rag_search_tool],
        llm=self.llm,
        verbose=True
    )

  def slide_design_agent(self):
    return Agent(
        role="Lead Content Creator",
        goal=dedent("""\
        Create compelling and accurate content for a presentation."""),
        backstory="As a lead content creator, you excel at creating compelling content for general audience consumption.",
        tools=[self.pdf_rag_search_tool],
        llm=self.llm,
        verbose=True
    )