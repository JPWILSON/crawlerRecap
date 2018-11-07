

def crawl_network(seed):
    web = {}
    to_crawl = []
    crawled = []
    to_crawl.append(seed)
    while to_crawl:
        extract_links(get_link_text(to_crawl.pop()), crawled, to_crawl, web)
    print('web is: ', web)
    return


def get_link_text(link):
    contents = ''
    with open(link, 'r') as f:
        s = f.read()
        contents += s
        if len(contents) > 10:
            print('successfully read in a page')
    return contents


def extract_links(link_text, crawled, to_crawl, web):
    if link_text not in web:
        web[link_text] = []
    crawled.append(link_text)
    linkins_page = 0
    link = True
    while link:
        page_contents = link_text
        start_link = page_contents.find(
            "\"", page_contents.find("<a href=")) + 1
        end_link = page_contents.find("\"", start_link + 1)
        if start_link == 0:
            link = None
        else:
            link = page_contents[start_link:end_link]
            page_contents = page_contents[end_link + 1:]
            if link not in web[link_text]:
                web[link_text].append(link)
            if link not in crawled and link not in to_crawl:
                to_crawl.append(link)
            linkins_page += 1
    print("finished searching for links in the page, there were: ", linkins_page)
    return


print('starting')
crawl_network('a.html')
print('done!')
