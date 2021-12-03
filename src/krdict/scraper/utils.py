"""
Provides utilities for scraping.
"""

_VIEW_URL = 'https://krdict.korean.go.kr/dicSearch/SearchView?ParaWordNo={}'
_WOTD_NOT_REQUIRED = [
    ('part_of_speech', str),
    ('vocabulary_grade', str),
    ('origin', str),
    ('pronunciation', str),
    ('pronunciation_urls', list),
    ('translation', dict)
]


def _extract_between(text, sep):
    sep_1 = text.find(sep)
    sep_2 = text.find(sep, sep_1 + 1)

    if sep_1 == -1 or sep_2 == -1:
        return None

    return text[sep_1 + 1:sep_2]

def _extract_digits(text):
    value = ''

    for char in text:
        if char.isdigit():
            value += char

    return int(value) if len(value) > 0 else 0

def _read_search_definitions(elem_list, translation_lang, guarantee_keys):
    definitions = []
    step = 3 if translation_lang else 1
    order = 1

    for idx in range(0, len(elem_list), step):
        dfn_elem = elem_list[idx]

        translation = None
        if translation_lang:
            strong_elem = dfn_elem.cssselect('strong')
            word_trns = strong_elem[0].tail.strip()[2:] if strong_elem else dfn_elem.text.strip()

            dfn_elem = elem_list[idx + 1]
            dfn_trns = elem_list[idx + 2].text.strip()

            if len(dfn_trns) > 0:
                translation = {}
                translation['definition'] = dfn_trns

                if len(word_trns) > 0:
                    translation['word'] = word_trns.strip()
                elif guarantee_keys:
                    translation['word'] = None

                translation['language'] = translation_lang

        strong_elem = dfn_elem.cssselect('strong')
        dfn = strong_elem[0].tail.strip()[2:] if strong_elem else dfn_elem.text.strip()

        dfn_obj = {
            'definition': dfn.strip(),
            'order': order
        }

        if translation is not None:
            dfn_obj['translation'] = translation
        elif guarantee_keys:
            dfn_obj['translation'] = None

        definitions.append(dfn_obj)
        order += 1

    return definitions

def _read_search_header(elem, parent_elem, guarantee_keys):
    a_elem = elem.cssselect('a')[0]

    headword_elem = a_elem.cssselect('span')[0]
    sup_elem = headword_elem.cssselect('sup')

    pos_elem = elem.cssselect('span.word_att_type1')
    details_elem = elem.cssselect('span.search_sub')[0]
    star_elem = details_elem.cssselect('span.star')
    hanja_elem = parent_elem.cssselect('dt > span:not(.word_att_type1):not(.search_sub)')

    target_code = int(extract_href(a_elem) or 0)
    result = {
        'target_code': target_code,
        'word': headword_elem.text.strip(),
        'url': _VIEW_URL.format(target_code)
    }

    [pronunciation_urls, pronunciation] = _read_search_pronunciation(details_elem)

    if len(pos_elem) > 0:
        result['part_of_speech'] = pos_elem[0].text.strip()[1:-1]
    elif guarantee_keys:
        result['part_of_speech'] = ''

    result['homograph_num'] = int(sup_elem[0].text.strip() if len(sup_elem) > 0 else 0)

    if len(hanja_elem) > 0:
        result['origin'] = hanja_elem[0].text.strip()[1:-1]
    elif guarantee_keys:
        result['origin'] = ''

    if len(star_elem) > 0:
        result['vocabulary_grade'] = _read_vocabulary_grade(star_elem[0])
    elif guarantee_keys:
        result['vocabulary_grade'] = ''

    if len(pronunciation) > 0 or len(pronunciation_urls) > 0:
        result['pronunciation'] = result['word'] if len(pronunciation) == 0 else pronunciation
    elif guarantee_keys:
        result['pronunciation'] = ''

    if len(pronunciation_urls) > 0:
        result['pronunciation_urls'] = pronunciation_urls
    elif guarantee_keys:
        result['pronunciation_urls'] = []

    return result

def _read_search_pronunciation(elem):
    urls = []
    pronunciation = elem.text.strip()

    for sound in elem.cssselect('a.sound'):
        url = extract_href(sound)

        if url is not None:
            urls.append(url)

        pronunciation += sound.tail.strip()

    if pronunciation.startswith('['):
        pronunciation = pronunciation[1:]
    if pronunciation.endswith(']'):
        pronunciation = pronunciation[:-1]

    return urls, pronunciation

def _read_vocabulary_grade(elem):
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

def read_wotd_details(result, dt_elem, dd_elems, exonym, guarantee_keys):
    """
    Reads informaton about the word of the day.
    """

    em_elem = dt_elem.cssselect('em')
    grade_elem = dt_elem.cssselect('span.star')

    if len(em_elem) == 1:
        result['part_of_speech'] = em_elem[0].text_content()

    if len(grade_elem) == 1:
        result['vocabulary_grade'] =  _read_vocabulary_grade(grade_elem[0])

    _read_wotd_pronunciation(dt_elem, result)

    if len(dd_elems) == 3:
        word_trns = dd_elems[0].text.strip()
        dfn_trns = dd_elems[2].text.strip()

        if len(dfn_trns) > 0:
            result['translation'] = {'definition': dfn_trns}

            if len(word_trns) > 0:
                result['translation']['word'] = word_trns

            result['translation']['language'] = exonym

    if guarantee_keys:
        for key, key_type in _WOTD_NOT_REQUIRED:
            if key in result:
                continue

            result[key] = '' if key_type == str else ([] if key_type == list else None)

        if result['translation'] and 'word' not in result['translation']:
            result['translation']['word'] = ''

def read_search_results(doc, translation_lang, guarantee_keys):
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

        result = _read_search_header(dt_elem[0], result_elem, guarantee_keys)
        result['definitions'] = _read_search_definitions(dd_elem, translation_lang, guarantee_keys)
        results.append(result)

    total = _extract_digits(total_text[0].text) if len(total_text) > 0 else 0
    return results, total
