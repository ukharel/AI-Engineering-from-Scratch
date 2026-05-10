# Input from previous step
layer_output = [5.2, -2.1, 0.0, 4.8]

def relu(vector):
    # This is the "Non-Linear" magic
    # It kills all negative signals
    return [max(0, x) for x in vector]

activated_output = relu(layer_output)

print(f"Before Activation (Linear): {layer_output}")
print(f"After Activation (Non-Linear): {activated_output}")
# Output: [5.2, 0, 0, 4.8]