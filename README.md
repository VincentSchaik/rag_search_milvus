# Milvus Lite Text Search Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rag-search-milvus-vincentschaik.streamlit.app/)

A simple demonstration of using Milvus Lite for semantic text search with vector embeddings.

## Live Demo

**Try it now:** [Launch Web App →](https://rag-search-milvus-vincentschaik.streamlit.app/)

Or run locally:
```bash
# Clone the repository
git clone https://github.com/VincentSchaik/rag_search_milvus.git
cd rag_search_milvus

# Install dependencies
pip install -r requirements.txt

# Run the web app
streamlit run app.py

# OR run the command-line demo
python text_search_demo.py
```

## What is Milvus Lite?

Milvus Lite is a lightweight version of Milvus that runs locally without requiring a separate server. It's perfect for:
- Prototyping and development
- Small-scale applications
- Learning vector databases
- Running on edge devices

## Features Demonstrated

This demo shows how to:
- Initialize Milvus Lite client
- Create a collection for storing text embeddings
- Generate embeddings using sentence-transformers
- Insert documents with their vector embeddings
- Perform semantic similarity search

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation

Install dependencies:
```bash
pip install -r requirements.txt
```

This will install:
- `pymilvus` - Milvus Python SDK with Milvus Lite support
- `milvus-lite` - Milvus Lite runtime
- `sentence-transformers` - For generating text embeddings
- `numpy` - Numerical computing library
- `streamlit` - Web application framework
- `transformers` - Transformer models support
- `torch` - PyTorch deep learning framework

## Usage

### Option 1: Web App (Interactive)

Run the Streamlit web application:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

Features:
- Interactive search interface
- Visual similarity scores with progress bars
- Example query buttons
- Document browser in sidebar
- Adjustable number of results

### Option 2: Command Line Demo

Run the demo script:

```bash
python text_search_demo.py
```

The script will:
1. Load a pre-trained embedding model (all-MiniLM-L6-v2)
2. Create a collection in Milvus Lite
3. Insert 8 sample documents about technology topics
4. Perform three example similarity searches
5. Display the top matching documents for each query

## Example Output

```
======================================================================
Milvus Lite Text Search Demo
======================================================================
Loading embedding model...
Initializing Milvus Lite...

Creating collection 'text_search_demo'...
Collection created successfully!

Inserting 8 documents into collection...
Documents inserted successfully!

======================================================================
Example Searches
======================================================================

Searching for: 'AI and machine learning technologies'

Top 3 similar documents:
1. [Distance: 0.4521] Artificial intelligence is transforming the technology industry.
2. [Distance: 0.5123] Machine learning models require large amounts of training data.
3. [Distance: 0.6234] Deep learning has revolutionized computer vision applications.

Searching for: 'database for vector similarity'

Top 3 similar documents:
1. [Distance: 0.3891] Vector databases enable efficient similarity search at scale.
2. [Distance: 0.5234] Cloud computing provides scalable infrastructure for applications.
3. [Distance: 0.6123] Machine learning models require large amounts of training data.

Searching for: 'understanding human text'

Top 3 similar documents:
1. [Distance: 0.4012] Natural language processing helps computers understand human language.
2. [Distance: 0.5789] Artificial intelligence is transforming the technology industry.
3. [Distance: 0.6234] Deep learning has revolutionized computer vision applications.

======================================================================
Demo completed successfully!
======================================================================
```

## How It Works

1. **Embedding Model**: The demo uses the `all-MiniLM-L6-v2` model from sentence-transformers, which converts text into 384-dimensional vectors.

2. **Milvus Lite**: Stores vectors in a local database file (`milvus_demo.db`) and provides efficient similarity search using cosine distance.

3. **Similarity Search**: When you search, your query is converted to a vector, and Milvus finds the most similar document vectors using distance metrics (lower distance = higher similarity).

## Deployment

### Deploy to Streamlit Community Cloud (Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository
6. Main file path: `app.py`
7. Click "Deploy"

Your app will be live at `https://your-app-name.streamlit.app`

**Note:** Streamlit Cloud automatically installs dependencies from `requirements.txt` and creates a fresh Milvus database on each deployment.

## Customization

You can modify the demo to:
- **Add your own documents**: Edit the `documents` list in `app.py` or `text_search_demo.py`
- **Try different search queries**: Type any text in the search box
- **Adjust the number of results**: Use the slider in the sidebar (1-8 results)
- **Use different embedding models**: Change `'all-MiniLM-L6-v2'` to another sentence-transformers model
- **Change the collection name**: Modify `COLLECTION_NAME` variable

## Project Structure

```
rag_search_milvus/
├── app.py                      # Streamlit web application
├── text_search_demo.py         # Command-line demo
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── .gitignore                  # Git ignore rules (excludes .db files)
└── .github/
    ├── copilot-instructions.md # GitHub Copilot workspace context
    └── workflows/
        └── streamlit.yml       # CI/CD pipeline (optional)
```

**Note:** Files like `milvus_demo.db`, `milvus_demo.db.lock`, and virtual environments are excluded via `.gitignore`.

## Learn More

This is a basic example. For more advanced use cases, check out:

- [Milvus Documentation](https://milvus.io/docs) - Complete Milvus guide
- [Milvus Lite GitHub](https://github.com/milvus-io/milvus-lite) - Source code and examples
- [RAG with Milvus](https://milvus.io/docs/integrate_with_langchain.md) - Build retrieval-augmented generation systems
- [LangChain Integration](https://python.langchain.com/docs/integrations/vectorstores/milvus) - Use Milvus with LangChain
- [LlamaIndex Integration](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/) - Use Milvus with LlamaIndex
- [Milvus Bootcamp](https://github.com/milvus-io/bootcamp) - More comprehensive examples including RAG and image search

## Contributing

Contributions are welcome! Feel free to:
- Report bugs via [GitHub Issues](https://github.com/VincentSchaik/rag_search_milvus/issues)
- Suggest new features
- Submit pull requests
- Improve documentation

## Support

- **Milvus Documentation**: [docs.milvus.io](https://milvus.io/docs)
- **Milvus Community**: [Discord](https://discord.gg/milvus)

## License

This project is open source and available under the MIT License.
