"""
Provides utilities for scraping.
"""

import requests
from lxml import html
from .types import MeaningCategory, SubjectCategory

_ADVANCED_SEARCH_URL = (
    'https://krdict.korean.go.kr/dicSearchDetail/searchDetailWordsResult?'
    'searchFlag=Y&searchOp=AND&syllablePosition='
)
_VIDEO_URL = (
    'https://krdict.korean.go.kr/dicSearch/viewMovieConfirm?'
    'searchKindValue=video&ParaWordNo={}&ParaSenseSeq={}&multiMediaSeq={}'
)
_VIEW_URL = 'https://krdict.korean.go.kr/dicSearch/SearchView?ParaWordNo={}'

_AFTER_SEARCH_URL = [
    'description',
    'last_build_date',
    'total_results',
    'page',
    'per_page',
    'results'
]
_LANG_INFO = {
    'mongolian': ['mon', 1, '몽골어'],
    'vietnamese': ['vie', 2, '베트남어'],
    'thai': ['tha', 3, '타이어'],
    'indonesian': ['ind', 4, '인도네시아어'],
    'russian': ['rus', 5, '러시아어'],
    'english': ['eng', 6, '영어'],
    'japanese': ['jpn', 7, '일본어'],
    'french': ['fra', 8, '프랑스어'],
    'spanish': ['spa', 9, '스페인어'],
    'arabic': ['ara', 10, '아랍어'],
    'chinese': ['chn', 11, '중국어']
}
_LANG_MAP = {
    '0': 'all',
    '1': '0',
    '2': '32',
    '3': '97',
    '4': '17',
    '25': '16'
}
_LANG_SKIP = [
    12,
    15,
    16,
    21,
    24,
    25,
    26,
    27,
    33,
    34,
    35,
    38,
    43,
    44
]
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
_WOTD_NOT_REQUIRED = [
    ('part_of_speech', str),
    ('vocabulary_grade', str),
    ('origin', str),
    ('pronunciation', str),
    ('pronunciation_urls', list),
    ('translation', dict)
]


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
        'convert': lambda x: _LANG_MAP.get(str(x),
            '99' if int(x) > 47 or int(x) in _LANG_SKIP
            else str(int(x) - 4 - len([i for i in _LANG_SKIP if i < int(x)])))
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
        'get_all': lambda: ['1', '2', '3', '0'],
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
        'get_all': lambda: [str(i) for i in range(1, 15)] + ['27'],
        'convert': lambda x: '27' if str(x) == '15' else str(x)
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


def _build_advanced_search_url(params):
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
            value_arr = (
                adv_mapper['get_all']() if 'get_all' in adv_mapper
                else adv_mapper['value'].values()
            )

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

def _build_language_query(lang):
    [nation, code, exo] = _LANG_INFO.get(lang, ['', 0, ''])

    if code == 0:
        return '', '', None

    return f'&nation={nation}&nationCode={code}', f'{nation}/', exo

def _build_sense_category_query(category):
    category = MeaningCategory.get_value(category, category)

    if category <= 0 or category > 153:
        return '&lgCategoryCode=0&miCategoryCode=-1'

    if category == 1:
        return '&lgCategoryCode=1&miCategoryCode=-1'

    code_large = 0
    code_mid = 1000 + category if category < 129 else 1100 + category

    for idx, cat_max in enumerate(_SENSE_CAT_MAX):
        if category == cat_max + 1:
            code_large = idx + 2
            code_mid = -1
            break

        if category <= cat_max:
            code_large = idx + 1
            break

    return f'&lgCategoryCode={code_large}&miCategoryCode={code_mid}'

def _build_subject_category_query(category):
    if not isinstance(category, list):
        category = [category]

    value = ''

    for cat in category:
        cat_value = SubjectCategory.get_value(cat, cat)

        if cat_value == '0':
            value = ''

            for i in range(1, 107):
                value += f'&actCategory={_convert_subject_cat(i)}'

            return value

        value += f'&actCategory={_convert_subject_cat(cat_value)}'

    return value


def _extract_between(string, sep):
    sep_1 = string.find(sep)
    sep_2 = string.find(sep, sep_1 + 1)

    if sep_1 == -1 or sep_2 == -1:
        return None

    return string[sep_1 + 1:sep_2]

def _extract_digits(text):
    value = ''

    for char in text:
        if char.isdigit():
            value += char

    return int(value) if len(value) > 0 else 0

def _extract_url(elem):
    href = elem.get('href', '')
    return _extract_between(href, "'")

def _extract_video_urls(script_content):
    content = script_content.split(',')

    urls = []
    for raw_str in content:
        extracted = _extract_between(raw_str, "'")
        if extracted is not None and extracted != 'video':
            urls.append(extracted)

    return urls


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

def _get_vocabulary_grade(elem):
    grade = len(elem.cssselect('i.ri-star-s-fill'))
    if grade == 1:
        return '고급'
    if grade == 2:
        return '중급'
    if grade == 3:
        return '초급'

    return ''


def _insert_search_url(response, url):
    if 'error' in response:
        return

    values = []
    data = response['data']
    for field in _AFTER_SEARCH_URL:
        values.append(data[field])
        del data[field]

    data['search_url'] = url
    for idx, field in enumerate(_AFTER_SEARCH_URL):
        data[field] = values[idx]


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

        pronunciation_info[idx]['url'] = _extract_url(elem)

    if 'pronunciation_info' not in word_info:
        word_info['pronunciation_info'] = pronunciation_info

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

    target_code = int(_extract_url(a_elem) or 0)
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
        result['vocabulary_grade'] = _get_vocabulary_grade(star_elem[0])
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
        url = _extract_url(sound)

        if url is not None:
            urls.append(url)

        pronunciation += sound.tail.strip()

    if pronunciation.startswith('['):
        pronunciation = pronunciation[1:]
    if pronunciation.endswith(']'):
        pronunciation = pronunciation[:-1]

    return urls, pronunciation

def _read_search_results(doc, translation_lang, guarantee_keys):
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
                urls.append([_extract_url(elem), text_nodes[-1]])

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

def _read_wotd_details(result, dt_elem, dd_elems, exonym, guarantee_keys):
    em_elem = dt_elem.cssselect('em')
    grade_elem = dt_elem.cssselect('span.star')

    if len(em_elem) == 1:
        result['part_of_speech'] = em_elem[0].text_content()

    if len(grade_elem) == 1:
        result['vocabulary_grade'] =  _get_vocabulary_grade(grade_elem[0])

    for detail_elem in dt_elem.cssselect('span:not(.star)'):
        text = detail_elem.text_content().strip()

        if text.startswith('('):
            result['origin'] = text[1:-1]
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
