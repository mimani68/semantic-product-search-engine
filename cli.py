import argparse
import logging

from scripts.embedding_product_file import product_encoding_job
from scripts.embedding_sample_image_folder import encode_image_job
from scripts.database_provisioning import pinecone_db_provisioning

def main():
    parser = argparse.ArgumentParser(description="Data processing and indexing tool")
    subparsers = parser.add_subparsers(help='sub-command help')

    index_creator = subparsers.add_parser('index_creator', help='A tools for create database provisioning')
    index_creator.add_argument('--loglevel')
    index_creator.add_argument('--namespace')
    index_creator.set_defaults(func=pinecone_db_provisioning)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        if args.loglevel:
            logging.basicConfig(level=args.loglevel.upper())
        args.func(args)
        return 0
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    main()