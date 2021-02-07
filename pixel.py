from PIL import Image
import os

original_folder = "import"
export_folder = "export"
size = 512
steps = 64
factor = 8

def pixellate(image):
    pixels = image.load()
    result_image = Image.new(mode = "RGBA", size=image.size)
    result_pixels = result_image.load()
    for y in range(steps):
        for x in range(steps):
            color = pixels[x * factor, y * factor]
            for yy in range(factor):
                for xx in range(factor):
                    result_pixels[x * factor + xx, y * factor + yy] = color
    return result_image

folder = os.listdir(original_folder)
for file in folder:
    img1 = Image.open(f"{original_folder}/{file}")
    result = pixellate(img1)
    result.save(f"{export_folder}/{file}")
