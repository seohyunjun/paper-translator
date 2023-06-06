import openai

from langchain.document_loaders import PyPDFLoader, ArxivLoader 

#from langchain.document_loaders import TextLoader

from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.callbacks import get_openai_callback
import pdb
from tqdm import tqdm 

def load_paper(config):
    """Load paper from pdf or arxiv"""
    ## PDF Loader
    if config.pdf:
        loader = PyPDFLoader(config.pdf)
        load_paper = loader.load()
        assert load_paper, 'Invalid pdf file'

    ## Arxiv Loader
    if config.arxiv:
        loader = ArxivLoader(config.arxiv,load_max_docs=400)
        load_paper = loader.load()
        assert load_paper, 'Invalid arxiv number'
    
    config.paper = load_paper 
    print(f"page number: {len(load_paper)}")
    #return load_paper

def splitter(config):
    """Split text into sentences"""

    ## splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=config.chunk_size, separators=['\n\n'])
    
    doc = text_splitter.split_documents(config.paper)
    
    for i,d in enumerate(doc):
        if 'Reference'in d.page_content:
            Reference = i
            doc[Reference].page_content = doc[Reference].page_content.split('Reference')[0]
        
        doc[i].page_content = doc[i].page_content.replace('.\n','!-!').replace('\n',' ').replace('!-!','.\n')
    config.document = doc[:Reference+1]    
    config.reference = doc[Reference+1:]        


def translate(config):
    ## LLM
    llm = ChatOpenAI(max_tokens=config.max_tokens, model='gpt-3.5-turbo')
    #llm = ChatOpenAI()
    chain = load_summarize_chain(llm, chain_type="stuff", verbose=config.verbose)
    
    # chain.llm_chain.prompt.template = '''following this guide.\nsummaries of sentence.\nYou must use Markdown format.\ntranslate into korean.\n
    # ----------------\n
    # {text}\n
    # # korean:'''
    # chain.llm_chain.prompt.template = """summaries sentence with Output Markdown format translate into Korean\n
    # --------------------\n
    # {text}\n
    # Output:"""
    
    chain.llm_chain.prompt.template = """your task is translate text arxiv paper into Korean with Markdown format.\n
    ```\n
    Input: {text}\n
    Output: ## Title""" # [5]
    
    # chain.llm_chain.prompt.template = """
    # Your task is translate text arxiv paper.\n
    # arxiv paper text below, delimited by triple backticks.\n
    # you Must translate into Korean output with Markdown format.\n
    # arxiv paper: ```{text}```\n
    # output: ## Title\n
    # """ # [8]
    
    
    # chain.llm_chain.prompt.template = """summaries sentence. you must answer in Korean and in Markdown format\n
    # --------------------\n
    # {text}\n
    # answer:"""
    
    completion_tokens = 0
    prompt_tokens = 0
    total_cost = 0
    total_tokens = 0
    
    results = []
    for page in tqdm(config.document, total=len(config.document)):
        
        with get_openai_callback() as cb:
            
            result = chain.run([page]) 
            print(result)      
            
            completion_tokens+=cb.completion_tokens
            prompt_tokens+=cb.prompt_tokens
            total_cost+=cb.total_cost
            total_tokens+=cb.total_tokens
        results.append(result)
    
    print(f"completion_tokens: {completion_tokens}\n")
    print(f"prompt_tokens: {prompt_tokens}\n")
    print(f"total_cost: {total_cost}\n")
    print(f"total_tokens: {total_tokens}\n")
    
    for result in results:
        print(result)
    
    if config.outputfile:
        with open(config.outputfile, 'w') as f: 
            for result in results:
                f.writelines(result)
            f.writelines('\n# Reference\n')
            for ref in config.reference:
                f.writelines(ref.page_content)
            
            f.writelines('\n# Cost\n')
            f.writelines(f"\n- completion_tokens: {completion_tokens}\n")
            f.writelines(f"- prompt_tokens: {prompt_tokens}\n")
            f.writelines(f"- total_cost: {total_cost}$\n")
            f.writelines(f"- total_tokens: {total_tokens}\n")
    print("Done!")

