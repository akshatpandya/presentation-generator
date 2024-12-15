from textwrap import dedent
from crewai import Agent
from crewai_tools import PDFSearchTool

class PresentationGeneratorAgents:

  def content_extractor_agent(self, pdf_content_extractor_tool, pdf_path: str):
    return Agent(
      name="PDF Extractor",
      role=dedent(f"""\
          Extracts text content from PDF documents and prepares it for summarization. 
          Instruction: Use {pdf_path} as the input parameter for the tool.
      """),
      backstory="An expert in extracting all the text from PDF documents.",
      goal="Ensure all relevant text from the PDF is extracted.",
      tools=[pdf_content_extractor_tool],
      verbose=True
    )
  
  def content_summarizer_agent(self):
    return Agent(
      name="Content Summarizer",
      role="Summarizes the extracted content into concise, presentation-friendly points.",
      goal="Generate clean and structured summaries for each section of the PDF.",
      backstory="An expert in distilling lengthy documents into digestible key points.",
      tools=[],
      verbose=True
    )
  
  def slide_creator_agent(self):
    return Agent(
      name="Slide Creator",
      role="reates presentation slides from summarized content.",
      goal="Transform the summaries into structured presentation slides with headings and bullet points.",
      backstory="A master at designing well-organized presentation slides.",
      tools=[],
      verbose=True
    )
