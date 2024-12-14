from crewai import Task
from textwrap import dedent

class PresentationGeneratorTasks:
  def document_review_task(self, agent, document):
    return Task(description=dedent(f"""\
      PDF to read: {document}.

      Create a list of 5 most important topics in the document.
      """),
      expected_output = "A list of 5 most important topics in the document arranged in  bullet points.",
      agent=agent
    )

  def content_extraction_task_and_summarization(self, agent, document):
    return Task(description=dedent(f"""\
    PDF to read: {document}.

    Task: Given a list of main topics in the document, summarize each topic using the information given in the document.
    
    Your output should be in the following format:
    <Topic 1>
    <Summary>

    <Topic 2>
    <Summary>
    
    ...
    """),
    expected_output = "Summarize each topic from the input list of topics using the information in the document.",
    agent=agent
  )

  def slide_design_task(self, agent, document):
    return Task(description=dedent(f"""\
    PDF to read: {document}.

    Organize the content into a 8 slide presentation.

    The presentation structure should be as following:
    Slide 1: Title Slide (Title, Subtitle, Your Name, Date)
    Slide 2: Introduction/Agenda (Overview of what will be covered)
    Slides 3-7: Summaries of the main topics. One slide per topic.
    Slide 8: Thank you slide.

    The output should have the following template:

    Slide 1:
    <Heading>
    <Content>

    Slide 2:
    <Heading>
    <Content>

    ...

    Slide 8:
    <Heading>
    <Content>
    """),
    expected_output = "Organize the content into 8 slides, following the specified template.",
    agent=agent)