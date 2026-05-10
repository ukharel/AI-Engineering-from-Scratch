x = 2.0
w1 = 0.5
w2 = 0.8
target = 10.0

# 1. Forward Pass
hidden = x * w1       # 1.0
prediction = hidden * w2 # 0.8
loss = (prediction - target)**2 # (-9.2)^2 = 84.64

# 2. Backpropagation (The Chain Rule)
# We want to know: How does w1 affect the Loss?

# a. How did the 'Prediction' affect the Loss? (Outer derivative)
d_loss_d_pred = 2 * (prediction - target) # -18.4

# b. How did 'w2' affect the prediction? 
d_pred_d_w2 = hidden # 1.0

# c. How did 'hidden' affect the prediction?
d_pred_d_hidden = w2 # 0.8

# d. How did 'w1' affect 'hidden'?
d_hidden_d_w1 = x # 2.0

# --- THE GRADIENTS ---
gradient_w2 = d_loss_d_pred * d_pred_d_w2 
# "Blame" for w2 = (Error) * (Input to w2)

gradient_w1 = d_loss_d_pred * d_pred_d_hidden * d_hidden_d_w1
# "Blame" for w1 = (Error) * (Path through w2) * (Input to w1)

print(f"Gradient for w2: {gradient_w2}")
print(f"Gradient for w1: {gradient_w1}")