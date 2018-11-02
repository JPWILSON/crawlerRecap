import urllib.request
import os


#contents = urllib.request.urlopen('a.html', ).read()
#__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname('a.html')))


# file_one = "a.html"

# content = ""
# with open(file_one, "r") as f:
#     s = f.read()
#     content += s

# print(content)


# Process to list all pages
# Need a dictionary mapping all links to the pages they point to
# need a list of pages to crawl
# need a list of pages crawled
# need a seed page

# process:
# need a crawl method that grabs the links in a page


# def crawl_page(page):
def get_page_contents(link):
    page_contents = ''
    with open(link, "r") as f:
        s = f.read()
        page_contents += s
    return page_contents


def get_new_link(string):
    # takes in a string, finds the first link,
    # returns it along with shortened string starting at end of first link.
    start_link = (string.find("\"")) + 1
    end_link = string.find('\"', start_link)
    link_one = string[start_link:end_link]
    # print(type(link_one)) Check that is is a string
    # print(link_one) Check that is only includes the link file and not the quotations or anything else
    return link_one, string[end_link + 1:]

# def get_next_target(get_link(string))  May not need this


def get_all_links(link):
    page_contents = get_page_contents(link)
    if link not in web:
        web[link] = []
        print("web: ", web)
    else:
        return
    if link in crawled:
        return
    while page_contents:
        print("pgct", page_contents)
        next_link, new_string = get_new_link(page_contents)
        if next_link:
            if next_link not in web[link]:
                web[link].append(next_link)
            if next_link not in to_crawl and next_link not in crawled:
                to_crawl.append(next_link)
        page_contents = new_string
    crawled.append(link)
    print(to_crawl)
    print(crawled)
    return


def crawl_web(seed):
    to_crawl.append(seed)
    while to_crawl:
        get_all_links(to_crawl.pop())
    return web


web = {}
seed = "a.html"
to_crawl = []
crawled = []
print(crawl_web(seed))
