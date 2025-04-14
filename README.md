Here’s a clean and professional `README.md` file for your GitHub repository:

---

# 📄 Lightweight RAG PDF QA with Ollama & Gradio

This project is a lightweight, RAM-efficient **PDF-based Question Answering (QA)** application. It uses the **LangChain** ecosystem to build a Retrieval-Augmented Generation (RAG) pipeline powered by a **quantized Ollama-compatible model** and **FAISS** for vector search.

> ✅ Designed for small documents and low-resource machines.

---

## 🚀 Features

- 🔍 Load and chunk a small PDF (1–5 pages recommended)
- 💡 Embed using **MiniLM** (`sentence-transformers/all-MiniLM-L6-v2`)
- 🧠 Vector search with **FAISS**
- 🤖 LLM-powered answers using quantized `Gemma 3B` (via Ollama)
- 🧑‍💻 User-friendly **Gradio** chat interface

---

## 📦 Requirements

- Python 3.9+
- [Ollama](https://ollama.com/) installed and running
- `data/small_doc.pdf` file (sample input document)

### Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```txt
gradio
langchain
langchain-community
sentence-transformers
faiss-cpu
```

---

## 🛠️ Usage

1. **Ensure Ollama is running.**  
   You can pull and serve the model first:
   ```bash
   ollama pull hf.co/unsloth/gemma-3-1b-it-GGUF:Q5_K_M
   ```

2. **Place a small PDF file** in the `data/` folder. Rename it as `small_doc.pdf` or change the filename in the script.

3. **Run the app**:
   ```bash
   python app.py
   ```

4. **Chat with your PDF!** 🎉  
   A browser window will open with the Gradio chat interface.

---

## 🧠 How It Works

1. **Load & Chunk**: The PDF is split into small chunks (256 characters) with a bit of overlap.
2. **Embed & Index**: Each chunk is converted to a vector using MiniLM, stored using FAISS.
3. **Retrieve & Generate**: Top 2 relevant chunks are retrieved and fed to the LLM (Gemma 3B via Ollama).
4. **Chat**: Responses are generated based on context, displayed via Gradio.

---

## 📁 Project Structure

```
├── data/
│   └── small_doc.pdf         # Your input PDF file
├── vector_store/             # Auto-generated FAISS index
├── app.py                    # Main script
├── requirements.txt
└── README.md
```

---

## 🤖 Model Info

- Model: [`Gemma 3B Instruct`](https://huggingface.co/unsloth/gemma-3-1b-it-GGUF)
- Format: GGUF (Q5_K_M quantization)
- Hosted via [Ollama](https://ollama.com)

---

## ⚠️ Notes

- Best used for small documents due to memory limits.
- Embeddings are saved locally and reused on next run.
- You can replace the PDF or switch to a different LLM or embedding model with minimal changes.

---

## 📌 To-Do

- [ ] Add support for larger PDFs (pagination or streaming)
- [ ] Enable file upload via Gradio
- [ ] Dockerize the app

---

## 📝 License

MIT License

---

Let me know if you want a version with file upload or multi-PDF support added!
