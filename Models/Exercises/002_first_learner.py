# A tiny "learning model"
w = 8
x = 2
actual = 4

# make a prediction
prediction = x * w
error = prediction - actual
loss = error ** 2

# update the weight by increment or decrement
while loss > 0.01:  # continue until the error is small enough
    if error > 0:
        w -= 0.001  # decrease weight if prediction is too high
    else:
        w += 0.001  # increase weight if prediction is too low
    # print every few thousand iterations weight and loss for debugging
    if int(w * 1000) % 5000 == 0:
        print(f"Current Weight: {w}, Loss: {loss}")
    # Recalculate the prediction and error
    prediction = x * w
    error = prediction - actual
    loss = error ** 2

print(f"Final Prediction: {prediction}")
print(f"Final Weight: {w}")