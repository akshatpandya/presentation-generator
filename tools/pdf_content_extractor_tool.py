from typing import Type, List
from crewai_tools import BaseTool
from pydantic import BaseModel, Field
from langchain.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

class PDFContentExtractorToolInput(BaseModel):
    document_path: str = Field(..., description="Path to the PDF document.")

class PDFContentExtractorTool(BaseTool):
    name: str = "PDFContentExtractorTool"
    description: str = "A tool that takes a PDF document as an input and extracts all the text from it."
    args_schema: Type[BaseModel] = PDFContentExtractorToolInput

    def _run(self, document_path: str) -> List[Document]:
        loader = PyPDFLoader(document_path)
        pages = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.split_documents(pages)
        return docs
    