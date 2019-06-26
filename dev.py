import requests
from lxml import html

def links(url_suffix):
    r = requests.get('https://en.wikipedia.org{}'.format(url_suffix))
    tree = html.fromstring(r.content)
    # grab all <a/> elements in the content section of the article
    return tree.xpath('//*[@id="mw-content-text"]/div//a/@href')