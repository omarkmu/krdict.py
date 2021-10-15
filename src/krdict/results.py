"""
Handles processing of search results, including key remapping,
type conversion, and restructuring.
"""

from typing import Any

def _handle_conju_info(elem):
    if not 'conjugation_info' in elem:
        return elem

    for key in list(elem['conjugation_info'].keys()):
        elem[key] = elem['conjugation_info'][key]

    del elem['conjugation_info']

    return elem

def _handle_link_type(elem):
    return elem == 'C'

_CONVERT_LIST = [
    'category_info',
    'conjugation_info',
    'derivative_info',
    'example_info',
    'results',
    'multimedia_info',
    'original_language_info',
    'pattern_info',
    'pronunciation_info',
    'reference_info',
    'related_info',
    'definitions',
    'definition_info',
    'subword_info',
    'subdefinition_info',
    'translations'
]
_CONVERT_NUM = [
    'error_code',
    'num_results',
    'link_target_code',
    'order',
    'start_index',
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
_REMAPS = {
    'channel': 'data',
    'conju_info': 'conjugation_info',
    'der_info': 'derivative_info',
    'item': 'results',
    'lastBuildDate': 'last_build_date',
    'link_type': 'has_target_code',
    'num': 'num_results',
    'ref_info': 'reference_info',
    'rel_info': 'related_info',
    'sup_no': 'homograph_num',
    'sense': 'definitions',
    'sense_info': 'definition_info',
    'sense_order': 'order',
    'subsense_info': 'subdefinition_info',
    'pos': 'part_of_speech',
    'start': 'start_index',
    'word_grade': 'vocabulary_grade',
    'translation': 'translations',
    'trans_lang': 'language',
    'trans_word': 'word',
    'trans_dfn': 'definition',
    'total': 'total_results'
}

def postprocessor(_, key: str, value: Any):
    """
    Performs postprocessing on elements converted from XML.
    """

    if value is None:
        return None

    if key in _HANDLERS:
        value = _HANDLERS[key](value)

    if isinstance(value, dict):
        for l_key in _CONVERT_LIST:
            if l_key in value and not isinstance(value[l_key], list):
                value[l_key] = [value[l_key]]
        for s_key in _CONVERT_SINGLE:
            if s_key in value and isinstance(value[s_key], list):
                value[s_key] = value[s_key][0]

    key = _REMAPS[key] if key in _REMAPS else key
    value = int(value) if key in _CONVERT_NUM else value

    return key, value
