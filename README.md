[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fseohyunjun%2Fpaper-translator&count_bg=%2379C83D&title_bg=%233B3B3B&icon=googletranslate.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)              

# paper-translator
1. This is a paper translator(`korean`) using Langchain.  
2. It automatically translates addresses or files in the form of PDF files.



### version history
#### v0.1.3 2023/6/23
- URL -> markdown
  - require `brew install libmagic`


#### v0.1.2 2023/6/15  
- ChatGPT API Update : gpt-3.5-turbo-16k 
  - token 4k -> 16k (about 3 pages cover per 1 request)

#### v0.1.1 2023/6/6  
- ConstitutionalChain(test) : if output format is wrong, fix it.

#### v0.1.0 2023/6/4
- paper translator using Langchain
- preprocessing for paper (ex, split Reference)

## Usage guide

Since Langchain's llm model uses OpenAI, an OpenAI API Key is required. 

```shell
export OPENAI_API_KEY='sk-...'
```

### Install guide

```shell
git clone https://github.com/seohyunjun/paper-translator
cd paper-tanslator
python -m pip install -r ./requirements.txt
```

### Example 

```commandline
python main.py --pdf https://arxiv.org/pdf/2304.06035v1.pdf --verbose 1 --outputfile ChooseYourWeapon.md
```

