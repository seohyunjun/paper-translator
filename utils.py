import openai

from langchain.document_loaders import PyPDFLoader, ArxivLoader

from langchain import LLMChain
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.callbacks import get_openai_callback
from tqdm import tqdm

from langchain.prompts import PromptTemplate


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

    ## Arxiv Loader
    if config.arxiv:
        loader = ArxivLoader(query=config.arxiv)
        load_paper = loader.load()

        assert load_paper, "Invalid arxiv number"
    # if config.html:

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

    llm = ChatOpenAI(model="gpt-3.5-turbo-0613", temperature=0)
    llm.temperature = 0

    # template = """"your task is align arxiv paper into Markdown format.\n
    # ```\n
    # Input: {text}
    # Markdown: """

    template = """Your task is to proofread sentences and correct typos and align sentence refer to front and back.\n
    fix the sentence below with markdown format, delimited by triple backticks.\n
    if sentence in figure or table. annotate and fix markdown formatting.\n
    
    sentence: {text}\n
    markdown:
    """
    qa_prompt = PromptTemplate(
        template=template,
        input_variables=["text"],
    )
    qa_chain = LLMChain(llm=llm, prompt=qa_prompt, verbose=True)

    ## Valid Chain
    # constitutional_chain = ConstitutionalChain.from_llm(
    # llm=llm,
    # chain=qa_chain,
    # constitutional_principles=[
    #     ConstitutionalPrinciple(
    #         critique_request="Do the markdown headers use what's in the text?",
    #         revision_request="the markdown header uses the content in the text.",
    #     )
    # ],
    # verbose=True
    # )

    for i, d in tqdm(enumerate(doc), total=len(doc)):
        result = qa_chain(d.page_content)
        doc[i].page_content = result["text"]

    config.document = doc


def translate(config):
    ## LLM
    llm = ChatOpenAI(model=config.model)
    # llm = ChatOpenAI()
    chain = load_summarize_chain(llm, chain_type="stuff", verbose=config.verbose)

    chain.llm_chain.prompt.template = """your task is translate text arxiv paper into Korean with Markdown format.\n
    Input: {text}\n
    Output: ### title """  # [5]

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
