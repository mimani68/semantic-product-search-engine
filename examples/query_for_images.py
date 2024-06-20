import torch, clip, json
from PIL import Image

NUMBER_OF_RANK=2
QUERY_TEXT='automotive'

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

text = clip.tokenize([QUERY_TEXT]).to(device)

image_database = [Image.open(f"images/{number}.jpg") for number in range(1,6)]
image_database_processed = [
    preprocess(im) for im in image_database
]
with torch.no_grad():
    image_features = model.encode_image(torch.stack(image_database_processed))
    text_features = model.encode_text(text)

with open("./database/image_embeddings.json", "w") as f:
    json.dump(image_features.tolist(), f)

with open("./database/image_embeddings.json", "r") as f:
    image_features_loaded = json.loads(f.read())
    image_features_loaded = torch.stack([torch.Tensor(item) for item in image_features_loaded])

image_features_loaded /= image_features_loaded.norm(dim=-1, keepdim=True)
text_features /= text_features.norm(dim=-1, keepdim=True)
similarity = (100.0 * text_features @ image_features_loaded.T).softmax(dim=-1)
values, indices = similarity[0].topk(NUMBER_OF_RANK)

print("Top predictions:")
for value, index in zip(values, indices):
    print(f"image={index.tolist()+1}.jpg ({value.tolist()})")

# Top predictions:
# image=5.jpg (0.6776257157325745)
# image=1.jpg (0.31812483072280884)
