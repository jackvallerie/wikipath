import requests, sys, re
from lxml import html


def main():
    if len(sys.argv) > 2:
        start_page = sys.argv[1]
        target_page = sys.argv[2]
    else:
        print('Usage: {} start_page target_page'.format(sys.argv[0]))
        sys.exit()

    viisted = {}
    queue = []
    wiki_spider(start_page, target_page, viisted, queue)


def wiki_spider(start_page, target_page, visited, queue):
    '''
    Recursively crawl through wikipedia articles starting at the start_page
    to find the target_page
    '''
    page = requests.get('https://en.wikipedia.org{}'.format(start_page))
    tree = html.fromstring(page.content)

    for a in tree.xpath('//*[@id="mw-content-text"]/div//a'):
        href = a.xpath('@href')
        href = href[0] if href != [] else ''
        if re.match('^/wiki/(Category:(?!.*:)|(?!.*:)).*', href) and href not in visited:
            
            visited[href] = True
            queue.append(href)

            # found our target
            if href == target_page:
                print(href)
                # get_path(curr_node)


if __name__ == "__main__":
    main()