from colorit import init_colorit, color
from PIL import Image

init_colorit()
x = int(input("Размер: "))

image = Image.open(input("Файл: "))
image = image.resize((x, x))

for y in range(image.size[1]):
    for x in range(image.size[0]):
        print(color("w", image.getpixel((x, y))), end='')
    print()
