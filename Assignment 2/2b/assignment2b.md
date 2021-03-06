#### Broad Steps
##### Step 0: Read input and output


```python

X = np.random.randint(2,size=(3,4))
Y = np.random.randint(2,size=(3,1))
```


| X |   |   |   | Wh |   |   | Bh |   |   | hidden_layer_input |   |   | hidden_layer_activations |   |   | Wout | Bout | output | Y | E |
|---|---|---|---|----|---|---|----|---|---|--------------------|---|---|--------------------------|---|---|------|------|--------|---|---|
| 0 | 0 | 1 | 0 |    |   |   |    |   |   |                    |   |   |                          |   |   |      |      |        | 1 |   |
| 0 | 1 | 0 | 0 |    |   |   |    |   |   |                    |   |   |                          |   |   |      |      |        | 1 |   |
| 0 | 1 | 0 | 0 |    |   |   |    |   |   |                    |   |   |                          |   |   |      |      |        | 0 |   |

![Step 0](images/step0.png)

##### Step 1: Initialize weights and biases with random values (There are methods to initialize weights and biases but for now initialize with random values)


 


```python

wh = np.random.random(size=(4, 3))
bh = np.random.random(size=(1,3))

wout = np.random.random(size=(3,1))
bout = np.random.random(size=(1))
```

| ﻿X |   |   |   | Wh         |            |            | Bh         |            |            | hidden_layer_input |   |   | hidden_layer_activations |   |   | Wout       | Bout       | output | Y | E |
|---|---|---|---|------------|------------|------------|------------|------------|------------|--------------------|---|---|--------------------------|---|---|------------|------------|--------|---|---|
| 0 | 0 | 1 | 0 | 0.40508046 | 0.14088848 | 0.30496994 | 0.87486257 | 0.83188755 | 0.31602472 |                    |   |   |                          |   |   | 0.98433046 | 0.72832801 |        | 1 |   |
| 0 | 1 | 0 | 0 | 0.3951567  | 0.53103593 | 0.65167937 |            |            |            |                    |   |   |                          |   |   | 0.87326864 |            |        | 1 |   |
| 0 | 1 | 0 | 0 | 0.21677381 | 0.29163813 | 0.858407   |            |            |            |                    |   |   |                          |   |   | 0.91545553 |            |        | 0 |   |
|   |   |   |   | 0.57774779 | 0.4591112  | 0.80576803 |            |            |            |                    |   |   |                          |   |   |            |            |        |   |   |


![Step 1](images/step1.png)

##### Step 2: Calculate hidden layer input:

```python
X = np.array([[0, 0, 1, 0], [0, 1, 0, 0], [0, 1, 0, 0]])

wh = np.array([[0.40508046, 0.14088848, 0.30496994],
               [0.3951567, 0.53103593, 0.65167937],
               [0.21677381, 0.29163813, 0.858407],
               [0.57774779, 0.4591112, 0.80576803]])

bh = np.array([0.87486257, 0.83188755, 0.31602472])

hidden_layer_input = np.dot(X, wh) + bh
```

| ﻿X |   |   |   | Wh         |            |            | Bh         |            |            | hidden_layer_input |            |            | hidden_layer_activations |   |   | Wout       | Bout       | output | Y | E |
|---|---|---|---|------------|------------|------------|------------|------------|------------|--------------------|------------|------------|--------------------------|---|---|------------|------------|--------|---|---|
| 0 | 0 | 1 | 0 | 0.40508046 | 0.14088848 | 0.30496994 | 0.87486257 | 0.83188755 | 0.31602472 | 1.09163638         | 1.12352568 | 1.17443172 |                          |   |   | 0.98433046 | 0.72832801 |        | 1 |   |
| 0 | 1 | 0 | 0 | 0.3951567  | 0.53103593 | 0.65167937 |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 |                          |   |   | 0.87326864 |            |        | 1 |   |
| 0 | 1 | 0 | 0 | 0.21677381 | 0.29163813 | 0.858407   |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 |                          |   |   | 0.91545553 |            |        | 0 |   |
|   |   |   |   | 0.57774779 | 0.4591112  | 0.80576803 |            |            |            |                    |            |            |                          |   |   |            |            |        |   |   |


![Step 2](images/step2.png)

##### Step 3: Perform non-linear transformation on hidden linear input

```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


hiddenlayer_activations = sigmoid(hidden_layer_input)

```

| ﻿X |   |   |   | Wh         |            |            | Bh         |            |            | hidden_layer_input |            |            | hidden_layer_activations |            |            | Wout       | Bout       | output | Y | E |
|---|---|---|---|------------|------------|------------|------------|------------|------------|--------------------|------------|------------|--------------------------|------------|------------|------------|------------|--------|---|---|
| 0 | 0 | 1 | 0 | 0.40508046 | 0.14088848 | 0.30496994 | 0.87486257 | 0.83188755 | 0.31602472 | 1.09163638         | 1.12352568 | 1.17443172 | 0.74868974               | 0.75464211 | 0.76394514 | 0.98433046 | 0.72832801 |        | 1 |   |
| 0 | 1 | 0 | 0 | 0.3951567  | 0.53103593 | 0.65167937 |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.74868974               | 0.79623443 | 0.72466164 | 0.87326864 |            |        | 1 |   |
| 0 | 1 | 0 | 0 | 0.21677381 | 0.29163813 | 0.858407   |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.78074605               | 0.79623443 | 0.72466164 | 0.91545553 |            |        | 0 |   |
|   |   |   |   | 0.57774779 | 0.4591112  | 0.80576803 |            |            |            |                    |            |            |                          |            |            |            |            |        |   |   |

![Step 3](images/step3.png)

##### Step 4: Perform linear and non-linear transformation of hidden layer activation at output layer

```python
wout = np.array([[0.98433046],
                 [0.87326864],
                 [0.91545553]])

bout = np.array([[0.72832801]])

output_layer_input = np.dot(hiddenlayer_activations, wout) + bout

output = sigmoid(output_layer_input)

```

| ﻿X |   |   |   | Wh         |            |            | Bh         |            |            | hidden_layer_input |            |            | hidden_layer_activations |            |            | Wout       | Bout       | output     | Y | E |
|---|---|---|---|------------|------------|------------|------------|------------|------------|--------------------|------------|------------|--------------------------|------------|------------|------------|------------|------------|---|---|
| 0 | 0 | 1 | 0 | 0.40508046 | 0.14088848 | 0.30496994 | 0.87486257 | 0.83188755 | 0.31602472 | 1.09163638         | 1.12352568 | 1.17443172 | 0.74868974               | 0.75464211 | 0.76394514 | 0.98433046 | 0.72832801 | 0.94394048 | 1 |   |
| 0 | 1 | 0 | 0 | 0.3951567  | 0.53103593 | 0.65167937 |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.74868974               | 0.79623443 | 0.72466164 | 0.87326864 |            | 0.94560549 | 1 |   |
| 0 | 1 | 0 | 0 | 0.21677381 | 0.29163813 | 0.858407   |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.78074605               | 0.79623443 | 0.72466164 | 0.91545553 |            | 0.94560549 | 0 |   |
|   |   |   |   | 0.57774779 | 0.4591112  | 0.80576803 |            |            |            |                    |            |            |                          |            |            |            |            |            |   |   |

![Step 4](images/step4.png)

##### Step 5: Calculate gradient of Error(E) at output layer

```python
y = np.array([[1],
              [1],
              [1]])
E = y - output

```
| ﻿X |   |   |   | Wh         |            |            | Bh         |            |            | hidden_layer_input |            |            | hidden_layer_activations |            |            | Wout       | Bout       | output     | Y | E          |
|---|---|---|---|------------|------------|------------|------------|------------|------------|--------------------|------------|------------|--------------------------|------------|------------|------------|------------|------------|---|------------|
| 0 | 0 | 1 | 0 | 0.40508046 | 0.14088848 | 0.30496994 | 0.87486257 | 0.83188755 | 0.31602472 | 1.09163638         | 1.12352568 | 1.17443172 | 0.74868974               | 0.75464211 | 0.76394514 | 0.98433046 | 0.72832801 | 0.94394048 | 1 | 0.05605952 |
| 0 | 1 | 0 | 0 | 0.3951567  | 0.53103593 | 0.65167937 |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.74868974               | 0.79623443 | 0.72466164 | 0.87326864 |            | 0.94560549 | 1 | 0.05439451 |
| 0 | 1 | 0 | 0 | 0.21677381 | 0.29163813 | 0.858407   |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.78074605               | 0.79623443 | 0.72466164 | 0.91545553 |            | 0.94560549 | 0 | 0.05439451 |
|   |   |   |   | 0.57774779 | 0.4591112  | 0.80576803 |            |            |            |                    |            |            |                          |            |            |            |            |            |   |            |


![Step 5](images/step5.png)

##### Step 6: Compute slope at output and hidden layer

```python
def derivatives_sigmoid(x):
    return x * (1 - x)


slope_output_layer = derivatives_sigmoid(output)
slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
```

| ﻿X |   |   |                    | Wh         |            |            | Bh         |            |            | hidden_layer_input |            |            | hidden_layer_activations |                    |            | Wout       | Bout       | output     | Y | E          |
|---|---|---|--------------------|------------|------------|------------|------------|------------|------------|--------------------|------------|------------|--------------------------|--------------------|------------|------------|------------|------------|---|------------|
| 0 | 0 | 1 | 0                  | 0.40508046 | 0.14088848 | 0.30496994 | 0.87486257 | 0.83188755 | 0.31602472 | 1.09163638         | 1.12352568 | 1.17443172 | 0.74868974               | 0.75464211         | 0.76394514 | 0.98433046 | 0.72832801 | 0.94394048 | 1 | 0.05605952 |
| 0 | 1 | 0 | 0                  | 0.3951567  | 0.53103593 | 0.65167937 |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.74868974               | 0.79623443         | 0.72466164 | 0.87326864 |            | 0.94560549 | 1 | 0.05439451 |
| 0 | 1 | 0 | 0                  | 0.21677381 | 0.29163813 | 0.858407   |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.78074605               | 0.79623443         | 0.72466164 | 0.91545553 |            | 0.94560549 | 0 | 0.05439451 |
|   |   |   |                    | 0.57774779 | 0.4591112  | 0.80576803 |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |            |            |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |            |            |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |            |            |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |            |            |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |            |            |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   | Slope_hidden_layer |            |            |            |            |            |            |                    |            |            |                          | Slope_output_layer |            |            |            |            |   |            |
|   |   |   | 0.18815341         | 0.1851574  | 0.18033297 |            |            |            |            |                    |            |            |                          | 0.05291685         |            |            |            |            |   |            |
|   |   |   | 0.17118166         | 0.16224516 | 0.19952715 |            |            |            |            |                    |            |            |                          | 0.05143575         |            |            |            |            |   |            |
|   |   |   | 0.17118166         | 0.16224516 | 0.19952715 |            |            |            |            |                    |            |            |                          | 0.05143575         |            |            |            |            |   |            |


![Step 6](images/step6.png)

##### Step 7: Compute delta at output layer

```python
lr = 1
d_output = E * slope_output_layer * lr
```
| ﻿X |   |   |                    | Wh         |            |                       | Bh         |            |            | hidden_layer_input |            |            | hidden_layer_activations |                    |            | Wout       | Bout       | output     | Y | E          |
|---|---|---|--------------------|------------|------------|-----------------------|------------|------------|------------|--------------------|------------|------------|--------------------------|--------------------|------------|------------|------------|------------|---|------------|
| 0 | 0 | 1 | 0                  | 0.40508046 | 0.14088848 | 0.30496994            | 0.87486257 | 0.83188755 | 0.31602472 | 1.09163638         | 1.12352568 | 1.17443172 | 0.74868974               | 0.75464211         | 0.76394514 | 0.98433046 | 0.72832801 | 0.94394048 | 1 | 0.05605952 |
| 0 | 1 | 0 | 0                  | 0.3951567  | 0.53103593 | 0.65167937            |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.74868974               | 0.79623443         | 0.72466164 | 0.87326864 |            | 0.94560549 | 1 | 0.05439451 |
| 0 | 1 | 0 | 0                  | 0.21677381 | 0.29163813 | 0.858407              |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.78074605               | 0.79623443         | 0.72466164 | 0.91545553 |            | 0.94560549 | 0 | 0.05439451 |
|   |   |   |                    | 0.57774779 | 0.4591112  | 0.80576803            |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |            |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |            |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |            |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |            |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |            |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   | Slope_hidden_layer |            |            | error_at_hidden_layer |            |            |            |                    |            |            |                          | Slope_output_layer |            |            |            |            |   |            |
|   |   |   | 0.18815341         | 0.1851574  | 0.18033297 | 0.00292001            | 0.00259055 | 0.00271569 |            |                    |            |            |                          | 0.05291685         |            |            |            |            |   |            |
|   |   |   | 0.17118166         | 0.16224516 | 0.19952715 | 0.00275398            | 0.00244325 | 0.00256128 |            |                    |            |            |                          | 0.05143575         |            |            |            |            |   |            |
|   |   |   | 0.17118166         | 0.16224516 | 0.19952715 | 0.00275398            | 0.00244325 | 0.00256128 |            |                    |            |            |                          | 0.05143575         |            |            |            |            |   |            |

![Step 7](images/step7.png)

##### Step 8: Calculate Error at hidden layer

```python
Error_at_hidden_layer = np.dot(d_output, wout.T)
```

| ﻿X |   |   |                    | Wh         |                    |                       | Bh         |            |            | hidden_layer_input |            |            | hidden_layer_activations |                    |            | Wout       | Bout       | output     | Y | E          |
|---|---|---|--------------------|------------|--------------------|-----------------------|------------|------------|------------|--------------------|------------|------------|--------------------------|--------------------|------------|------------|------------|------------|---|------------|
| 0 | 0 | 1 | 0                  | 0.40508046 | 0.14088848         | 0.30496994            | 0.87486257 | 0.83188755 | 0.31602472 | 1.09163638         | 1.12352568 | 1.17443172 | 0.74868974               | 0.75464211         | 0.76394514 | 0.98433046 | 0.72832801 | 0.94394048 | 1 | 0.05605952 |
| 0 | 1 | 0 | 0                  | 0.3951567  | 0.53103593         | 0.65167937            |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.74868974               | 0.79623443         | 0.72466164 | 0.87326864 |            | 0.94560549 | 1 | 0.05439451 |
| 0 | 1 | 0 | 0                  | 0.21677381 | 0.29163813         | 0.858407              |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.78074605               | 0.79623443         | 0.72466164 | 0.91545553 |            | 0.94560549 | 0 | 0.05439451 |
|   |   |   |                    | 0.57774779 | 0.4591112          | 0.80576803            |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   | Slope_hidden_layer |            |                    | error_at_hidden_layer |            |            |            |                    |            |            |                          | Slope_output_layer |            |            |            |            |   |            |
|   |   |   | 0.18815341         | 0.1851574  | 0.18033297         | 0.00292001            | 0.00259055 | 0.00271569 |            |                    |            |            |                          | 0.05291685         |            |            |            |            |   |            |
|   |   |   | 0.17118166         | 0.16224516 | 0.19952715         | 0.00275398            | 0.00244325 | 0.00256128 |            |                    |            |            |                          | 0.05143575         |            |            |            |            |   |            |
|   |   |   | 0.17118166         | 0.16224516 | 0.19952715         | 0.00275398            | 0.00244325 | 0.00256128 |            |                    |            |            |                          | 0.05143575         |            |            |            |            |   |            |
|   |   |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            | delta_hidden_layer |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            | 0.00054941         | 0.00047966            | 0.00048973 |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            | 0.00047143         | 0.00039641            | 0.00051105 |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |   |   |                    |            | 0.00047143         | 0.00039641            | 0.00051105 |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |

![Step 8](images/step8.png)

##### Step 9: Compute delta at hidden layer

```python
d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
```
| ﻿X |               |   |                    | Wh         |                    |                       | Bh         |            |            | hidden_layer_input |            |            | hidden_layer_activations |                    |            | Wout       | Bout       | output     | Y | E          |
|---|---------------|---|--------------------|------------|--------------------|-----------------------|------------|------------|------------|--------------------|------------|------------|--------------------------|--------------------|------------|------------|------------|------------|---|------------|
| 0 | 0             | 1 | 0                  | 0.40508046 | 0.14088848         | 0.30496994            | 0.87635484 | 0.83316002 | 0.31753654 | 1.09163638         | 1.12352568 | 1.17443172 | 0.74868974               | 0.75464211         | 0.76394514 | 0.99092022 | 0.73689015 | 0.94394048 | 1 | 0.05605952 |
| 0 | 1             | 0 | 0                  | 0.39609956 | 0.53182874         | 0.65270146            |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.74868974               | 0.79623443         | 0.72466164 | 0.87996273 |            | 0.94560549 | 1 | 0.05439451 |
| 0 | 1             | 0 | 0                  | 0.21732322 | 0.29211779         | 0.85889673            |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.78074605               | 0.79623443         | 0.72466164 | 0.92177672 |            | 0.94560549 | 0 | 0.05439451 |
|   |               |   |                    | 0.57774779 | 0.4591112          | 0.80576803            |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   | Slope_hidden_layer |            |                    | error_at_hidden_layer |            |            |            |                    |            |            |                          | Slope_output_layer |            |            |            |            |   |            |
|   |               |   | 0.18815341         | 0.1851574  | 0.18033297         | 0.00292001            | 0.00259055 | 0.00271569 |            |                    |            |            |                          | 0.05291685         |            |            |            |            |   |            |
|   |               |   | 0.17118166         | 0.16224516 | 0.19952715         | 0.00275398            | 0.00244325 | 0.00256128 |            |                    |            |            |                          | 0.05143575         |            |            |            |            |   |            |
|   |               |   | 0.17118166         | 0.16224516 | 0.19952715         | 0.00275398            | 0.00244325 | 0.00256128 |            |                    |            |            |                          | 0.05143575         |            |            |            |            |   |            |
|   |               |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   | Learning Rate | 1 |                    |            | delta_hidden_layer |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            | 0.00054941         | 0.00047966            | 0.00048973 |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            | 0.00047143         | 0.00039641            | 0.00051105 |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            | 0.00047143         | 0.00039641            | 0.00051105 |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |

![Step 9](images/step9.png)

##### Step 10: Update weight at both output and hidden layer

```python
wout = wout + np.dot(hiddenlayer_activations.T, d_output) * lr
wh = wh + np.dot(X.T, d_hiddenlayer) * lr
```



##### Step 11: Update biases at both output and hidden layer

```python

bh = bh + np.sum(d_hiddenlayer, axis=0) * lr
bout = bout + np.sum(d_output, axis=0) * lr

```
| ﻿X |               |   |                    | Wh         |                    |                       | Bh         |            |            | hidden_layer_input |            |            | hidden_layer_activations |                    |            | Wout       | Bout       | output     | Y | E          |
|---|---------------|---|--------------------|------------|--------------------|-----------------------|------------|------------|------------|--------------------|------------|------------|--------------------------|--------------------|------------|------------|------------|------------|---|------------|
| 0 | 0             | 1 | 0                  | 0.40508046 | 0.14088848         | 0.30496994            | 0.87635484 | 0.83316002 | 0.31753654 | 1.09163638         | 1.12352568 | 1.17443172 | 0.74868974               | 0.75464211         | 0.76394514 | 0.99092022 | 0.73689015 | 0.94394048 | 1 | 0.05605952 |
| 0 | 1             | 0 | 0                  | 0.39609956 | 0.53182874         | 0.65270146            |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.74868974               | 0.79623443         | 0.72466164 | 0.87996273 |            | 0.94560549 | 1 | 0.05439451 |
| 0 | 1             | 0 | 0                  | 0.21732322 | 0.29211779         | 0.85889673            |            |            |            | 1.27001927         | 1.36292348 | 0.96770409 | 0.78074605               | 0.79623443         | 0.72466164 | 0.92177672 |            | 0.94560549 | 0 | 0.05439451 |
|   |               |   |                    | 0.57774779 | 0.4591112          | 0.80576803            |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   | Slope_hidden_layer |            |                    | error_at_hidden_layer |            |            |            |                    |            |            |                          | Slope_output_layer |            |            |            |            |   |            |
|   |               |   | 0.18815341         | 0.1851574  | 0.18033297         | 0.00292001            | 0.00259055 | 0.00271569 |            |                    |            |            |                          | 0.05291685         |            |            |            |            |   |            |
|   |               |   | 0.17118166         | 0.16224516 | 0.19952715         | 0.00275398            | 0.00244325 | 0.00256128 |            |                    |            |            |                          | 0.05143575         |            |            |            |            |   |            |
|   |               |   | 0.17118166         | 0.16224516 | 0.19952715         | 0.00275398            | 0.00244325 | 0.00256128 |            |                    |            |            |                          | 0.05143575         |            |            |            |            |   |            |
|   |               |   |                    |            |                    |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   | Learning Rate | 1 |                    |            | delta_hidden_layer |                       |            |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            | 0.00054941         | 0.00047966            | 0.00048973 |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            | 0.00047143         | 0.00039641            | 0.00051105 |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |
|   |               |   |                    |            | 0.00047143         | 0.00039641            | 0.00051105 |            |            |                    |            |            |                          |                    |            |            |            |            |   |            |


![Step 9](images/step9.png)
