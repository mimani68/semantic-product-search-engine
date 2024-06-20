import clip, os
import torch
from PIL import Image
from utiles.image_manipulation import clean_and_transform_photo

def image_embedding(image_path: str):

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load(os.getenv('CLIP_MODEL'), device=device)

    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    # image = clean_and_transform_photo(image_path)

    image_features = model.encode_image(image)

    return image_features

