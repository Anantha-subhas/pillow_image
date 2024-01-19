from PIL import Image
import os

# Specify the directory containing the images
image_directory = "images"

# Create a new directory for saving PNGs
output_directory = "output_png"
os.makedirs(output_directory, exist_ok=True)

for file in os.listdir(image_directory):
    if file.endswith(".jpeg") or file.endswith(".jpg"):
        # Construct the full path to the image file
        file_path = os.path.join(image_directory, file)

        # Open the image using the full path
        img = Image.open(file_path)

        # Separate the filename and extension
        img_name, img_ext = os.path.splitext(file)

        # Specify the full path for saving the PNG
        output_path = os.path.join(output_directory, "{}.png".format(img_name))

        # Save the image as PNG
        img.save(output_path)

# Display the list of files in the output directory
print(os.listdir(output_directory))
