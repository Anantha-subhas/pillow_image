from PIL import Image
import os

# image1 = Image.open("images/img1.jpeg")
# image1.show()

# image1.save("images/img1.png")

# print(os.listdir("images")) this shows all the file inside an img directory (".") => <entire dir>

# Create a new directory for saving PNGs
output_directory = "pngs"
os.makedirs(output_directory, exist_ok=True)

for file in os.listdir("images"):
    if file.endswith(".jpeg") or file.endswith(".jpg"):  # both jpeg and jpg
        i = Image.open(f"images/{file}")  # open an img file
        i_name, i_exe = os.path.splitext(file)  # separated by a dot eg: img1.jpeg "img1" "jpeg"
        i.save(f"{output_directory}/{i_name}.png")  # already created pngs_dir