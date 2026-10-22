
def makeImage():
    rawImage = [
       [183, 180, 117,  46, 100],
    [  4, 222,  95,  55, 120],
    [ 19,  45, 181, 238,  51],
    [160, 140, 224,   0, 190],
    [ 29,  10,  35, 125, 136]
    ]
    
    image = []
    for rawRow in rawImage:
        row = []  
        for pixel in rawRow:
            pixel = limitValue(pixel)
            row.append(pixel)
        image.append(row)  
        
    return image
 
 
def showImage(image):
    for row in image:
        line = ""
        for pixel in row:
            line = line + str(pixel).rjust(5)
        print(line)
    print()

def showColorImage(image):
    for row in image:
        line = ""
        for pixel in row:
            line = line + str(pixel).rjust(20)
        print(line)
    print()
#this function is just to make the colored image inversions look more tidy, it isn't important.
 
 
def limitValue(number):
    if number < 0:
        return 0
    if number > 255:
        return 255
    return number
 
 
def invertImage(image):
    newImage = []
    for row in image:
        newRow = []
        for pixel in row:
            pixel = limitValue(pixel)
            newRow.append(255 - pixel)
        newImage.append((newRow))
    return newImage
 
 
def changeBrightness(image, amount):
    newImage = []
    for row in image:
        newRow = []
        for pixel in row:
            newRow.append(limitValue(pixel + amount))
        newImage.append(newRow)
    return newImage
 
 
def thresholdImage(image, cutoff):
    newImage = []
    for row in image:
        newRow = []
        for pixel in row:
            if pixel >= cutoff:
                newRow.append(255)
            else:
                newRow.append(0)
        newImage.append(newRow)
    return newImage
 
 
def flipLeftRight(image):
    newImage = []
    for row in image:
        newRow = []
        for pixel in row:
            newRow.insert(0, pixel)
        newImage.append(newRow)
    return newImage
 
 
def flipUpDown(image):
    newImage = []
    for row in image:
        newImage.insert(0, row[:])
    return newImage
#colon creates a brand new copy of that row, if we dont use it the row memory adress for new one will be the same as original image.
# so if anything is modified in the new img row it'll link to the old one too.  
 
def rotateRight(image):
    height = len(image)
    width = len(image[0])
    newImage = []
    for x in range(width):
        newRow = []
        for y in range(height - 1, -1, -1):
            newRow.append(image[y][x])
        newImage.append(newRow)
    return newImage
 # it goes to 1st column, takes the column bottom to top, and then puts it as a row in the new matrix... and so on

 
def getPixel(image, y, x):
    height = len(image)
    width = len(image[0])
    if y < 0:
        y = 0
    if y > height - 1:
        y = height - 1
    if x < 0:
        x = 0
    if x > width - 1:
        x = width - 1
    return image[y][x]
    #basically if the program tries to search an image out of bounds it simply pulls it back in place.
 
def findEdges(image):
    kernel = [
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1],
    ]
    #the kernel simply takes every pixel as the centre and amplifies its brightness while being relative to its surroundings and reducing the overall by subtracting with the surroundings' brightness.
    height = len(image)
    width = len(image[0])
    newImage = []
    for y in range(height):
        newRow = []
        for x in range(width):
            total = 0
            for ky in range(3):
                for kx in range(3):
                    pixel = getPixel(image, y + ky - 1, x + kx - 1)
                    total = total + pixel * kernel[ky][kx]
            newRow.append(limitValue(total))
        newImage.append(newRow)
    return newImage
   #scans your image pixel by pixel, checks how drastically each pixel's brightness differs from its 8 surrounding neighbors
 # basically loops 1 and 2 select a centre pixel and loops 3 n 4 multiply it and the surroundings with kernel weights to find effect of edges
 
def makeColorImage():
    image = [
        [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
        [[255, 255, 0], [255, 255, 255], [0, 255, 255]],
        [[0, 0, 0], [128, 128, 128], [255, 0, 255]],
    ]
    return image
 # Need to learn how to save colored images as a portable pixel map (ppm). 
 #basic functions such as grayscaling and inverting a row do not require ppm.
def colorToGray(image):
    newImage = []
    for row in image:
        newRow = []
        for pixel in row:
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            newRow.append(average)
        newImage.append(newRow)
    return newImage
 
 
def invertColorImage(image):
    newImage = []
    for row in image:
        newRow = []
        for pixel in row:
            newRow.append([255 - pixel[0], 255 - pixel[1], 255 - pixel[2]])
        newImage.append(newRow)
    return newImage
 
 
image = makeImage()
print("Original")
showImage(image)
print("Inverted")
showImage(invertImage(image))
print("Brighter by 60")
showImage(changeBrightness(image, 60))
print("Threshold")
showImage(thresholdImage(image, 180))
print("Flip left-right")
showImage(flipLeftRight(image))
print("Flip up-down")
showImage(flipUpDown(image))
print("Rotate right")
showImage(rotateRight(image))
print("Edges")
showImage(findEdges(image))
 
colorImage = makeColorImage()
print("Color image as gray")
showImage(colorToGray(colorImage))
print("Color inverted:")
showColorImage(invertColorImage(colorImage))