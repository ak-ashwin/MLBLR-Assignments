# Step 0: Read input and output
import numpy as np
import math

# X = np.random.randint(2,size=(3,4))
# Y = np.random.randint(2,size=(3,1))

# Step 1: Initialize weights and biases with random values (There are methods to initialize weights and biases but for now initialize with random values)

wh = np.random.random(size=(4, 3))
# bh = np.random.random(size=(1,3))

# wout = np.random.random(size=(3,1))
# bout = np.random.random(size=(1))

# Step 2: Calculate hidden layer input:
X = np.array([[0, 0, 1, 0], [0, 1, 0, 0], [0, 1, 0, 0]])

wh = np.array([[0.40508046, 0.14088848, 0.30496994],
               [0.3951567, 0.53103593, 0.65167937],
               [0.21677381, 0.29163813, 0.858407],
               [0.57774779, 0.4591112, 0.80576803]])

bh = np.array([0.87486257, 0.83188755, 0.31602472])

hidden_layer_input = np.dot(X, wh) + bh


# Step 3: Perform non-linear transformation on hidden linear input
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


hiddenlayer_activations = sigmoid(hidden_layer_input)

# Step 4: Perform linear and non-linear transformation of hidden layer activation at output layer
wout = np.array([[0.98433046],
                 [0.87326864],
                 [0.91545553]])

bout = np.array([[0.72832801]])

output_layer_input = np.dot(hiddenlayer_activations, wout) + bout

output = sigmoid(output_layer_input)

# Step 5: Calculate gradient of Error(E) at output layer
y = np.array([[1],
              [1],
              [1]])
E = y - output


# Step 6: Compute slope at output and hidden layer

# Derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)


slope_output_layer = derivatives_sigmoid(output)
slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)

# Step 7: Compute delta at output layer
lr = 1
d_output = E * slope_output_layer * lr

# Step 8: Calculate Error at hidden layer
Error_at_hidden_layer = np.dot(d_output, wout.T)

# Step 9: Compute delta at hidden layer

d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer

# Step 10: Update weight at both output and hidden layer

wout = wout + np.dot(hiddenlayer_activations.T, d_output) * lr
wh = wh + np.dot(X.T, d_hiddenlayer) * lr

# Step 11: Update biases at both output and hidden layer

bh = bh + np.sum(d_hiddenlayer, axis=0) * lr
bout = bout + np.sum(d_output, axis=0) * lr

print(bh)
print(bout)
