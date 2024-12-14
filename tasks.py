from crewai import Task
from textwrap import dedent

class PresentationGeneratorTasks:
  def document_review_task(self, agent, document):
    return Task(description=dedent(f"""\
      PDF to read: {document}.

      Thoroughly read the PDF to understand its content and main messages.
      Note important sections, headings, and subheadings that could be relevant for creating a presentation.

      You final report should crealy articulate the key sections of the document.
      Keep in mind, that these sections should give a holistic view of the information in the document to an audience viewing the presentation.
      """),
      expected_output = "A list of key sections in the document.",
      agent=agent
    )

  def outline_task(self, agent, document):
    return Task(description=dedent(f"""\
      PDF to read: {document}.

      Determine the Structure: Decide on the structure of the presentation. Typically, a presentation includes:
      - Title Slide
      - Introduction
      - Main Points (usually 3-5 main points)
      - Conclusion
      - Q&A or Contact Information
      Draft a Slide Outline: Based on the content of the PDF, outline what each slide will cover. The outline should be for 10 slides.
      """),
      expected_output = "A 10 slide presentation outline with topics for each slide.",
      agent=agent
    )

  def content_extraction_task_and_summarization(self, agent, document):
    return Task(description=dedent(f"""\
    PDF to read: {document}.

    Select Key Points: Extract key information, statistics, quotes, and data from the PDF that will be useful for each slide.
    Summarize Content: Summarize lengthy sections into concise bullet points or short paragraphs.
    """),
    expected_output = "Key information, statistics, quotes, and data extracted from the PDF, summarized into concise points.",
    agent=agent
  )

  def slide_design_task(self, agent, document):
    return Task(description=dedent(f"""\
    PDF to read: {document}.

    Create 10 slides for the presentation and design the content for each of them.

    The presentation structure should be as following:
    Slide 1: Title Slide (Title, Subtitle, Your Name, Date)
    Slide 2: Introduction/Agenda (Overview of what will be covered)
    Slides 3-9: Main Points (Each slide covers a specific key point or section from the PDF)
    Slide 10: Q&A/Contact Information (Provide details for further inquiries or discussion)

    The output should have the following template:

    Slide 1:
    <Heading>
    <Content>

    Slide 2:
    <Heading>
    <Content>

    ...

    Slide 10:
    <Heading>
    <Content>
    """),
    expected_output = "Content for 10 presentation slides, following the specified template.",
    agent=agent)