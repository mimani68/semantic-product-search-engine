import os
from pinecone import Pinecone
import json
from utiles.image_embedding import image_embedding

from dotenv import load_dotenv

load_dotenv()

EMBEDDING_FILE = "./database/image_embeddings.json"

image_folder = os.getenv("IMAGE_FOLDER")
image_files = os.listdir(image_folder)

def encode_image_job():
    db_type = os.getenv("DB_TYPE")
    image_embeddings = {}
    for image_file in image_files:
        print(f"EMBEDDING | {image_file}")
        image_path = os.path.join(image_folder, image_file)
        image_embeddings[image_file] = image_embedding(image_path)

        if db_type != "JSON":
            api_key = os.getenv("PINECONE_API_KEY")
            index_name = os.getenv("PINECONE_INDEX_NAME")
            namespace = os.getenv("PINECONE_NAMESPACE")
            pc = Pinecone(
                api_key=api_key,
            )

            index = pc.Index(host=index_name)
            upsert_response = index.upsert(
                vectors=[
                    ("embedding", image_embeddings[image_file], {"file": image_file}),
                ],
                namespace=namespace
            )

            print(f"Images {image_file} embedded and stored in Pinecone database successfully.")
        
    if db_type == "JSON":
        with open(EMBEDDING_FILE, "w") as f:
            json.dump(image_embeddings, f)
