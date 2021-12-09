"""
Handles making requests to the dictionary website.
"""

import requests
from lxml import html
from ..types import (
    isiterable,
    SortMethod,
    MeaningCategory,
    SubjectCategory,
    ScraperTranslationLanguage
)

_ADVANCED_SEARCH_URL = (
    'https://krdict.korean.go.kr/dicSearchDetail/searchDetailWordsResult?'
    'searchFlag=Y&searchOp=AND&syllablePosition='
)
_BASE_URL = 'https://krdict.korean.go.kr{}/mainAction'
_CAT_MEANING_URL = (
    'https://krdict.korean.go.kr{}/dicSearchDetail/searchDetailSenseCategoryResult?'
    'searchFlag=Y{}&currentPage={}&blockCount={}&sort={}{}'
)
_CAT_SUBJECT_URL = (
    'https://krdict.korean.go.kr{}/dicSearchDetail/searchDetailActCategoryResult?'
    'searchFlag=Y{}&currentPage={}&blockCount={}&sort={}{}'
)
_SEARCH_URL = (
    'https://krdict.korean.go.kr/dicSearch/search?'
    'mainSearchWord={}&currentPage={}&blockCount={}&sort={}'
)
_VIDEO_URL = (
    'https://krdict.korean.go.kr/dicSearch/viewMovieConfirm?'
    'searchKindValue=video&ParaWordNo={}&ParaSenseSeq={}&multiMediaSeq={}'
)

_LANG_INFO = (
    ('eng', 6, '영어'),
    ('jpn', 7, '일본어'),
    ('fra', 8, '프랑스어'),
    ('spa', 9, '스페인어'),
    ('ara', 10, '아랍어'),
    ('mon', 1, '몽골어'),
    ('vie', 2, '베트남어'),
    ('tha', 3, '타이어'),
    ('ind', 4, '인도네시아어'),
    ('rus', 5, '러시아어'),
    ('chn', 11, '중국어')
)
_SENSE_CAT_MAX = [
    17,
    30,
    41,
    50,
    59,
    76,
    83,
    92,
    100,
    110,
    118,
    125,
    133,
    153
]

_ADVANCED_PARAM_MAP = {
    'q': {
        'name': 'query'
    },
    'start': {
        'name': 'currentPage'
    },
    'num': {
        'name': 'blockCount'
    },
    'sort': {
        'name': 'sort',
        'value': {
            'dict': 'W',
            'popular': 'C'
        }
    },
    'target': {
        'name': 'searchTarget',
        'default': '1',
        'value': {
            '1': 'word',
            '2': 'definition',
            '3': 'example',
            '4': 'org_language',
            '5': 'pronunciation',
            '6': 'conjugation',
            '7': 'shorten',
            '8': 'idiom',
            '9': 'proverb',
            '10': 'reference'
        }
    },
    'lang': {
        'name': 'searchOrglanguage',
        'default': '0',
        'value': {
            '0': 'all',
            '1': '0',
            '2': '32',
            '3': '97',
            '4': '17',
            '5': '1',
            '6': '2',
            '7': '3',
            '8': '4',
            '9': '5',
            '10': '6',
            '11': '7',
            '12': '99',
            '13': '8',
            '14': '9',
            '15': '99',
            '16': '99',
            '17': '10',
            '18': '11',
            '19': '12',
            '20': '13',
            '21': '99',
            '22': '14',
            '23': '15',
            '24': '99',
            '25': '16',
            '26': '99',
            '27': '99',
            '28': '16',
            '29': '17',
            '30': '18',
            '31': '19',
            '32': '20',
            '33': '99',
            '34': '99',
            '35': '99',
            '36': '21',
            '37': '22',
            '38': '99',
            '39': '23',
            '40': '24',
            '41': '25',
            '42': '26',
            '43': '99',
            '44': '99',
            '45': '27',
            '46': '28',
            '47': '29',
            '48': '99',
            '49': '99'
        }
    },
    'method': {
        'name': 'wordCondition',
        'default': 'exact',
        'value': {
            'exact': 'wordSame',
            'include': 'wordAll',
            'start': 'wordStart',
            'end': 'wordEnd'
        }
    },
    'type1': {
        'name': 'gubun',
        'default': 'all',
        'value': {
            'word': 'W',
            'phrase': 'P',
            'expression': 'E'
        }
    },
    'type2': {
        'name': 'wordNativeCode',
        'default': 'all',
        'value': {
            'native': '1',
            'chinese': '2',
            'loanword': '3',
            'hybrid': '0'
        }
    },
    'level': {
        'name': 'imcnt',
        'default': 'all',
        'value': {
            'level1': '1',
            'level2': '2',
            'level3': '3',
            '': '0'
        }
    },
    'pos': {
        'name': 'sp_code',
        'all_value': '0',
        'default': '0',
        'value': {
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9',
            '10': '10',
            '11': '11',
            '12': '12',
            '13': '13',
            '14': '14',
            '15': '27'
        }
    },
    'multimedia': {
        'name': 'multimedia',
        'all_value': '0',
        'default': '0',
        'value': {
            '1': 'P',
            '2': 'I',
            '3': 'V',
            '4': 'S',
            '5': 'A',
            '6': 'N'
        }
    },
    'letter_s': {
        'name': 'searchSyllableStart'
    },
    'letter_e': {
        'name': 'searchSyllableEnd',
        'value': {
            '0': '80'
        }
    },
    'sense_cat': {
        'convert': lambda tup: f'&senseCategoryTop={tup[0]}&senseCategoryMiddle={tup[1]}',
        'value': {
            '1': ('1', '1001'),
            '2': ('1', '1002'),
            '3': ('1', '1003'),
            '4': ('1', '1004'),
            '5': ('1', '1005'),
            '6': ('1', '1006'),
            '7': ('1', '1007'),
            '8': ('1', '1008'),
            '9': ('1', '1009'),
            '10': ('1', '1010'),
            '11': ('1', '1011'),
            '12': ('1', '1012'),
            '13': ('1', '1013'),
            '14': ('1', '1014'),
            '15': ('1', '1015'),
            '16': ('1', '1016'),
            '17': ('1', '1017'),
            '18': ('2', '1018'),
            '19': ('2', '1019'),
            '20': ('2', '1020'),
            '21': ('2', '1021'),
            '22': ('2', '1022'),
            '23': ('2', '1023'),
            '24': ('2', '1024'),
            '25': ('2', '1025'),
            '26': ('2', '1026'),
            '27': ('2', '1027'),
            '28': ('2', '1028'),
            '29': ('2', '1029'),
            '30': ('2', '1030'),
            '31': ('3', '1031'),
            '32': ('3', '1032'),
            '33': ('3', '1033'),
            '34': ('3', '1034'),
            '35': ('3', '1035'),
            '36': ('3', '1036'),
            '37': ('3', '1037'),
            '38': ('3', '1038'),
            '39': ('3', '1039'),
            '40': ('3', '1040'),
            '41': ('3', '1041'),
            '42': ('4', '1042'),
            '43': ('4', '1043'),
            '44': ('4', '1044'),
            '45': ('4', '1045'),
            '46': ('4', '1046'),
            '47': ('4', '1047'),
            '48': ('4', '1048'),
            '49': ('4', '1049'),
            '50': ('4', '1050'),
            '51': ('5', '1051'),
            '52': ('5', '1052'),
            '53': ('5', '1053'),
            '54': ('5', '1054'),
            '55': ('5', '1055'),
            '56': ('5', '1056'),
            '57': ('5', '1057'),
            '58': ('5', '1058'),
            '59': ('5', '1059'),
            '60': ('6', '1060'),
            '61': ('6', '1061'),
            '62': ('6', '1062'),
            '63': ('6', '1063'),
            '64': ('6', '1064'),
            '65': ('6', '1065'),
            '66': ('6', '1066'),
            '67': ('6', '1067'),
            '68': ('6', '1068'),
            '69': ('6', '1069'),
            '70': ('6', '1070'),
            '71': ('6', '1071'),
            '72': ('6', '1072'),
            '73': ('6', '1073'),
            '74': ('6', '1074'),
            '75': ('6', '1075'),
            '76': ('6', '1076'),
            '77': ('7', '1077'),
            '78': ('7', '1078'),
            '79': ('7', '1079'),
            '80': ('7', '1080'),
            '81': ('7', '1081'),
            '82': ('7', '1082'),
            '83': ('7', '1083'),
            '84': ('8', '1084'),
            '85': ('8', '1085'),
            '86': ('8', '1086'),
            '87': ('8', '1087'),
            '88': ('8', '1088'),
            '89': ('8', '1089'),
            '90': ('8', '1090'),
            '91': ('8', '1091'),
            '92': ('8', '1092'),
            '93': ('9', '1093'),
            '94': ('9', '1094'),
            '95': ('9', '1095'),
            '96': ('9', '1096'),
            '97': ('9', '1097'),
            '98': ('9', '1098'),
            '99': ('9', '1099'),
            '100': ('9', '1100'),
            '101': ('10', '1101'),
            '102': ('10', '1102'),
            '103': ('10', '1103'),
            '104': ('10', '1104'),
            '105': ('10', '1105'),
            '106': ('10', '1106'),
            '107': ('10', '1107'),
            '108': ('10', '1108'),
            '109': ('10', '1109'),
            '110': ('10', '1110'),
            '111': ('11', '1111'),
            '112': ('11', '1112'),
            '113': ('11', '1113'),
            '114': ('11', '1114'),
            '115': ('11', '1115'),
            '116': ('11', '1116'),
            '117': ('11', '1117'),
            '118': ('11', '1118'),
            '119': ('12', '1119'),
            '120': ('12', '1120'),
            '121': ('12', '1121'),
            '122': ('12', '1122'),
            '123': ('12', '1123'),
            '124': ('12', '1124'),
            '125': ('12', '1125'),
            '126': ('13', '1126'),
            '127': ('13', '1127'),
            '128': ('13', '1128'),
            '129': ('13', '1229'),
            '130': ('13', '1230'),
            '131': ('13', '1231'),
            '132': ('13', '1232'),
            '133': ('13', '1233'),
            '134': ('14', '1234'),
            '135': ('14', '1235'),
            '136': ('14', '1236'),
            '137': ('14', '1237'),
            '138': ('14', '1238'),
            '139': ('14', '1239'),
            '140': ('14', '1240'),
            '141': ('14', '1241'),
            '142': ('14', '1242'),
            '143': ('14', '1243'),
            '144': ('14', '1244'),
            '145': ('14', '1245'),
            '146': ('14', '1246'),
            '147': ('14', '1247'),
            '148': ('14', '1248'),
            '149': ('14', '1249'),
            '150': ('14', '1250'),
            '151': ('14', '1251'),
            '152': ('14', '1252'),
            '153': ('14', '1253')
        }
    },
    'subject_cat': {
        'name': 'actCategoryList',
        'all_value': '0',
        'value': {
            '1': '20001',
            '2': '20002',
            '3': '20003',
            '4': '20004',
            '5': '20005',
            '6': '20006',
            '7': '20007',
            '8': '20008',
            '9': '20009',
            '10': '20010',
            '11': '20011',
            '12': '20012',
            '13': '20013',
            '14': '20014',
            '15': '20015',
            '16': '20016',
            '17': '20017',
            '18': '20018',
            '19': '20019',
            '20': '20020',
            '21': '20021',
            '22': '20022',
            '23': '20023',
            '24': '20024',
            '25': '20025',
            '26': '20026',
            '27': '20027',
            '28': '20028',
            '29': '20029',
            '30': '20030',
            '31': '20031',
            '32': '20032',
            '33': '20033',
            '34': '20034',
            '35': '20035',
            '36': '20036',
            '37': '20037',
            '38': '20038',
            '39': '20039',
            '40': '30001',
            '41': '30002',
            '42': '30003',
            '43': '30004',
            '44': '30005',
            '45': '30006',
            '46': '30007',
            '47': '30008',
            '48': '30009',
            '49': '30010',
            '50': '30011',
            '51': '30012',
            '52': '30013',
            '53': '30014',
            '54': '30015',
            '55': '30016',
            '56': '30017',
            '57': '30018',
            '58': '30019',
            '59': '30020',
            '60': '30021',
            '61': '30022',
            '62': '30023',
            '63': '30024',
            '64': '30025',
            '65': '30026',
            '66': '30027',
            '67': '30028',
            '68': '30029',
            '69': '30030',
            '70': '30031',
            '71': '30032',
            '72': '30033',
            '73': '30034',
            '74': '30035',
            '75': '30036',
            '76': '30037',
            '77': '40001',
            '78': '40002',
            '79': '40003',
            '80': '40004',
            '81': '40005',
            '82': '40006',
            '83': '40007',
            '84': '40008',
            '85': '40009',
            '86': '40010',
            '87': '40011',
            '88': '40012',
            '89': '40013',
            '90': '40014',
            '91': '40015',
            '92': '40016',
            '93': '40017',
            '94': '40018',
            '95': '40019',
            '96': '40020',
            '97': '40021',
            '98': '40022',
            '99': '40023',
            '100': '40024',
            '101': '40025',
            '102': '40026',
            '103': '40027',
            '104': '40028',
            '105': '40029',
            '106': '40030'
        }
    }
}


def _get_advanced_param(adv_mapper, value, value_only=False):
    if adv_mapper.get('name') != 'query' and ',' in value:
        params = []

        for val in value.split(','):
            param = _get_advanced_param(adv_mapper, val)
            if val is None:
                continue

            params.append(param)

        return ''.join(params)

    if 'value' in adv_mapper:
        value = adv_mapper['value'].get(value, value)

    if 'convert' in adv_mapper and not value_only:
        return adv_mapper['convert'](value)

    return value if value_only else f'&{adv_mapper["name"]}={value}'

def _get_advanced_all_params(adv_mapper):
    if not 'all_params' in adv_mapper:
        all_query = []

        for value in adv_mapper['value'].values():
            all_query.append(f'&{adv_mapper["name"]}={value}')

        adv_mapper['all_params'] = ''.join(all_query)

    return adv_mapper['all_params']

def _get_language_info(lang):
    lang = ScraperTranslationLanguage.get_value(lang)

    if not lang or lang == 0:
        return (None, 0, None)

    return _LANG_INFO[lang - 1]


def _build_advanced_search_url(params):
    url = [_ADVANCED_SEARCH_URL]

    for adv_key, adv_mapper in _ADVANCED_PARAM_MAP.items():
        param_value = params.get(adv_key, adv_mapper.get('default'))

        if param_value is None:
            continue

        param_value = str(param_value)
        use_all = 'all_value' in adv_mapper or adv_mapper.get('default') == 'all'
        all_value = adv_mapper.get('all_value', 'all')

        if use_all and param_value == all_value:
            url.append(_get_advanced_all_params(adv_mapper))
            continue

        param = _get_advanced_param(adv_mapper, param_value)
        if param is not None:
            url.append(param)

    return ''.join(url)

def _build_search_url(params):
    return _SEARCH_URL.format(
        params.get('q'),
        params.get('start', 1),
        params.get('num', 10),
        'W' if params.get('sort') != 'popular' else 'C'
    )

def _build_sense_category_query(category):
    category = MeaningCategory.get_value(category, category)

    if category <= 0 or category > 153:
        return '&lgCategoryCode=0&miCategoryCode=-1'

    if category == 1:
        return '&lgCategoryCode=1&miCategoryCode=-1'

    code_large = 0
    code_mid = 1000 + category if category < 129 else 1100 + category

    for idx, cat_max in enumerate(_SENSE_CAT_MAX):
        if category == cat_max + 1:
            code_large = idx + 2
            code_mid = -1
            break

        if category <= cat_max:
            code_large = idx + 1
            break

    return f'&lgCategoryCode={code_large}&miCategoryCode={code_mid}'

def _build_subject_category_query(category):
    if not isiterable(category, exclude=(str,)):
        category = (category,)

    value = []

    for cat in category:
        cat_value = SubjectCategory.get_value(cat, cat)

        if cat_value == '0':
            value = []

            for i in range(1, 107):
                value.append(f'&actCategory={map_advanced_param("subject_cat", i)}')

            return ''.join(value)

        value.append(f'&actCategory={map_advanced_param("subject_cat", cat_value)}')

    return ''.join(value)


def _build_video_url(target_code, dfn_idx, media_idx):
    return _VIDEO_URL.format(target_code, dfn_idx + 1, media_idx + 1)


def map_advanced_param(param, value):
    """
    Maps an advanced parameter value to the value expected by the API.
    """

    return _get_advanced_param(_ADVANCED_PARAM_MAP[param], str(value), True)

def send_request(kwargs, response_type):
    """
    Sends a request to a URL and parses the response with lxml.
    """

    lang_info = _get_language_info(kwargs.get('translation_language'))
    page = int(kwargs.get('page', 1))
    per_page = int(kwargs.get('per_page', 10))

    nation, code, _ = lang_info

    url: str

    if response_type == 'word_of_the_day':
        url = _BASE_URL.format(f'/{nation}' if nation else '')

    elif response_type in ('meaning_category', 'subject_category'):
        is_meaning = response_type == 'meaning_category'
        query_builder = (
            _build_sense_category_query if is_meaning else _build_subject_category_query
        )

        url = (_CAT_MEANING_URL if is_meaning else _CAT_SUBJECT_URL).format(
            f'/{nation}' if nation else '',
            f'&nation={nation}&nationCode={code}' if nation else '',
            page,
            per_page,
            'C' if SortMethod.get_value(kwargs.get('sort')) == 'popular' else 'W',
            query_builder(kwargs.get('category', 0))
        )

    else:
        raise ValueError

    try:
        response = requests.get(url, headers={'Accept-Language': '*'})
        response.raise_for_status()
        return (html.fromstring(response.text), url, lang_info, page, per_page)
    except requests.exceptions.RequestException as exc:
        raise exc
