import os
from PIL import Image, ImageOps

def char(value):
    value = round(1 - value, 1)
    # Inverts and rounds the grayscale value to one decimal
    if value == 0.0:
        return " "
    if value == 0.1:
        return "."
    if value == 0.2:
        return ":"
    if value == 0.3:
        return "-"
    if value == 0.4:
        return "="
    if value == 0.5:
        return "+"
    if value == 0.6:
        return "*"
    if value == 0.7:
        return "#"
    if value == 0.8:
        return "%"
    if value == 0.9 or value == 1:
        return "@"
    

imageName = input("Enter the name of the image you would like to convert: ")
imagePath = os.getcwd() + "/" + imageName
# os.getcwd() gets the file path of the folder the program is located in

image = Image.open(imagePath)

textName = input("Enter the name of the file where you would like to store the art: ")
textPath = os.getcwd() + "/" + textName

print("This image's dimensions are: " + str(image.size))
rec = round(max(image.size) / 100)
pixelConst = int(input(f"Choose the size (in px) that one character will represent (Recommended: {rec}): "))
newWidth = round(image.size[0] / pixelConst)
newHeight = round(image.size[1] / pixelConst)

# Resizes Image
# Resizing the image is necessary, as some images are very high resolution, which would result
# in extremely long lines of text, which would defeat the purpose of copy pasting
print("\nImage resizing....")
image = image.resize((newWidth, newHeight))
print("Resizing finished.")

# Converts image to grayscale
print("\nConverting to grayscale....")
image = ImageOps.grayscale(image)
print("Conversion finished.")

# Gets the grayscale value for each pixel and normalizes it
print("\nCalculating....")

pixelValues = list(image.getdata())
counter = 0
for i in pixelValues:
    pixelValues[counter] = round(i / 255, 1) 
    counter += 1    

print("Calculating finished.")

# Starts printing
print("\nPrinting image....")

textFile = open(textPath, "w")
counter = 0
for no in pixelValues:
    textFile.write(char(no))
    counter += 1

    if counter == image.size[0]:
        textFile.write("\n")
        counter = 0

print("Printing finished.")