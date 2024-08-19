from PIL import Image
import os

# Ruta de la carpeta donde se encuentran las imágenes
images_folder = "images\\"

# Obtener la lista de archivos en la carpeta y filtrarla para que solo incluya archivos .png
images_files = sorted(
    [f for f in os.listdir(images_folder) if f.endswith(".png")],
    key=lambda x: int(os.path.splitext(x)[0].replace("bbd", ""))
)

# char images in object image list
images = [Image.open(os.path.join(images_folder, f)) for f in images_files]

# Ruta del archivo PDF de salida
pdf_path = "images\\images.pdf"

# Save
images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
