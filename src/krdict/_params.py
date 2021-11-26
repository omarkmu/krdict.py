"""
Transforms input parameters into API-compliant dicts.
"""

from enum import Enum
from .types.meaning_category import _MEANING_CATEGORY_STRINGS
from .types.subject_category import _SUBJECT_CATEGORY_STRINGS

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
        'value': {
            'alphabetical': 'dict'
        }
    },
    'search_type': {
        'name': 'part',
        'value': {
            'idiom_proverb': 'ip',
            'definition': 'dfn',
            'example': 'exam'
        }
    },
    'translation_language': {
        'name': 'trans_lang',
        'value': {
            'all': 0,
            'english': 1,
            'japanese': 2,
            'french': 3,
            'spanish': 4,
            'arabic': 5,
            'mongolian': 6,
            'vietnamese': 7,
            'thai': 8,
            'indonesian': 9,
            'russian': 10
        }
    },
    'search_target': {
        'name': 'target',
        'value': {
            'headword': 1,
            'definition': 2,
            'example': 3,
            'original_language': 4,
            'pronunciation': 5,
            'application': 6,
            'application_shorthand': 7,
            'idiom': 8,
            'proverb': 9,
            'reference_info': 10
        }
    },
    'target_language': {
        'name': 'lang',
        'value': {
            'all': 0,
            'native_word': 1,
            'sino-korean': 2,
            'unknown': 3,
            'english': 4,
            'greek': 5,
            'dutch': 6,
            'norwegian': 7,
            'german': 8,
            'latin': 9,
            'russian': 10,
            'romanian': 11,
            'maori': 12,
            'malay': 13,
            'mongolian': 14,
            'basque': 15,
            'burmese': 16,
            'vietnamese': 17,
            'bulgarian': 18,
            'sanskrit': 19,
            'serbo-croatian': 20,
            'swahili': 21,
            'swedish': 22,
            'arabic': 23,
            'irish': 24,
            'spanish': 25,
            'uzbek': 26,
            'ukrainian': 27,
            'italian': 28,
            'indonesian': 29,
            'japanese': 30,
            'chinese': 31,
            'czech': 32,
            'cambodian': 33,
            'quechua': 34,
            'tagalog': 35,
            'thai': 36,
            'turkish': 37,
            'tibetan': 38,
            'persian': 39,
            'portuguese': 40,
            'polish': 41,
            'french': 42,
            'provencal': 43,
            'finnish': 44,
            'hungarian': 45,
            'hebrew': 46,
            'hindi': 47,
            'other': 48,
            'danish': 49
        }
    },
    'search_method': {
        'name': 'method'
    },
    'classification': {
        'name': 'type1'
    },
    'origin_type': {
        'name': 'type2'
    },
    'vocabulary_grade': {
        'name': 'level',
        'value': {
            'beginner': 'level1',
            'intermediate': 'level2',
            'advanced': 'level3'
        }
    },
    'part_of_speech': {
        'name': 'pos',
        'value': {
            'all': 0,
            'noun': 1,
            'pronoun': 2,
            'numeral': 3,
            'particle': 4,
            'verb': 5,
            'adjective': 6,
            'determiner': 7,
            'adverb': 8,
            'interjection': 9,
            'affix': 10,
            'bound noun': 11,
            'auxiliary verb': 12,
            'auxiliary adjective': 13,
            'ending': 14,
            'none': 15
        }
    },
    'multimedia_info': {
        'name': 'multimedia',
        'value': {
            'all': 0,
            'photo': 1,
            'illustration': 2,
            'video': 3,
            'animation': 4,
            'sound': 5,
            'none': 6
        }
    },
    'min_syllables': {
        'name': 'letter_s'
    },
    'max_syllables': {
        'name': 'letter_e'
    },
    'meaning_category': {
        'name': 'sense_cat',
        'value': _MEANING_CATEGORY_STRINGS
    },
    'subject_category': {
        'name': 'subject_cat',
        'value': _SUBJECT_CATEGORY_STRINGS
    },
    'target_code': {
        'name': 'q'
    }
}


def _get_map_value(mapper, value):
    if isinstance(value, list):
        return ','.join(map(lambda x: _get_map_value(mapper, x), value))
    if isinstance(value, Enum):
        value = value.value

    if 'value' in mapper and value in mapper['value']:
        return str(mapper['value'][value])

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
        new_value = _get_map_value(mapper, params[key])

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
