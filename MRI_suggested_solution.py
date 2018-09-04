import numpy as np
import matplotlib.pyplot as plt
#import the necessary libraries

"""
Please read the instructions:

The objective of this checkpoint is to edit the original brain image to a desired shape
The MRI image is represented by a numpy array

The process includes two steps:
1. Crop the center for any dimension where the original is larger than the desired
2. Pad to desired shape for any dimension where the original is smaller than the desired

The main command has already been done for you
Although you can use the completed show_slices to do sanity check if necessary
What you need to do is to complete the crop_center and pad_todesire function

If you have done well, the module should output the shape change
and the final comparison should be True

For the small MRI image the shape change should be:
(65, 65, 55)--->(60, 60, 55)--->(60, 60, 60)
For the large MRI image the shape change should be:
(130, 130, 110)--->(120, 120, 110)--->(120, 120, 120)
"""


def show_slices(img):
       """ Function to display the MRI image 
           This function has been completed for you"""
       slices = [img[int(img.shape[0]/2), :, :],
                 img[:, int(img.shape[1]/2), :],
                 img[:, :, int(img.shape[2]/2)]]
       fig, axes = plt.subplots(1, len(slices))
       for i, slice in enumerate(slices):
           axes[i].imshow(slice.T, cmap="gray", origin="lower")
       plt.show()


def crop_center(img,crop_shape):
    """ Function to crop the center according to the given shape
        Think about what these terms mean
        Add a one line code that return the cropped image
        You may want to review the section 3 of the lab"""
    x,y,z = img.shape
    cropx = crop_shape[0]
    cropy = crop_shape[1]
    cropz = crop_shape[2]
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)
    startz = z//2-(cropz//2)
    return img[startx:startx+cropx,starty:starty+cropy, startz:startz+cropz]

def pad_todesire(img, desired_shape):
    """ Function to pad the image to the desired shape
        What you need to do is to calculate the six numbers needed to form npad
        The names are self-explantary: for example X_before means the number of pixels
        we want to pad before the image in the x dimension"""
    X_before = int((desired_shape[0]-img.shape[0])/2)
    Y_before = int((desired_shape[1]-img.shape[1])/2)
    Z_before = int((desired_shape[2]-img.shape[2])/2)
    X_after = desired_shape[0]-img.shape[0]-X_before
    Y_after = desired_shape[1]-img.shape[1]-Y_before
    Z_after = desired_shape[2]-img.shape[2]-Z_before

    npad = ((X_before, X_after),
            (Y_before, Y_after),
            (Z_before, Z_after))
    padded = np.pad(img, pad_width=npad, mode='constant', constant_values=0)

    return padded


MRI_img = np.load('MRI_img_small.npy')    #Load the original image
result = np.load('result_small.npy')      #This is the correct answer
desired_shape = [60, 60, 60]              #This is the shape that we want

original_shape = list(MRI_img.shape)      #We record the original shape in a list

crop_shape = original_shape
for i in range (3):
    if desired_shape[i] < original_shape[i]:
        crop_shape[i] = desired_shape[i]      #These steps simply output the desired shape
                                               #after the cropping operation

cropped_img = crop_center(MRI_img, crop_shape)   #Crop the image
final_img = pad_todesire(cropped_img, desired_shape)   #Pad the image to the desired shape

print(str(MRI_img.shape) + "--->"
      + str(cropped_img.shape) + "--->"
      + str(final_img.shape))               #For sanity check we output the shape change
            
print (np.array_equal(final_img, result))   #This should be true if your have correctly
                                             #implemented the functions


#Bonus
"""
If you have implemented the functions logically
They should be able to take in larger images as well

Replace the following lines to see if they can do so:
"""
#MRI_img = np.load('MRI_img_large.npy')
#result = np.load('result_large.npy')
#desired_shape = [120, 120, 120] 
