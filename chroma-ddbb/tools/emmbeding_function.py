import google.generativeai as genai

EMBED_MODEL = "models/embedding-001"


# Configurar API Key de Gemini
genai.configure(api_key="AIzaSyD7vtxHQQyNrE1E3aCMeeC32BADpnogE0E")

# ====================================
# FUNCIÓN PARA GENERAR EMBEDDINGS
# ====================================
def embed_text(text: str) -> list[float]:
    """Genera embedding con Gemini (modelo embedding-001)."""
    result = genai.embed_content(
        model=EMBED_MODEL,
        content=text
    )
    return result["embedding"]