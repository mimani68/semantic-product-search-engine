import os

from utiles.database import pinecone

def db_ops(args):
    conn = pinecone.connection()
    index = conn.Index(os.getenv('PINECONE_INDEX_NAME'))
    
    # INDEX status
    print('🚩 INDEX status')
    print(index.describe_index_stats())

    # List of ids
    print('🚩 List of ids')
    for ids in index.list(namespace=os.getenv('PINECONE_NAMESPACE')):
        print(ids)

    # List of items
    print('🚩 List items')
    items = index.list_paginated(
        # prefix='pref',
        limit=5,
        namespace=os.getenv('PINECONE_NAMESPACE')
    )
    # print(items)
    print(items.vectors)