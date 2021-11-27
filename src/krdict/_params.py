"""
Transforms input parameters into API-compliant dicts.
"""

from .types import (
    Classification,
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


def _map_value(mapper, value):
    if isinstance(value, list):
        return ','.join(map(lambda x: _map_value(mapper, x), value))

    if 'type' in mapper:
        return str(mapper['type'].get_value(value, value))

    return str(value)

def transform_search_params(params: dict) -> None:
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

def transform_view_params(params: dict) -> None:
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
