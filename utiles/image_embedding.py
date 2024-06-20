import clip, os
import torch
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"

def image_embedding(image_path: str):
    model, preprocess = clip.load(os.getenv('CLIP_MODEL'), device=device)
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    image_features = model.encode_image(image)
    return image_features.tolist()

