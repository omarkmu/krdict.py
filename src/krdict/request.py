"""
Transforms input parameters into API-compliant dicts.
"""

import requests
from xmltodict import parse as parse_xml

from ._results import postprocessor
from .scraper import extend_view, extend_search, extend_advanced_search
from .types import (
    Classification,
    KRDictException,
    MeaningCategory,
    MultimediaType,
    PartOfSpeech,
    SearchMethod,
    SearchTarget,
    SearchType,
    SortMethod,
    SubjectCategory,
    TargetLanguage,
    TranslationLanguage,
    OriginType,
    VocabularyLevel
)

_SEARCH_URL = 'https://krdict.korean.go.kr/api/search'
_VIEW_URL = 'https://krdict.korean.go.kr/api/view'
_DEFAULTS = {
    'API_KEY': None,
    'FETCH_MULTIMEDIA': False,
    'FETCH_PAGE_DATA': True,
    'RAISE_SCRAPER_ERRORS': False,
    'USE_SCRAPER': False
}
_PARAM_MAPS = {
    'query': {
        'name': 'q'
    },
    'page': {
        'name': 'start'
    },
    'per_page': {
        'name': 'num'
    },
    'sort': {
        'name': 'sort',
        'type': SortMethod
    },
    'search_type': {
        'name': 'part',
        'type': SearchType
    },
    'translation_language': {
        'name': 'trans_lang',
        'type': TranslationLanguage
    },
    'search_target': {
        'name': 'target',
        'type': SearchTarget
    },
    'target_language': {
        'name': 'lang',
        'type': TargetLanguage
    },
    'search_method': {
        'name': 'method',
        'type': SearchMethod
    },
    'classification': {
        'name': 'type1',
        'type': Classification
    },
    'origin_type': {
        'name': 'type2',
        'type': OriginType
    },
    'vocabulary_grade': {
        'name': 'level',
        'type': VocabularyLevel
    },
    'part_of_speech': {
        'name': 'pos',
        'type': PartOfSpeech
    },
    'multimedia_info': {
        'name': 'multimedia',
        'type': MultimediaType
    },
    'min_syllables': {
        'name': 'letter_s'
    },
    'max_syllables': {
        'name': 'letter_e'
    },
    'meaning_category': {
        'name': 'sense_cat',
        'type': MeaningCategory
    },
    'subject_category': {
        'name': 'subject_cat',
        'type': SubjectCategory
    },
    'target_code': {
        'name': 'q'
    }
}


def _get_search_type(search_type):
    value = SearchType.get_value(search_type)

    if value == 'ip':
        return 'idiom_proverb'

    if value == 'dfn':
        return 'definition'

    if value == 'exam':
        return 'example'

    if value == 'word':
        return value

    return search_type

def _map_value(mapper, value):
    if isinstance(value, list):
        return ','.join(map(lambda x: _map_value(mapper, x), value))

    if 'type' in mapper:
        return str(mapper['type'].get_value(value, value))

    return str(value)

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


def _transform_params(params, search_type):
    params = params.copy()

    url = None

    if 'key' not in params and _DEFAULTS['API_KEY'] is not None:
        params['key'] = _DEFAULTS['API_KEY']
    if 'raise_api_errors' in params:
        del params['raise_api_errors']
    if 'guarantee_keys' in params:
        del params['guarantee_keys']
    if 'options' in params:
        del params['options']

    if search_type == 'view':
        url = _VIEW_URL
        transform_view_params(params)
    else:
        url = _SEARCH_URL
        transform_search_params(params)

    return params, url


def send_request(params, search_type=None):
    """
    Sends a request to the API endpoint specified by ``search_type`` and returns a response object.

    - ``search_type``: The type of search which should be performed
    ``'word' | 'idiom_proverb' | 'definition' | 'example' | 'view'``.
    - ``params``: The provided input parameters.

    """

    search_type = _get_search_type(search_type or params.get('search_type', 'word'))
    options = params.get('options', {})
    guarantee = params.get('guarantee_keys', False)
    raise_api_errors = params.get('raise_api_errors', False)

    (params, url) = _transform_params(params, search_type)

    try:
        response = requests.get(url, params)
        response.raise_for_status()
        result = parse_xml(
            response.text,
            dict_constructor=dict,
            postprocessor=lambda _, k, v: postprocessor(k, v, search_type, guarantee)
        )

        if raise_api_errors and 'error' in result:
            error = result['error']
            raise KRDictException(error['message'], error['error_code'], params)

        result['request_params'] = params
        result['response_type'] = search_type if 'error' not in result else 'error'

        if 'data' in result and 'results' not in result['data']:
            result['data']['results'] = []

        return _postprocess(result, params, options, search_type)
    except requests.exceptions.RequestException as exc:
        raise exc

def set_default(name, value):
    """
    Sets the default value of the given option.

    - ``name``: The name of the option to set.
        - ``'fetch_multimedia'``: Controls whether multimedia is scraped during view queries.
        No effect unless the 'use_scraper' option is True.
        - ``'fetch_page_data'``: Controls whether pronunciation URLs and extended language
        information are scraped. No effect unless the 'use_scraper' option is True.
        - ``'raise_scraper_errors'``: Controls whether errors that occur during scraping are raised.
        No effect unless the 'use_scraper' option is True.
        - ``'use_scraper'``: Controls whether the scraper should be used to fetch more information.
    - ``value``: Boolean value; sets or unsets a default value.

    """

    name = name.upper()

    if name == 'API_KEY' or name not in _DEFAULTS:
        return

    _DEFAULTS[name] = value is True

def set_key(key):
    """
    Sets the API key to use when a key is not specified in a request.

    - ``key``: The API key to use, or None to unset the key.

    """

    _DEFAULTS['API_KEY'] = key

def transform_search_params(params):
    """
    Transforms input search parameters into an API-compliant dict.

    - ``params``: The provided input parameters.

    """

    for key in list(params.keys()):
        if params[key] is None:
            del params[key]
            continue
        if key not in _PARAM_MAPS:
            continue

        mapper = _PARAM_MAPS[key]
        new_key = mapper['name']
        new_value = _map_value(mapper, params[key])

        params[new_key] = new_value

        if key != new_key:
            del params[key]

    if 'trans_lang' in params and 'translated' not in params:
        params['translated'] = 'y'
    if 'letter_s' in params and 'letter_e' not in params:
        params['letter_e'] = '0'
    if 'letter_e' in params and 'letter_s' not in params:
        params['letter_s'] = '1'

def transform_view_params(params):
    """
    Transforms input view parameters into an API-compliant dict.

    - ``params``: The provided input parameters.

    """

    if 'target_code' in params:
        params['method'] = 'target_code'
    else:
        if 'query' in params:
            if 'homograph_num' in params:
                params['query'] += str(params['homograph_num'])
                del params['homograph_num']
            else:
                params['query'] += '0'

    transform_search_params(params)
