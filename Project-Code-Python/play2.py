from PIL import Image, ImageChops, ImageOps, ImageDraw
import numpy as np
import math

img1 = Image.open('./Problems/Basic Problems B/Basic Problem B-09/A.png').convert('1')
img2 = Image.open('./Problems/Basic Problems B/Basic Problem B-12/C.png').convert('1')



def close_enough(a, b):
    np_a = np.array(a)
    np_b = np.array(b)
    return np.mean(np_a == np_b)  # >= .95


def o(var):
    # return Image.open('./Problems/Basic Problems B/Basic Problem B-10/' + var + '.png').convert('RGB')
    # return Image.open('./Problems/Challenge Problems C/Challenge Problem C-01/' + var + '.png').convert('RGB')
    return Image.open('./Problems/Basic Problems C/Basic Problem C-09/' + var + '.png').convert('1')


a = o("A")
c = o("C")
width, height = a.size
# box=(left, upper, right, lower)

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    #Bounding box given as a 4-tuple defining the left, upper, right, and lower pixel coordinates.
    #If the image is completely empty, this method returns None.
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

#c = c.crop((0, 0, width/2, height))

#a = a.crop((width/2, 0, width, height))

def left_side(x):
    width, height = x.size
    return trim(x.crop((0, 0, width / 2, height)))

def right_side(x):
    width, height = x.size
    return trim(x.crop((width / 2, 0, width, height)))


print(close_enough(left_side(a), right_side(c)), "test for close enough")


c = right_side(c).show()
a = left_side(a).show()
# a = np.array(o(str("4")))
# a = np.array(o(str("H")))
# b = np.array(o(str("G")))
# print(np.linalg.norm(b-a), "g-h")
#


def margin_of_error(a, b, moe=1):
    """
    This will check if the values are within the margin of error
    3 give or take
    """
    if a - moe <= b <= a + moe:
        return True
    return False


last = 0
last_diff = 0


def black_pixels(i):
    global last_diff, last
    a = np.array(o(str(i)))
    black_pixels = ((-1 < a) & (a < 50)).sum()
    if margin_of_error(1305, black_pixels-8151, 200):
        print("this is the one!!!!")
    this_diff = black_pixels - last
    print(black_pixels, this_diff, i)
    last_diff = this_diff
    last = black_pixels
    print(black_pixels-8736)
    print("")



for i in range(1, 9):
    black_pixels(i)

pset = list("ABCDEFGH")

for i in pset:
    black_pixels(i)

print(abs(9053-100), "test")
# Dynamic Programming implementation of LCS problem

# end of function lcs


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
# print("Length of LCS is ", lcs(a, b))

# 21871.790736014278
# 20096.21173256293
# 6090709389
# 6150440958