
# import
from llama_index.vector_stores import ChromaVectorStore
from llama_index import Document

from llama_index.storage.storage_context import StorageContext
from llama_index.embeddings import HuggingFaceEmbedding
from IPython.display import Markdown, display
import chromadb

from llama_index import GPTVectorStoreIndex, StorageContext, ServiceContext
from llama_index.embeddings.openai import OpenAIEmbedding

#chroma_client = chromadb.Client(database="./chroma_db")
chroma_client = chromadb.PersistentClient(path="./chroma_db")

def createOrget_collection(collection_name:str):
    collection_list =  [collection.name for collection in chroma_client.list_collections()]
    if collection_name not in collection_list:
        collection = chroma_client.create_collection(name=collection_name)
    else:
        collection = chroma_client.get_collection(name=collection_name)

    return collection

def preprocess_doc(document):
    docs = []
    for i, row in enumerate(document):
        docs.append(Document(
            text=row.page_content,
            doc_id=int(i),
        ))
    return docs
    
def chromadb_embed(collection_name: str, docs: list, model: str='text-embedding-3-small', embed_batch_size: int=100):
    # # create the index if it does not exist already
    # collection = createOrget_collection(collection_name)
    
    # # set up ChromaVectorStore and load in data
    # vector_store = ChromaVectorStore(chroma_collection=collection)
    
    # # setup our storage (vector db)
    # storage_context = StorageContext.from_defaults(
    #     vector_store=vector_store
    # )
    # load vector db
    collection = chroma_client.get_or_create_collection(collection_name)
    
    # setup the index/query process, ie the embedding model (and completion if used)
    vector_store = ChromaVectorStore(chroma_collection=collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    embed_model = OpenAIEmbedding(model=model, embed_batch_size=embed_batch_size)

    service_context = ServiceContext.from_defaults(embed_model=embed_model)
    
    index = GPTVectorStoreIndex.from_documents(
        preprocess_doc(docs), storage_context=storage_context,
        service_context=service_context
    )
    
    # index = GPTVectorStoreIndex.from_documents(
    #     documents, storage_context=storage_context, service_context=service_context
    # )