import os
from pinecone import Pinecone
import torch
import clip
from PIL import Image
import json
from dotenv import load_dotenv

from utiles.image_manipulation import clean_and_transform_photo

load_dotenv()

device = "cuda" if torch.cuda.is_available() else "cpu"
model = clip.load("ViT-B/32", jit=False)[0].to(device)

image_folder = os.getenv("IMAGE_FOLDER")
image_files = os.listdir(image_folder)

def encode_image():
    db_type = os.getenv("DB_TYPE")
    image_embeddings = {}
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(clean_and_transform_photo(image_path))
        image_input = clip.tokenize([image]).to(device)
        
        with torch.no_grad():
            embedding = model.encode_image(image_input)
        
        embedding_list = embedding[0].tolist()
    
    if db_type == "JSON":
        image_embeddings[image_file] = embedding_list
        
        with open("image_embeddings.json", "w") as f:
            json.dump(image_embeddings, f)
    
        print("Images embedded and stored in JSON file successfully.")
    else:
        api_key = os.getenv("PINECONE_API_KEY")
        index_name = os.getenv("INDEX_NAME")
        namespace = os.getenv("NAMESPACE")
        pc = Pinecone(
            api_key=api_key,
            # proxy_url='https://your-proxy.com'
        )
        # pc.create_index(
        #     name=index_name,
        #     dimension=1536,
        #     metric='euclidean',
        #     # spec=ServerlessSpec(
        #     #     cloud='aws',
        #     #     region='us-west-2'
        #     # )
        # )
        index = pc.Index(host=index_name)
        upsert_response = index.upsert(
            vectors=[
                ("embedding", embedding_list, {"file": image_file}),
            ],
            namespace=namespace
        )

        print("Images embedded and stored in Pinecone database successfully.")
