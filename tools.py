from crewai_tools import LlamaIndexTool
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


class Tools:
    
    def __init__(self, user_input):
        self.user_input = user_input
    
    def rag_tool(self, llm):
        reader = SimpleDirectoryReader(input_files=[self.user_input])
        document = reader.load_data()
        index = VectorStoreIndex.from_documents(document, show_progress=True)
        query_engine = index.as_query_engine(similarity_top_k=5, llm=llm)
        query_tool = LlamaIndexTool.from_query_engine(
            query_engine,
            name="PDF Rag Tool",
            description="Use this tool to query the PDF."
        )
        return query_tool