# Advance Image Recognition

This advance image recognition model can recognise most of the things which you see daily.

This make use of the Keras,TensorFlow and some Python requests library.

## Keras and TensorFlow

_Keras_ is a high-level neural network library that serves as an easy-to-use abstraction layer on top of the numerical computation library TensorFlow. It even provides access via its **keras.applications** module to ILSVRC competition-winning convolutional network models like _ResNet50_ (developed by Microsoft Research) and _InceptionV3_ (developed by Google Research) for free and unrestricted use. To install, follow the instructions at:

[**Keras Insatallation**](https://keras.io/#installation)

[**TensorFlow installation**](https://www.tensorflow.org/install/)
  
OR

* open terminal and type : _pip install tensorflow keras_ and hit Enter.                     
                     
### After Tensorflow and keras are installed :
Run **`python classify.py --image ./images/img_name.jpg`** (change the _img_name.jpg_ with a appropriate image name).

OR

Run **`python classify.py --image_url http://abc.jpg`** \[where http://www.abc.jpg is the image url]
