"""
Provides utilities for scraping.
"""

from krdict.types.scraper import ScrapedExampleResponse
from ..types import (
    ScrapedWordResponse,
    SearchType,
    WordOfTheDayResponse
)
from .request import _get_lang_query

_VIEW_URL = 'https://krdict.korean.go.kr/dicSearch/SearchView?ParaWordNo={}'
_TRANSLATED_VIEW_URL = 'https://krdict.korean.go.kr{}/dicSearch/SearchView?{}ParaWordNo={}'


def _extract_between(text, sep):
    sep_1 = text.find(sep)
    sep_2 = text.find(sep, sep_1 + 1)

    if sep_1 == -1 or sep_2 == -1:
        return None

    return text[sep_1 + 1:sep_2]

def _extract_digits(text):
    value = [char for char in text if char.isdigit()]
    return int(''.join(value)) if len(value) > 0 else 0

def _get_base_result(a_elem, word_text, nation, code):
    target_code = int(extract_href(a_elem) or 0)
    result = {
        'target_code': target_code,
        'word': word_text,
        'link': _VIEW_URL.format(target_code)
    }

    if nation:
        result['trans_link'] = _TRANSLATED_VIEW_URL.format(
            *_get_lang_query(nation, code),
            target_code
        )

    return result

def _read_search_definitions(elem_list, exonym):
    definitions = []
    step = 3 if exonym else 1
    order = 1

    for idx in range(0, len(elem_list), step):
        dfn_elem = elem_list[idx]

        translation = None
        if exonym:
            strong_elem = dfn_elem.cssselect('strong')
            word_trns = strong_elem[0].tail.strip()[2:] if strong_elem else dfn_elem.text.strip()

            dfn_elem = elem_list[idx + 1]
            dfn_trns = elem_list[idx + 2].text.strip()

            if len(dfn_trns) > 0:
                translation = {}
                translation['trans_dfn'] = dfn_trns

                if len(word_trns) > 0:
                    translation['trans_word'] = word_trns.strip()

                translation['trans_lang'] = exonym

        strong_elem = dfn_elem.cssselect('strong')
        dfn = strong_elem[0].tail.strip()[2:] if strong_elem else dfn_elem.text.strip()

        dfn_obj = {
            'sense_order': order,
            'definition': dfn.strip()
        }

        if translation is not None:
            dfn_obj['translation'] = translation

        definitions.append(dfn_obj)
        order += 1

    return definitions

def _read_example_text(text, sup_no):
    paren = text.find('(')
    rparen = text.find(')')
    colon = text.find(':')
    word_text = text[colon + 1:rparen].strip()
    example_text = text[:paren].strip()

    if sup_no:
        word_text = word_text[:-len(str(sup_no))].strip()

    return word_text, example_text

def _read_search_header(elem, parent_elem, nation, code):
    a_elem = elem.cssselect('a')[0]

    headword_elem = a_elem.cssselect('span')[0]
    sup_elem = headword_elem.cssselect('sup')

    pos_elem = elem.cssselect('span.word_att_type1')
    details_elem = elem.cssselect('span.search_sub')[0]
    star_elem = details_elem.cssselect('span.star')
    hanja_elem = parent_elem.cssselect('dt > span:not(.word_att_type1):not(.search_sub)')

    result = _get_base_result(a_elem, headword_elem.text.strip(), nation, code)
    pronunciation, pronunciation_urls = _read_search_pronunciation(details_elem)

    if len(pos_elem) > 0:
        result['pos'] = pos_elem[0].text.strip()[1:-1]

    result['sup_no'] = int(sup_elem[0].text.strip() if len(sup_elem) > 0 else 0)

    if len(hanja_elem) > 0:
        result['origin'] = hanja_elem[0].text.strip()[1:-1]

    if len(star_elem) > 0:
        result['word_grade'] = _read_vocabulary_level(star_elem[0])

    if len(pronunciation) > 0 or len(pronunciation_urls) > 0:
        result['pronunciation'] = result['word'] if len(pronunciation) == 0 else pronunciation

    if len(pronunciation_urls) > 0:
        result['pronunciation_urls'] = pronunciation_urls

    return result

def _read_search_pronunciation(elem):
    urls = []
    pronunciation = [elem.text.strip()]

    for sound in elem.cssselect('a.sound'):
        url = extract_href(sound)

        if url is not None:
            urls.append(url)

        pronunciation.append(sound.tail.strip())

    pronunciation = ''.join(pronunciation)

    if pronunciation.startswith('['):
        pronunciation = pronunciation[1:]
    if pronunciation.endswith(']'):
        pronunciation = pronunciation[:-1]

    return pronunciation, urls

def _read_vocabulary_level(elem):
    grade = len(elem.cssselect('i.ri-star-s-fill'))
    if grade == 1:
        return '고급'
    if grade == 2:
        return '중급'
    if grade == 3:
        return '초급'

    return ''

def _read_wotd_pronunciation(dt_elem, result):
    for detail_elem in dt_elem.cssselect('span:not(.star)'):
        text = detail_elem.text_content().strip()

        if text.startswith('('):
            result['origin'] = text[1:-1]
            continue
        if not text.startswith('['):
            continue

        urls = []
        for sound in detail_elem.cssselect('a.sound'):
            url = extract_href(sound)

            if url is not None:
                urls.append(url)

        result['pronunciation'] = detail_elem.text.strip()[1:]
        if len(urls) > 0:
            result['pronunciation_urls'] = urls

def _read_wotd(doc, nation, code, exonym):
    dt_elem = doc.cssselect('dl.today_word > dt')[0]
    dd_elems = doc.cssselect('dl.today_word > dd')
    word_elem = dt_elem.cssselect('a')[0]
    strong_elem = word_elem.cssselect('strong')[0]
    sup_elems = word_elem.cssselect('strong > sup')

    dfn_idx = 0 if not nation or len(dd_elems) < 3 else 1
    result = {
        'target_code': int(extract_href(word_elem) or 0),
        'word': strong_elem.text.strip(),
        'definition': dd_elems[dfn_idx].text_content().strip()
    }

    result['link'] = _VIEW_URL.format(result['target_code'])

    if nation:
        result['trans_link'] = _TRANSLATED_VIEW_URL.format(
            *_get_lang_query(nation, code),
            result['target_code']
        )

    result['sup_no'] = int(sup_elems[0].text_content() or 0 if len(sup_elems) > 0 else 0)

    read_wotd_details(
        result,
        dt_elem,
        dd_elems,
        exonym
    )

    return result


def extract_href(elem):
    """
    Extracts the URL from the href attribute of the given element.
    """

    href = elem.get('href', '')
    return _extract_between(href, "'")

def extract_video_urls(script_content):
    """
    Extracts video URLs from the content of a script element.
    """

    content = script_content.split(',')

    urls = []
    for raw_str in content:
        extracted = _extract_between(raw_str, "'")
        if extracted is not None and extracted != 'video':
            urls.append(extracted)

    return urls

def parse_response(*args):
    """
    Transforms a scraped HTTP response to a response object.
    """

    doc, response_type, url, url_kr, page, per_page, lang_info = args
    response_type = SearchType.get_value(response_type, response_type)

    if response_type == 'word_of_the_day':
        return WordOfTheDayResponse(_read_wotd(doc, *lang_info))

    if response_type in ('meaning_category', 'subject_category', 'word'):
        results, total = read_search_results(doc, *lang_info)
        return ScrapedWordResponse({
            'link': url_kr,
            'trans_link': url,
            'start': page,
            'num': per_page,
            'total': total,
            'item': results
        })

    if response_type == 'exam':
        results, total = read_examples(doc, lang_info[0], lang_info[1])
        return ScrapedExampleResponse({
            'link': url_kr,
            'trans_link': url,
            'start': page,
            'num': per_page,
            'total': total,
            'item': results
        })

    raise ValueError

def read_conjugation_pronunciation(arr, urls, idx):
    """
    Reads the URLs of conjugations' pronunciations.
    """

    if idx == -1:
        return -1

    for pron_info in arr:
        [cur_url, url_text] = urls[idx]

        if url_text.endswith(pron_info['pronunciation']):
            pron_info['url'] = cur_url
            idx += 1

        if idx >= len(urls):
            return -1

    return idx

def read_pronunciation(word_info, sounds):
    """
    Reads the URLs of words' pronunciations.
    """

    pronunciation_info = word_info.get('pronunciation_info', [])
    for idx, elem in enumerate(sounds):
        if idx >= len(pronunciation_info):
            pronunciation_info.append({ 'pronunciation': word_info['word'] })

        pronunciation_info[idx]['url'] = extract_href(elem)

    if 'pronunciation_info' not in word_info:
        word_info['pronunciation_info'] = pronunciation_info

def read_view_hanja_info(cur_obj, dl_elem):
    """
    Reads extended hanja information.
    """

    dt_element = dl_elem.cssselect('dt')
    dd_elements = dl_elem.cssselect('dd:not(.chi_boosu)')
    detail_element = dl_elem.cssselect('dd.chi_boosu')

    if len(dt_element) == 0 or len(dd_elements) == 0 or len(detail_element) == 0:
        return

    hanja = dt_element[0].text_content()
    if hanja == '/':
        cur_obj['original_language'] += hanja
        return

    details = detail_element[0].text_content()

    slash_idx = details.find('/')
    stroke_idx = details.find('총획')

    info = {'hanja': hanja}

    if slash_idx != -1 and stroke_idx != -1:
        info['radical'] = details[3:slash_idx]

        strokes = details[stroke_idx + 3:]
        if strokes.isdigit():
            info['stroke_count'] = int(strokes)

    readings = []
    for dd_elem in dd_elements:
        normalized_reading = dd_elem.text_content().strip().replace('\xa0', ' ')
        readings.append(normalized_reading)

    info['readings'] = readings
    cur_obj['hanja_info'].append(info)
    cur_obj['original_language'] += hanja

def read_wotd_details(result, dt_elem, dd_elems, exonym):
    """
    Reads informaton about the word of the day.
    """

    em_elem = dt_elem.cssselect('em')
    grade_elem = dt_elem.cssselect('span.star')

    if len(em_elem) > 0:
        result['pos'] = em_elem[0].text_content()

    if len(grade_elem) == 1:
        result['word_grade'] =  _read_vocabulary_level(grade_elem[0])

    _read_wotd_pronunciation(dt_elem, result)

    if len(dd_elems) == 3:
        word_trns = dd_elems[0].text.strip()
        dfn_trns = dd_elems[2].text.strip()

        if len(dfn_trns) > 0:
            result['translation'] = {'trans_dfn': dfn_trns}

            if len(word_trns) > 0:
                result['translation']['trans_word'] = word_trns

            result['translation']['trans_lang'] = exonym

def read_search_results(doc, nation, code, exonym):
    """
    Reads search result information.
    """

    results = []
    search_results = doc.cssselect('div.search_result > dl')
    total_text = doc.cssselect('span.search_tit > em')

    for result_elem in search_results:
        dt_elem = result_elem.cssselect('dt')
        dd_elem = result_elem.cssselect('dd')

        if len(dt_elem) == 0 or len(dd_elem) == 0:
            continue

        result = _read_search_header(dt_elem[0], result_elem, nation, code)
        result['sense'] = _read_search_definitions(dd_elem, exonym)
        results.append(result)

    total = _extract_digits(total_text[0].text) if len(total_text) > 0 else 0
    return results, total

def read_examples(doc, nation, code):
    """
    Reads example information.
    """

    results = []
    search_results = doc.cssselect('div.search_result > ul > li > a')
    total_text = doc.cssselect('span.search_tit > em')

    for result_elem in search_results:
        text = result_elem.text_content().strip()
        sup_elem = result_elem.cssselect('sup')

        if len(text) == 0:
            continue

        sup_text = sup_elem[0].text.strip() if len(sup_elem) > 0 else ''
        sup_no = int(sup_text) if sup_text else 0

        word_text, example_text = _read_example_text(text, sup_no)

        result = _get_base_result(result_elem, word_text, nation, code)
        result['sup_no'] = sup_no
        result['example'] = example_text
        results.append(result)

    total = _extract_digits(total_text[0].text) if len(total_text) > 0 else 0
    return results, total
