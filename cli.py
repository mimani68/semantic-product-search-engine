import argparse

from scripts.embedding_product_file import product_encoding_job
from scripts.embedding_sample_image_folder import encode_image_job
from scripts.database_provisioning import pinecone_db_provisioning

def main():
    parser = argparse.ArgumentParser(description="Data processing and indexing tool")
    subparsers = parser.add_subparsers(help='sub-command help')

    index_creator = subparsers.add_parser('index_creator', help='A help')
    # index_creator.add_argument('--namespace')

    args = parser.parse_args()

    if args == 'index_creator':
        pinecone_db_provisioning()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()