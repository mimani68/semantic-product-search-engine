import os
import json
from pinecone import Pinecone
from dotenv import load_dotenv

from utiles.image_embedding import image_embedding

load_dotenv()

PRODUCT_JSON_FILE = os.getenv("PRODUCT_JSON_FILE")
PRODUCT_EMBEDDING_LIMIT = os.getenv("PRODUCT_EMBEDDING_LIMIT")

def product_encoding_job():
    counter = 0
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX_NAME")
    namespace = os.getenv("PINECONE_NAMESPACE")
    pc = Pinecone(
        api_key=api_key,
    )
    index = pc.Index(host=index_name)

    with open(PRODUCT_JSON_FILE, "r") as f:
        products = json.loads(f.read())

    for item in products:
        if counter > PRODUCT_EMBEDDING_LIMIT:
            break
        counter = counter+1
        print(f"Product | {item['name']}")
        if len(item['images']) <= 0:
            continue

        upsert_response = index.upsert(
            vectors=[
                ("embedding", image_embedding(item['images'][0]), 
                    {
                        "code": item['code'],
                        "title": item['name'],
                        "keywords": item['title'],
                        "description": item['description'],
                    }
                ),
            ],
            namespace=namespace
        )
