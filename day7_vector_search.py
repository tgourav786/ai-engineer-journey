from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Day 7 - Vector Search for RAG")

# Load your knowledge base
with open("knowledge_base.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split into chunks (how real RAG does it)
chunks = text.split("\n")
chunks = [c for c in chunks if len(c) > 20] # remove small lines

print(f"Created {len(chunks)} chunks from knowledge base")

# Create vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(chunks)

# Ask a question
question = "What ML project did I build?"
q_vector = vectorizer.transform([question])

# Find best chunk
scores = cosine_similarity(q_vector, vectors)[0]
best_idx = scores.argmax()

print(f"\nQuestion: {question}")
print(f"Best Answer Chunk: {chunks[best_idx]}")
print(f"Similarity Score: {scores[best_idx]:.2f}")
print("\n✅ Day 7 done - Your AI can now SEARCH your data!")