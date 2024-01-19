from PIL import Image
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