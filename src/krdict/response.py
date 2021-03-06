"""
Handles processing of search results, including key remapping,
type conversion, and restructuring.
"""

from xmltodict import parse as parse_xml
from .types import KRDictException
from .scraper import extend_view, extend_search, extend_advanced_search


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
_DEFAULTS = {
    'FETCH_MULTIMEDIA': False,
    'FETCH_PAGE_DATA': True,
    'RAISE_SCRAPER_ERRORS': False,
    'USE_SCRAPER': False
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

def _postprocess(response, params, options, search_type):
    if 'error' in response:
        return response

    if search_type == 'view' and options.get('use_scraper', _DEFAULTS['USE_SCRAPER']):
        fetch_page = options.get('fetch_page_data', _DEFAULTS['FETCH_PAGE_DATA'])
        fetch_media = options.get('fetch_multimedia', _DEFAULTS['FETCH_MULTIMEDIA'])
        raise_errors = options.get('raise_scraper_errors', _DEFAULTS['RAISE_SCRAPER_ERRORS'])
        return extend_view(response, fetch_page, fetch_media, raise_errors)

    use_scraper = (
        params.get('part') == 'word'
        and options.get('use_scraper', _DEFAULTS['USE_SCRAPER'])
        and options.get('fetch_page_data', _DEFAULTS['FETCH_PAGE_DATA'])
    )

    if use_scraper:
        raise_errors = options.get('raise_scraper_errors', _DEFAULTS['RAISE_SCRAPER_ERRORS'])
        return (
            extend_advanced_search(response, raise_errors) if params.get('advanced') == 'y'
            else extend_search(response, raise_errors)
        )

    return response


def parse_response(kwargs, api_response, request_params, search_type):
    """
    Transforms an HTTP response to a response object.

    - ``kwargs``: The provided input keyword arguments.
    - ``api_response``: Whether or not this an advanced search.
    - ``request_params``: The request parameters which were sent to the API.
    - ``search_type``: The type of search which was performed.
    """

    response = parse_xml(
        api_response.text,
        dict_constructor=dict,
        postprocessor=(
            lambda _, k, v:
            postprocessor(k, v, search_type, kwargs.get('guarantee_keys', False))
        )
    )

    if kwargs.get('raise_api_errors', False) and 'error' in response:
        error = response['error']
        raise KRDictException(error['message'], error['error_code'], request_params)

    response['request_params'] = request_params
    response['response_type'] = search_type if 'error' not in response else 'error'

    if 'data' in response and 'results' not in response['data']:
        response['data']['results'] = []

    return _postprocess(response, request_params, kwargs.get('options', {}), search_type)

def postprocessor(key, value, search_type, guarantee_keys):
    """
    Performs postprocessing on elements converted from XML.

    - ``key``: The original XML node name.
    - ``value``: The unprocessed value.
    - ``search_type``: The type of search which produced this key-value pair.
    - ``guarantee_keys``: Whether to guarantee keys in dicts.
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

        if guarantee_keys and key in _NOT_REQUIRED_KEYS:
            _guarantee(value, search_type, _NOT_REQUIRED_KEYS[key])

        key = _REMAPS.get(key, key)
    else:
        key = _REMAPS.get(key, key)
        value = int(value) if key in _CONVERT_NUM else value



    return key, value

def set_default(option, value):
    """
    Sets the default value of the given option.

    - ``option``: The name of the option to set.
        - ``'fetch_multimedia'``: Controls whether multimedia is scraped during view queries.
        No effect unless the 'use_scraper' option is True.
        - ``'fetch_page_data'``: Controls whether pronunciation URLs and extended language
        information are scraped. No effect unless the 'use_scraper' option is True.
        - ``'raise_scraper_errors'``: Controls whether errors that occur during scraping are raised.
        No effect unless the 'use_scraper' option is True.
        - ``'use_scraper'``: Controls whether the scraper should be used to fetch more information.
    - ``value``: Boolean value; sets or unsets a default value.
    """

    option = option.upper()

    if option not in _DEFAULTS:
        return

    _DEFAULTS[option] = value is True
