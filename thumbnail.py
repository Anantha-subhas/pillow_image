from PIL import Image, ImageFilter
import os

#  create dirs
os.makedirs("200", exist_ok=True)
os.makedirs("500", exist_ok=True)
size_200 = (200, 200)
size_500 = (500, 500)

for f in os.listdir("images"):
    if f.endswith(".jpg") or f.endswith("jpeg"):
        i = Image.open(f"images/{f}")

        fn, ln = os.path.splitext(f)

        i.thumbnail(size_200)
        i.save(f"200/{fn}200{ln}")  # don't use . ln comes with .jpeg

        i.thumbnail(size_500)
        i.save(f"500/{fn}500{ln}")

img = Image.open("images/img1.jpeg")
img.rotate(90).save("images/img1-rotate.jpeg")

convert = Image.open("images/img2.jpg")
img.convert(mode="L").save("images/b&w.jpg")

blur_img = Image.open("images/img2.jpg")
img.filter(ImageFilter.GaussianBlur(10)).save("images/img2_blur.jpg")