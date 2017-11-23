import mechanize
import cookielib
from bs4 import BeautifulSoup
from src.models.post import Post
from src.models.thread import ThreadPage

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
# br.set_debug_http(True)
# br.set_debug_redirects(True)
# br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


######### Code starts here
#r = br.open("http://forum.novelupdates.com/threads/aestus-domus-aurea-the-last-poster-is-the-winner-hard-mode.9669/")
# r = br.open("https://forum.novelupdates.com/threads/9669/page-78")
r = br.open("https://forum.novelupdates.com/threads/47262")
html = r.read()

soup = BeautifulSoup(html, 'html.parser')
thread = ThreadPage(soup)
print str(len(thread.posts))
print str(thread.current_page)
print str(thread.total_pages)
print type(thread.posts[0].author)

"""
page = soup.find('ol', id='messageList')
messages = page.find_all('li', 'message ')


posts = []
for message in messages:
    posts.append(Post(message))
print posts
print posts[0].get_id()
"""


# page = soup.find('span', class_='pageNavHeader')
# page_string = page.contents[0].encode('utf-8')
# Page 1 of 66

# print soup.prettify().encode('utf-8')
