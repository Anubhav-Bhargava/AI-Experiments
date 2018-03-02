import numpy as np
import keras
import argparse
from keras.models import load_model
from scipy.misc import *

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())


# dimensions of our images.
img_width, img_height = 150, 150

#read image
image = imread(args["image"])

#resize image into 150 X 150 X 3
image=imresize(image,(img_width,img_height,3))

#reshape image as required by the model 1 X 150 X 150 X3
image=image.reshape(1,img_width,img_height,3)

#Load our pre-trained model
model = load_model('models/my_model.h5')


#predicting
pred=model.predict_classes(image)

#print prediction
if pred==0:

	print 'alcohol_beverage_bottles'

else:

	print 'water_bottles'