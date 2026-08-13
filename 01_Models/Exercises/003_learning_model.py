# Learning model with gradient descent and learning rate and using mean from NumPy
import numpy as np

# initialize weight, input, and actual output
w = 8
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
learning_rate = 0.01

# make a prediction
prediction = x * w

# calculate the error and loss
error = prediction - y
loss = error ** 2

# Mean of squared loss
mean_loss = np.mean(loss)

# update the weight by increment or decrement using gradient descent
while mean_loss > 0.01:  # continue until the error is small enough
    # Calculate the gradient (derivative of loss with respect to weight)
    gradient = 2 * np.mean(error * x)
    
    # Update the weight using the learning rate and gradient
    w -= learning_rate * gradient
    
    # Recalculate the prediction, error, and loss
    prediction = x * w
    error = prediction - y
    loss = error ** 2
    mean_loss = np.mean(loss)

    # print every few iterations weight and mean loss for debugging
    if int(w * 1000) % 5000 == 0:
        print(f"Current Weight: {w}, Mean Loss: {mean_loss}")

print(f"Final Prediction: {prediction}")
print(f"Final Weight: {w}")
