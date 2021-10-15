"""
Provides functions which query the Korean Learner's Dictionary API.
"""

import requests
from xmltodict import parse as parse_xml
from ._params import transform_search_params, transform_view_params
from ._results import postprocessor
from .scraper import extend_view, extend_search, extend_advanced_search

_SEARCH_URL = 'https://krdict.korean.go.kr/api/search'
_VIEW_URL = 'https://krdict.korean.go.kr/api/view'
_DEFAULTS = {
    'API_KEY': None,
    'FETCH_MULTIMEDIA': False,
    'FETCH_PAGE_DATA': True,
    'RAISE_SCRAPER_ERRORS': False,
    'USE_SCRAPER': False
}

class KRDictException(Exception):
    """
    Contains information about an API error.
    This exception is only thrown if the argument passed to the
    `raise_api_errors` parameter is True.
    """

    def __init__(self, message, error_code, params):
        super().__init__(message)

        self.message = message
        self.error_code = error_code
        self.request_params = params

    def __reduce__(self):
        return (KRDictException, (self.message, self.error_code, self.request_params))

def _send_request(url, params):
    raise_api_errors = False
    if 'key' not in params and _DEFAULTS['API_KEY'] is not None:
        params['key'] = _DEFAULTS['API_KEY']
    if 'raise_api_errors' in params:
        raise_api_errors = params['raise_api_errors'] is True
        del params['raise_api_errors']
    if 'options' in params:
        del params['options']

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        result = parse_xml(
            response.text,
            dict_constructor=dict,
            postprocessor=postprocessor
        )

        if raise_api_errors and 'error' in result:
            error = result['error']
            raise KRDictException(error['message'], error['error_code'], params)

        result['request_params'] = params
        if 'data' in result and 'results' not in result['data']:
            result['data']['results'] = []

        return result
    except requests.exceptions.RequestException as exc:
        raise exc


def advanced_search(**kwargs):
    """
    Performs an advanced search on the Korean Learner's Dict API.
    """

    kwargs['advanced'] = 'y'
    transform_search_params(kwargs)

    options = kwargs.get('options', {})
    use_scraper = (kwargs.get('part', 'word') == 'word'
        and options.get('use_scraper', _DEFAULTS['USE_SCRAPER'])
        and options.get('fetch_page_data', _DEFAULTS['FETCH_PAGE_DATA']))

    if use_scraper:
        response = _send_request(_SEARCH_URL, kwargs)

        if 'error' in response:
            return response

        raise_errors = options.get('raise_scraper_errors', _DEFAULTS['RAISE_SCRAPER_ERRORS'])
        return extend_advanced_search(response, raise_errors)

    return _send_request(_SEARCH_URL, kwargs)

def search(**kwargs):
    """
    Performs a search on the Korean Learner's Dict API.
    """

    transform_search_params(kwargs)


    options = kwargs.get('options', {})
    use_scraper = (kwargs.get('part', 'word') == 'word'
        and options.get('use_scraper', _DEFAULTS['USE_SCRAPER'])
        and options.get('fetch_page_data', _DEFAULTS['FETCH_PAGE_DATA']))

    if use_scraper:
        response = _send_request(_SEARCH_URL, kwargs)

        if 'error' in response:
            return response

        raise_errors = options.get('raise_scraper_errors', _DEFAULTS['RAISE_SCRAPER_ERRORS'])
        return extend_search(response, raise_errors)

    return _send_request(_SEARCH_URL, kwargs)

def search_definitions(**kwargs):
    """
    Performs a definition search on the Korean Learner's Dict API.
    """

    transform_search_params(kwargs)
    kwargs['part'] = 'dfn'
    return _send_request(_SEARCH_URL, kwargs)

def search_examples(**kwargs):
    """
    Performs an example search on the Korean Learner's Dict API.
    """

    transform_search_params(kwargs)
    kwargs['part'] = 'exam'
    return _send_request(_SEARCH_URL, kwargs)

def search_idioms_proverbs(**kwargs):
    """
    Performs a search for idioms and proverbs on the Korean Learner's Dict API.
    """

    transform_search_params(kwargs)
    kwargs['part'] = 'ip'
    return _send_request(_SEARCH_URL, kwargs)

def search_words(**kwargs):
    """
    Performs a search for words on the Korean Learner's Dict API.
    """

    transform_search_params(kwargs)
    if 'part' in kwargs:
        del kwargs['part']

    options = kwargs.get('options', {})
    use_scraper = (options.get('use_scraper', _DEFAULTS['USE_SCRAPER'])
        and options.get('fetch_page_data', _DEFAULTS['FETCH_PAGE_DATA']))

    if use_scraper:
        response = _send_request(_SEARCH_URL, kwargs)

        if 'error' in response:
            return response

        raise_errors = options.get('raise_scraper_errors', _DEFAULTS['RAISE_SCRAPER_ERRORS'])
        return extend_search(response, raise_errors)

    return _send_request(_SEARCH_URL, kwargs)

def set_default(name, value):
    """
    Sets the default value of the given option.
    """

    name = name.upper()

    if name == 'API_KEY' or name not in _DEFAULTS:
        return

    _DEFAULTS[name] = value is True

def set_key(key):
    """
    Sets the API key to use when a key is not specified in a request.

    Args:
        key: The API key to use, or None to unset the key.
    """

    _DEFAULTS['API_KEY'] = key

def view(**kwargs):
    """
    Performs a view query on the Korean Learner's Dict API.
    """

    transform_view_params(kwargs)

    options = kwargs.get('options', {})
    if options.get('use_scraper', _DEFAULTS['USE_SCRAPER']) is True:
        response = _send_request(_VIEW_URL, kwargs)

        if 'error' in response:
            return response

        fetch_page = options.get('fetch_page_data', _DEFAULTS['FETCH_PAGE_DATA'])
        fetch_media = options.get('fetch_multimedia', _DEFAULTS['FETCH_MULTIMEDIA'])
        raise_errors = options.get('raise_scraper_errors', _DEFAULTS['RAISE_SCRAPER_ERRORS'])
        return extend_view(response, fetch_page, fetch_media, raise_errors)

    return _send_request(_VIEW_URL, kwargs)
