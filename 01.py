from PIL import Image, ImageChops

p1 = Image.open("p1.jpg")
p2 = Image.open("p2.jpg")


farkbul = ImageChops.difference(p1, p2)

if farkbul.getbbox():
    farkbul.show()