from textwrap import dedent
from crewai import Agent
from crewai_tools import PDFSearchTool

class PresentationGeneratorAgents:

  def document_review_agent(self, llm, pdf_rag_search_tool):
    return Agent(
        role="Lead Research Analyst",
        goal=dedent("""\
        Thoroughly read the PDF to understand its content and main messages and highlight the key topics of the document.
        """),
        backstory="As a Lead Research Analyst in a premier content developmment firm, you excel at dissecting the data into key insights.",
        tools=[pdf_rag_search_tool],
        llm=llm,
        verbose=True
    )

  def content_extraction_task_and_summarization_agent(self, llm, pdf_rag_search_tool):
    return Agent(
        role="Technical Writer",
        goal=dedent("""\
        Given a list of topics, summarize the information in the document for each topic."""),
        backstory="As a Technical Writer, you excel at gathering the most important information, context, and the gist of large amounts of data and summarize it into bullet points for quick consumption.",
        tools=[pdf_rag_search_tool],
        llm=llm,
        verbose=True
    )

  def slide_design_agent(self, llm):
    return Agent(
        role="Lead Content Creator",
        goal=dedent("""\
        Create compelling and accurate content for a presentation."""),
        backstory="As a lead content creator, you excel at creating compelling content for general audience consumption.",
        tools=[],
        llm=llm,
        verbose=True
    )
  
  def manager(self):
        return Agent(
            role="Project Manager",
            goal="Efficiently manage the crew and ensure high-quality task completion",
            backstory="You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
            allow_delegation=True
        )