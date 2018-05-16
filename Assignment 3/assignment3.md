#### Image Augmentation:
We need a lot of images for training and predicting image classification problems. Sometimes we have access to a huge set of data and sometimes we don’t. What we would like to train on our different variations of the image. So, that based on any variation it can recognize or auto-fill the are with that color or shape.

There are different techniques for image augmentation:
**1. Resizing:**
Image resizing is the most important technique to apply before starting as the size of the image you've trained on matters a lot. Previously, I had used a python library which can detect the cheque number from an image of a cheque. The interesting fact was that it was not working on a particular image and I had faced a similar issue before and I realized that if you resize the image to the size of the training image that they had provided then it'll work. I tried that and it started working for all images. IMAGE RESIZING is the most import technique before starting anything.

**2. Scaling:**
It depends on what scale the image was trained on. For eg: Photos which are zoomed and then trained might need padding around it. But the scale at which it was trained will be greater than the original size of the image.

**3. Translation:** 
If you want the object to be detected at any place an image then you need train it for translation so that it can recognize the image if it is at the bottom, side or on top.

**4. Rotation:** 
Similar to translation we need to detect any object if it is inverted or if someone has taken a snapshot in a landscape mode. Basically, we are covering this for all any image which has a slight movement from the baseline or even 90,180 degrees shift in an image.

**5. Flipping:**
Similar to the rotation we need to check for flipped left or flipped right or transpose of an image. 

**6. Brightness:**
Based on the lighting conditions and shaded area the image training can be improved.






#### Convolution:

CNN is a neural network which consists of neurons which have weights and biases. It takes an input and alters the weights and biases and does a dot product on the input layer and forwards it to the next layer to do the next operation. After the weights are added it is called as an Activation layer.

a. Usual Convolutions (stick to 3x3):
    3x3 kernels are basically filters used to detect edges, blur, increase sharpness etc.

##### Edge Detection Matrix:
```
    [ 0  1  0 ]     
A = [ 1 -4  1 ]    
    [ 0  1  0 ] 
```

##### Blur Matrix:
```
    [ 1  1  1 ]     
A = [ 1  1  1 ]    
    [ 1  1  1 ] 
```

##### Sharpness Matrix:
```
    [  0  -1   0 ]     
A = [ -1   5  -1 ]    
    [  0  -1   0 ] 
```



##### b. 1x1 Convolution
  This Matrix learns what exactly each channel has to learn. It is also called as a PWC(Point wise convolution) If you multiply the number of dimensions with itself then you get PWC. For Eg: 13x13 on 13x13= 1x1



**MaxPooling**
It always extracts the max features,
Max Pooling is always **2x2**.
It is used for matrices reduction.
It is used to retain the best features(50%).

Because 3x3 is 33.33% but we need to retain more info so we need 50% of the scaled image.

Maxpooling is done after extracting feature layers like texture, edge detection, etc..

After applying a few layers use Maxpooling.

It reduces matrix from 256x256 to 256x256/2x2. So, 132x132.




#### Regularization:

Regularization can be defined as how well your model is trained to general errors or changes which are not present in your training set. Generalization of your model is called Regularization.Regularization is necessary to avoid overfitting but maintaining accuracy.


##### 1. DropOut:
Some random nodes are removed in each training repetition along with their input and output connections. It can be applied to either input layer or the hidden layer. Training time reduces if you apply dropout but the number of iterations to converge increases. It makes your model more robust for any changes.

##### 2. Label Smoothing (non-intuitive awesomeness)
Label smoothing gives a probability of similarity. It is an important function used in regularization especially for models trained with cross-entropy error. It basically allows values which are not exactly 1 but around 0.9 or 0.8 to pass hence it does not reject out all values but keeps values closer to the requires output.


