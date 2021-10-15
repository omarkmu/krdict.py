"""
Retrieves information from the krdict website via scraping.
"""

from ._scraper_utils import (
    _build_advanced_search_link,
    _extract_url,
    _fetch_view_images,
    _fetch_view_videos,
    _read_view_pronunciation,
    _read_view_original_language,
    _send_request
)

_BASE_URL = 'https://krdict.korean.go.kr/mainAction'
_SEARCH_URL = (
    'https://krdict.korean.go.kr/dicSearch/search?'
    'mainSearchWord={}&currentPage={}&blockCount={}&sort={}')
_VIEW_URL = 'https://krdict.korean.go.kr/dicSearch/SearchView?ParaWordNo={}'


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

    url = _build_advanced_search_link(response['request_params'])
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

def fetch_daily_word():
    """
    Fetches the Korean word of the day by
    scraping the dictionary website.
    """

    [_, doc] = _send_request(_BASE_URL, True)

    dt_elem = doc.cssselect('dl.today_word > dt')[0]
    word_elem = dt_elem.cssselect('a')[0]
    sup = word_elem.cssselect('strong > sup')[0]
    sup_text = sup.text_content()
    target_code_text = _extract_url(word_elem)

    result = {
        'target_code': int(target_code_text) if target_code_text is not None else 0,
        'word': sup.xpath('preceding-sibling::text()')[0].strip(),
        'definition': doc.cssselect('dl.today_word > dd')[0].text_content().strip(),
        'url': _VIEW_URL.format(target_code_text),
        'homograph_num': int(sup_text) if len(sup_text) > 0 else 0
    }

    em_elem = dt_elem.cssselect('em')
    grade_elem = dt_elem.cssselect('span.star')

    if len(em_elem) == 1:
        result['part_of_speech'] = em_elem[0].text_content()
    if len(grade_elem) == 1:
        result['vocabulary_grade'] = grade_elem[0].get('title')

    for detail_elem in dt_elem.cssselect('span:not(.star)'):
        text = detail_elem.text_content().strip()

        if text.startswith('('):
            result['original_language'] = text[1:-1]
            continue
        if not text.startswith('['):
            continue

        urls = []
        for sound in detail_elem.cssselect('a.sound'):
            url = _extract_url(sound)

            if url is not None:
                urls.append(url)

        result['pronunciation'] = detail_elem.text.strip()[1:]
        if len(urls) > 0:
            result['pronunciation_urls'] = urls

    return { 'data': result }

__all__ = [
    'extend_advanced_search',
    'extend_search',
    'extend_view',
    'fetch_daily_word'
]
