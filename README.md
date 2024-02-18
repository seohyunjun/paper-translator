[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fseohyunjun%2Fpaper-translator&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)         

# paper-translator
1. This is a paper translator(`korean`) using Langchain.  
2. It automatically translates addresses or files in the form of PDF files.



### version history

#### v0.1.8 2024/02/13
- Add ChromaDB 

#### v0.1.7 2023/12/16
- Vectorstore using pinecone 

#### v0.1.6 2023/11/27
- add GPT4-Vision API

#### v0.1.5 2023/7/25
- add Youtube Script translator(using youtube-dl) 

<details>
<summary>version history</summary>

#### v0.1.4 2023/7/9
- use langchain schema 

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

</details>


## Usage guide
Since Langchain's llm model uses OpenAI, an OpenAI API Key is required. 

```shell
# OPENAI API key
OPENAI_API_KEY="..."

# Pinecone API key
PINECONE_API_KEY="..."
PINECONE_ENVIRONEMENT="..."
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

---

<a href="mailto:bnmy6581@gmail.com">
    <img src="https://img.shields.io/badge/
    Gmail-EA4335?style=for-the-badge&logo=Gmail&logoColor=white"> 
</a>
<a href="https://pf.kakao.com/_vxhjyxj">
    <img src="https://img.shields.io/badge/
    KakaoBot-FFCD00?style=for-the-badge&logoColor=black&logo=KakaoTalk"> 
</a>
<p>
<a href="https://pf.kakao.com/_vxhjyxj">
<img src='./src/kakaobot.png' width=200 align='left'/>
</p>

