import chromadb
from tools.emmbeding_function import embed_text

# ============================
# CONFIG
# ============================
CHROMA_HOST = "localhost"
CHROMA_PORT = 9000
COLLECTION_NAME = "docs_telnet"

# Conexión con Chroma
chroma_client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
print(f"Conectado a Chroma (heartbeat): {chroma_client.heartbeat()}")

# Obtener colección existente
collection = chroma_client.get_collection(name=COLLECTION_NAME)
print(f"📚 Colecciones disponibles: {[c.name for c in chroma_client.list_collections()]}")

# ============================
# QUERY DE PRUEBA
# ============================
query = "Cómo inicio el sistema?"
query_embedding = embed_text(query)

rsp = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

print(rsp)