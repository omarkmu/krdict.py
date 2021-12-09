"""
Handles fetching and reading information from the krdict website.
"""

from .request import send_request
from ..types import (
    ScrapedWordResponse,
    WordOfTheDayResponse
)
from .utils import (
    extract_href,
    read_search_results,
    read_wotd_details
)

_TRANSLATED_VIEW_URL = 'https://krdict.korean.go.kr{}/dicSearch/SearchView?{}&ParaWordNo={}'


def fetch_today_word(**kwargs):
    """
    Fetches information about the word of the day by scraping the dictionary website.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/#wordofthedayresponse)
    for details.

    - ``translation_language``: The language for which translations should be included.
    """


    doc, _, (nation, code, exonym), *_ = send_request(kwargs, 'word_of_the_day')

    dt_elem = doc.cssselect('dl.today_word > dt')[0]
    dd_elems = doc.cssselect('dl.today_word > dd')
    word_elem = dt_elem.cssselect('a')[0]
    strong_elem = word_elem.cssselect('strong')[0]
    sup_elems = word_elem.cssselect('strong > sup')

    dfn_idx = 0 if not nation and len(dd_elems) < 3 else 1
    result = {
        'target_code': int(extract_href(word_elem) or 0),
        'word': strong_elem.text.strip(),
        'definition': dd_elems[dfn_idx].text_content().strip()
    }

    result['link'] = _TRANSLATED_VIEW_URL.format(
        f'/{nation}' if nation else '',
        f'&nation={nation}&nationCode={code}' if nation else '',
        result['target_code']
    )
    result['sup_no'] = int(sup_elems[0].text_content() or 0 if len(sup_elems) > 0 else 0)

    read_wotd_details(
        result,
        dt_elem,
        dd_elems,
        exonym
    )

    return WordOfTheDayResponse(result)

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

    doc, url, (_, _, exonym), page, per_page = send_request(kwargs, 'meaning_category')
    results, total = read_search_results(doc, exonym)

    return ScrapedWordResponse({
        'link': url,
        'start': int(page),
        'num': int(per_page),
        'total': total,
        'item': results
    })

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

    doc, url, (_, _, exonym), page, per_page = send_request(kwargs, 'subject_category')
    results, total = read_search_results(doc, exonym)

    return ScrapedWordResponse({
        'link': url,
        'start': int(page),
        'num': int(per_page),
        'total': total,
        'item': results
    })
