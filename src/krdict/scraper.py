"""
Retrieves information from the krdict website via scraping.
"""

from .types import SortMethod
from ._scraper_utils import (
    _build_advanced_search_url,
    _build_language_query,
    _build_sense_category_query,
    _build_subject_category_query,
    _extract_url,
    _fetch_view_images,
    _fetch_view_videos,
    _insert_search_url,
    _read_search_results,
    _read_view_pronunciation,
    _read_view_original_language,
    _read_wotd_details,
    _send_request
)

_BASE_URL = 'https://krdict.korean.go.kr/{}mainAction'
_SEARCH_URL = (
    'https://krdict.korean.go.kr/dicSearch/search?'
    'mainSearchWord={}&currentPage={}&blockCount={}&sort={}')
_SUBJECT_URL = (
    'https://krdict.korean.go.kr/{}dicSearchDetail/searchDetailActCategoryResult?'
    'searchFlag=Y{}&currentPage={}&blockCount={}&sort={}{}')
_SENSE_URL = (
    'https://krdict.korean.go.kr/{}dicSearchDetail/searchDetailSenseCategoryResult?'
    'searchFlag=Y{}&currentPage={}&blockCount={}&sort={}{}')
_TRANSLATED_VIEW_URL = 'https://krdict.korean.go.kr/{}dicSearch/SearchView?ParaWordNo={}{}'


def extend_advanced_search(response, raise_errors):
    """
    Extends word search results with pronunciation URLs by scraping the dictionary website.
    This function modifies the response in-place, and returns the modified object.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/#wordsearchresponse)
    for details about return types.

    - ``response``: The word search results to extend.
    - ``raise_errors``: Whether errors that occur during scraping should be raised or ignored.

    """

    if len(response['data']['results']) == 0:
        return response

    # query-based advanced search cannot handle this case
    if int(response['request_params'].get('letter_e', -1)) == 0:
        return response

    url = _build_advanced_search_url(response['request_params'])
    [success, doc] = _send_request(url, raise_errors)
    if not success:
        return response

    results = response['data']['results']
    elements = doc.cssselect('div.search_result > dl')

    for idx, result in enumerate(results):
        if idx >= len(elements):
            break

        urls = []
        for elem in elements[idx].cssselect('a.sound'):
            pron_url = _extract_url(elem)
            if pron_url is not None:
                urls.append(pron_url)

        if len(urls) > 0:
            result['pronunciation_urls'] = urls

    _insert_search_url(response, url)
    return response

def extend_search(response, raise_errors):
    """
    Extends word search results with pronunciation URLs by scraping the dictionary website.
    This function modifies the response in-place, and returns the modified object.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/#wordsearchresponse)
    for details about return types.

    - ``response``: The word search results to extend.
    - ``raise_errors``: Whether errors that occur during scraping should be raised or ignored.

    """

    if len(response['data']['results']) == 0:
        return response

    params = response['request_params']
    url = _SEARCH_URL.format(
        params['q'],
        params.get('start', 1),
        params.get('num', 10),
        'W' if params.get('sort') != 'popular' else 'C')

    [success, doc] = _send_request(url, raise_errors)
    if not success:
        return response

    results = response['data']['results']
    elements = doc.cssselect('dl.printArea')

    for idx, result in enumerate(results):
        if idx >= len(elements):
            break

        urls = []
        for elem in elements[idx].cssselect('a.sound'):
            pron_url = _extract_url(elem)
            if pron_url is not None:
                urls.append(pron_url)

        if len(urls) > 0:
            result['pronunciation_urls'] = urls

    _insert_search_url(response, url)
    return response

def extend_view(response, fetch_page_data, fetch_multimedia, raise_errors):
    """
    Extends view query results with pronunciation URLs, multimedia URLs, and extended hanja
    information by scraping the dictionary website.
    This function modifies the response in-place, and returns the modified object.

    See the [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/#viewresponse)
    for details about return types.

    - ``response``: The word search results to extend.
    - ``fetch_page_data``: Whether page data (URLs and hanja information) should be scraped.
    - ``fetch_multimedia``: Whether multimedia URLs should be scraped.
    - ``raise_errors``: Whether errors that occur during scraping should be raised or ignored.

    """

    if len(response['data']['results']) == 0:
        return response

    word_info = response['data']['results'][0]['word_info']
    target_code = response['data']['results'][0]['target_code']

    if fetch_page_data:
        url = response['data']['url']

        [success, doc] = _send_request(url, raise_errors)
        if success:
            _read_view_pronunciation(doc, word_info)
            _read_view_original_language(doc, word_info)

    if fetch_multimedia:
        for dfn_idx, dfn_info in enumerate(word_info['definition_info']):
            if 'multimedia_info' not in dfn_info:
                continue

            for media_idx, multimedia in enumerate(dfn_info['multimedia_info']):
                if multimedia['type'] in ('사진', '삽화'):
                    _fetch_view_images(multimedia, raise_errors)
                elif multimedia['type'] in ('동영상', '애니메이션'):
                    _fetch_view_videos(multimedia, target_code, dfn_idx, media_idx, raise_errors)

    return response

def fetch_today_word(**kwargs):
    """
    Fetches information about the word of the day by scraping the dictionary website.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/#wordofthedayresponse)
    for details about return types.

    - ``guarantee_keys``: Sets whether keys that are missing from the response should be inserted
    with default values. A value of ``True`` guarantees that every key that is not required
    is included, including keys set by the scraper. Default values:
        - The empty string ``""`` for string values.
        - Zero ``0`` for integer values.
        - An empty list ``[]`` for list values.
        - ``None`` for dictionary values. This only applies to the ``translation`` field.
    - ``translation_language``: A language to include a translation for. Possible values:
        - ``'chinese'``
        - ``'english'``
        - ``'japanese'``
        - ``'french'``
        - ``'spanish'``
        - ``'arabic'``
        - ``'mongolian'``
        - ``'vietnamese'``
        - ``'thai'``
        - ``'indonesian'``
        - ``'russian'``

    """

    [lang_query, nation, exonym] = _build_language_query(kwargs.get('translation_language'))
    [_, doc] = _send_request(_BASE_URL.format(nation), True)

    dt_elem = doc.cssselect('dl.today_word > dt')[0]
    dd_elems = doc.cssselect('dl.today_word > dd')
    word_elem = dt_elem.cssselect('a')[0]
    strong_elem = word_elem.cssselect('strong')[0]
    sup_elems = word_elem.cssselect('strong > sup')

    dfn_idx = 0 if not nation and len(dd_elems) < 3 else 1
    result = {
        'target_code': int(_extract_url(word_elem) or 0),
        'word': strong_elem.text.strip(),
        'definition': dd_elems[dfn_idx].text_content().strip()
    }

    result['url'] = _TRANSLATED_VIEW_URL.format(nation, result['target_code'], lang_query)
    result['homograph_num'] = int(sup_elems[0].text_content() or 0 if len(sup_elems) > 0 else 0)

    _read_wotd_details(
        result,
        dt_elem,
        dd_elems,
        exonym,
        kwargs.get('guarantee_keys', False)
    )

    return {'data': result, 'response_type': 'word_of_the_day'}

def fetch_meaning_category_words(**kwargs):
    """
    Fetches words that belong to the provided meaning category.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/scraper/#fetch_meaning_category_words)
    for details.

    - ``guarantee_keys``: Sets whether keys that are missing from the response should be inserted
    with default values. A value of ``True`` guarantees that every key that is not required
    is included, including keys set by the scraper. Default values:
        - The empty string ``""`` for string values.
        - Zero ``0`` for integer values.
        - An empty list ``[]`` for list values.
        - ``None`` for dictionary values. This only applies to the ``translation`` field.
    - ``category``: The meaning category to fetch.
    - ``page``: The page at which the search should start ``[1, 1000]``.
    - ``per_page``: The maximum number of search results to return ``[10, 100]``.
    - ``sort``: The sort method that should be used.
    - ``translation_language``: A language to include translations for.

    """

    page = kwargs.get('page', 1)
    per_page = kwargs.get('per_page', 10)
    [lang, nation, exonym] = _build_language_query(kwargs.get('translation_language'))
    url = _SENSE_URL.format(
        nation,
        lang,
        page,
        per_page,
        'C' if SortMethod.get_value(kwargs.get('sort')) == 'popular' else 'W',
        _build_sense_category_query(kwargs.get('category', 0)))

    [_, doc] = _send_request(url, True)
    [results, total] = _read_search_results(doc, exonym, kwargs.get('guarantee_keys', False))

    return {
        'data': {
            'search_url': url,
            'page': int(page),
            'per_page': int(per_page),
            'total_results': total,
            'results': results
        },
        'response_type': 'scraped_word'
    }

def fetch_subject_category_words(**kwargs):
    """
    Fetches words that belong to one of the provided subject categories.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/scraper/#fetch_subject_category_words)
    for details.

    - ``guarantee_keys``: Sets whether keys that are missing from the response should be inserted
    with default values. A value of ``True`` guarantees that every key that is not required
    is included, including keys set by the scraper. Default values:
        - The empty string ``""`` for string values.
        - Zero ``0`` for integer values.
        - An empty list ``[]`` for list values.
        - ``None`` for dictionary values. This only applies to the ``translation`` field.
    - ``category``: The subject category to fetch.
    - ``page``: The page at which the search should start ``[1, 1000]``.
    - ``per_page``: The maximum number of search results to return ``[10, 100]``.
    - ``sort``: The sort method that should be used.
    - ``translation_language``: A language to include translations for.

    """

    page = kwargs.get('page', 1)
    per_page = kwargs.get('per_page', 10)
    [lang, nation, exonym] = _build_language_query(kwargs.get('translation_language'))
    url = _SUBJECT_URL.format(
        nation,
        lang,
        page,
        per_page,
        'C' if SortMethod.get_value(kwargs.get('sort')) == 'popular' else 'W',
        _build_subject_category_query(kwargs.get('category', 0)))

    [_, doc] = _send_request(url, True)
    [results, total] = _read_search_results(doc, exonym, kwargs.get('guarantee_keys', False))

    return {
        'data': {
            'search_url': url,
            'page': int(page),
            'per_page': int(per_page),
            'total_results': total,
            'results': results
        },
        'response_type': 'scraped_word'
    }

__all__ = [
    'extend_advanced_search',
    'extend_search',
    'extend_view',
    'fetch_today_word',
    'fetch_meaning_category_words',
    'fetch_subject_category_words'
]
