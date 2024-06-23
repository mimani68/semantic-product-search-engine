import os

from utiles.database import pinecone

def db_ops(args):
    conn = pinecone.connection()
    index = conn.Index(os.getenv('PINECONE_INDEX'))

    # Delete namespace
    # index.delete(delete_all=True, namespace=os.getenv('PINECONE_NAMESPACE'))

    # Delete one element
    # index.delete(ids=['4353063_12232972'], namespace=os.getenv('PINECONE_NAMESPACE'))

    INDEX status
    print('🚩 INDEX status')
    print(index.describe_index_stats())

    # List of ids
    print('🚩 List of ids')
    for ids in index.list(namespace=os.getenv('PINECONE_NAMESPACE'), limit=100):
        print(ids)

    # List of items
    print('🚩 List items')
    items = index.list_paginated(
        # prefix='pref',
        limit=5,
        namespace=os.getenv('PINECONE_NAMESPACE'),
    )
    print(items.vectors)

    # # Get example
    # print('🚩 Get single item')
    # sample_item = index.fetch(["id1016190_Multi"], namespace=os.getenv('PINECONE_NAMESPACE'))
    # print(sample_item)