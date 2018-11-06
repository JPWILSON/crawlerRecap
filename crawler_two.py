def crawl_network(seed):
    web = {}
    to_crawl = []
    crawled = []
    to_crawl.append(seed)
    while to_crawl:
        extract_links(get_link_text(to_crawl.pop()), crawled, to_crawl)
    print(web)


def get_link_text(link):
    pass


def extract_links(link_text, crawled, to_crawl):
    pass
