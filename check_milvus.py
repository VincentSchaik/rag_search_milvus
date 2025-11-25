"""
Simple script to check if Milvus Lite is installed and working.
"""

print("Checking Milvus Lite installation...\n")

# Check 1: Import pymilvus
try:
    from pymilvus import MilvusClient
    print("✓ pymilvus is installed")
except ImportError as e:
    print(f"✗ pymilvus import failed: {e}")
    exit(1)

# Check 2: Create a local file-based client
try:
    client = MilvusClient("./test_milvus.db")
    print("✓ MilvusClient created successfully (using local file)")
except Exception as e:
    print(f"✗ Failed to create MilvusClient: {e}")
    exit(1)

# Check 3: Create a test collection
try:
    collection_name = "test_collection"
    
    # Drop if exists
    if client.has_collection(collection_name):
        client.drop_collection(collection_name)
    
    # Create collection
    client.create_collection(
        collection_name=collection_name,
        dimension=128,
    )
    print(f"✓ Created test collection '{collection_name}'")
except Exception as e:
    print(f"✗ Failed to create collection: {e}")
    exit(1)

# Check 4: Insert test data
try:
    test_data = [
        {"id": 0, "vector": [0.1] * 128, "text": "test document 1"},
        {"id": 1, "vector": [0.2] * 128, "text": "test document 2"},
    ]
    client.insert(collection_name=collection_name, data=test_data)
    print(f"✓ Inserted {len(test_data)} test documents")
except Exception as e:
    print(f"✗ Failed to insert data: {e}")
    exit(1)

# Check 5: Perform a search
try:
    results = client.search(
        collection_name=collection_name,
        data=[[0.15] * 128],
        limit=2,
        output_fields=["text"]
    )
    print(f"✓ Search completed successfully, found {len(results[0])} results")
except Exception as e:
    print(f"✗ Search failed: {e}")
    exit(1)

# Cleanup
try:
    client.drop_collection(collection_name)
    print(f"✓ Cleaned up test collection")
except Exception as e:
    print(f"⚠ Cleanup warning: {e}")

print("\n" + "="*50)
print("✅ Milvus Lite is installed and working correctly!")
print("="*50)
