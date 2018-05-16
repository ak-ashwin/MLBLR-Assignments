#### Convolution

CNN is a neural network which can *detect patterns*. It can be used on image analysis or data analysis. But it is mostly used in image analysis. 

CNN has hidden layers/filters. It reads the image and adds a filter on top of it which transforms the data. You can keep adding features and to retrieve more information on the data/image. 

Filters/layers added can detect edges, orientation, color, object, texture and more you train it'll understand that the particular image is lion, eagle or a table. 

The image here is like a noun and operation/action is like a verb. So, when an action is performed on an image then that function is called as an Activation function.

(CNN = CORRELATION = Summation of all pixels)
*Neural Network* is like an **organisation**. *RESNET* is like a SPY (CHAMCHA)

 **CNN Steps:**
  1. Features
  2. Textures
  3. Parts Of The Object
  4. Make Object
  5. Make The Scene


##### Filter/Kernel/Layer:
The filter is a *matrix of values* which outputs a **manipulated matrix**. Here we can have a matrix of size 3x3 and go over another matrix which is of size 5x5. 

The Filter/matrix of size 3x3 will go over each pixel in that image matrix of size 5x5 and convert it to a 3x3 matrix. This matrix might contain values after edge detection or any other transformation that was applied. *1 Kernel* will give 1 Channel.  Channel is also called a *Feature Map*.

Every GPU allocates **32 filters/kernels** as *default* . Even we assign 17 it still assigns 32 and hence we lose 15 filters. We add more filters to extract more information.




**Activation Function:**

*Activation function* of a neuron outputs values between 0 and 1, based on the sample/input data passed. It is the operation applied to the image. It extracts the features from the image and passes it forward based on the number of inputs. 
Eg: If you are detecting edges then all white edges which are dominant stays and all black edges which are negative will be converted to 0. But the edges with a very high value of black are considered. This is a called an Activation function(RELU)

There are different types of activation function, namely:
Sigmoid
Relu( Rectified Linear Unit)
Leaky Relu

Activation functions are applied layer after layer until you get the required output.

~~~~
Relu Formula : f(x)=max(0,x)
~~~~

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYzNjE2OTc4NV19
-->