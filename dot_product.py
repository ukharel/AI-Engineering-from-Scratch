# Our "Space": [Sweetness, Crunchiness]
concept_apple = [8, 9]
concept_lemon = [1, 2]

# The User asks for something "Sweet and Crunchy"
user_query = [9, 8]

def dot_product(v1, v2):
    # This measures how much two vectors "align"
    return sum(x * y for x, y in zip(v1, v2))

# Calculate alignment
alignment_with_apple = dot_product(user_query, concept_apple)
alignment_with_lemon = dot_product(user_query, concept_lemon)

print(f"Alignment with Apple: {alignment_with_apple}") # 72 + 72 = 144
print(f"Alignment with Lemon: {alignment_with_lemon}") # 9 + 16 = 25

if alignment_with_apple > alignment_with_lemon:
    print("The AI thinks you want an Apple!")