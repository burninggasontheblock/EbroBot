# EbroBot: Your Intelligent LLM Chatbot

## Overview
EbroBot is a powerful, interactive chatbot application built using state-of-the-art language models. It incorporates the capabilities of OpenAI's GPT-4o-mini and Chroma vector database to deliver context-aware, high-quality responses while leveraging uploaded documents as a knowledge base. The project is designed to simplify human-computer interaction through natural language processing and knowledge retrieval.

---

## Project Structure

### 1. `chatbot.py`
This script serves as the main entry point for the chatbot interface. It:
- Configures and initializes the chatbot's language model (`ChatOpenAI`) and vector database (`Chroma`).
- Sets up file upload functionality to extend the chatbot's knowledge base dynamically.
- Implements a Gradio-based user interface for seamless interaction.

### 2. `ingest_database.py`
This script prepares the knowledge base by:
- Loading documents (e.g., PDFs) from the `data` directory.
- Splitting the documents into manageable chunks for efficient processing.
- Embedding the chunks using `OpenAIEmbeddings` and storing them in the Chroma vector database.

---

## Features

### 1. Chatbot with Enhanced Retrieval
- **Streamed Responses:** Generates partial answers while processing longer queries for a real-time experience.
- **Context-Aware Conversations:** Leverages conversation history to provide coherent responses.
- **Knowledge-Driven Answers:** Responds based solely on the knowledge provided by the uploaded documents.

### 2. File Upload
- Users can upload text-based files to dynamically enhance the chatbot's knowledge base.
- Documents are processed, embedded, and stored in the vector database for retrieval.

### 3. Document Ingestion
- Handles large datasets with efficient chunking and embedding strategies.
- Ensures persistence of the vector database for continuous use.

---

## Prerequisites

### 1. Environment Setup
- Python 3.8+
- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

### 2. API Keys
- Ensure that the OpenAI API key is set up in a `.env` file:
  ```
  OPENAI_API_KEY=your_openai_api_key
  ```

---

## Usage

### 1. Ingest Documents
To process and store documents in the vector database:
```bash
python ingest_database.py
```

### 2. Launch the Chatbot
Start the Gradio-based chatbot interface:
```bash
python chatbot.py
```

The chatbot will be accessible at the URL provided by Gradio (e.g., `http://127.0.0.1:****`).

---

## Directory Structure
```plaintext
.
├── data/                  # Directory for documents to be ingested
├── chroma_db/             # Persistent Chroma vector database
├── chatbot.py             # Main chatbot script
├── ingest_database.py     # Script to ingest documents
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
```

---

## Dependencies
- [LangChain](https://github.com/hwchase17/langchain)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Gradio](https://gradio.app/)
- [Chroma](https://github.com/chroma-core/chroma)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

---

## Future Enhancements
- Support for additional file formats (e.g., Word, CSV).
- Advanced conversational memory to handle complex dialogs.
- Deployment on cloud platforms for scalability.

---

## Contributing
Contributions are welcome! Please follow the standard GitHub workflow:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- OpenAI for providing the language model API.
- LangChain for the robust integration framework.
- The open-source community for their contributions.

