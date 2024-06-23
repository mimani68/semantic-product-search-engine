import argparse
import logging

from scripts.embedding_product_file import product_encoding_job
from scripts.database_provisioning import pinecone_db_provisioning

def main():
    parser = argparse.ArgumentParser(description="Data processing and indexing tool")
    subparsers = parser.add_subparsers(help='sub-command help')

    index_creator = subparsers.add_parser('index_creator', help='A tools for create database provisioning')
    index_creator.add_argument('--loglevel')
    index_creator.add_argument('--namespace')
    index_creator.set_defaults(func=pinecone_db_provisioning)

    job_crawling = subparsers.add_parser('job_crawling', help='A tools for download product list and store in db')
    job_crawling.set_defaults(func=product_encoding_job)
    
    args = parser.parse_args()

    if hasattr(args, 'func'):
        # if args.loglevel:
        #     logging.basicConfig(level=args.loglevel.upper())
        args.func(args)
        return 0
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    main()