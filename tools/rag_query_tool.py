from typing import Type
from crewai_tools import BaseTool
from pydantic import BaseModel, Field
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

class RAGQueryToolInput(BaseModel):
    query: str = Field(..., description="Query to search in the document")

class RAGQueryTool(BaseTool):
    name: str = "RAGQueryTool"
    description: str = (
        "A tool that answers a query by searching through a document using LlamaIndex's RAG pipeline. Input must be a dictionary with a single key 'query' where the value is a string. Example: {'query': 'Main points in the document'}."
    )
    args_schema: Type[BaseModel] = RAGQueryToolInput


    def __init__(self, llm, document_path: str):
        """
        Initialize the tool with a document path.

        :llm the LLM to use for querying the document
        :param document_path: Path to the document (e.g., .txt, .pdf, etc.).
        """

        super().__init__()
        object.__setattr__(self, "document_path", document_path)
        object.__setattr__(self, "llm", llm)
        object.__setattr__(self, "index", None)

        # Set up the RAG pipeline
        self._initialize_index()

    def _initialize_index(self):
        """
        Initializes the LlamaIndex RAG pipeline by loading the document and creating an index.
        """
        print("Building the index...")
        # Load the document and build the index
        documents = SimpleDirectoryReader(input_files=[self.document_path]).load_data()
        object.__setattr__(self, "index", VectorStoreIndex.from_documents(documents))

    def _run(self, query: str) -> str:
        """
        Run the tool to answer a query using the RAG pipeline.

        :param query: The input query to search the document.
        :return: The generated answer.
        """
        if not self.index:
            raise ValueError("Index has not been initialized.")

        print(f"Running query: {query}")
        query_engine = self.index.as_query_engine(llm=self.llm, response_mode='tree_summarize')
        response = query_engine.query(query)
        return response.response
        