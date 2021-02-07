from PIL import Image
import os

original_folder = "import"
export_folder = "exporthex"
size = 512
w = 10
h = 17
factor = size / (h - 1)

def pixellate(image, w):
    d = 1
    pixels = image.load()
    result_image = Image.new(image.mode, (1000, 1000), color = (255, 255, 255))
    result_pixels = result_image.load()
    for y in range(h):
        for x in range(w -1):
            color = pixels[x * factor + (h - w) * factor / 2 + factor / 2, y * (factor * 0.87) + factor * 0.87 / 2]
            for yy in range(28):
                for xx in range(28):
                    result_pixels[x * factor + (h - w) * factor / 2 + factor / 2 + xx, y * (factor * 0.87) + factor * 0.87 / 2 + yy] = color
        w = w + d
        if w == h:
            d = -1

    return result_image

folder = os.listdir(original_folder)
for file in folder[:50]:
    img1 = Image.open(f"{original_folder}/{file}")
    result = pixellate(img1, w)
    result.save(f"{export_folder}/{file}")
