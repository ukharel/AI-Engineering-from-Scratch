import math

def get_magnitude(v):
    # L2 Norm: Root of the sum of squares
    return math.sqrt(sum(x**2 for x in v))

def normalize(v):
    mag = get_magnitude(v)
    if mag == 0: return v
    return [x / mag for x in v]

def euclidean_distance(v1, v2):
    # Distance is just the magnitude of the difference vector
    diff_vec = [x1 - x2 for x1, x2 in zip(v1, v2)]
    return get_magnitude(diff_vec)

# Example: AI Prediction vs. Reality
target_truth = [10, 0]    # The truth is strictly "Type A"
ai_prediction = [8, 2]    # AI thinks it's mostly "Type A" but a bit of "Type B"

print(f"Prediction Strength (Magnitude): {get_magnitude(ai_prediction):.2f}")
print(f"Prediction 'Flavor' (Unit Vector): {normalize(ai_prediction)}")
print(f"How 'Wrong' is the AI (Distance): {euclidean_distance(ai_prediction, target_truth):.2f}")