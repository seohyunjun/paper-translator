import openai

from langchain.document_loaders import PyPDFLoader, ArxivLoader 

#from langchain.document_loaders import TextLoader

from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter
from langchain.callbacks import get_openai_callback
import pdb
from tqdm import tqdm 

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, ConstitutionalChain
from langchain.chains.constitutional_ai.models import ConstitutionalPrinciple

def load_paper(config):
    """Load paper from pdf or arxiv"""
    ## PDF Loader
    if config.pdf:
        loader = PyPDFLoader(config.pdf)
        load_paper = loader.load()
        assert load_paper, 'Invalid pdf file'

    ## Arxiv Loader
    if config.arxiv:
        config.arxiv = '2305.11206'
        
        loader = ArxivLoader(query = config.arxiv)
        load_paper = loader.load()
        
        assert load_paper, 'Invalid arxiv number'
    
    config.paper = load_paper 
    print(f"page number: {len(load_paper)}")
    #return load_paper

def splitter(config):
    """splitter paper into chunk size"""

    ## splitter
    config.chunk_size = 2000
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=config.chunk_size, separators=["\n\n"])
    ## splitter
    #text_splitter = CharacterTextSplitter(chunk_size=config.chunk_size, separator="\n\n")
    doc = text_splitter.split_documents(config.paper)
    len(doc)
    #llm = OpenAI(max_tokens=-1)
    llm = ChatOpenAI()

    template = """"your task is align arxiv paper into Markdown format.\n
    ```\n
    Input: {text}
    Markdown: """

    qa_prompt = PromptTemplate(
        template=template,
        input_variables=["text"],
    )
        
    qa_chain = LLMChain(llm=llm, prompt=qa_prompt,verbose=True)
    

    constitutional_chain = ConstitutionalChain.from_llm(
    llm=llm,
    chain=qa_chain,
    constitutional_principles=[
        ConstitutionalPrinciple(
            critique_request="Do the markdown headers use what's in the text?",
            revision_request="the markdown header uses the content in the text.",
        )
    ],
    verbose=True
    )
    
    
    for i,d in enumerate(doc):
        try:
            result = constitutional_chain(d.page_content)
        except:
            dot_split = d.page_content.split('.')
            page_1 = '.'.join(dot_split[:len(dot_split)//2])
            page_2 = '.'.join(dot_split[len(dot_split)//2+1:])
            result1 = constitutional_chain(page_1)
            result2 = constitutional_chain(page_2)
            result = {'text':'','output':''}
            result['text'] = result1['text'] + result2['text']
            result['output'] = result1['output'] + result2['output']
            
        if '# Reference'in result['output']:
            Reference = i        
        #doc[i].page_content = doc[i].page_content.replace('.\n','!-!').replace('\n',' ').replace('!-!','.\n')
        doc[i].page_content = result['output']
        
        print(result['output'])
    
    config.document = doc[:Reference+1]    
    config.reference = doc[Reference+1:]
     
def translate(config):
    ## LLM
    llm = ChatOpenAI(max_tokens=config.max_tokens, model='gpt-3.5-turbo')
    #llm = ChatOpenAI()
    chain = load_summarize_chain(llm, chain_type="stuff", verbose=config.verbose)
    
    chain.llm_chain.prompt.template = """your task is translate text arxiv paper into Korean with Markdown format.\n
    ```\n
    Input: {text}\n
    Output: """ # [5]
    

    # chain.llm_chain.prompt.template = """
    # Your task is translate text arxiv paper.\n
    # arxiv paper text below, delimited by triple backticks.\n
    # if text doesn't have title. do not use ##\n
    # you Must translate into Korean output with Markdown format.\n
    # ```
    # arxiv paper: {text}\n
    # output: 
    # ## Abstract etc (Do not translate)\n
    # """ # [8]
    
    len(config.document)
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
