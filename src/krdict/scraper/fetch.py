"""
Handles fetching and reading information from the krdict website.
"""

from .request import send_request
from .utils import parse_response


def fetch_today_word(**kwargs):
    """
    Fetches information about the word of the day by scraping the dictionary website.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/#wordofthedayresponse)
    for details.

    - ``translation_language``: The language for which translations should be included.
    """


    return parse_response(*send_request(kwargs, 'word_of_the_day'))

def fetch_meaning_category_words(**kwargs):
    """
    Fetches words that belong to the provided meaning category.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/scraper/#fetch_meaning_category_words)
    for details.

    - ``category``: The meaning category to fetch.
    - ``page``: The page at which the search should start ``[1, 1000]``.
    - ``per_page``: The maximum number of search results to return ``[10, 100]``.
    - ``sort``: The sort method that should be used.
    - ``translation_language``: A language for which translations should be included.
    """

    return parse_response(*send_request(kwargs, 'meaning_category'))

def fetch_subject_category_words(**kwargs):
    """
    Fetches words that belong to one of the provided subject categories.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/scraper/#fetch_subject_category_words)
    for details.

    - ``category``: The subject category to fetch.
    - ``page``: The page at which the search should start ``[1, 1000]``.
    - ``per_page``: The maximum number of search results to return ``[10, 100]``.
    - ``sort``: The sort method that should be used.
    - ``translation_language``: A language for which translations should be included.
    """

    return parse_response(*send_request(kwargs, 'subject_category'))

def search(**kwargs):
    """
    Performs a search on the Korean Learners' Dictionary
    Returns a dict with contents dependent on the value of the ``search_type`` parameter.

    See the [documentation](https://krdictpy.readthedocs.io/en/stable/return_types)
    for details.

    - ``query``: The search query.
    - ``key``: The API key. If a key was set with ``set_key``, this can be omitted.
    - ``page``: The page at which the search should start ``[1, 1000]``.
    - ``per_page``: The maximum number of search results to return ``[10, 100]``.
    - ``sort``: The sort method that should be used.
    - ``search_type``: The type of search to perform.
    - ``translation_language``: The language for which translations should be included.
    """

    return parse_response(*send_request(kwargs, kwargs.get('search_type', 'word')))
