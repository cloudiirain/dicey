#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Novel Updates Forum - Bot Thread Page Tracker

Read the messages for a NUF thread starting on a given page.

Examples:
    python handle_page.py [url] [page_number]

"""

import argparse

__author__ = 'cloudiirain'
__version__ = '0.0.1'
__status__ = 'development'


def handle_page(url, page):
    """Read the messages for a thread starting on a given page.

    Args:
        url (str): URL of the page to query
        page (int): Page number to start at

    Returns:
        None

    """
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',
                        help='URL to the NUF thread')
    args = parser.parse_args()
    handle_page(args.deploy)
