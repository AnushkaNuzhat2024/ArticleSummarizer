## Overview:
This web app can summerize news articles using newspaper4k (extension of newspaper3k) python library that uses natural language processing techniques. In addition, NiceGUI framework has been used to provide a smooth and simple UI for the user.

## Requirements:
Python >= 3.12

## Installation:
Using a pipenv or conda environment

* pipenv

```bash
pipenv install
pipenv shell
python news_summerizer.py
```

or
* Miniconda/Anaconda
```bash
conda create -n "news_summerizer" python=3.12
conda activate news_summerizer
pip install -r requirements.txt
python news_summerizer.py
```

## References
* Newspaper4k: https://newspaper4k.readthedocs.io/en/latest/
* NiceGUI: https://nicegui.io/
