"""
Provides functions that query the Korean Learners' Dictionary API.
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
    ``raise_api_errors`` parameter is True.

    - ``message``: The error message associated with the error.
    - ``error_code``: The error code returned by the API.
    - ``request_params``: A dict containing the transformed parameters
    that were sent to the API.

    """

    def __init__(self, message, error_code, params):
        super().__init__(message)

        self.message = message
        self.error_code = error_code
        self.request_params = params

    def __reduce__(self):
        return (KRDictException, (self.message, self.error_code, self.request_params))


def _send_request(url, params, search_type):
    raise_api_errors = False
    guarantee = False
    if 'key' not in params and _DEFAULTS['API_KEY'] is not None:
        params['key'] = _DEFAULTS['API_KEY']
    if 'raise_api_errors' in params:
        raise_api_errors = params['raise_api_errors'] is True
        del params['raise_api_errors']
    if 'guarantee_keys' in params:
        guarantee = params['guarantee_keys'] is True
        del params['guarantee_keys']
    if 'options' in params:
        del params['options']

    try:
        response = requests.get(url, params=params)
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

        return result
    except requests.exceptions.RequestException as exc:
        raise exc


def advanced_search(**kwargs):
    """
    Performs an advanced search on the Korean Learners' Dictionary API.
    Returns a dict with contents dependent on the value of the ``search_type``
    parameter and whether an error occurred.

    See the [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/)
    for details about return types.

    - ``query``: The search query.
    - ``raise_api_errors``: Sets whether a ``KRDictException`` will be raised if an API error
    occurs. A value of ``True`` guarantees that the result is not an error object.
    - ``guarantee_keys``: Sets whether keys that are missing from the response should be inserted
    with default values. A value of ``True`` guarantees that every key that is not required
    is included, including keys set by the scraper. Default values:
        - The empty string `""` for string values.
        - Zero `0` for integer values.
        - An empty list `[]` for list values.
    - ``key``: The API key. If a key was set with ``set_key``, this can be omitted.
    - ``page``: The page at which the search should start ``[1, 1000]``.
    - ``per_page``: The maximum number of search results to return ``[10, 100]``.
    - ``sort``: The sort method that should be used ``'alphabetical' | 'dict'``.
    - ``search_type``: The type of search to perform
    ``'word' | 'idiom_proverb' | 'definition' | 'example'``.
        - Note: Values other than ``'word'`` are unsupported and not recommended for use.
    - ``translation_language``: A language or list of languages to include translations for.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#translationlanguage).
    - ``search_target``: The target field of the search query.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#searchtarget).
    - ``target_language``: The original language to search by. If ``search_target``
    is set to any value other than ``'original_language'``, this parameter has no effect.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#targetlanguage).
    - ``search_method``: The method used to match against the query.
    ``'exact' |'include' |'start' |'end'``
    - ``classification``: An entry classification to filter by.
    ``'all' | 'word' | 'phrase' | 'expression'``
    - ``origin_type``: A word origin type to filter by.
    ``'all' | 'native' | 'hanja' | 'loanword' | 'hybrid'``
    - ``vocabulary_grade``: A vocabulary level to filter by.
    ``'all' | 'beginner' | 'intermediate' | 'advanced'``
    - ``part_of_speech``: A part of speech to filter by.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#partofspeech).
    - ``multimedia_info``: A multimedia type to filter by.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#multimediatype).
    - ``min_syllables``: The minimum number of syllables in result words ``[1, 80]``.
    - ``max_syllables``: The maximum number of syllables in results words. A value of ``0`` denotes
    no maximum ``[0, 80]``.
    - ``meaning_category``: The meaning category to filter by.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#meaningcategory).
    - ``subject_category``: A subject category to filter by.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#subjectcategory).
    - ``options``: Additional options to apply.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#optionsdict).

    """

    kwargs['advanced'] = 'y'
    search_type = kwargs.get('search_type', 'word')
    transform_search_params(kwargs)

    options = kwargs.get('options', {})
    use_scraper = (kwargs.get('part', 'word') == 'word'
        and options.get('use_scraper', _DEFAULTS['USE_SCRAPER'])
        and options.get('fetch_page_data', _DEFAULTS['FETCH_PAGE_DATA']))

    if use_scraper:
        response = _send_request(_SEARCH_URL, kwargs, search_type)

        if 'error' in response:
            return response

        raise_errors = options.get('raise_scraper_errors', _DEFAULTS['RAISE_SCRAPER_ERRORS'])
        return extend_advanced_search(response, raise_errors)

    return _send_request(_SEARCH_URL, kwargs, search_type)

def search(**kwargs):
    """
    Performs a search on the Korean Learners' Dictionary API.
    Returns a dict with contents dependent on the value of the ``search_type``
    parameter and whether an error occurred.

    See the [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/)
    for details about return types.

    - ``query``: The search query.
    - ``raise_api_errors``: Sets whether a ``KRDictException`` will be raised if an API error
    occurs. A value of ``True`` guarantees that the result is not an error object.
    - ``guarantee_keys``: Sets whether keys that are missing from the response should be inserted
    with default values. A value of ``True`` guarantees that every key that is not required
    is included, including keys set by the scraper. Default values:
        - The empty string `""` for string values.
        - Zero `0` for integer values.
        - An empty list `[]` for list values.
    - ``key``: The API key. If a key was set with ``set_key``, this can be omitted.
    - ``page``: The page at which the search should start ``[1, 1000]``.
    - ``per_page``: The maximum number of search results to return ``[10, 100]``.
    - ``sort``: The sort method that should be used ``'alphabetical' | 'dict'``.
    - ``search_type``: The type of search to perform
    ``'word' | 'idiom_proverb' | 'definition' | 'example'``.
    - ``translation_language``: A language or list of languages to include translations for.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#translationlanguage).
    - ``options``: Additional options to apply.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#optionsdict).

    """

    search_type = kwargs.get('search_type', 'word')
    transform_search_params(kwargs)

    options = kwargs.get('options', {})
    use_scraper = (kwargs.get('part', 'word') == 'word'
        and options.get('use_scraper', _DEFAULTS['USE_SCRAPER'])
        and options.get('fetch_page_data', _DEFAULTS['FETCH_PAGE_DATA']))

    if use_scraper:
        response = _send_request(_SEARCH_URL, kwargs, search_type)

        if 'error' in response:
            return response

        raise_errors = options.get('raise_scraper_errors', _DEFAULTS['RAISE_SCRAPER_ERRORS'])
        return extend_search(response, raise_errors)

    return _send_request(_SEARCH_URL, kwargs, search_type)

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

def view(**kwargs):
    """
    Performs a view query on the Korean Learners' Dictionary API.
    Returns either a dict with information about a dictionary entry, or an error object
    if an error occurred.

    See the [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/)
    for details about return types.

    - ``query``: The search query.
    - ``homograph_num``: The superscript number used to distinguish homographs.
    - ``target_code``: The target code of the desired result.
    - ``raise_api_errors``: Sets whether a KRDictException will be raised if an API error occurs.
    A value of ``True`` guarantees that the result is not an error object.
    - ``guarantee_keys``: Sets whether keys that are missing from the response should be inserted
    with default values. A value of ``True`` guarantees that every key that is not required
    is included, including keys set by the scraper. Default values:
        - The empty string `""` for string values.
        - Zero `0` for integer values.
        - An empty list `[]` for list values.
    - ``key``: The API key. If a key was set with set_key, this can be omitted.
    - ``translation_language``: A language or list of languages to include translations for.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#translationlanguage).
    - ``options``: Additional options to apply.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#optionsdict).

    """

    transform_view_params(kwargs)

    options = kwargs.get('options', {})
    if options.get('use_scraper', _DEFAULTS['USE_SCRAPER']) is True:
        response = _send_request(_VIEW_URL, kwargs, 'view')

        if 'error' in response:
            return response

        fetch_page = options.get('fetch_page_data', _DEFAULTS['FETCH_PAGE_DATA'])
        fetch_media = options.get('fetch_multimedia', _DEFAULTS['FETCH_MULTIMEDIA'])
        raise_errors = options.get('raise_scraper_errors', _DEFAULTS['RAISE_SCRAPER_ERRORS'])
        return extend_view(response, fetch_page, fetch_media, raise_errors)

    return _send_request(_VIEW_URL, kwargs, 'view')


__all__ = [
    'advanced_search',
    'search',
    'set_default',
    'set_key',
    'view',
    'KRDictException'
]
