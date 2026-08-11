# A tiny "model"

w = 8
x = 2
actual = 4

prediction = x * w
error = prediction - actual

absolute_loss = abs(error)
squared_loss = error ** 2

print(f"Prediction: {prediction}")
print(f"Error: {error}")
print(f"Absolute Loss: {absolute_loss}")
print(f"Squared Loss: {squared_loss}")