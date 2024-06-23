import os
from urllib3 import make_headers
from pinecone import Pinecone

def connection():
    pc = Pinecone(
        api_key=os.getenv('PINECONE_API_KEY'),
        # proxy_url='https://your-proxy.com',
        # proxy_headers=make_headers(proxy_basic_auth='username:password'),
        # ssl_ca_certs='path/to/cert-bundle.pem'
    )
    return pc
