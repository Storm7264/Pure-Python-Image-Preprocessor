
def makeImage():
    image = [
        [10, 10, 10, 10, 10],
        [10, 200, 10, 10, 10],
        [10, 200, 10, 10, 10],
        [10, 200, 200, 200, 10],
        [10, 10, 10, 10, 10],
    ]
    return image
 
 
def showImage(image):
    for row in image:
        line = ""
        for pixel in row:
            line = line + str(pixel).rjust(5)
        print(line)
    print()
 
 
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
            newRow.append(255 - pixel)
        newImage.append(newRow)
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
 
 
def findEdges(image):
    kernel = [
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1],
    ]
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
 
 
def makeColorImage():
    image = [
        [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
        [[255, 255, 0], [255, 255, 255], [0, 255, 255]],
        [[0, 0, 0], [128, 128, 128], [255, 0, 255]],
    ]
    return image
 
 
def saveColorImage(image, fileName):
    height = len(image)
    width = len(image[0])
    file = open(fileName, "w")
    file.write("P3\n")
    file.write(str(width) + " " + str(height) + "\n")
    file.write("255\n")
    for row in image:
        for pixel in row:
            file.write(str(pixel[0]) + " " + str(pixel[1]) + " " + str(pixel[2]) + "\n")
    file.close()
 
 
def loadColorImage(fileName):
    file = open(fileName, "r")
    words = file.read().split()
    file.close()
    width = int(words[1])
    height = int(words[2])
    position = 4
    image = []
    for y in range(height):
        row = []
        for x in range(width):
            red = int(words[position])
            green = int(words[position + 1])
            blue = int(words[position + 2])
            row.append([red, green, blue])
            position = position + 3
        image.append(row)
    return image
 
 
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
print("Threshold at 100")
showImage(thresholdImage(image, 100))
print("Flip left-right")
showImage(flipLeftRight(image))
print("Flip up-down")
showImage(flipUpDown(image))
print("Rotate right")
showImage(rotateRight(image))
print("Edges")
showImage(findEdges(image))
 
colorImage = makeColorImage()
saveColorImage(colorImage, "test.ppm")
loaded = loadColorImage("test.ppm")
print("Color image loaded from PPM, as gray")
showImage(colorToGray(loaded))
print("Color inverted, first row:", invertColorImage(loaded)[0])