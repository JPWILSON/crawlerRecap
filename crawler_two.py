

def crawl_network(seed):
    web = {}
    to_crawl = []
    crawled = []
    to_crawl.append(seed)
    while to_crawl:
        extract_links(to_crawl.pop(), crawled, to_crawl, web)
    print('web is: ', web)
    return


def get_link_text(link):
    contents = ''
    with open(link, 'r') as f:
        s = f.read()
        contents += s
        # if len(contents) > 10:
        #print('successfully read in a page')
    return contents


def extract_links(linky, crawled, to_crawl, web):
    link_text = get_link_text(linky)
    if linky not in web:
        web[linky] = []
    crawled.append(linky)
    linksin_page = 0
    link = True
    page_contents = link_text
    while link:
        start_link = page_contents.find(
            "\"", page_contents.find("<a href=")) + 1
        end_link = page_contents.find("\"", start_link + 1)
        if start_link < 1:
            link = None
        else:
            link = page_contents[start_link:end_link]
            page_contents = page_contents[end_link + 1:]
            if link not in web[linky]:
                web[linky].append(link)
            if link not in crawled and link not in to_crawl:
                to_crawl.append(link)
            linksin_page += 1
    # print("finished searching for links in the page, there were: ", linksin_page)
    # print('web: ', web)
    # print('web for this link list: ', web[linky])
    return


# print('starting')
crawl_network('a.html')
# print('done!')
