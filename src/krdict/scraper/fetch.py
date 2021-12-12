"""
Handles fetching and reading information from the krdict website.
"""

from .request import send_request
from .utils import parse_response


def advanced_search(**kwargs):
    """
    Performs an advanced search on the Korean Learners' Dictionary.

    See the [documentation](https://krdictpy.readthedocs.io/en/stable/return_types) for details.

    - ``query``: The search query.
    - ``page``: The page at which the search should start ``[1, 1000]``.
    - ``per_page``: The maximum number of search results to return ``[10, 100]``.
    - ``sort``: The sort method that should be used.
    - ``translation_language``: The language for which translations should be included.
    - ``search_target``: The target field of the search query.
    - ``target_language``: The original language to search by. If ``search_target``
    is set to any value other than ``SearchTarget.ORIGINAL_LANGUAGE``, this parameter
    has no effect.
    - ``search_method``: The method used to match against the query.
    - ``classification``: An entry classification to filter by.
    - ``origin_type``: A word origin type to filter by.
    - ``vocabulary_level``: A vocabulary level to filter by.
    - ``part_of_speech``: A part of speech to filter by.
    - ``multimedia_type``: A multimedia type to filter by.
    - ``min_syllables``: The minimum number of syllables in result words ``[1, 80]``.
    - ``max_syllables``: The maximum number of syllables in result words ``[1, 80]``.
    - ``meaning_category``: The meaning category to filter by.
    - ``subject_category``: A subject category to filter by.
    - ``search_conditions``: An array of search condition objects to filter by.
    """

    return parse_response(*send_request(kwargs, 'advanced'))

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
    Performs a search on the Korean Learners' Dictionary.
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
