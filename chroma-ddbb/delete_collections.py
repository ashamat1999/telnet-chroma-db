import chromadb

chroma_client = chromadb.HttpClient(host='localhost', port=9000)
chroma_client.heartbeat()

collections = chroma_client.list_collections()
# Iterate through the collections and delete each one
for collection in collections:
    print(f"Deleting collection: {collection.name}")
    chroma_client.delete_collection(collection.name)

print(chroma_client.list_collections(), '----')