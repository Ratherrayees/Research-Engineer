# Gradient Descent

## What it is
Gradient descent is the process of repeatedly adjusting a model’s parameters in the direction that reduces the loss, with the goal of finding parameter values that minimize it.
## Why it exists
Gradient descent exists to give a model an efficient method for improving its parameters. Instead of randomly changing parameters or testing every possible value, it uses the gradient to determine which direction should reduce the loss, then repeatedly updates the parameters toward lower loss.
## How it works
Gradient descent works by determining how the loss changes when a parameter changes. The gradient tells us the direction and strength of that relationship, and then the parameter is updated in the direction that reduces the loss.
## Mental model
 Think of the model’s parameters as its current position in a landscape where height represents loss. The gradient tells us which direction goes uphill fastest, so gradient descent moves in the opposite direction, toward lower loss. The learning rate controls how large each step is.
## Important terms
- **Parameter** — a value the model can change during learning, such as a weight or bias.
- **Loss** — a measure of how wrong the model’s prediction is.
- **Gradient** — tells how the loss changes with respect to a parameter; its sign gives direction and its magnitude gives strength.
- **Learning rate** — controls how large each parameter update is.
- **Update step** — the actual change applied to a parameter.
- **Minimum** — a point where the loss is lower than the surrounding values.
## How it connects to other concepts
**Gradient descent sits at the center of model learning.** The loss function tells us what needs to be minimized. Derivatives tell us how the loss changes when parameters change. Those derivatives form the gradient. The learning rate determines how much of that gradient is used for each update. In neural networks, backpropagation efficiently calculates these gradients across many layers so gradient descent can update the model’s weights and biases.
## Implementation understanding
 I started with an initial weight of 8 and a set of input values. I set the learning rate to 0.01. On the first prediction, the model calculated the error, squared loss, and mean loss. The mean loss showed how wrong the model was overall and was also used to decide whether training should continue. The gradient was then calculated to determine how the weight should change in order to reduce the loss. The weight was adjusted according to the gradient and learning rate. After updating the weight, the model recalculated the predictions, errors, and loss, and repeated this process until the mean loss became small enough. For debugging, I printed some iterations and finally printed the final predictions and learned weight.
## What confused me
- I was also initially confused about how the gradient can tell us which direction to move without manually trying different weight values.At first I confused the role of mean loss with the role of the gradient. I thought mean loss helped decide whether the weight should increase or decrease. I later understood that mean loss only tells me how wrong the model is overall, while the gradient tells me how changing the weight affects the loss and therefore which direction the weight should move.

## Questions
- How is the gradient actually calculated mathematically?
- Why does the derivative give us the direction that reduces loss?
- What happens when there are millions of parameters instead of one weight?
- How does backpropagation calculate gradients for all those parameters?
- Can gradient descent get stuck somewhere instead of finding the best possible minimum?
## Corrections / updated understanding
**Initial understanding:** I thought mean loss helped determine whether the weight should increase or decrease.

**Updated understanding:** Mean loss measures the model's overall error and can be used as a stopping condition. The gradient determines how the parameter should change. The learning rate controls the size of that change.
## Related notes
- [Model Learning Implementation](../01_Models/Exercises/003_learning_model.py)
- [Current Status](../05_Progress/CURRENT_STATUS.md)
- [Math Overview](../03_Math/Math.md)
- [Day 2](../03_Math/Notes/day002.md)
- [Day 3](../03_Math/Notes/day003.md)
