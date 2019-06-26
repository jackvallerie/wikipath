import requests, sys, re
from lxml import html
from page_node import PageNode


class WikiSpider:
    def __init__(self, start_page_url_suffix, target_page):
        self.start_page = PageNode(url_suffix=start_page_url_suffix,
                                   parent=None)
        self.target_page = PageNode(url_suffix=target_page, parent=None)
        self.visited = set([start_page_url_suffix])
        self.queue = [self.start_page]


    def crawl(self):
        '''
        Recursively crawl through wikipedia articles starting at the start_page
        to find the target_page
        '''
        while self.queue:
            curr_page = self.queue.pop()
            print("Crawling {}".format(curr_page.url_suffix))
            links = self.get_page_links(curr_page.url_suffix)

            for a in links:
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
                    
                    print("Adding {} to the queue".format(href))
                    self.visited.add(href)
                    self.queue.append(PageNode(url_suffix=href, parent=curr_page))

                    # found our target
                    if href == self.target_page.url_suffix:
                        print('Found target:{}'.format(href))
                        self.get_path(curr_page)
                        return


    def get_path(self, curr_page):
        link_path = [self.get_page_title(self.target_page.url_suffix)]
        while curr_page:
            link_path.insert(0, self.get_page_title(curr_page.url_suffix))
            curr_page = curr_page.parent
        
        print(link_path)


    def get_page_links(self, url_suffix):
        r = requests.get('https://en.wikipedia.org{}'.format(url_suffix))
        tree = html.fromstring(r.content)
        # grab all <a/> elements in the content section of the article
        return tree.xpath('//*[@id="mw-content-text"]/div//a')


    def get_page_title(self, url_suffix):
        r = requests.get('https://en.wikipedia.org{}'.format(url_suffix))
        tree = html.fromstring(r.content)
        title = tree.xpath('//*[@id="firstHeading"]/text()')
        if title == []:
            title = tree.xpath('//*[@id="firstHeading"]/i/text()')

        return title[0]