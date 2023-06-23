import openai

from langchain.document_loaders import PyPDFLoader, ArxivLoader

from langchain import LLMChain
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.callbacks import get_openai_callback
from tqdm import tqdm

from langchain.prompts import PromptTemplate
from langchain.document_loaders import UnstructuredURLLoader
import re


def clean_number(doc):
    """fix paper numbering"""
    doc_length = len(doc)
    for i in range(doc_length):
        if i == doc_length - 1:
            break

        if re.findall("\n[0-9]+", doc[i].page_content.split(" ")[-1]):
            doc[i + 1].page_content = (
                re.findall("\n[0-9]+", doc[i].page_content.split(" ")[-1])[-1]
                + "\n\n"
                + doc[i + 1].page_content
            )
            doc[i].page_content = doc[i].page_content[
                : -len(re.findall("\n[0-9]+", doc[i].page_content.split(" ")[-1])[-1])
            ]
    return doc


def load_paper(config):
    """Load paper from pdf or arxiv"""
    ## PDF Loader
    if config.pdf:
        loader = PyPDFLoader(config.pdf)
        load_paper = loader.load()
        assert load_paper, "Invalid pdf file"
        config.paper = load_paper
        print(f"page number: {len(load_paper)}")

    ## Arxiv Loader
    if config.arxiv:
        loader = ArxivLoader(query=config.arxiv)
        load_paper = loader.load()
        assert load_paper, "Invalid arxiv number"
        config.paper = load_paper
        print(f"page number: {len(load_paper)}")
    
    ## Unstructed HTML Loader
    if config.html:
        urls = [config.html]
        loader = UnstructuredURLLoader(urls=urls)
        load_paper = loader.load()

        assert load_paper, "Invalid html file"
        config.paper = load_paper
        print(f"page number: {len(load_paper)}")
    # return load_paper


def splitter(config):
    """splitter paper into chunk size"""

    ## splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.chunk_size, separators=["\n\n"]
    )
    ## splitter
    # text_splitter = CharacterTextSplitter(chunk_size=config.chunk_size, separator="\n\n")
    doc = text_splitter.split_documents(config.paper)
    doc = clean_number(doc)
    config.document = doc


def translate(config):
    ## LLM
    llm = ChatOpenAI(model=config.model)
    # llm = ChatOpenAI()
    chain = load_summarize_chain(llm, chain_type="stuff", verbose=config.verbose)
    
    
    if config.pdf:
        chain.llm_chain.prompt.template = """Please translate arxiv paper with Markdown format using header.
        you Must translate into Korean.
        Paper:\n\n{text}"""  # [5]
    
    if config.html:
        chain.llm_chain.prompt.template = """This is web page. \n
        following this guide.\n
        1. Output is Markdown format.\n
        2. You must translate into Korean.\n
        ```\n
        web page: {text}""" 
    
    print(f"document: {len(config.document)}")
    completion_tokens = 0
    prompt_tokens = 0
    total_cost = 0
    total_tokens = 0

    results = []
    for page in tqdm(config.document, total=len(config.document)):

        with get_openai_callback() as cb:

            result = chain.run([page])
            print(result)
            result.replace('```논문:', '')
            result.replace('```', '')
            result.replace('\n', '')
            

            completion_tokens += cb.completion_tokens
            prompt_tokens += cb.prompt_tokens
            total_cost += cb.total_cost
            total_tokens += cb.total_tokens
        results.append(result)
            
    print(f"completion_tokens: {completion_tokens}\n")
    print(f"prompt_tokens: {prompt_tokens}\n")
    print(f"total_cost: {total_cost}\n")
    print(f"total_tokens: {total_tokens}\n")

    for result in results:
        print(result)
    if config.outputfile:
        with open(config.outputfile, "w") as f:
            for result in results:
                f.writelines(result)

            f.writelines("\n# Cost\n")
            f.writelines(f"\n- completion_tokens: {completion_tokens}\n")
            f.writelines(f"- prompt_tokens: {prompt_tokens}\n")
            f.writelines(f"- total_cost: {total_cost}$\n")
            f.writelines(f"- total_tokens: {total_tokens}\n")
    print("Done!")

