# Pure-Python-Image-Preprocessor

# Image Preprocessor

A small Python program that works on images stored as plain lists of numbers. It uses no libraries, only basic loops, lists and functions. I wrote it for my MES_1002 assignment to understand how image operations work underneath.

## How images are stored

A grayscale image is a list of rows, and each row is a list of numbers from 0 (black) to 255 (white). The test image is a 5x5 "L" shape, which is small enough to check by eye. I used an L because it is not symmetric, so flips and rotations are easy to see.

A colour pixel is a list of three numbers: red, green and blue.

## What it does

Pixel operations
- invert
- brightness change (values are kept between 0 and 255)
- threshold (everything becomes black or white)

Geometric operations
- flip left to right
- flip top to bottom
- rotate 90 degrees clockwise

Neighbourhood operation
- edge detection with a 3x3 kernel (-1 around the edges, 8 in the middle)

Bonus
- write and read a PPM (P3) file by hand
- convert a colour image to grayscale
- invert a colour image

## Border handling

Pixels on the edge of the image have neighbours that do not exist. For those, I use the nearest pixel that does exist. I chose this because it is simple, and because it does not create fake edges along the border of a plain background. Filling the gaps with 0 would do that, and skipping the border would make the output image smaller.

## How to run

You need Python 3.

    python3 imageTools.py

It prints the original image and the result of each operation. It also creates a file called test.ppm, reads it back, and prints it as grayscale.

## Example

Original:

       10   10   10   10   10
       10  200   10   10   10
       10  200   10   10   10
       10  200  200  200   10
       10   10   10   10   10

Rotated right:

       10   10   10   10   10
       10  200  200  200   10
       10  200   10   10   10
       10  200   10   10   10
       10   10   10   10   10

## Notes

- Every function returns a new image and leaves the original alone.
- On this tiny image the edge detection output looks the same as the threshold output, because the difference between the L and the background is so large that it hits 255. It looks different on smoother images.
