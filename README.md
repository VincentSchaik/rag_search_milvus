# Milvus Lite Text Search Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app.streamlit.app)

A simple demonstration of using Milvus Lite for semantic text search with vector embeddings.

## 🎮 Live Demo

**Try it now:** [Launch Web App →](https://your-app.streamlit.app)

Or run locally:
```bash
# Clone the repository
git clone https://github.com/VincentSchaik/rag_search_milvus.git
cd yrag_search_milvus

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

1. Clone or download this project

2. Install dependencies:
```bash
pip install -r requirements.txt
```

This will install:
- `pymilvus` - Milvus Python SDK with Milvus Lite support
- `sentence-transformers` - For generating text embeddings
- `numpy` - Numerical computing library
- `streamlit` - Web application framework

## Usage

### Option 1: Web App (Interactive)

Run the Streamlit web application:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

Features:
- 🔍 Interactive search interface
- 📊 Visual similarity scores
- 🎯 Example query buttons
- 📚 Document browser

### Option 2: Command Line Demo

Run the demo script:

```bash
python text_search_demo.py
```

The script will:
1. Load a pre-trained embedding model (all-MiniLM-L6-v2)
2. Create a collection in Milvus Lite
3. Insert sample documents about technology topics
4. Perform three example similarity searches
5. Display the top matching documents for each query

## Example Output

```
Loading embedding model...
Initializing Milvus Lite...

Creating collection 'text_search_demo'...
Collection created successfully!

Inserting 8 documents into collection...
Documents inserted successfully!

Searching for: 'AI and machine learning technologies'

Top 3 similar documents:
1. [Distance: 0.4521] Artificial intelligence is transforming the technology industry.
2. [Distance: 0.5123] Machine learning models require large amounts of training data.
3. [Distance: 0.6234] Deep learning has revolutionized computer vision applications.
```

## How It Works

1. **Embedding Model**: The demo uses the `all-MiniLM-L6-v2` model from sentence-transformers, which converts text into 384-dimensional vectors.

2. **Milvus Lite**: Stores vectors in a local database file (`milvus_demo.db`) and provides efficient similarity search.

3. **Similarity Search**: When you search, your query is converted to a vector, and Milvus finds the most similar document vectors using distance metrics.

## Deployment

### Deploy to Streamlit Community Cloud (Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Click "Deploy"

Your app will be live at `https://your-app.streamlit.app`

### Other Deployment Options

- **Hugging Face Spaces**: Great for ML demos
- **Railway**: $5/month hobby plan
- **Render**: Free tier available
- **Docker**: Use the included Dockerfile (coming soon)

## Customization

You can modify the demo to:
- Add your own documents (edit the `documents` list)
- Try different search queries
- Adjust the number of results (`top_k` parameter)
- Use different embedding models
- Change the collection name

## Project Structure

```
milvus-lite-demo/
├── app.py                  # Streamlit web application
├── text_search_demo.py     # Command-line demo
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
├── .streamlit/
│   └── config.toml        # Streamlit configuration
└── .github/
    ├── copilot-instructions.md
    └── workflows/
        └── streamlit.yml  # CI/CD pipeline
```

## Learn More

This is a basic example. For more advanced use cases, check out:

- [Milvus Documentation](https://milvus.io/docs) - Complete Milvus guide
- [Milvus Lite Examples](https://github.com/milvus-io/milvus-lite) - More demo applications
- [RAG with Milvus](https://milvus.io/docs/integrate_with_langchain.md) - Build retrieval-augmented generation systems
- [LangChain Integration](https://python.langchain.com/docs/integrations/vectorstores/milvus) - Use Milvus with LangChain
- [LlamaIndex Integration](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/) - Use Milvus with LlamaIndex
- [Image Search Example](https://github.com/milvus-io/bootcamp) - Build image similarity search

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is open source and available under the MIT License.

## Support

- GitHub Issues: [Report a bug](https://github.com/yourusername/your-repo-name/issues)
- Milvus Community: [Join Discord](https://discord.gg/milvus)
- Documentation: [Milvus Docs](https://milvus.io/docs)
