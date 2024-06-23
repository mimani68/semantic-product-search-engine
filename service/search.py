import os

from utiles.text_embedding import text_embedding
from utiles.database.pinecone import connection

def semantic_image_search_service(query_text: str, number: int):
    if not query_text:
        return {
            "message": "Query is not defined."
        }
        
    if not number:
        number = 10
        
    # Embedded text query
    embedded_query_text = text_embedding(query_text)

    # Query something in data store
    conn = connection()
    index = conn.Index(os.getenv('PINECONE_INDEX'))
    result = index.query(
        namespace=os.getenv('PINECONE_NAMESPACE'),
        vector=embedded_query_text[0],
        top_k=number,
        include_values=False,
        include_metadata=True
    )
    return result


def text_search_service(query_text: str, number: int):
    if not query_text:
        return {
            "message": "Query is not defined."
        }
       
    if not number:
        number = 10
        
    # Query search result
    conn = connection()
    index = conn.Index(os.getenv('PINECONE_INDEX'))
    result = index.query(
        namespace=os.getenv('PINECONE_NAMESPACE'),
        top_k=number,
        filter={
            "title": {"$eq": query_text},
        },
        include_values=False,
        include_metadata=True
    )
    return result


def hybrid_search_service(query_text: str, number : int):
    if not query_text:
        return {
            "message": "Query is not defined."
        }
    
    if not number:
        number = 10

    # Embed query string
    embedded_query_text = text_embedding(query_text)
        
    # Query search result
    conn = connection()
    index = conn.Index(os.getenv('PINECONE_INDEX'))
    result = index.query(
        namespace=os.getenv('PINECONE_NAMESPACE'),
        vector=embedded_query_text,
        top_k=number,
        filter={
            "title": {"$eq": query_text},
        },
        include_values=False,
        include_metadata=True
    )
    return result