from PIL import Image, ImageChops, ImageOps, ImageDraw
import numpy as np
import math

img1 = Image.open('./Problems/Basic Problems B/Basic Problem B-09/A.png').convert('RGB')
img2 = Image.open('./Problems/Basic Problems B/Basic Problem B-12/C.png').convert('RGB')



def close_enough(a, b):
    np_a = np.array(a)
    np_b = np.array(b)
    return np.mean(np_a == np_b)  # >= .95


def o(var):
    # return Image.open('./Problems/Basic Problems B/Basic Problem B-10/' + var + '.png').convert('RGB')
    # return Image.open('./Problems/Challenge Problems C/Challenge Problem C-01/' + var + '.png').convert('RGB')
    return Image.open('./Problems/Basic Problems C/Basic Problem C-07/' + var + '.png').convert('RGB')


def np_print(arr):
    with np.printoptions(threshold=np.inf):
        print(arr)


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
    print(black_pixels-8151)
    print("")


for i in range(1, 9):
    black_pixels(i)

pset = list("ABCDEFGH")

for i in pset:
    black_pixels(i)


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