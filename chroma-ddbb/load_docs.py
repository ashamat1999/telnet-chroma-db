import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders.parsers import TesseractBlobParser
from uuid import uuid4

from tools.emmbeding_function import embed_text

# ==========================================
# CONFIG: CHROMA
# ==========================================
CHROMA_HOST = "localhost"
CHROMA_PORT = 9000
COLLECTION_NAME = "docs_telnet"

client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={"description": "Documentos internos TELNET (3 páginas por PDF)"}
)

# ==========================================
# CONFIG: RUTA DEL PDF
# ==========================================
PDF_PATH = "./docs/manual_pdv.pdf"

# ==========================================
# LOADER DEL PDF (CON OCR)
# ==========================================
loader = PyPDFLoader(
    PDF_PATH,
    mode="page",
    images_inner_format="html-img",
    images_parser=TesseractBlobParser(),
)

docs = loader.load()

print(f"📄 Páginas cargadas: {len(docs)}")

# ==========================================
# PROCESAR SOLO LAS PRIMERAS 3 PÁGINAS
# ==========================================
PAGES_TO_LOAD = 3
docs_subset = docs[:PAGES_TO_LOAD]

print(f"🔍 Cargando {PAGES_TO_LOAD} páginas a Chroma…")

for i, doc in enumerate(docs_subset):
    page_text = doc.page_content.strip()

    # Evitar páginas vacías
    if not page_text:
        print(f"⚠️ Página {i} vacía, se omite.")
        continue

    # Crear embedding
    emb = embed_text(page_text)

    # Insertar en Chroma
    collection.add(
        ids=[str(uuid4())],
        documents=[page_text],
        embeddings=[emb],
        metadatas=[{"source": PDF_PATH, "page": i}]
    )

    print(f"✅ Página {i} cargada correctamente.")


print("\n🎉 Listo: primeros 3 documentos cargados a Chroma.")