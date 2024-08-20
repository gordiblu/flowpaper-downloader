from PIL import Image
import os

# folder path where .png are located
path = "images\\"

# filter by .png
images_files = sorted(
    [f for f in os.listdir(path) if f.endswith(".png")],
    key=lambda x: int(os.path.splitext(x)[0].replace("bbd", ""))
)

# char images in object image list
images = [Image.open(os.path.join(path, f)) for f in images_files]

# pdf file name and path
pdf_path = f"{path}images.pdf"

# Save
images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
