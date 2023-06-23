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
    args.add_argument("--pdf", type=str)
    args.add_argument("--arxiv", type=str)
    args.add_argument("--html", type=str, default='https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/Prompt_Injection.html')
    args.add_argument("--verbose", type=bool, default=True)
    args.add_argument("--chunk_size", type=int, default=5000)
    args.add_argument("--outputfile", type=str)
    args.add_argument("--model", type=str, default="gpt-3.5-turbo-16k")
    
    config = args.parse_args()
    
    if config.pdf:
        config.outputfile = config.pdf.split("/")[-1].split(".")[0] + ".md" 

    
    if config.html:
        config.outputfile = config.html.split("/")[-1].split(".html")[0] + ".md" 
    
    main(config)
