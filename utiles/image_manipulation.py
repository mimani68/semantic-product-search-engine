import os
from PIL import Image

def clean_and_transform_photo(photo_path, output_size=(512, 512)):
    try:
        dir_name, file_name = os.path.split(photo_path)
        name, ext = os.path.splitext(file_name)
        output_path = os.path.join(dir_name, f"{name}_cleaned{ext}")        
        with Image.open(photo_path) as img:
            img = img.resize(output_size)
            img = img.convert('L')
            img.save(output_path)
            return img
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return

transformed_image = clean_and_transform_photo("images/1.jpg")
