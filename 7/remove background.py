import rembg
from PIL import Image


input_image = Image.open ("dino.jpg.jpg")
output_image = rembg.remove(input_image)
output_image.save("result.png")