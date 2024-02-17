from setuptools import setup


setup(
    name="paper-translator",
    version="0.1.7",
    description="Tranlsate paper into Korean",
    author="seohyunjun",
    author_email="bnmy6581@gmail.com",
    url="https://github.com/seohyunjun/paper-translator",
    install_requires=["langchain", "openai", "arxiv", "pymupdf"],
)
