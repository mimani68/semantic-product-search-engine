from dotenv import load_dotenv

from scripts.embedding_product_file import product_encoding_job

load_dotenv()

product_encoding_job()