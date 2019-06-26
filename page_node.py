import requests
from lxml import html

class PageNode:
    def __init__(self, url_suffix, parent):
        self.url_suffix = url_suffix 
        self.parent = parent
