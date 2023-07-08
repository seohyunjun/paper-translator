import argparse
from utils2 import *


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
    args.add_argument("--verbose", type=bool, default=True)
    args.add_argument("--chunk_size", type=int, default=5000)
    args.add_argument("--outputfile", type=str, default='test.md')
    #args.add_argument("--model", type=str, default="gpt-4-0613")
    args.add_argument("--model", type=str, default="gpt-3.5-turbo-16k")
    config = args.parse_args()

    main(config)
