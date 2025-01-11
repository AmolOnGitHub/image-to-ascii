import os
from PIL import Image, ImageOps

def grayscale(value):
    scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,. "
    
    # Normalisation 
    length = len(scale) - 1
    normVal = round(value * length / 255)

    return scale[normVal]


imageName = input("Enter the name of the image you would like to convert: ")
imagePath = os.getcwd() + "/" + imageName

image = Image.open(imagePath)

textName = input("Enter the name of the file where you would like to store the art: ")
textPath = os.getcwd() + "/" + textName


print("This image's dimensions are: " + str(image.size))
rec = round(max(image.size) / 100)
pixelConst = int(input(f"Choose the size (in px) that one character will represent (Recommended: {rec}): "))
newWidth = round(image.size[0] / pixelConst)
newHeight = round(image.size[1] / pixelConst)

#Resizes Image
print("\nImage resizing....")
image = image.resize((newWidth, newHeight))
print("Resizing finished.")

#Converts image to grayscale
print("\nConverting to grayscale....")
image = ImageOps.grayscale(image)
print("Conversion finished.")

#Gets the grayscale value for each pixel
print("\nCalculating....")
pixelValues = list(image.getdata())
print("Calculating finished.")

#Starts printing
print("\nPrinting image....")

textFile = open(textPath, "w")
counter = 0
for no in pixelValues:
    textFile.write(grayscale(no))
    counter += 1
    if counter == image.size[0]:
        textFile.write("\n")
        counter = 0
        
print("Printing finished.")