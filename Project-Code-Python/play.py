from PIL import Image, ImageChops, ImageOps

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
    return Image.open('./Problems/Basic Problems B/Basic Problem B-04/' + var + '.png').convert('RGB')


a = o("A")
b = o("B")
a_mirror = ImageOps.mirror(a)
diff = ImageChops.difference(a_mirror, b)
print(diff.getbbox())  # they are different?????? aaaahhhh!!!!

diff.show()
a_mirror.show()
b.show()
