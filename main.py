import argparse
from utils import *
from dotenv import load_dotenv
load_dotenv()


def main(config):

    ## Paper Loader
    load_paper(config)
    ## Splitter
    splitter(config)

    translate(config)
    ################################################

if __name__ == "__main__":
    # argeparse
    args = argparse.ArgumentParser()
    args.add_argument("--pdf", type=str)
    args.add_argument("--arxiv", type=str)
    args.add_argument("--html", type=str)
    args.add_argument("--youtube", type=str)
    args.add_argument("--verbose", type=bool, default=True)
    args.add_argument("--chunk_size", type=int, default=5000)
    args.add_argument("--outputfile", type=str, default='test.md')
    args.add_argument("--model", type=str, default="gpt-3.5-turbo-16k")
    args.add_argument("--embedding_model", type=str, default="text-embedding-3-small")
    args.add_argument("--title", type=str)
    # pinecone args
    args.add_argument("--pinecone", type=bool, default=False)
    args.add_argument("--chromadb", type=bool, default=True)
    config = args.parse_args()

    main(config)
