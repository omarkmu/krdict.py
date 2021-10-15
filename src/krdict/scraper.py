"""
Retrieves information from the krdict website via scraping.
"""

import requests
from lxml import html

_BASE_URL = 'https://krdict.korean.go.kr/mainAction'
_ADVANCED_SEARCH_URL = (
    'https://krdict.korean.go.kr/dicSearchDetail/searchDetailWordsResult?'
    'searchFlag=Y&searchOp=AND&syllablePosition='
)
_SEARCH_URL = (
    'https://krdict.korean.go.kr/dicSearch/search?'
    'mainSearchWord={}&currentPage={}&blockCount={}&sort={}')
_VIDEO_URL = (
    'https://krdict.korean.go.kr/dicSearch/viewMovieConfirm?'
    'searchKindValue=video&ParaWordNo={}&ParaSenseSeq={}&multiMediaSeq={}')
_VIEW_URL = 'https://krdict.korean.go.kr/dicSearch/SearchView?ParaWordNo={}'

_LANG_MAP = {
    '0': 'all',
    '1': '0',
    '2': '32',
    '3': '97',
    '4': '17',
    '25': '16'
}
_SENSE_CAT_MAX = [
    17,
    30,
    41,
    50,
    59,
    76,
    83,
    92,
    100,
    110,
    118,
    125,
    133,
    153
]

def _map_lang(value):
    map_value = _LANG_MAP.get(value)
    if map_value is not None:
        return map_value

    value = int(value)
    delta = -1
    if value < 12:
        delta = 4
    elif value in (13, 14):
        delta = 5
    elif 17 <= value < 21:
        delta = 7
    elif value in (22, 23):
        delta = 8
    elif 28 <= value < 33:
        delta = 10
    elif value in (36, 37):
        delta = 13
    elif 39 <= value < 43:
        delta = 14
    elif 45 <= value < 48:
        delta = 16

    if delta == -1:
        return '99'

    return str(value - delta)

def _map_pos(value):
    value = str(value)
    if value == '15':
        return '27'

    return value
def _get_all_pos():
    pos = []

    for i in range(1, 15):
        pos.append(str(i))

    pos.append('27')
    return pos
def _get_all_level():
    return ['1', '2', '3', '0']

def _convert_subject_cat(value):
    value = int(value)

    if value == 0:
        values = []
        for i in range(1, 107):
            values.append(_convert_subject_cat(i))

        return ','.join(values)

    if value < 40:
        return str(20000 + value)

    if value < 77:
        return str(30000 + value - 39)

    return str(40000 + value - 76)

def _convert_sense_cat(value):
    value = int(value)

    if value == 0 or value > 153:
        return None

    top = ''
    middle = ''

    if 1 <= value < 129:
        middle = str(1000 + value)
    elif value >= 129:
        middle = str(1100 + value)

    for idx, top_max in enumerate(_SENSE_CAT_MAX):
        if value <= top_max:
            top = str(idx + 1)
            break

    return {'senseCategoryTop': top, 'senseCategoryMiddle': middle}

_ADVANCED_PARAM_MAP = {
    'q': {
        'name': 'query'
    },
    'start': {
        'name': 'currentPage'
    },
    'num': {
        'name': 'blockCount'
    },
    'sort': {
        'name': 'sort',
        'value': {
            'dict': 'W',
            'popular': 'C'
        }
    },
    'target': {
        'name': 'searchTarget',
        'default': '1',
        'value': {
            '1': 'word',
            '2': 'definition',
            '3': 'example',
            '4': 'org_language',
            '5': 'pronunciation',
            '6': 'conjugation',
            '7': 'shorten',
            '8': 'idiom',
            '9': 'proverb',
            '10': 'reference'
        }
    },
    'lang': {
        'name': 'searchOrglanguage',
        'default': '0',
        'convert': _map_lang
    },
    'method': {
        'name': 'wordCondition',
        'default': 'exact',
        'value': {
            'exact': 'wordSame',
            'include': 'wordAll',
            'start': 'wordStart',
            'end': 'wordEnd'
        }
    },
    'type1': {
        'name': 'gubun',
        'use_all': True,
        'default': 'all',
        'value': {
            'word': 'W',
            'phrase': 'P',
            'expression': 'E'
        }
    },
    'type2': {
        'name': 'wordNativeCode',
        'use_all': True,
        'default': 'all',
        'value': {
            'native': '1',
            'chinese': '2',
            'loanword': '3',
            'hybrid': '0'
        }
    },
    'level': {
        'name': 'imcnt',
        'use_all': True,
        'get_all': _get_all_level,
        'default': 'all',
        'value': {
            'level1': '1',
            'level2': '2',
            'level3': '3'
        }
    },
    'pos': {
        'name': 'sp_code',
        'use_all': True,
        'all_value': '0',
        'default': '0',
        'get_all': _get_all_pos,
        'convert': _map_pos
    },
    'multimedia': {
        'name': 'multimedia',
        'use_all': True,
        'all_value': '0',
        'default': '0',
        'value': {
            '1': 'P',
            '2': 'I',
            '3': 'V',
            '4': 'S',
            '5': 'A',
            '6': 'N'
        }
    },
    'letter_s': {
        'name': 'searchSyllableStart'
    },
    'letter_e': {
        'name': 'searchSyllableEnd'
    },
    'sense_cat': {
        'convert': _convert_sense_cat
    },
    'subject_cat': {
        'name': 'actCategoryList',
        'multi': True,
        'convert': _convert_subject_cat
    }
}

def _extract_between(string, sep):
    sep_1 = string.find(sep)
    sep_2 = string.find(sep, sep_1 + 1)

    if sep_1 == -1 or sep_2 == -1:
        return None

    return string[sep_1 + 1:sep_2]

def _extract_pronunciation_url(sound):
    href = sound.get('href', '')
    return _extract_between(href, "'")

def _extract_video_urls(script_content):
    content = script_content.split(',')

    urls = []
    for raw_str in content:
        extracted = _extract_between(raw_str, "'")
        if extracted is not None and extracted != 'video':
            urls.append(extracted)

    return urls

def _get_advanced_all_value(adv_mapper):
    if 'get_all' in adv_mapper:
        return adv_mapper['get_all']()

    return adv_mapper['value'].values()

def _get_advanced_map_value(adv_mapper, value):
    if isinstance(value, list):
        values = []

        for val in value:
            val = _get_advanced_map_value(adv_mapper, val)
            values.append(val)

        return values

    if 'value' in adv_mapper:
        return adv_mapper['value'].get(str(value))

    if 'convert' in adv_mapper:
        return adv_mapper['convert'](value)

    return value

def _build_advanced_search_link(params):
    url = _ADVANCED_SEARCH_URL

    for adv_key in list(_ADVANCED_PARAM_MAP.keys()):
        adv_mapper = _ADVANCED_PARAM_MAP[adv_key]
        param_value = params.get(adv_key, adv_mapper.get('default'))

        if param_value is None:
            continue

        param_value = str(param_value)
        use_all = adv_mapper.get('use_all', False)
        all_value = adv_mapper.get('all_value', 'all')

        if use_all and param_value == all_value:
            value_arr = _get_advanced_all_value(adv_mapper)

            url += f'&all_{adv_mapper["name"]}=ALL'
            for value in value_arr:
                url += f'&{adv_mapper["name"]}={value}'

            continue

        if use_all or adv_mapper.get('multi', False):
            param_value = _get_advanced_map_value(adv_mapper, param_value.split(','))
        else:
            param_value = _get_advanced_map_value(adv_mapper, param_value)

        if isinstance(param_value, list):
            for value in param_value:
                url += f'&{adv_mapper["name"]}={value}'
        elif isinstance(param_value, dict):
            for key in param_value.keys():
                url += f'&{key}={param_value[key]}'
        else:
            url += f'&{adv_mapper["name"]}={param_value}'

    return url

def _read_conju_pronunciation(arr, urls, idx):
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

def _read_page_pronunciation(word_info, sounds):
    pronunciation_info = word_info.get('pronunciation_info', [])
    for idx, elem in enumerate(sounds):
        if idx >= len(pronunciation_info):
            pronunciation_info.append({ 'pronunciation': word_info['word'] })

        pronunciation_info[idx]['url'] = _extract_pronunciation_url(elem)

    if 'pronunciation_info' not in word_info:
        word_info['pronunciation_info'] = pronunciation_info

def _read_view_hanja_info(cur_obj, dl_elem):
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

def _read_view_pronunciation(doc, word_info):
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
            _read_page_pronunciation(word_info, sounds)
        elif row_title == '활용' and 'conjugation_info' in word_info:
            urls = []
            for elem in sounds:
                text_nodes = elem.xpath('preceding-sibling::text()')
                urls.append([_extract_pronunciation_url(elem), text_nodes[-1]])

            idx = 0
            for conju_info in word_info['conjugation_info']:
                if 'pronunciation_info' in conju_info:
                    idx = _read_conju_pronunciation(conju_info['pronunciation_info'], urls, idx)

                abbr_info = conju_info.get('abbreviation_info')
                if abbr_info is not None and 'pronunciation_info' in abbr_info:
                    idx = _read_conju_pronunciation(abbr_info['pronunciation_info'], urls, idx)

def _read_view_original_language(doc, word_info):
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
        if len(td_elements) == 0:
            continue

        cur = info[info_idx]
        if cur['language_type'] != '한자':
            cur['original_language'] += td_elements[0].text_content()
            continue

        for dl_elem in td_elements[0].cssselect('dl'):
            _read_view_hanja_info(cur, dl_elem)

def _send_request(url, raise_errors):
    try:
        response = requests.get(url, headers={'Accept-Language': '*'})
        response.raise_for_status()
        doc = html.fromstring(response.text)

        return [True, doc]
    except requests.exceptions.RequestException as exc:
        if raise_errors:
            raise exc

        return [False, None]

def _fetch_view_images(multimedia, raise_errors):
    if 'url' not in multimedia:
        return

    [success, doc] = _send_request(multimedia['url'], raise_errors)
    if not success:
        return

    img = doc.cssselect('p.pic > img')

    if len(img) == 0:
        return

    url = img[0].get('src')
    if url is not None:
        multimedia['media_urls'] = [url]

def _fetch_view_videos(multimedia, target_code, dfn_idx, media_idx, raise_errors):
    req_url = _VIDEO_URL.format(target_code, dfn_idx + 1, media_idx + 1)

    [success, doc] = _send_request(req_url, raise_errors)
    if not success:
        return

    vid_script = doc.cssselect('body > div script')
    if len(vid_script) == 0:
        return

    urls = _extract_video_urls(vid_script[0].text_content())
    if len(urls) > 0:
        multimedia['media_urls'] = urls



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
            pron_url = _extract_pronunciation_url(elem)
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
            pron_url = _extract_pronunciation_url(elem)
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
    target_code_text = _extract_between(word_elem.get('href'), "'")

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
            url = _extract_pronunciation_url(sound)

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
