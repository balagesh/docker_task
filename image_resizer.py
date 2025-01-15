from PIL import Image
import os


input_folder = './input_images'
output_folder = './output_images'

desired_size = (100, 100)

for filename in os.listdir(input_folder):
    with Image.open(os.path.join(input_folder, filename)) as img:
        img.thumbnail(desired_size)
        img.save(os.path.join(output_folder, filename))
        print(f"Ready: {filename}")
