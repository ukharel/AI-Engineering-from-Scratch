import math

# Concept A: "Technology"
tech_vec = [0.9, 0.1, 0.0] 
# Concept B: "Innovation" (Very related to Tech)
inn_vec = [0.8, 0.2, 0.1]
# Concept C: "Banana" (Unrelated)
fruit_vec = [0.0, 0.1, 0.9]

def cosine_similarity(v1, v2):
    dot = sum(a*b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a**2 for a in v1))
    mag2 = math.sqrt(sum(b**2 for b in v2))
    return dot / (mag1 * mag2)

print(f"Similarity (Tech vs Innovation): {cosine_similarity(tech_vec, inn_vec):.4f}")
print(f"Similarity (Tech vs Fruit): {cosine_similarity(tech_vec, fruit_vec):.4f}")