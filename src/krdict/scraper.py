"""
Retrieves information from the krdict website via scraping.
"""

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
    'searchFlag=Y{}&currentPage={}&blockCount={}&sort={}{}'
)
_TRANSLATED_VIEW_URL = 'https://krdict.korean.go.kr/{}dicSearch/SearchView?ParaWordNo={}{}'


def extend_advanced_search(response, raise_errors):
    """
    Extends word search results with pronunciation URLs
    by scraping the dictionary website.
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
    Extends word search results with pronunciation URLs
    by scraping the dictionary website.
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
    Extends view query results with pronunciation URLs,
    multimedia URLs, and extended original language information
    by scraping the dictionary website.
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

def fetch_today_word(translation_language=None):
    """
    Fetches the Korean word of the day by
    scraping the dictionary website.
    """

    [lang_query, nation, exonym] = _build_language_query(translation_language)
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

    _read_wotd_details(result, dt_elem, dd_elems, nation, exonym)

    return {'data': result}

def fetch_meaning_category_words(**kwargs):
    """
    Fetches words that belong to the
    provided meaning category.
    """

    page = kwargs.get('page', 1)
    per_page = kwargs.get('per_page', 10)
    [lang, nation, exonym] = _build_language_query(kwargs.get('translation_language', ''))
    url = _SENSE_URL.format(
        nation,
        lang,
        page,
        per_page,
        'C' if kwargs.get('sort') == 'popular' else 'W',
        _build_sense_category_query(kwargs.get('category', 0)))

    [_, doc] = _send_request(url, True)
    [results, total] = _read_search_results(doc, exonym)

    return {
        'data': {
            'search_url': url,
            'page': int(page),
            'per_page': int(per_page),
            'total_results': total,
            'results': results
        }
    }

def fetch_subject_category_words(**kwargs):
    """
    Fetches words that belong to one of the
    provided subject categories.
    """

    page = kwargs.get('page', 1)
    per_page = kwargs.get('per_page', 10)
    [lang, nation, exonym] = _build_language_query(kwargs.get('translation_language', ''))
    url = _SUBJECT_URL.format(
        nation,
        lang,
        page,
        per_page,
        'C' if kwargs.get('sort') == 'popular' else 'W',
        _build_subject_category_query(kwargs.get('category', 0)))

    [_, doc] = _send_request(url, True)
    [results, total] = _read_search_results(doc, exonym)

    return {
        'data': {
            'search_url': url,
            'page': int(page),
            'per_page': int(per_page),
            'total_results': total,
            'results': results
        }
    }

__all__ = [
    'extend_advanced_search',
    'extend_search',
    'extend_view',
    'fetch_today_word',
    'fetch_meaning_category_words',
    'fetch_subject_category_words'
]
