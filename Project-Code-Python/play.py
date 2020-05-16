from PIL import Image, ImageChops

img1 = Image.open('./Problems/Basic Problems B/Basic Problem B-01/A.png').convert('RGB')
img2 = Image.open('./Problems/Basic Problems B/Basic Problem B-12/C.png').convert('RGB')


diff = ImageChops.difference(img2, img1)

print(diff.getbbox())
if diff.getbbox():
    diff.show()


