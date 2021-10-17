"""
Handles processing of search results, including key remapping,
type conversion, and restructuring.
"""

from typing import Any


def _handle_conju_info(elem):
    if 'conjugation_info' not in elem:
        return elem

    for key in list(elem['conjugation_info'].keys()):
        elem[key] = elem['conjugation_info'][key]

    del elem['conjugation_info']

    if 'pronunciation_info' in elem:
        pron_info = elem['pronunciation_info']
        del elem['pronunciation_info']
        elem['pronunciation_info'] = pron_info

    if 'abbreviation_info' in elem:
        abbr_info = elem['abbreviation_info']
        del elem['abbreviation_info']
        elem['abbreviation_info'] = abbr_info

    return elem

def _handle_link_type(elem):
    return elem == 'C'


_CONVERT_LIST = [
    'category_info',
    'conjugation_info',
    'definitions',
    'definition_info',
    'derivative_info',
    'example_info',
    'multimedia_info',
    'original_language_info',
    'pattern_info',
    'pronunciation_info',
    'reference_info',
    'related_info',
    'results',
    'subword_info',
    'subdefinition_info',
    'translations'
]
_CONVERT_NUM = [
    'error_code',
    'order',
    'page',
    'per_page',
    'homograph_num',
    'target_code',
    'total_results'
]
_CONVERT_SINGLE = [
    'part_of_speech'
]
_HANDLERS = {
    'conju_info': _handle_conju_info,
    'link_type': _handle_link_type
}
_NOT_REQUIRED_KEYS = {
    'abbreviation_info': [
        ('pronunciation_info', list)
    ],
    'channel': [
        ('search_url', str, ['word'])
    ],
    'conjugation_info': [
        ('pronunciation_info', list),
        ('abbreviation_info', list)
    ],
    'definition_info': [
        ('reference', str),
        ('translations', list),
        ('example_info', list),
        ('pattern_info', list),
        ('related_info', list),
        ('multimedia_info', list)
    ],
    'derivative_info': [
        ('target_code', int)
    ],
    'item': [
        ('origin', str, ['word']),
        ('pronunciation', str, ['word']),
        ('vocabulary_grade', str, ['word']),
        ('pronunciation_urls', list, ['word'])
    ],
    'multimedia_info': [
        ('media_urls', list)
    ],
    'original_language_info': [
        ('hanja_info', list)
    ],
    'pronunciation_info': [
        ('url', str)
    ],
    'pattern_info': [
        ('pattern_reference', str)
    ],
    'related_info': [
        ('target_code', int)
    ],
    'reference_info': [
        ('target_code', int)
    ],
    'sense': [
        ('translations', list)
    ],
    'subdefinition_info': [
        ('example_info', list),
        ('related_info', list)
    ],
    'translation': [
        ('word', str)
    ],
    'word_info': [
        ('allomorph', str),
        ('original_language_info', list),
        ('pronunciation_info', list),
        ('conjugation_info', list),
        ('derivative_info', list),
        ('reference_info', list),
        ('category_info', list),
        ('subword_info', list)
    ]
}
_REMAPS = {
    'channel': 'data',
    'conju_info': 'conjugation_info',
    'der_info': 'derivative_info',
    'item': 'results',
    'lastBuildDate': 'last_build_date',
    'link': 'url',
    'link_target_code': 'target_code',
    'link_type': 'has_target_code',
    'num': 'per_page',
    'ref_info': 'reference_info',
    'rel_info': 'related_info',
    'sup_no': 'homograph_num',
    'sense': 'definitions',
    'sense_info': 'definition_info',
    'sense_order': 'order',
    'subsense_info': 'subdefinition_info',
    'pos': 'part_of_speech',
    'start': 'page',
    'word_grade': 'vocabulary_grade',
    'translation': 'translations',
    'trans_lang': 'language',
    'trans_word': 'word',
    'trans_dfn': 'definition',
    'total': 'total_results',
    'written_form': 'name'
}


def _guarantee(value, search_type, keys):
    for tup in keys:
        key = tup[0]
        key_type = tup[1]

        if len(tup) == 3 and search_type not in tup[2]:
            continue
        if key in value:
            continue

        if key_type == str:
            value[key] = ''
        elif key_type == int:
            value[key] = 0
        elif key_type == list:
            value[key] = []


def postprocessor(key: str, value: Any, search_type: str, guarantee: bool):
    """
    Performs postprocessing on elements converted from XML.
    """

    if value is None:
        return None

    if key in _HANDLERS:
        value = _HANDLERS[key](value)

    if isinstance(value, dict):
        for c_key in value:
            if c_key in _CONVERT_LIST and not isinstance(value[c_key], list):
                value[c_key] = [value[c_key]]
            elif c_key in _CONVERT_SINGLE and isinstance(value[c_key], list):
                value[c_key] = value[c_key][0]

        if guarantee and key in _NOT_REQUIRED_KEYS:
            _guarantee(value, search_type, _NOT_REQUIRED_KEYS[key])

        key = _REMAPS.get(key, key)
    else:
        key = _REMAPS.get(key, key)
        value = int(value) if key in _CONVERT_NUM else value



    return key, value
