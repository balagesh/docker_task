from PIL import Image
import os


input_folder = os.getenv('INOUT _FOLDER', 'input_images')
output_folder = os.getnev('OUTPUT_FOLDER', 'output_images')

if not os.path.exist(output_folder):
    os.makedirs(output_folder)

desired_size = (100, 100)

for filename in os.listdir(input_folder):
    with Image.open(os.path.join(input_folder, filename)) as img:
        img.thumbnail(desired_size)
        img.save(os.path.join(output_folder, filename))
        print(f"Ready: {filename}")
