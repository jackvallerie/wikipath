import requests, sys, re
from lxml import html
from page_node import PageNode


class WikiSpider:
    def __init__(self, start_page_url_suffix, start_page_title, target_page):
        self.start_page = start_page_url_suffix
        self.target_page = target_page
        self.visited = {}
        self.queue = []
        self.head = PageNode(url_suffix=start_page,
                             title=start_page_title,
                             parent=None, 
                             children=[])


    def crawl(self):
        '''
        Recursively crawl through wikipedia articles starting at the start_page
        to find the target_page
        '''
        page = requests.get('https://en.wikipedia.org{}'.format(self.start_page))
        tree = html.fromstring(page.content)

        # grab all <a/> elements in the content section of the article
        for a in tree.xpath('//*[@id="mw-content-text"]/div//a'):
            href = a.xpath('@href')
            href = href[0] if href != [] else '' # some hrefs are empty

            '''
            We only want to crawl wiki articles (i.e. no external links, no Wikipedia
            reference pages), so we filter to only look at hrefs of the form
            '/wiki/blah' where blah is either the url field specifiying a wiki article
            (e.g. 'Cuisine_of_Hawaii') or something of the form 'Category:' not followed
            by another identifier (e.g. 'Category:American_cuisine', not 'Category:CS1_maint:')
            '''
            if re.match('^/wiki/(Category:(?!.*:)|(?!.*:)).*', href) and href not in self.visited:
                
                self.visited[href] = True
                self.queue.append(href)

                # found our target
                if href == self.target_page:
                    print(href)
                    # get_path(curr_node)

    def get_path(self):
        pass