print("Day 6 - RAG Chatbot Started")

# We will use your own journey data
with open("README.md", "r", encoding="utf-8") as f:
    readme_text = f.read()

print(f"Loaded README: {len(readme_text)} characters")
print("This is our knowledge base for RAG")

# Save as knowledge base
with open("knowledge_base.txt", "w", encoding="utf-8") as f:
    f.write(readme_text)
    f.write("\n\nProjects:\n- Iris Flower Classifier 100% accuracy\n- Pandas Analysis\n- SQL Analysis")

print("✅ knowledge_base.txt created - Ready for embeddings tomorrow!")