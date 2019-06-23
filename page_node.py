class PageNode:
    def __init__(self, url_suffix, title, parent, children):
        self.url_suffix = url_suffix
        self.title = title
        self.parent = parent
        self.children = children