"""Thread class."""

import mechanize
import cookielib
from bs4 import BeautifulSoup

__author__ = 'cloudiirain'
__version__ = '0.0.1'
__status__ = 'development'


class Bot(object):
    """A bot agent capable of interacting with NUF.

    Attributes
        bot: (Browser) The Mechanize Browser object.
        username: (string) The NUF account username of the bot.
        password: (string) The NUF account password of the bot.

    """

    def __init__(self, username=None, password=None):
        """Construct a bot given a NUF account username/password.

        Args:
            username: (string) The NUF account username of the bot.
            password: (string) The NUF account password of the bot.

        """
        # Browser
        self.bot = mechanize.Browser()

        # Cookie Jar
        cj = cookielib.LWPCookieJar()
        self.bot.set_cookiejar(cj)

        # Browser options
        self.bot.set_handle_equiv(True)
        self.bot.set_handle_gzip(True)
        self.bot.set_handle_redirect(True)
        self.bot.set_handle_referer(True)
        self.bot.set_handle_robots(False)

        # Follows refresh 0 but not hangs on refresh > 0
        self.bot.set_handle_refresh(
            mechanize._http.HTTPRefreshProcessor(),
            max_time=1
        )

        # User-Agent (this is cheating, ok?)
        self.bot.addheaders = [(
            'User-agent',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) '
            'Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'
        )]

        # Miscellaneous instance Variables
        self.username = username
        self.password = password

    def login(self):
        """Log in the bot."""
        pass

    def logout(self):
        """Log out the bot."""
        pass

    def get_post(self, post_id):
        """Fetch the page containing the post id and return BeautifulSoup.

        Args:
            post_id: (int) The NUF id of the post.

        """
        url = 'https://forum.novelupdates.com/posts/{}'.format(post_id)
        html = self.bot.open(url).read()
        return BeautifulSoup(html, 'html.parser')

    def get_thread(self, thread_id, page=None):
        """Fetch the requested thread/page and return BeautifulSoup.

        Args:
            thread_id: (int) The NUF id of the thread.
            page: (int) The page number.

        """
        if page:
            url = 'https://forum.novelupdates.com/threads/{}/page-{}'.format(
                thread_id, page
            )
        else:
            url = 'https://forum.novelupdates.com/threads/{}'.format(thread_id)
        html = self.bot.open(url).read()
        return BeautifulSoup(html, 'html.parser')
