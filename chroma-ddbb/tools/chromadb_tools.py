import os


# ==============================
# SIMPLE CHUNKER
# ==============================
def chunk_text(text, chunk_size=500, overlap=50):
    """Divide un texto en chunks con solapamiento."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# ==============================
# LOAD TXT FILES
# ==============================
def load_txt_files(folder):
    docs = []
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
                docs.append((filename, text))
    return docs


