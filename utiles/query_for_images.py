from typing import List
import torch, clip

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def semantic_images_query(query: str, embedded_images: List[float], NUMBER_OF_RANK=2):
    result = []
    
    text = clip.tokenize([query]).to(device)
    with torch.no_grad():
        text_features = model.encode_text(text)

    image_features_loaded = torch.stack([torch.Tensor(item) for item in embedded_images])

    image_features_loaded /= image_features_loaded.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * text_features @ image_features_loaded.T).softmax(dim=-1)
    values, indices = similarity[0].topk(NUMBER_OF_RANK)

    for value, index in zip(values, indices):
        result.append({
            "file_index": index.tolist(),
            "score": value.tolist()
        })

    return result
        

