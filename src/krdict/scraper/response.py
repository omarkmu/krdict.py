"""
Provides utilities for scraping.
"""

import re
from typing import Any
from .request import get_language_query, send_multimedia_request
from ..types import SearchType

from .constants import (
    _ALL_REFERENCE_STR,
    _CONJUGATION_STR,
    _DERIVATIVE_STR,
    _POS_STR,
    _PRONUNCIATION_STR,
    _RESPONSE_TYPES,
    _VIEW_TRANSLATION_MAPS,
    _SENTENCE_PATT_STR,
    _SENTENCE_PATT_REF_STR,
    _SENTENCE_REFERENCE_STR,
    _RELATED_STRINGS,
    _VIEW_URL
)

_ALLO_PATT = r'^\(.+?\)→'
_CONJU_PATT = r'([^[(]+)(?:\[([^\]]+)\])?(?:\(([^[]+)(?:\[([^\]]+)\])?\))?'
_MULTIMEDIA_URL = 'http://dicmedia.korean.go.kr:8899/front/search/searchResultView.do?file_no={}'


def _extract_between(text, sep):
    sep_1 = text.find(sep)
    sep_2 = text.find(sep, sep_1 + 1)

    if sep_1 == -1 or sep_2 == -1:
        return None

    return text[sep_1 + 1:sep_2]

def _extract_digits(text):
    value = [char for char in text if char.isdigit()]
    return int(''.join(value)) if len(value) > 0 else 0

def _extract_href(elem):
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


def _get_base_result(a_elem, word_text, lang_info):
    target_code = int(_extract_href(a_elem) or 0)
    result = {
        'target_code': target_code,
        'word': word_text,
        'link': _VIEW_URL.format('', '', target_code)
    }

    nation, code, exonym = lang_info

    if nation:
        result['trans_link'] = [{
            'url': _VIEW_URL.format(
                *get_language_query(nation, code),
                target_code
            ),
            'language': exonym
        }]

    return result

def _get_example_text(elem):
    text = []
    for idx, example_el in enumerate([elem, *elem.iterchildren()]):
        is_br = example_el.tag == 'br'
        text.append((example_el.text or '').lstrip() if not is_br else '\n')
        text.append((example_el.tail or '').lstrip() if idx > 0 else '')

    return ''.join(text).strip()


def _read_search_definitions(elem_list, lang_info, response_type):
    definitions = []
    *_, exonym = lang_info
    step = 3 if exonym else 1

    for idx in range(0, len(elem_list), step):
        dfn_elem = elem_list[idx]

        translation = None
        if exonym:
            strong_elem = dfn_elem.cssselect('strong')
            word_trns = (
                strong_elem[0].tail.strip()[2:]
                if strong_elem and response_type != 'dfn'
                else dfn_elem.text_content().strip()
            )

            dfn_elem = elem_list[idx + 1]
            dfn_trns = elem_list[idx + 2].text.strip()

            if len(dfn_trns) > 0:
                translation = {}
                translation['trans_dfn'] = dfn_trns

                if len(word_trns) > 0:
                    translation['trans_word'] = word_trns.strip()

                translation['trans_lang'] = exonym

        strong_elem = dfn_elem.cssselect('strong')
        dfn = (
            strong_elem[0].tail.strip()[2:] if strong_elem and response_type != 'dfn'
            else dfn_elem.text_content().strip()
        )

        dfn_obj = {
            'sense_order': len(definitions) + 1,
            'definition': dfn.strip()
        }

        if translation is not None:
            dfn_obj['translation'] = [translation]

        definitions.append(dfn_obj)

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

def _read_search_header(elem, parent_elem, lang_info):
    a_elem = elem.cssselect('a')[0]

    headword_elem = a_elem.cssselect('span')[0]
    sup_elem = headword_elem.cssselect('sup')

    pos_elem = elem.cssselect('span.word_att_type1')
    details_elem = elem.cssselect('span.search_sub')[0]
    star_elem = details_elem.cssselect('span.star')
    hanja_elem = parent_elem.cssselect('dt > span:not(.word_att_type1):not(.search_sub)')

    result = _get_base_result(a_elem, headword_elem.text.strip(), lang_info)
    pronunciation, pronunciation_urls = _read_search_pronunciation(details_elem)

    if len(pos_elem) > 0:
        result['pos'] = pos_elem[0].text.strip()[1:-1]

    sup_text = sup_elem[0].text.strip() if len(sup_elem) > 0 else ''
    result['sup_no'] = int(sup_text) if sup_text else 0

    if len(hanja_elem) > 0:
        result['origin'] = hanja_elem[0].text.strip()[1:-1]

    if len(star_elem) > 0:
        result['word_grade'] = _read_vocabulary_level(star_elem[0])

    if len(pronunciation) > 0 or len(pronunciation_urls) > 0:
        result['pronunciation'] = result['word'] if len(pronunciation) == 0 else pronunciation

    if len(pronunciation_urls) > 0:
        result['pronunciation_urls'] = pronunciation_urls

    return result

def _read_minimal_search_header(elem, lang_info):
    a_elem = elem.cssselect('a')[0]

    word_elem = a_elem.cssselect('span')[0]
    sup_elem = word_elem.cssselect('sup')

    result = _get_base_result(a_elem, word_elem.text.strip(), lang_info)

    sup_text = sup_elem[0].text.strip() if len(sup_elem) > 0 else ''
    result['sup_no'] = int(sup_text) if sup_text else 0

    return result

def _read_search_pronunciation(elem):
    urls = []
    pronunciation = [elem.text.strip()]

    for sound in elem.cssselect('a.sound'):
        url = _extract_href(sound)

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
            url = _extract_href(sound)

            if url is not None:
                urls.append(url)

        result['pronunciation'] = detail_elem.text.strip()[1:]
        if len(urls) > 0:
            result['pronunciation_urls'] = urls

def _read_wotd_details(result, dt_elem, dd_elems, exonym):
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
            result['translation'] = [{'trans_dfn': dfn_trns}]

            if len(word_trns) > 0:
                result['translation'][0]['trans_word'] = word_trns

            result['translation'][0]['trans_lang'] = exonym

def _read_wotd(doc, lang_info):
    nation, code, exonym = lang_info
    dt_elem = doc.cssselect('dl.today_word > dt')[0]
    dd_elems = doc.cssselect('dl.today_word > dd')
    word_elem = dt_elem.cssselect('a')[0]
    strong_elem = word_elem.cssselect('strong')[0]
    sup_elems = word_elem.cssselect('strong > sup')

    dfn_idx = 0 if not nation or len(dd_elems) < 3 else 1
    result = {
        'target_code': int(_extract_href(word_elem) or 0),
        'word': strong_elem.text.strip(),
        'definition': dd_elems[dfn_idx].text_content().strip()
    }

    result['link'] = _VIEW_URL.format('', '', result['target_code'])

    if nation:
        result['trans_link'] = [{
            'url': _VIEW_URL.format(
                *get_language_query(nation, code),
                result['target_code']
            ),
            'language': exonym
        }]

    result['sup_no'] = int(sup_elems[0].text_content() or 0 if len(sup_elems) > 0 else 0)

    _read_wotd_details(
        result,
        dt_elem,
        dd_elems,
        exonym
    )

    return result, 1

def _read_conju_pronunciations(pron_match, pron_map):
    if not pron_match:
        return []

    pron_info = list(map(lambda x: {'pronunciation': x.strip()}, pron_match.split('/')))
    for p_info in pron_info:
        pron = p_info['pronunciation']
        if pron not in pron_map:
            pron_map[pron] = []

        pron_map[pron].append(p_info)

    return pron_info

def _read_conju_pronunciation_urls(conju_info, sounds, pron_map, headword):
    for sound in sounds:
        text_nodes = sound.xpath('preceding-sibling::text()')
        if not text_nodes:
            continue

        text = text_nodes[-1].split(',')[-1].split('/')[-1].split('[')[-1]
        href = _extract_href(sound)

        if text in pron_map:
            for pron_info in pron_map[text]:
                pron_info['link'] = href
        else:
            conju_info.append({
                'conjugation_info': {
                    'conjugation': '',
                    'pronunciation_info': [{'pronunciation': headword, 'link': href}]
                }
            })

def _read_conjugation_info(word_info, dd_el, headword):
    span = dd_el.cssselect('span.search_sub')[0]
    sounds = span.cssselect('a')

    text_list = ''.join([
        (e.text if i == 0 else e.tail) or '' for i, e in enumerate([span] + sounds)
    ]).split(',')

    conju_info = []
    pron_map = {}

    for text in text_list:
        match = re.match(_CONJU_PATT, text)
        if not match:
            continue

        info: dict[str, Any] = {
            'conjugation_info': {
                'conjugation': match[1].strip(),
                'pronunciation_info': _read_conju_pronunciations(match[2], pron_map)
            }
        }

        if match[3] is not None:
            info['abbreviation_info'] = [{
                'abbreviation': match[3].strip(),
                'pronunciation_info': _read_conju_pronunciations(match[4], pron_map)
            }]

        conju_info.append(info)

    _read_conju_pronunciation_urls(conju_info, sounds, pron_map, headword)
    word_info['conju_info'] = conju_info

def _read_pronunciation(word_info, dd_el):
    span = dd_el.cssselect('span.search_sub')[0]
    sounds = span.cssselect('a')
    text_list = (span.text + ''.join(map(lambda x: x.tail, sounds))).strip()[1:-1].split('/')

    pron_info = []
    for idx, elem in enumerate(text_list):
        pron_info.append({
            'pronunciation': elem or word_info['word'],
            'link': (_extract_href(sounds[idx]) or '') if idx < len(sounds) else ''
        })

    word_info['pronunciation_info'] = pron_info

def _read_related_info(parent_el, lang_info, type_=None):
    rel_info = []
    nation, code, exonym = lang_info

    for idx, elem in enumerate([parent_el] + [*parent_el.iterchildren()]):
        text_list = ((elem.text if idx == 0 else elem.tail) or '').split(',')

        if idx > 0 and elem.tag == 'a':
            target_code = int(_extract_href(elem) or 0)
            obj = None

            if target_code != 0:
                obj = {
                    'word': (elem.text or '').strip(),
                    'link_target_code': target_code,
                    'link': _VIEW_URL.format('', '', target_code),
                    'trans_link': [{
                        'url': _VIEW_URL.format(
                            *get_language_query(nation, code),
                            target_code
                        ),
                        'language': exonym
                    }],
                    'link_type': 'C'
                }
            else:
                obj = {
                    'word': (elem.text or '').strip(),
                    'link_type': 'T'
                }

            if type_ is not None:
                obj['type'] = type_

            rel_info.append(obj)

        for text in text_list:
            if not text.strip():
                continue

            text_obj = {
                'word': text.strip(),
                'link_type': 'T'
            }

            if type_ is not None:
                text_obj['type'] = type_

            rel_info.append(text_obj)

    return rel_info

def _read_definition_footer(def_obj, lang_info, elem):
    nation, *_ = lang_info
    translation_map = _VIEW_TRANSLATION_MAPS.get(nation, {})
    dl_elements = elem.cssselect('div.heading_wrap > dl')

    reference = elem.cssselect('div.star_wrap > p')
    if reference:
        span = reference[0].cssselect('span')
        def_obj['reference'] = (span[0].tail if span else reference[0].text_content()).strip()

    for dl_el in dl_elements:
        dd_el = dl_el.cssselect('dd')[0]
        dt_text = dl_el.cssselect('dt')[0].text_content().strip()
        footer_type = translation_map.get(dt_text, dt_text).strip()

        if footer_type in _RELATED_STRINGS:
            if 'rel_info' not in def_obj:
                def_obj['rel_info'] = []
            def_obj['rel_info'].extend(_read_related_info(dd_el, lang_info, footer_type))
        elif footer_type == _SENTENCE_PATT_STR:
            def_obj['pattern_info'] = list(map(
                lambda x: {'pattern': x.strip()},
                dd_el.text_content().split(',')
            ))
        elif footer_type == _SENTENCE_PATT_REF_STR:
            def_obj['pattern_reference'] = dd_el.text_content().strip()
        elif footer_type == _SENTENCE_REFERENCE_STR:
            def_obj['reference'] = dd_el.text_content().strip()

def _read_definitions(word_info, def_elements, lang_info, subword=False):
    def_info = []
    *_, exonym = lang_info

    for elem in def_elements:
        trans_word = elem.cssselect('p.subMultiTrans' if subword else 'p.multiTrans')
        dfn_text = (
            elem.cssselect(
                ('p.subSenseDef' if subword else 'p.senseDef')
                if trans_word else 'p.printArea'
            )[0].text_content() or ''
        ).strip()

        def_obj = {
            'definition': (
                dfn_text[len(def_info) + 2:].strip()
                if dfn_text.startswith(str(len(def_info) + 1))
                else dfn_text
            ),
            'example_info': list(map(
                lambda e: {'example': _get_example_text(e)}, elem.cssselect('ul.dot > li')
            ))
        }

        if trans_word:
            trans_word = (trans_word[0].text_content() or '').strip()
            def_obj['translation'] = [{
                'trans_word': (
                    trans_word[len(def_info) + 2:].strip()
                    if dfn_text.startswith(str(len(def_info) + 1))
                    else trans_word
                ),
                'trans_dfn': (
                    elem.cssselect(
                        'p.subMultiSenseDef' if subword else 'p.multiSenseDef'
                    )[0].text_content() or ''
                ).strip(),
                'trans_lang': exonym
            }]

        _read_definition_footer(def_obj, lang_info, elem)

        def_info.append(def_obj)

    if not subword and len(def_info) == 1 and re.match(_ALLO_PATT, def_info[0]['definition']):
        allomorph = def_info[0]['definition']
        word_info['allomorph'] = allomorph[allomorph.find('(') + 1:allomorph.find(')')]

    return def_info

def _read_view_hanja_info(cur_obj, dl_elem):
    dt_element = dl_elem.cssselect('dt')
    dd_elements = dl_elem.cssselect('dd:not(.chi_boosu)')
    detail_element = dl_elem.cssselect('dd.chi_boosu')

    if len(dt_element) == 0 or len(dd_elements) == 0 or len(detail_element) == 0:
        return

    hanja = dt_element[0].text_content().strip()
    if hanja == '/':
        cur_obj['original_language'] += hanja
        return

    details = detail_element[0].text_content().strip()

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

def _read_origin(word_info, nation, rows):
    original_language_info = []
    language_map = _VIEW_TRANSLATION_MAPS.get(nation, {})

    for tr_elem in rows:
        th_elem = tr_elem.cssselect('th')
        if len(th_elem) > 0:
            language_type = (th_elem[0].text_content() or '').strip()
            original_language_info.append({
                'original_language': '',
                'language_type': language_map.get(language_type, language_type)
            })

            if original_language_info[-1]['language_type'] == '한자':
                original_language_info[-1]['hanja_info'] = []

        td_elements = tr_elem.cssselect('td')
        if len(td_elements) == 0:
            continue

        cur = original_language_info[-1]
        if cur['language_type'] != '한자':
            cur['original_language'] += td_elements[0].text_content().strip()
            continue

        for dl_elem in td_elements[0].cssselect('dl'):
            _read_view_hanja_info(cur, dl_elem)

    word_info['original_language_info'] = original_language_info

def _read_media_urls(doc, is_video):
    if is_video:
        vid_script = doc.cssselect('body > div script')
        if not vid_script:
            return []

        return _extract_video_urls(vid_script[0].text_content())

    img = doc.cssselect('p.img > img')
    if not img:
        return []

    return [img[0].get('src')]

def _read_multimedia(word_info, multimedia_elements, target_code, fetch_multimedia):
    for li_elem in multimedia_elements:
        a_elem = li_elem.cssselect('a')[0]

        href = a_elem.get('href')
        href_components = href[href.find('(') + 1:href.rfind(')')].split(',')

        if len(href_components) != 4:
            href = a_elem.get('onclick')
            href_components = href[href.find('(') + 1:href.rfind(')')].split(',')

        file_no, def_order, media_order = map(_extract_digits, href_components[1:])

        def_info = word_info['sense_info'][def_order - 1]
        if 'multimedia_info' not in def_info:
            def_info['multimedia_info'] = []

        is_video = href_components[0] == "'video'"
        media_info = {
            'label': li_elem.cssselect('p')[0].text_content().strip(),
            'type': '동영상' if is_video else '사진',
            'file_no': file_no,
            'link': _MULTIMEDIA_URL.format(file_no),
            'thumb_link': a_elem.cssselect('img')[0].get('src', '')
        }

        def_info['multimedia_info'].append(media_info)

        if fetch_multimedia:
            media_info['content_urls'] = _read_media_urls(
                send_multimedia_request({
                    'multimedia_type': 3 if is_video else 1,
                    'target_code': target_code,
                    'definition_order': def_order,
                    'media_order': media_order
                }),
                is_video
            )

def _read_subwords(word_info, subword_elements, lang_info):
    subword_info = []
    nation, *_ = lang_info
    translation_map = _VIEW_TRANSLATION_MAPS.get(nation, {})

    for elem in subword_elements:
        title_el = elem.cssselect('dl.idiom_title')[0]
        subword_unit = title_el.cssselect('dt')[0].text_content().strip()

        subword = title_el.cssselect('dd')[0].text_content().strip()
        subword_unit = translation_map.get(subword_unit, subword_unit)

        subword_info.append({
            'subword': subword,
            'subword_unit': subword_unit,
            'subsense_info': _read_definitions(
                elem,
                elem.cssselect('div.explain_list_wrap > div.explain_list'),
                lang_info,
                True
            )
        })

    word_info['subword_info'] = subword_info

def _read_search_results(doc, response_type, lang_info):
    results = []
    search_results = doc.cssselect('div.search_result > dl')
    total_text = doc.cssselect('span.search_tit > em')

    for result_elem in search_results:
        dt_elem = result_elem.cssselect('dt')
        dd_elem = result_elem.cssselect('dd')

        if len(dt_elem) == 0 or len(dd_elem) == 0:
            continue

        result: dict
        if response_type in ('dfn', 'ip'):
            result = _read_minimal_search_header(dt_elem[0], lang_info)
        else:
            result = _read_search_header(dt_elem[0], result_elem, lang_info)

        result['sense'] = _read_search_definitions(dd_elem, lang_info, response_type)
        results.append(result)

    total = _extract_digits(total_text[0].text) if len(total_text) > 0 else 0
    return results, total

def _read_examples(doc, lang_info):
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

        result = _get_base_result(result_elem, word_text, lang_info)
        result['sup_no'] = sup_no
        result['example'] = example_text
        results.append(result)

    total = _extract_digits(total_text[0].text) if len(total_text) > 0 else 0
    return results, total

def _read_view_header_box(word_info, dl_elements, headword, lang_info):
    nation, *_ = lang_info
    translation_map = _VIEW_TRANSLATION_MAPS.get(nation, {})

    for dl_el in dl_elements:
        ref_img = dl_el.cssselect('dt > img[alt="가봐라"]')

        dd_el = dl_el.cssselect('dd')[0]
        dt_text = _DERIVATIVE_STR if ref_img else (dl_el.cssselect('dt')[0].text or '').strip()
        info_type = translation_map.get(dt_text, dt_text).strip()

        if info_type == _POS_STR:
            word_info['pos'] = dd_el.cssselect('span')[0].text.strip()[1:-1]
        elif info_type == _PRONUNCIATION_STR:
            _read_pronunciation(word_info, dd_el)
        elif info_type == _CONJUGATION_STR:
            _read_conjugation_info(word_info, dd_el, headword)
        elif info_type == _DERIVATIVE_STR:
            deriv_el = dd_el.cssselect('span.search_sub')[0]
            word_info['der_info'] = _read_related_info(deriv_el, lang_info)
        elif info_type in (_ALL_REFERENCE_STR, _SENTENCE_REFERENCE_STR):
            word_info['reference'] = dd_el.text_content().strip()

def _read_view_content(doc, target_code, lang_info, kwargs):
    result_div = doc.cssselect('div.search_detail')

    if not result_div:
        return [], 0

    result_div = result_div[0]
    headword_span = result_div.cssselect('span.word_head')[0]
    headword_text = (headword_span.text or '').strip()

    if not headword_text:
        return [], 0

    sup = headword_span.cssselect('sup')
    grade_elem = result_div.cssselect('span.star')

    word_info = {
        'word': headword_text,
        'sup_no': int(sup[0].text or '0') if sup else 0,
        'word_grade': _read_vocabulary_level(grade_elem[0]) if grade_elem else ''
    }

    _read_view_header_box(
        word_info,
        result_div.cssselect('div.word_head_box > dl'),
        headword_text,
        lang_info
    )
    _read_origin(
        word_info,
        lang_info[0],
        doc.cssselect('div.chi_tooltip > table > tbody > tr')
    )
    word_info['sense_info'] = _read_definitions(
        word_info,
        result_div.cssselect('div.search_detail_view > div.detail_list > div.explain_list'),
        lang_info
    )
    _read_subwords(
        word_info,
        result_div.cssselect('div.idiom_wrap > div'),
        lang_info
    )
    _read_multimedia(
        word_info,
        result_div.cssselect('div.multi_list div.sliderkit-nav li'),
        target_code,
        kwargs.get('fetch_multimedia', False)
    )

    return [{
        'target_code': target_code,
        'word_info': word_info
    }], 1

def _read_response(*args):
    doc, response_type, target_code, lang_info, scndary_trans_langs, kwargs = args

    if response_type == 'exam':
        return _read_examples(doc, lang_info)

    if response_type == 'word_of_the_day':
        return _read_wotd(doc, lang_info)

    if response_type == 'view':
        return _read_view_content(doc, target_code, lang_info, kwargs)

    return _read_search_results(doc, response_type, lang_info)


def parse_response(*args):
    """
    Transforms a scraped HTTP response into a response object.
    """

    doc, response_type, url, kwargs, lang_info, trans_urls, scndary_trans_langs = args
    target_code = int(kwargs.get('target_code', 0))
    response_type = SearchType.get_value(response_type, response_type)

    if response_type not in _RESPONSE_TYPES:
        raise ValueError

    results, total = _read_response(
        doc,
        response_type,
        target_code,
        lang_info,
        scndary_trans_langs,
        kwargs
    )

    return _RESPONSE_TYPES[response_type]({
        'link': url,
        'trans_link': trans_urls,
        'start': int(kwargs.get('page', 1)),
        'num': int(kwargs.get('per_page', 10)),
        'total': total,
        'item': results
    })
