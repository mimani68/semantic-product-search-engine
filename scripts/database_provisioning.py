import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

def pinecone_db_provisioning():
    # pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
    # from pinecone import Pinecone, ServerlessSpec

    # pc.create_index(
    #     name=os.getenv("PINECONE_INDEX_NAME"),
    #     dimension=755,
    #     metric="euclidean",
    #     spec=ServerlessSpec(
    #         cloud="aws",
    #         region="us-east-1"
    #     ) 
    # )
    print("Salam")