"""Thread class."""

from post import Post

__author__ = 'cloudiirain'
__version__ = '0.0.1'
__status__ = 'development'


class Thread(object):
    """Represents a thread or part of a thread in the NUF forum.

    Attributes:
        id: (int) The NUF id for the thread
        posts (list): A list of Post objects.

    """

    def __init__(self, bot, thread, post=None):
        """Construct a page given a thread id and/or post id.

        Args:
            bot (Bot): The Bot object acting as the agent.
            thread (int): The id of the thread to parse.
            post (int): The id of the post to start from.

        """
        if post:
            url = 'https://forum.novelupdates.com/posts/{}'.format(post)
        else:
            url = 'https://forum.novelupdates.com/threads/{}'.format(thread)
        





class ThreadPage(object):
    """Represents a single page of a NUF thread.

    Attributes:
        posts: (list) A list of Post objects.
        current_page: (int) The current page number.
        total_pages: (int) The total number of pages.

    """

    def __init__(self, soup):
        """Construct a page given a BeautifulSoup object.

        Args:
            soup (bs4.Tag): BeautifulSoup Tag object.

        """
        # Load the posts in this page
        self.posts = []
        messages = soup.find('ol', id='messageList').find_all('li', 'message ')
        for message in messages:
            self.posts.append(Post(message))

        # Determine the page number in the thread
        nav = soup.find('span', 'pageNavHeader')
        if nav:
            self.current_page = int(nav.string.split(' ')[1])
            self.total_pages = int(nav.string.split(' ')[3])
        else:
            self.current_page = 1
            self.total_pages = 1
