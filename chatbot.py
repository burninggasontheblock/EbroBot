from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
import gradio as gr
from dotenv import load_dotenv
import os

load_dotenv()

# Configuration
DATA_PATH = r"data"
CHROMA_PATH = r"chroma_db"

embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")

# Initiate the model
llm = ChatOpenAI(temperature=0.5, model='gpt-4o-mini')

# Connect to the chromadb
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH,
)

# Set up the vectorstore to be the retriever
num_results = 5
retriever = vector_store.as_retriever(search_kwargs={'k': num_results})

# Function to handle file uploads
def upload_file(filepath):
    if not os.path.exists(filepath):
        return "File not found!"
    
    with open(filepath, "r") as f:
        content = f.read()

    # Add content to the vector store
    vector_store.add_texts([content])
    vector_store.persist()
    return f"File '{os.path.basename(filepath)}' uploaded and processed successfully."

# Function to handle chatbot responses
def stream_response(message, history):
    docs = retriever.invoke(message)
    knowledge = ""
    for doc in docs:
        knowledge += doc.page_content + "\n\n"

    rag_prompt = f"""
    You are an assistant that answers questions based on provided knowledge.
    Use only the information in "The knowledge" section to respond.
    Do not mention the knowledge source to the user.

    The question: {message}

    Conversation history: {history}

    The knowledge: {knowledge}
    """

    partial_message = ""
    for response in llm.stream(rag_prompt):
        partial_message += response.content
        yield partial_message

# Set up the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# EbroBot! the LLM Chatbot")
    with gr.Row():
        chatbot = gr.ChatInterface(
            stream_response,
            textbox=gr.Textbox(
                placeholder="Send to the EnroBot LLM...",
                container=False,
                autoscroll=True,
                scale=7
            )
        )
        uploader = gr.File(label="Upload File", type="filepath", interactive=True)

    uploader.upload(upload_file, uploader, gr.Textbox(lines=2))

# Launch the Gradio app
demo.launch(share=True)
