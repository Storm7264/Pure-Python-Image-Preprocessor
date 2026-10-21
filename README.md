# Pure-Python-Image-Preprocessor

# Image Preprocessor

A small Python program that shows how digital images work, using only plain Python. There are no libraries, so every step is visible: just lists, loops and basic maths.

An image is stored as a grid (a list of rows) of numbers from 0 to 255. 0 is black and 255 is white. The program starts with a tiny 5x5 image so you can check every result by eye.

## What it does

**Pixel operations** (each pixel is changed on its own)
- Invert: turns each value `v` into `255 - v`
- Brightness: adds or subtracts a number, and keeps the result between 0 and 255
- Threshold: pixels at or above a cutoff become white (255), and the rest become black (0)

**Geometric operations** (pixels move around)
- Flip left-right
- Flip up-down
- Rotate 90 degrees clockwise

**Neighbourhood operation** (each pixel looks at the pixels around it)
- Edge detection with a 3x3 kernel

**Bonus**
- RGB colour images, where each pixel is `[red, green, blue]`
- Writing and reading PPM (P3) files by hand
- Colour to grayscale conversion
- Colour invert

## How to run

You need Python 3 and nothing else.

```
python3 imageTools.py
```

The program prints the original image and the result of every operation. It also creates a small file called `test.ppm`.

## Example

```
Original                    Rotate right
   10   10   10   10   10      10   10   10   10   10
   10  200   10   10   10      10  200  200  200   10
   10  200   10   10   10      10  200   10   10   10
   10  200  200  200   10      10  200   10   10   10
   10   10   10   10   10      10   10   10   10   10
```

## How the edge detection works

The kernel is a 3x3 grid of weights:

```
-1 -1 -1
-1  8 -1
-1 -1 -1
```

For each pixel, the program multiplies the pixel and its 8 neighbours by the matching weights and adds everything up. In a flat area the sum is 0 (black). Where the brightness changes sharply the sum is large (bright), so edges show up.

**Border handling:** pixels on the edge of the image have missing neighbours. When a neighbour is outside the image, the program uses the nearest pixel that does exist (the border pixel is "copied" outward). This was chosen because:
- it is simple to understand and to code,
- a plain background does not create fake edges along the border,
- the output image keeps the same size as the input.

## PPM format

PPM (P3) is a plain text image format. It is easy to read by hand:

```
P3
3 3
255
255 0 0
0 255 0
...
```

The lines are: the magic word `P3`, then width and height, then the maximum value (255), then one line of `red green blue` per pixel.

## Project layout

```
imageTools.py   all the code
README.md       this file
test.ppm        created when you run the program
```

## Notes

- All results are returned as new images. The original image is never changed.
- Variable names are kept short and simple on purpose, and the code uses plain loops so it is easy to follow.
