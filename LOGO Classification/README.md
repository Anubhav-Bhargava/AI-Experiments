# LOGO Classification

This code classifies company logos in a given image.

# Dataset

It is trained on [Flickr Logos 27 dataset](http://image.ntua.gr/iva/datasets/flickr_logos/)

# Prerequisites

>The code is developed for python 2.7 using a jupyter notebook

>All dependencies are mentioned in Requirements.txt 

# Algorithms

I've used **Convolution Neural Network** for the classification. 

The code in the file [logo_classif_aug.ipynb](https://github.com/Anubhav-Bhargava/AI-Experiments/blob/master/LOGO%20Classification/logo_classif_aug.ipynb) 
is trained on a smaller dataset. It reaches a test accuracy of ~52% after training for 200 epochs

While the code in the file [logo_classif_crop_aug.ipynb](https://github.com/Anubhav-Bhargava/AI-Experiments/blob/master/LOGO%20Classification/logo_classif_crop_aug.ipynb)
is trained using on annotated images with bounding boxes of the logo instances in the image. There are multiple logo instances per class image.
It reached a **test accuracy** of **~96%** after training for **150 epochs**.

