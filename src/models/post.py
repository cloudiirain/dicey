"""Post class."""

__author__ = 'cloudiirain'
__version__ = '0.0.1'
__status__ = 'development'


class Post(object):
    """Represents a post in a NUF thread.

    Attributes:
        id: (unicode) The NUF id for the post.
        author: (unicode) The author's username.
        text: (bs4.Tag) The content of the post.

    """

    def __init__(self, soup):
        """Construct a single post given a BeautifulSoup object.

        Args:
            soup (bs4.Tag): BeautifulSoup Tag object.

        """
        self.id = soup['id']
        self.author = soup['data-author']
        self.text = soup.find('div', 'messageContent').article

    def __str__(self):
        """Print string representation of the post."""
        return self.id

    def __repr__(self):
        """Print computer representation of the post."""
        return self.id

    def get_id(self):
        """Print the numeric integer of the id of this post."""
        return int(self.id.split('-')[1])
