from crewai import Task
from textwrap import dedent

class PresentationGeneratorTasks:
  def content_extraction_task(self, content_extractor_agent):
      return Task(
          description=dedent("""
            Extract the text content from the PDF document.
          """),
          expected_output="All the text from the PDF document.",
          agent=content_extractor_agent
      )
  
  def content_summarization_task(self, content_summarizer_agent, summarize_content_tool, context):
      return Task(
          description=dedent("""
            Summarize the extracted content into presentation-ready key points.                  
          """),
          expected_output="A summary of the extracted content in presentation-ready key points",
          agent=content_summarizer_agent,
          context=context,
          tools=[summarize_content_tool]
      )
  
  def slide_creator_task(self, slide_creator_agent, context):
      return Task(
          description=dedent("""
            Create structured presentation slides from the summarized content.
            
            The output should be in the following format:
            Slide 1: <content>
            Slide 2: <content> 
            Slide 3: <content>  
            ...              
          """),
          expected_output="Structured presentation slides in the given output format.",
          agent=slide_creator_agent,
          context=context
      )
    