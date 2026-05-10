# Our Input: [Sugar Content, Caffeine Content]
energy_drink = [0.8, 0.9]

# Our Matrix (The "Brain"): 
# Row 1: How much inputs contribute to "Health Risk"
# Row 2: How much inputs contribute to "Energy Boost"
weights = [
    [0.7, 0.6], # Weights for Health Risk
    [0.4, 0.9]  # Weights for Energy Boost
]

def layer_forward(input_vec, weight_matrix):
    output = []
    for row in weight_matrix:
        # Each row of the matrix dots with the input vector
        dot_result = sum(i * w for i, w in zip(input_vec, row))
        output.append(dot_result)
    return output

prediction = layer_forward(energy_drink, weights)

print(f"Input: {energy_drink}")
print(f"Output (Health Risk, Energy Boost): {prediction}")