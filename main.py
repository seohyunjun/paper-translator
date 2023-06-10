import argparse
from utils import *

def main(config):
    
    ## Paper Loader
    load_paper(config)

    ## Splitter
    splitter(config)
    
    translate(config)
    ################################################
if __name__=='__main__':
    # argeparse
    args = argparse.ArgumentParser()
    args.add_argument('--pdf', type=str, default='https://arxiv.org/pdf/2305.11206.pdf')
    args.add_argument('--arxiv', type=str)
    args.add_argument('--verbose', type=bool, default=True)
    args.add_argument('--max_tokens', type=int, default=1000)
    args.add_argument('--chunk_size', type=int, default=800)
    args.add_argument('--outputfile', type=str)
    config = args.parse_args()                  
    main(config)
    