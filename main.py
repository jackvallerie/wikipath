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
        print('Usage: {} start_page_url_suffix target_page_url_suffix'.format(sys.argv[0]))
        sys.exit()

    spider = WikiSpider(start_page_url_suffix, target_page)
    spider.crawl()

if __name__ == "__main__":
    main()
