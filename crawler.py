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


web = {}
seed = "a.html"
to_crawl = []
crawled = []


def crawl_page(page):
    page_contents = ''
    with open(page, "r") as f:
        s = f.read()
        page_contents += s
    return page_contents


def get_link(string):
    # takes in a string, finds the first link,
    # returns it along with shortened string starting at end of first link.
    start_link = (string.find("\"")) + 1
    end_link = string.find('\"', start_link)
    link_one = string[start_link:end_link]
    # print(type(link_one)) Check that is is a string
    # print(link_one) Check that is only includes the link file and not the quotations or anything else
    return link_one, string[end_link + 1:]

# def get_next_target

# def get_all_links()


print(get_link("This is the page a linking to page <a href=\"b.html\">b</a><br>"))
