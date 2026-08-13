# A tiny "model"

w = 8
x = 2
actual = 4

prediction = x * w
loss = prediction - actual

absolute_loss = abs(loss)
squared_loss = loss ** 2

print(f"Prediction: {prediction}")
print(f"Loss: {loss}")
print(f"Absolute Loss: {absolute_loss}")
print(f"Squared Loss: {squared_loss}")