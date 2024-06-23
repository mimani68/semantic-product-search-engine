import os, json, requests
from pinecone import Pinecone
from dotenv import load_dotenv

from utiles.image_embedding import image_embedding

load_dotenv()

PRODUCT_JSON_FILE = os.getenv("PRODUCT_JSON_FILE")
PRODUCT_EMBEDDING_LIMIT = os.getenv("PRODUCT_EMBEDDING_LIMIT")

def product_encoding_job(args):
    counter = 0
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX")
    namespace = os.getenv("PINECONE_NAMESPACE")
    pc = Pinecone(
        api_key=api_key,
    )
    index = pc.Index(name=index_name)

    with open(PRODUCT_JSON_FILE, "r") as f:
        products = json.loads(f.read())

    ids = index.list(namespace=namespace)
    ids = [id for id in ids]

    for item in products:
        if counter > int(PRODUCT_EMBEDDING_LIMIT):
            break
        counter = counter+1

        # Skip any duplicated
        if item['code'] in ids[0]:
            print(f"Skip code={item['code']} title={item['name']}")
            continue

        print(f"Product | {item['name']}")
        if len(item['images']) <= 0:
            continue
        
        # Get/Download image
        response = requests.get(item['images'][0])
        if response.status_code != 200:
            print(f"Encounter download {item['name']} image")
            continue

        # Insert to database 
        upsert_response = index.upsert(
            vectors=[
                {
                    "id": item['code'],
                    "values": image_embedding(response.content)[0], 
                    "metadata": {
                        "code": item['code'],
                        "name": item['name'] or "*",
                        "description": item['description'] or "*",
                        "brand_name": item['brand_name'] or "*",
                        "material": item['material'] or "*",
                        "rating": item['rating'] or "*",
                        "current_price": item['current_price'] or "*",
                        "images": item['images'] or "*",
                        "old_price": item['old_price'] or "*",
                        "off_percent": item['off_percent'] or "*",
                    }
                }
            ],
            namespace=namespace,
        )
