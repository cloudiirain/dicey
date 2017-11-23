import mechanize
import cookielib
from bs4 import BeautifulSoup

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
r = br.open("http://forum.novelupdates.com/members/villain.44558/")
html = r.read()

soup = BeautifulSoup(html, 'html.parser')
profile = soup.find('ol', id='ProfilePostList')
print profile.prettify().encode('utf-8')

# print soup.prettify().encode('utf-8')

# Select the first (index zero) form
br.select_form(nr=0)

# Let's login
br.form['login'] = 'account'
br.form['password'] = 'password'
br.submit()

c = br.open("http://forum.novelupdates.com/members/dice.56504/")

for f in br.forms():
    print f

br.select_form(nr=0)
br.form['message'] = 'Hello World'
response = br.submit()

print response.info()
