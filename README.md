# Wikipath

Find the shortest path between two Wikipedia articles.

# Setup

Clone the repo, then set up a venv
```bash
python3 -m venv [envname]
```
activate it
```bash
source [envname]/bin/activate
```
and install dependencies
```bash
pip install requirements.txt
```

# Usage
Find two wikipedia articles and grab the last two fields in each URL (e.g. for https://en.wikipedia.org/wiki/Cuisine_of_Hawaii, use `/wiki/Cuisine_of_Hawaii`)

Then

```bash
python main.py [start_article] [target_article]
```
e.g.
```bash
python main.py /wiki/Cuisine_of_Hawaii /wiki/Food_history
```