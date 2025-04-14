import gradio as gr
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS  # LangChain's FAISS wrapper
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

# 1. Load and Process Documents (small chunks)
def load_and_chunk_documents(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=256,  # Smaller chunks → fewer vectors
        chunk_overlap=30
    )
    return text_splitter.split_documents(documents)

# 2. Initialize Embeddings with LIGHTWEIGHT model
def setup_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"  # 80MB model
    )
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local("vector_store")
    return vector_store

# 3. Load Quantized Ollama Model (RAM-friendly)
def load_llm():
    return Ollama(
        model="hf.co/unsloth/gemma-3-1b-it-GGUF:Q5_K_M", 
        temperature=0.3,
        system="Answer concisely using retrieved context."
    )

# 4. Build RAG Pipeline
def create_rag_pipeline(vector_store, llm):
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 2})  # Only 2 chunks
    )

# 5. Gradio Interface
def respond(query, history):
    result = rag_pipeline.invoke({"query": query})
    return result["result"]

if __name__ == "__main__":
    # Use a SMALL PDF to start (e.g., 1-5 pages)
    chunks = load_and_chunk_documents("data/small_doc.pdf")
    vector_store = setup_vector_store(chunks)
    llm = load_llm()
    rag_pipeline = create_rag_pipeline(vector_store, llm)
    gr.ChatInterface(respond).launch()
