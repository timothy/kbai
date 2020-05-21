from PIL import Image, ImageChops, ImageOps
import numpy as np
import math
img1 = Image.open('./Problems/Basic Problems B/Basic Problem B-01/A.png').convert('RGB')
img2 = Image.open('./Problems/Basic Problems B/Basic Problem B-12/C.png').convert('RGB')


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

def o(var):
    return Image.open('./Problems/Basic Problems B/Basic Problem B-05/' + var + '.png').convert('RGB')


a = o("A")
b = o("B")
a_mirror = ImageOps.mirror(a)
# a_mirror.show()
# a.rotate(90).show()
# b.rotate(90).show()
# a.rotate(180).show()
#
# a.rotate(270).show()


# b.show()
# ImageChops.difference(a_mirror, b).show()
np_a = np.array(a)
np_b = np.array(b)
result = np.mean(np_a == np_b)
print(math.floor(result * 100))

np_a = np.array(o("C"))
np_b = np.array(o("1"))
result = np.mean(np_a == np_b)
print(math.floor(result * 100))
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
