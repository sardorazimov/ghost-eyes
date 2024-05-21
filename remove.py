from PIL import Image

def convert_image(file_path):
    img = Image.open(file_path)
    new_file_path = file_path.replace('.jpg', '.png')
    img.save(new_file_path)

# Kullanımı:
convert_image('im.jpg')
