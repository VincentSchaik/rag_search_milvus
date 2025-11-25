"""
Milvus Lite Text Search Demo

This demo shows how to use Milvus Lite for semantic text search.
Milvus Lite is a lightweight version of Milvus that runs locally without
requiring a separate server.
"""

import os
# Disable TensorFlow to avoid compatibility issues
os.environ['USE_TF'] = '0'

from pymilvus import MilvusClient
from sentence_transformers import SentenceTransformer

# Initialize the embedding model
print("Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize Milvus Lite client (stores data in local file)
print("Initializing Milvus Lite...")
client = MilvusClient("milvus_demo.db")

# Collection name
COLLECTION_NAME = "text_search_demo"

# Sample documents to search through
documents = [
    "Artificial intelligence is transforming the technology industry.",
    "Machine learning models require large amounts of training data.",
    "Vector databases enable efficient similarity search at scale.",
    "Natural language processing helps computers understand human language.",
    "Deep learning has revolutionized computer vision applications.",
    "Cloud computing provides scalable infrastructure for applications.",
    "Cybersecurity is crucial for protecting digital assets.",
    "Quantum computing promises to solve complex computational problems.",
]

def create_collection():
    """Create a collection for storing text embeddings."""
    print(f"\nCreating collection '{COLLECTION_NAME}'...")
    
    # Drop collection if it already exists
    if client.has_collection(COLLECTION_NAME):
        client.drop_collection(COLLECTION_NAME)
    
    # Create collection with vector dimension matching our embedding model (384 dimensions)
    client.create_collection(
        collection_name=COLLECTION_NAME,
        dimension=384,  # all-MiniLM-L6-v2 produces 384-dimensional embeddings
    )
    print("Collection created successfully!")

def insert_documents():
    """Insert sample documents with their embeddings."""
    print("\nGenerating embeddings for documents...")
    
    # Generate embeddings for all documents
    embeddings = model.encode(documents)
    
    # Prepare data for insertion
    data = [
        {
            "id": i,
            "vector": embeddings[i].tolist(),
            "text": documents[i]
        }
        for i in range(len(documents))
    ]
    
    print(f"Inserting {len(documents)} documents into collection...")
    client.insert(collection_name=COLLECTION_NAME, data=data)
    print("Documents inserted successfully!")

def search_similar_texts(query_text, top_k=3):
    """Search for documents similar to the query text."""
    print(f"\nSearching for: '{query_text}'")
    
    # Generate embedding for query
    query_embedding = model.encode([query_text])[0].tolist()
    
    # Perform similarity search
    results = client.search(
        collection_name=COLLECTION_NAME,
        data=[query_embedding],
        limit=top_k,
        output_fields=["text"]
    )
    
    print(f"\nTop {top_k} similar documents:")
    for i, hit in enumerate(results[0], 1):
        print(f"{i}. [Distance: {hit['distance']:.4f}] {hit['entity']['text']}")
    
    return results

def main():
    """Main demo function."""
    print("=" * 70)
    print("Milvus Lite Text Search Demo")
    print("=" * 70)
    
    # Step 1: Create collection
    create_collection()
    
    # Step 2: Insert documents
    insert_documents()
    
    # Step 3: Perform example searches
    print("\n" + "=" * 70)
    print("Example Searches")
    print("=" * 70)
    
    # Example search 1
    search_similar_texts("AI and machine learning technologies", top_k=3)
    
    # Example search 2
    search_similar_texts("database for vector similarity", top_k=3)
    
    # Example search 3
    search_similar_texts("understanding human text", top_k=3)
    
    print("\n" + "=" * 70)
    print("Demo completed successfully!")
    print("=" * 70)

if __name__ == "__main__":
    main()
