"""
Streamlit web app for Milvus Lite text search demo
Run with: streamlit run app.py
"""

import os
os.environ['USE_TF'] = '0'

import streamlit as st
from pymilvus import MilvusClient
from sentence_transformers import SentenceTransformer

# Page config
st.set_page_config(
    page_title="Milvus Lite Text Search",
    page_icon="🔍",
    layout="wide"
)

# Initialize session state for query
if 'query' not in st.session_state:
    st.session_state.query = ""

# Initialize (with caching for performance)
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

@st.cache_resource
def init_milvus():
    client = MilvusClient("milvus_demo.db")
    return client

model = load_model()
client = init_milvus()

COLLECTION_NAME = "text_search_demo"

# Sample documents
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

def setup_collection():
    """Initialize collection with sample data"""
    if client.has_collection(COLLECTION_NAME):
        return True
    
    client.create_collection(
        collection_name=COLLECTION_NAME,
        dimension=384,
    )
    
    embeddings = model.encode(documents)
    data = [
        {"id": i, "vector": embeddings[i].tolist(), "text": documents[i]}
        for i in range(len(documents))
    ]
    client.insert(collection_name=COLLECTION_NAME, data=data)
    return True

def search_texts(query, top_k=5):
    """Search for similar documents"""
    query_embedding = model.encode([query])[0].tolist()
    results = client.search(
        collection_name=COLLECTION_NAME,
        data=[query_embedding],
        limit=top_k,
        output_fields=["text"]
    )
    return results[0]

# Main UI
st.title("🔍 Milvus Lite Text Search Demo")
st.markdown("### Semantic search powered by vector embeddings")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This demo showcases **Milvus Lite** for semantic text search.
    
    **How it works:**
    1. Documents are converted to vector embeddings
    2. Your query is also converted to a vector
    3. Milvus finds the most similar document vectors
    
    **Technology:**
    - Milvus Lite (vector database)
    - Sentence Transformers (embeddings)
    - Streamlit (web interface)
    """)
    
    st.divider()
    
    st.header("📚 Sample Documents")
    with st.expander("View all documents"):
        for i, doc in enumerate(documents, 1):
            st.markdown(f"{i}. {doc}")
    
    st.divider()
    
    top_k = st.slider("Number of results", 1, 8, 3)

# Initialize collection
with st.spinner("Initializing Milvus Lite..."):
    setup_collection()

# Search interface
st.markdown("---")

# Example queries - these buttons update session state and trigger rerun
st.markdown("**Try these examples:**")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🤖 AI & ML", use_container_width=True):
        st.session_state.query = "AI and machine learning technologies"
        st.rerun()
with col2:
    if st.button("💾 Databases", use_container_width=True):
        st.session_state.query = "database for vector similarity"
        st.rerun()
with col3:
    if st.button("💬 Language", use_container_width=True):
        st.session_state.query = "understanding human text"
        st.rerun()

# Search input - uses session state
query = st.text_input(
    "🔎 Enter your search query:",
    value=st.session_state.query,
    placeholder="e.g., AI and machine learning technologies",
    help="Type any text and find semantically similar documents"
)

# Update session state when text input changes
if query != st.session_state.query:
    st.session_state.query = query

# Perform search
if query:
    st.markdown("---")
    st.subheader("🎯 Search Results")
    
    with st.spinner("Searching..."):
        results = search_texts(query, top_k)
    
    if results:
        for i, hit in enumerate(results, 1):
            distance = hit['distance']
            text = hit['entity']['text']
            
            # Calculate similarity percentage (inverse of distance)
            similarity = max(0, (1 - distance) * 100)
            
            with st.container():
                col_rank, col_content = st.columns([0.5, 9.5])
                
                with col_rank:
                    st.markdown(f"### {i}")
                
                with col_content:
                    st.markdown(f"**{text}**")
                    st.progress(similarity / 100)
                    st.caption(f"Similarity: {similarity:.1f}% | Distance: {distance:.4f}")
                
                st.divider()
    else:
        st.warning("No results found.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with Milvus Lite 🚀 | <a href='https://milvus.io/docs'>Learn More</a></p>
</div>
""", unsafe_allow_html=True)