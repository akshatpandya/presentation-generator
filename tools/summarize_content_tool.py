from typing import Type, List, Any
from crewai_tools import BaseTool
from pydantic import BaseModel, Field
from langchain_core.documents import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI

class SummarizeContentToolInput(BaseModel):
    documents: List[Document] = Field(..., description="List of documents to summarize using LangChain")
    llm: Any = Field(..., description="LLM model object")

class SummarizeContentTool(BaseTool):
    name: str = "SummarizeContentTool"
    description: str = "A tool that takes a list of documents and summarizes then using LangChain"
    args_schema: Type[BaseModel] = SummarizeContentToolInput

    def _run(documents):
        llm = OpenAI(temperature=0.5)
        chain = load_summarize_chain(llm, chain_type="map_reduce")
        summary = chain.run(documents)
        return summary