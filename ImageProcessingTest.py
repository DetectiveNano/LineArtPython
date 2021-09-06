## DetectiveNano 9/5/21
## image processing test code used for topoSTL project

#import shit
import skimage
from skimage import data, io, filters, util
from skimage.color import rgb2gray

import tkinter
from tkinter import Tk    
from tkinter.filedialog import askopenfilename

import sys, os 

import matplotlib
from matplotlib import image, pyplot

import numpy

## give myself credi
print("---------------------------")
print("Written by DetectiveNano")
print("---------------------------")
# load image as pixel array
running = True
while(running == True):
    Tk().withdraw() 
    #filename = ""
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    #if(filename == "") :
    selectedImage = image.imread(filename) # select image and read it into a numpy array
    #else:
        #filename = ""
        #filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    # summarize shape of the pixel array
    print(selectedImage.dtype)
    print(selectedImage.shape)

    print(type(selectedImage))


    grayscale = rgb2gray(selectedImage)
    edge_sobel = filters.sobel(grayscale)
    finalLine = util.invert(edge_sobel)

    fig, axes = pyplot.subplots(ncols=3, sharex=True, sharey=True,
                             figsize=(8, 4))
    ax = axes.ravel()

    ax[0].imshow(selectedImage)
    ax[0].set_title("Original")
    ax[1].imshow(edge_sobel, cmap=pyplot.cm.gray)
    ax[1].set_title('First Line')
    ax[2].imshow(finalLine, cmap=pyplot.cm.gray)
    ax[2].set_title('Line')
    fig.tight_layout()

    pyplot.show()

    ##for some fucking reason the output appears as white but saves as yellow and i need to fucking fix that


    print("Do you want to save the final line art ? Third image shown.")
    saveDecision = input("Enter 'yes' or 'no' ." + '\n' )
    if(saveDecision == 'yes'):
        saveFileName = input("Enter File Name to Save \n")
        pyplot.imsave(saveFileName + '.png', finalLine, cmap= pyplot.cm.gray)
input("Press enter to end.")