"""
Handles processing of search results, including key remapping,
type conversion, and restructuring.
"""

from collections import deque
from lxml import etree
from .types import KRDictException
from .scraper import extend_view, extend_search, extend_advanced_search


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
    'word_grade': 'vocabulary_level',
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

def _parse_xml(xml):
    result = {}
    root = etree.fromstring(xml.encode('utf-8'), None) # pylint: disable=c-extension-no-member

    stack = deque()
    stack.append((root, result))

    while len(stack) > 0:
        node, children = stack.pop()

        for child in node.iterchildren():
            key = _REMAPS.get(child.tag, child.tag)
            value = child.text and child.text.strip()

            # add the node to the stack if it has children
            if len(child):
                value = {}
                stack.append((child, value))
            elif not value:
                # skip empty elements with no children
                continue

            # convert expected lists to lists
            if key in _CONVERT_LIST and key not in children:
                children[key] = []

            # convert expected numbers to numbers
            if key in _CONVERT_NUM and isinstance(value, str):
                value = int(value)

            if isinstance(children.get(key), list):
                children[key].append(value)
            else:
                children[key] = value

    return {_REMAPS.get(root.tag, root.tag): result}

def _build_response(raw_response, request_params, search_type):
    # TODO: build class object
    raw_response['request_params'] = request_params
    raw_response['response_type'] = search_type if 'error' not in raw_response else 'error'

    return raw_response

def parse_response(kwargs, api_response, request_params, search_type):
    """
    Transforms an HTTP response to a response object.

    - ``kwargs``: The provided input keyword arguments.
    - ``api_response``: Whether or not this an advanced search.
    - ``request_params``: The request parameters which were sent to the API.
    - ``search_type``: The type of search which was performed.
    """

    raw_response = _parse_xml(api_response.text)

    if kwargs.get('raise_api_errors', False) and 'error' in raw_response:
        error = raw_response['error']
        raise KRDictException(error['message'], error['error_code'], request_params)

    if 'data' in raw_response and 'results' not in raw_response['data']:
        raw_response['data']['results'] = []

    response = _build_response(raw_response, request_params, search_type)
    return _postprocess(response, request_params, kwargs.get('options', {}), search_type)

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
