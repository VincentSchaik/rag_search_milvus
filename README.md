# Milvus Lite Text Search Demo

A simple demonstration of using Milvus Lite for semantic text search with vector embeddings.

## What is Milvus Lite?

Milvus Lite is a lightweight version of Milvus that runs locally without requiring a separate server. It's perfect for:
- Prototyping and development
- Small-scale applications
- Learning vector databases
- Running on edge devices

## Features Demonstrated

This demo shows how to:
- ✅ Initialize Milvus Lite client
- ✅ Create a collection for storing text embeddings
- ✅ Generate embeddings using sentence-transformers
- ✅ Insert documents with their vector embeddings
- ✅ Perform semantic similarity search

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

## Usage

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

## Customization

You can modify the demo to:
- Add your own documents (edit the `documents` list)
- Try different search queries
- Adjust the number of results (`top_k` parameter)
- Use different embedding models
- Change the collection name

## Learn More

This is a basic example. For more advanced use cases, check out:

- **RAG (Retrieval-Augmented Generation)**: Build question-answering systems
- **Image Search**: Use Milvus Lite for image similarity search
- **LangChain Integration**: Combine with LangChain for AI applications
- **LlamaIndex Integration**: Build knowledge bases and search systems

Visit the [Milvus documentation](https://milvus.io/docs) for comprehensive guides and examples.

## Troubleshooting

**Import errors**: Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

**TensorFlow/Keras errors**: The demo automatically disables TensorFlow support by setting `os.environ['USE_TF'] = '0'` to avoid compatibility issues. If you still encounter errors, ensure you have compatible versions of transformers and sentence-transformers installed.

**Database file locked**: If you get a database lock error, make sure no other instance of the demo is running.

**Memory issues**: The first run will download the embedding model (~90MB). Ensure you have a stable internet connection.

## Clean Up

To remove the local database file:
```bash
rm milvus_demo.db
```

## License

This demo is provided as-is for educational purposes.
