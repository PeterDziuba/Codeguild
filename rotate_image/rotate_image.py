from PIL import Image
img = Image.open("flowers.jpeg")

img2 = img.rotate(45)
img2.save("rotated.png")