import argparse

from scripts.embedding_product_file import product_encoding_job
from scripts.database_provisioning import pinecone_db_provisioning
from scripts.get_database import db_ops

def main():
    parser = argparse.ArgumentParser(description="Data processing and indexing tool")
    subparsers = parser.add_subparsers(help='sub-command help')

    create_index = subparsers.add_parser('create_index', help='A tools for create database provisioning')
    create_index.add_argument('--namespace')
    create_index.set_defaults(func=pinecone_db_provisioning)

    job_crawling = subparsers.add_parser('job_crawling', help='A tools for download product list and store in db')
    job_crawling.set_defaults(func=product_encoding_job)
    
    db_ops_command = subparsers.add_parser('db_ops', help='')
    db_ops_command.set_defaults(func=db_ops)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
        return 0
    else:
        parser.print_help()
        return 0

if __name__ == "__main__":
    main()