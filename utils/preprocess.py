import re

def clean_number(doc)-> list:
    """splitter align subtitle and content number

    Returns:
        list: document
    """    
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
