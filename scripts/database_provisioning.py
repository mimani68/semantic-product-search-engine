import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

def pinecone_db_provisioning(args):
    pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
    pc.create_index(
        name=os.getenv("PINECONE_INDEX_NAME"),
        dimension=755,
        metric="euclidean",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ) 
    )
    print("Database provisioning has been done")