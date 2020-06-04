from PIL import Image, ImageChops, ImageOps, ImageDraw
import numpy as np
import math

img1 = Image.open('./Problems/Basic Problems B/Basic Problem B-09/A.png').convert('RGB')
img2 = Image.open('./Problems/Basic Problems B/Basic Problem B-12/C.png').convert('RGB')


def consecutive_average(a):
    new_arr = []
    add_all = 0
    count = 1
    for x in range(len(a) - 1):
        if a[x + 1] == a[x] + 1:
            if count == 1:
                add_all += a[x] + a[x + 1]
            else:
                add_all += a[x + 1]
            count += 1
        else:
            new_arr.append(add_all / count)
            count = 1
            add_all = 0
    return new_arr

# TODO problem 10. A - B

# diff = ImageChops.difference(img2, img1)


# def _color_diff(color1, color2):
#     """
#     Uses 1-norm distance to calculate difference between two values.
#     """
#     if isinstance(color2, tuple):
#         return sum([abs(color1[i] - color2[i]) for i in range(0, len(color2))])
#     else:
#         return abs(color1 - color2)
#
#
# def floodfill(image, xy, value, border=None, thresh=0):
#     """
#     (experimental) Fills a bounded region with a given color.
#     :param image: Target image.
#     :param xy: Seed position (a 2-item coordinate tuple). See
#         :ref:`coordinate-system`.
#     :param value: Fill color.
#     :param border: Optional border value.  If given, the region consists of
#         pixels with a color different from the border color.  If not given,
#         the region consists of pixels having the same color as the seed
#         pixel.
#     :param thresh: Optional threshold value which specifies a maximum
#         tolerable difference of a pixel value from the 'background' in
#         order for it to be replaced. Useful for filling regions of
#         non-homogeneous, but similar, colors.
#     """
#     # based on an implementation by Eric S. Raymond
#     # amended by yo1995 @20180806
#     pixel = image.load()
#     x, y = xy
#     try:
#         background = pixel[x, y]
#         if _color_diff(value, background) <= thresh:
#             return  # seed point already has fill color
#         pixel[x, y] = value
#     except (ValueError, IndexError):
#         return  # seed point outside image
#     edge = {(x, y)}
#     # use a set to keep record of current and previous edge pixels
#     # to reduce memory consumption
#     full_edge = set()
#     while edge:
#         new_edge = set()
#         for (x, y) in edge:  # 4 adjacent method
#             for (s, t) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
#                 # If already processed, or if a coordinate is negative, skip
#                 if (s, t) in full_edge or s < 0 or t < 0:
#                     continue
#                 try:
#                     p = pixel[s, t]
#                 except (ValueError, IndexError):
#                     pass
#                 else:
#                     full_edge.add((s, t))
#                     if border is None:
#                         fill = _color_diff(p, background) <= thresh
#                     else:
#                         fill = p != value and p != border
#                     if fill:
#                         pixel[s, t] = value
#                         new_edge.add((s, t))
#         full_edge = edge  # discard pixels processed
#         edge = new_edge
#
#
# def fill_shape(a):
#     floodfill(a, xy=(0, 0), value=(255, 0, 255))  # fill around shape with magenta
#     a = np.array(a)
#     a[(a[:, :, 0:3] != [255, 0, 255]).any(2)] = [0, 0, 0]  # fill remaining white pixes with black
#     a[(a[:, :, 0:3] == [255, 0, 255]).all(2)] = [255, 255, 255]  # Revert magenta pixels to white
#     return Image.fromarray(a)
#


# fill_shape(img1).show()

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
    return np.mean(np_a == np_b)  # >= .95


def o(var):
    # return Image.open('./Problems/Basic Problems B/Basic Problem B-10/' + var + '.png').convert('RGB')
    # return Image.open('./Problems/Challenge Problems C/Challenge Problem C-01/' + var + '.png').convert('RGB')
    return Image.open('./Problems/Basic Problems C/Basic Problem C-02/' + var + '.png').convert('RGB')


pset = list("ABCDEFGH")
#
# A = np.array([0, 0, 0, 255, 255, 0, 0, 0, 0, 255])
#
# np_a = np.array(o("A"))
#
# idx = (np_a > -1) * (np_a < 1)
# print(np.where(idx))
#
# with np.printoptions(threshold=np.inf):
#     print(np.unique(np.where(idx)))

# np_a[:] = 0


# np_a[math.floor(np_a.shape[1] / 2), :] = 255
#
# print(np_a.shape[1])
#
# Image.fromarray(np_a).show()
# np_a = np.array(o(str("3")))
# idx = (np_a[math.floor(np_a.shape[1] / 2), :] > -1) * (np_a[math.floor(np_a.shape[1] / 2), :] < 1)
# # print(np.where(idx))
#
# with np.printoptions(threshold=np.inf):
#     print(np.unique(np.where(idx)), "3")

"""
Are they all the same size? check size first
is there a change of value in the position from problem to problem or does it stay relatively the same?

Stupid circle may have to draw more than one line or draw one that is not as centered

do everything twice or three times... Low, Med, High
"""
np_a = np.array(o(str("4")))
idx = (np_a[math.floor(np_a.shape[1] / 2), :] > -1) * (np_a[math.floor(np_a.shape[1] / 2), :] < 1)
idx2 = (np_a[math.floor((np_a.shape[1]+70) / 2), :] > -1) * (np_a[math.floor((np_a.shape[1]+70) / 2), :] < 1)
# print(np.where(idx))

with np.printoptions(threshold=np.inf):
    print(consecutive_average(np.unique(np.where(idx))), "4")
    print(consecutive_average(np.unique(np.where(idx2))), "4")

for i in pset:
    np_a = np.array(o(str(i)))
    idx = (np_a[math.floor(np_a.shape[1] / 2), :] > -1) * (np_a[math.floor(np_a.shape[1] / 2), :] < 1)
    # print(np.where(idx))
    #print(consecutive_average(np.unique(np.where(idx))))

    with np.printoptions(threshold=np.inf):
        print(" ")
        print(consecutive_average(np.unique(np.where(idx))), i)
        # print(np.unique(np.where(idx)).size, np.unique(np.where(idx)), i)

a = [0, 1, 2, 26, 27, 28, 29, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
     101, 102, 103, 104, 154, 155, 156, 157]


#
# print(np.count_nonzero(o(str(4))), 4)

# a = o("G")
# b = o("H")
# c = o("4")
# # d = o("4")
# print(np.count_nonzero(a))
# print(np.count_nonzero(b))
# print(np.count_nonzero(c))
# for i in range(1, 9):
#     print(np.count_nonzero(o(str(i))), i)


# print(close_enough(d, c))
# white = (255, 255, 255)
# rot = a.convert('RGBA').rotate(315, expand=0)
# fff = Image.new('RGBA', rot.size, (255,)*4)
# out = Image.composite(rot, fff, rot)
# out.convert(a.mode).show()
# a = np.array(a.rotate(315, Image.NEAREST, expand=0, fillcolor=white))
# b = np.array(b)
# print(np.mean(a == b))
# a = np.array(a.rotate(270))
# b = np.array(o("6"))
# # print(np.mean(a == b))
# # print(close_enough(a, b))
# black_pixels_a = np.all(o("A") == [0, 0, 0], axis=-1)
# black_pixels_b = np.all(o("B") == [0, 0, 0], axis=-1)
# black_pixels_c = np.all(o("C") == [0, 0, 0], axis=-1)
# black_pixels_6 = np.all(o("6") == [0, 0, 0], axis=-1)
#
# print(black_pixels_a, black_pixels_b, black_pixels_c, black_pixels_6)
# c = np.array(o("C"))
# three = np.array(o("3"))

# print("a=b", np.mean(a == b))
# print("n=b", np.mean(b == c))
# print("a=c", math.floor(np.mean(a == b)))
# print("b=3", np.mean(b == three))


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


# def margin_of_error(a, b, moe=1):
#     """
#     This will check if the values are within the margin of error
#     3 give or take
#     """
#     print(a - moe)
#     print(b)
#     print(a + moe)
#     if a - moe <= b <= a + moe:
#         return True
#     return False
#
#
# def similarity_score(a, b):
#     np_a = np.array(a)
#     np_b = np.array(b)
#     return np.mean(np_a == np_b)
#
#
# def a_2_c_as_b_2_x():
#     """A is to C as B is to X"""
#     a = o("A")
#     b = o("B")
#     c = o("C")
#     sim_score = math.floor(similarity_score(a, c) * 100)
#     for i in range(1, 7):
#         if margin_of_error(math.floor(similarity_score(b, o(str(i))) * 100), sim_score):
#             return i
#     return -1
#
#
# print(a_2_c_as_b_2_x())
