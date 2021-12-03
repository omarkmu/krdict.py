"""
Handles extending search results with scraping.
"""

from .utils import (
    extract_href,
    read_pronunciation,
    read_conjugation_pronunciation,
    read_view_hanja_info,
    extract_video_urls
)
from .request import send_extend_request, send_image_request, send_video_request


def _extend_advanced_search_response(doc, response, url):
    results = response['data']['results']
    elements = doc.cssselect('div.search_result > dl')

    for idx, result in enumerate(results):
        if idx >= len(elements):
            break

        urls = []
        for elem in elements[idx].cssselect('a.sound'):
            pron_url = extract_href(elem)
            if pron_url is not None:
                urls.append(pron_url)

        if len(urls) > 0:
            result['pronunciation_urls'] = urls

    response['data']['search_url'] = url

def _extend_search_response(doc, response, url):
    results = response['data']['results']
    elements = doc.cssselect('dl.printArea')

    for idx, result in enumerate(results):
        if idx >= len(elements):
            break

        urls = []
        for elem in elements[idx].cssselect('a.sound'):
            pron_url = extract_href(elem)
            if pron_url is not None:
                urls.append(pron_url)

        if len(urls) > 0:
            result['pronunciation_urls'] = urls

    response['data']['search_url'] = url

def _extend_view_pronunciation(doc, word_info):
    for row in doc.cssselect('div.word_head_box > dl'):
        row_title = row.cssselect('dt')
        content = row.cssselect('dd > span.search_sub')
        if len(row_title) == 0 or len(content) == 0:
            continue

        row_title = row_title[0].text_content()
        sounds = content[0].cssselect('a.sound')

        if len(sounds) == 0:
            continue

        if row_title == '발음':
            read_pronunciation(word_info, sounds)
        elif row_title == '활용' and 'conjugation_info' in word_info:
            urls = []
            for elem in sounds:
                text_nodes = elem.xpath('preceding-sibling::text()')
                urls.append([extract_href(elem), text_nodes[-1]])

            idx = 0
            for conju_info in word_info['conjugation_info']:
                if 'pronunciation_info' in conju_info:
                    pron_info = conju_info['pronunciation_info']
                    idx = read_conjugation_pronunciation(pron_info, urls, idx)

                abbr_info = conju_info.get('abbreviation_info')
                if abbr_info is not None and 'pronunciation_info' in abbr_info:
                    idx = read_conjugation_pronunciation(abbr_info['pronunciation_info'], urls, idx)

def _extend_view_original_language(doc, word_info):
    if 'original_language_info' not in word_info:
        return

    info = word_info['original_language_info']
    info_idx = -1

    for tr_elem in doc.cssselect('div.chi_tooltip > table > tbody > tr'):
        if len(tr_elem.cssselect('th')) > 0:
            info_idx += 1

            if info_idx >= len(info):
                break

            info[info_idx]['original_language'] = ''

            if info[info_idx]['language_type'] == '한자':
                info[info_idx]['hanja_info'] = []

        td_elements = tr_elem.cssselect('td')
        if len(td_elements) == 0 or info_idx == -1:
            continue

        cur = info[info_idx]
        if cur['language_type'] != '한자':
            cur['original_language'] += td_elements[0].text_content()
            continue

        for dl_elem in td_elements[0].cssselect('dl'):
            read_view_hanja_info(cur, dl_elem)

def _extend_images(multimedia, raise_errors):
    doc = send_image_request(multimedia, raise_errors)
    if doc is None:
        return

    img = doc.cssselect('p.pic > img')

    if len(img) == 0:
        return

    url = img[0].get('src')
    if url is not None:
        multimedia['media_urls'] = [url]

def _extend_videos(multimedia, target_code, dfn_idx, media_idx, raise_errors):
    doc = send_video_request(target_code, dfn_idx, media_idx, raise_errors)
    if doc is None:
        return

    vid_script = doc.cssselect('body > div script')
    if len(vid_script) == 0:
        return

    urls = extract_video_urls(vid_script[0].text_content())
    if len(urls) > 0:
        multimedia['media_urls'] = urls

def _extend_view_multimedia(response, raise_errors):
    word_info = response['data']['results'][0]['word_info']
    target_code = response['data']['results'][0]['target_code']

    for dfn_idx, dfn_info in enumerate(word_info['definition_info']):
        if 'multimedia_info' not in dfn_info:
            continue

        for media_idx, multimedia in enumerate(dfn_info['multimedia_info']):
            if multimedia['type'] in ('사진', '삽화'):
                _extend_images(multimedia, raise_errors)
            elif multimedia['type'] in ('동영상', '애니메이션'):
                _extend_videos(multimedia, target_code, dfn_idx, media_idx, raise_errors)

def _extend_response(doc, url, request_type, response):
    if doc is None:
        return response

    if request_type == 'advanced':
        _extend_advanced_search_response(doc, response, url)
    elif request_type == 'search':
        _extend_search_response(doc, response, url)
    elif request_type == 'view':
        word_info = response['data']['results'][0]['word_info']
        _extend_view_pronunciation(doc, word_info)
        _extend_view_original_language(doc, word_info)

    return response


def extend_advanced_search(response, raise_errors):
    """
    Extends word search results with pronunciation URLs by scraping the dictionary website.
    This function modifies the response in-place, and returns the modified object.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/#wordsearchresponse)
    for details.

    - ``response``: The word search results to extend.
    - ``raise_errors``: Whether errors that occur during scraping should be raised or ignored.
    """

    return _extend_response(*send_extend_request('advanced', response, raise_errors))

def extend_search(response, raise_errors):
    """
    Extends word search results with pronunciation URLs by scraping the dictionary website.
    This function modifies the response in-place, and returns the modified object.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/#wordsearchresponse)
    for details.

    - ``response``: The word search results to extend.
    - ``raise_errors``: Whether errors that occur during scraping should be raised or ignored.
    """

    return _extend_response(*send_extend_request('search', response, raise_errors))

def extend_view(response, fetch_page_data, fetch_multimedia, raise_errors):
    """
    Extends view query results with pronunciation URLs, multimedia URLs, and extended hanja
    information by scraping the dictionary website.
    This function modifies the response in-place, and returns the modified object.

    See the [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/#viewresponse)
    for details.

    - ``response``: The word search results to extend.
    - ``fetch_page_data``: Whether page data (URLs and hanja information) should be scraped.
    - ``fetch_multimedia``: Whether multimedia URLs should be scraped.
    - ``raise_errors``: Whether errors that occur during scraping should be raised or ignored.
    """

    if fetch_page_data:
        _extend_response(*send_extend_request('view', response, raise_errors))

    if fetch_multimedia:
        _extend_view_multimedia(response, raise_errors)

    return response
