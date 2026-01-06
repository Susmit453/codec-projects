from steuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'BAPPY AHMED'
SRC_REPO = 'SRC' 
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '1.0.0',
    author = AUTHOR_NAME,
    author_email = 'entbappy73@gmail.com',
    description = 'A sample Python project setup',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    python_requires = '>=3.10',
    install_requires = LIST_OF_REQUIREMENTS,
)