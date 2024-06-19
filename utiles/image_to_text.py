import clip, os
import torch
from PIL import Image
from typing import List
from utiles.image_manipulation import clean_and_transform_photo

def image_to_text(image_path: str, labels: List[str]):

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load(os.getenv('CLIP_MODEL'), device=device)

    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    # image = clean_and_transform_photo(image_path)
    text = clip.tokenize(labels).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
        
        logits_per_image, logits_per_text = model(image, text)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()

    return probs[0].tolist()


# print(image_to_text('./images/1.jpg', ["Shoreline", "a dog", "a cat", "seaside landscape"]))