import argparse
from utils import *


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
    args.add_argument("--pdf", type=str, default="https://arxiv.org/pdf/2305.11206.pdf")
    args.add_argument("--arxiv", type=str)
    args.add_argument("--verbose", type=bool, default=True)
    args.add_argument("--chunk_size", type=int, default=5000)
    args.add_argument("--outputfile", type=str)
    args.add_argument("--model", type=str, default="gpt-3.5-turbo-0613")
    config = args.parse_args()
    main(config)
