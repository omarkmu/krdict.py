"""
Handles making requests to the dictionary website.
"""

import requests
from lxml import html

_ADVANCED_SEARCH_URL = (
    'https://krdict.korean.go.kr/dicSearchDetail/searchDetailWordsResult?'
    'searchFlag=Y&searchOp=AND&syllablePosition='
)
_SEARCH_URL = (
    'https://krdict.korean.go.kr/dicSearch/search?'
    'mainSearchWord={}&currentPage={}&blockCount={}&sort={}')
_VIDEO_URL = (
    'https://krdict.korean.go.kr/dicSearch/viewMovieConfirm?'
    'searchKindValue=video&ParaWordNo={}&ParaSenseSeq={}&multiMediaSeq={}'
)

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

def _build_video_url(target_code, dfn_idx, media_idx):
    return _VIDEO_URL.format(target_code, dfn_idx + 1, media_idx + 1)


def map_advanced_param(param, value):
    """
    Maps an advanced parameter value to
    the value expected on the krdict website.
    """

    return _get_advanced_param(_ADVANCED_PARAM_MAP[param], str(value), True)

def send_request(url, raise_errors):
    """
    Sends a request to a URL and parses the response with lxml.
    """

    try:
        response = requests.get(url, headers={'Accept-Language': '*'})
        response.raise_for_status()
        doc = html.fromstring(response.text)

        return doc
    except requests.exceptions.RequestException:
        if raise_errors:
            raise

        return None

def send_extend_request(request_type, response, raise_errors):
    """
    Sends a request from an existing response and parses the response with lxml.
    """

    if len(response['data']['results']) == 0:
        return None, None, request_type, response

    url = None
    if request_type == 'advanced':
        url = _build_advanced_search_url(response['request_params'])
    elif request_type == 'search':
        url = _build_search_url(response['request_params'])
    elif request_type == 'view':
        url = response['data']['url']

    return send_request(url, raise_errors), url, request_type, response

def send_image_request(multimedia, raise_errors):
    """
    Sends a request for image multimedia information and parses the response with lxml.
    """

    if 'url' not in multimedia:
        return None

    return send_request(multimedia['url'], raise_errors)

def send_video_request(target_code, dfn_idx, media_idx, raise_errors):
    """
    Sends a request for video multimedia information and parses the response with lxml.
    """

    return send_request(_build_video_url(target_code, dfn_idx + 1, media_idx + 1), raise_errors)
