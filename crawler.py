import urllib.request
import os

# SOOOOOOOOOOOOO stupid, I have not been finding links!
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
    a_href = string.find("<a href=")
    start_link = string.find("\"", a_href) + 1
    #print('start_link', start_link)
    end_link = string.find('\"', start_link)
    #print('end_link', end_link)
    if start_link > 0:
        link_one = string[start_link:end_link]
    else:
        return(None, None)
    # print(type(link_one)) Check that is is a string
    # Check that is only includes the link file and not the quotations or anything else
    #print('link_one', link_one)
    return(link_one, string[end_link + 1:])


def get_all_links(link):
    print("even starting?")
    if link not in web:
        web[link] = []
        print("web: ", web)
    page_contents = get_page_contents(link)
    while page_contents:
        print("get here? ")
        print("pgct", page_contents)
        next_link, new_string = get_new_link(page_contents)
        print('how bout here ? ')
        print('next_link: ', next_link)
        print('new_string ', new_string)
        if next_link:
            print('into this condition ? ')
            if next_link not in web[link]:
                web[link].append(next_link)
            if next_link not in to_crawl and next_link not in crawled:
                to_crawl.append(next_link)
        else:
            print('next_link is not a link: ', next_link)
            page_contents = None
        if page_contents:
            page_contents = new_string
    crawled.append(link)
    print(to_crawl)
    print(crawled)
    return


web = {}
to_crawl = []
crawled = []
# get_all_links("a.html")


def crawl_web(seed):
    to_crawl.append(seed)
    while to_crawl:
        li = to_crawl.pop()
        if li not in crawled:
            get_all_links(li)
        else:
            return web
    return web


print(crawl_web("a.html"))
