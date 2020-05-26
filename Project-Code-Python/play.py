from PIL import Image, ImageChops, ImageOps, ImageDraw
import numpy as np
import math

img1 = Image.open('./Problems/Basic Problems B/Basic Problem B-01/A.png').convert('RGB')
img2 = Image.open('./Problems/Basic Problems B/Basic Problem B-12/C.png').convert('RGB')


# TODO problem 10. A - B

# diff = ImageChops.difference(img2, img1)


# print(diff.getbbox())
# if diff.getbbox():
#     diff.show()


def te(*t):
    final = []
    for i in t:
        final.append(i)
    return final


# a, b, c = te(5, "this", 42)

# print(b)

def close_enough(a, b):
    np_a = np.array(a)
    np_b = np.array(b)
    return np.mean(np_a == np_b) >= .95


def o(var):
    return Image.open('./Problems/Basic Problems B/Basic Problem B-10/' + var + '.png').convert('RGB')


a = np.array(o("A"))
b = np.array(o("B"))
c = np.array(o("C"))
three = np.array(o("3"))

# print("a=b", np.mean(a == b))
# print("n=b", np.mean(b == c))
print("a=c", math.floor(np.mean(a == c)*100))
print("b=3", np.mean(b == three))


# ImageDraw.floodfill(a, xy=(0, 0), value=(255, 0, 255), thresh=200)

# a.show()
# n = np.array(a)
# ap = np.count_nonzero(a)
# bp = np.count_nonzero(b)
# cp = np.count_nonzero(c)
# threep = np.count_nonzero(three)
#
# print("a-c", abs(ap - cp))
# print("b-3", abs(threep - bp))
# print("diff", abs(abs(ap - cp) - abs(threep - bp)))
# print("c-3", cp - threep)
#
# print("n=b", np.mean(n == b))
# print("c=3", np.mean(c == three))
#

#
# print("a-c", ap - cp)
# print("b-3", bp - threep)
#
# print(ap, bp, cp, threep)

# n[(n[:, :, 0:3] != [255, 0, 255]).any(2)] = [0, 0, 0]
#
# # Revert all artifically filled magenta pixels to white
# n[(n[:, :, 0:3] == [255, 0, 255]).all(2)] = [255, 255, 255]
# Image.fromarray(n).show()
#
# print(np.mean(n == b))

# count all extra black pixals from A to B and find img with the same amount.

#######################################
# a = np.array(o("A"))
# b = np.array(o("B"))
# c = np.array(o("C"))
#
# x = a-c
# result = b+x
#
# Image.fromarray(result).show()
####################################
# a_mirror = ImageOps.mirror(a)
# # a_mirror.show()
# # a.rotate(90).show()
# # b.rotate(90).show()
# # a.rotate(180).show()
# #
# # a.rotate(270).show()
#
#
# # b.show()
# # ImageChops.difference(a_mirror, b).show()
# np_a = np.array(a)
# np_b = np.array(b)
# result = np.mean(np_a == np_b)
# print(math.floor(result * 100))
#
# np_a = np.array(o("C"))
# np_b = np.array(o("1"))
# result = np.mean(np_a == np_b)
# print(math.floor(result * 100))
# 0.9572010869565217
# a_mirror = ImageOps.mirror(a)
# diff = ImageChops.difference(a_mirror, b)
# print("diff", diff.getbbox())  # they are different?????? aaaahhhh!!!!
# print("not diff", ImageChops.difference(a, b).getbbox())

# diff.show()
# a_mirror.show()
# b.show()

# np_a = np.array(a_mirror)
#
# np_b = np.array(b)
#
# result = np.mean(np_a == np_b)
# print(result)

# new_im = Image.fromarray(result)
# new_im.show()
# new_im.save("numpy_altered_sample2.png")


def margin_of_error(a, b, moe=1):
    """
    This will check if the values are within the margin of error
    3 give or take
    """
    print(a - moe)
    print(b)
    print(a + moe)
    if a - moe <= b <= a + moe:
        return True
    return False


def similarity_score(a, b):
    np_a = np.array(a)
    np_b = np.array(b)
    return np.mean(np_a == np_b)


def a_2_c_as_b_2_x():
    """A is to C as B is to X"""
    a = o("A")
    b = o("B")
    c = o("C")
    sim_score = math.floor(similarity_score(a, c) * 100)
    for i in range(1, 7):
        if margin_of_error(math.floor(similarity_score(b, o(str(i))) * 100), sim_score):
            return i
    return -1


print(a_2_c_as_b_2_x())
