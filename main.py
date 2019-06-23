from wiki_spider import WikiSpider
import requests, sys
from lxml import html

'''
python main.py
'''

def main():
    if len(sys.argv) > 2:
        start_page_url_suffix = sys.argv[1]
        target_page = sys.argv[2]
    else:
        print('Usage: {} start_page_url_suffix start_page_title target_page'.format(sys.argv[0]))
        sys.exit()

    page = requests.get('https://en.wikipedia.org{}'.format(start_page_url_suffix))
    tree = html.fromstring(page.content)
    start_page_title = tree.xpath('//*[@id="firstHeading"]/text()')[0]

    spider = WikiSpider(start_page_url_suffix, start_page_title, target_page)
    spider.crawl()

if __name__ == "__main__":
    main()