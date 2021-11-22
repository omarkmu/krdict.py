"""
Transforms input parameters into API-compliant dicts.
"""

from enum import Enum

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
        'value': {
            '전체': 0,
            '인간 > 전체': 1,
            '인간 > 사람의 종류': 2,
            '인간 > 신체 부위': 3,
            '인간 > 체력 상태': 4,
            '인간 > 생리 현상': 5,
            '인간 > 감각': 6,
            '인간 > 감정': 7,
            '인간 > 성격': 8,
            '인간 > 태도': 9,
            '인간 > 용모': 10,
            '인간 > 능력': 11,
            '인간 > 신체 변화': 12,
            '인간 > 신체 행위': 13,
            '인간 > 신체에 가하는 행위': 14,
            '인간 > 인지 행위': 15,
            '인간 > 소리': 16,
            '인간 > 신체 내부 구성': 17,
            '삶 > 전체': 18,
            '삶 > 삶의 상태': 19,
            '삶 > 삶의 행위': 20,
            '삶 > 일상 행위': 21,
            '삶 > 친족 관계': 22,
            '삶 > 가족 행사': 23,
            '삶 > 여가 도구': 24,
            '삶 > 여가 시설': 25,
            '삶 > 여가 활동': 26,
            '삶 > 병과 증상': 27,
            '삶 > 치료 행위': 28,
            '삶 > 치료 시설': 29,
            '삶 > 약품류': 30,
            '식생활 > 전체': 31,
            '식생활 > 음식': 32,
            '식생활 > 채소': 33,
            '식생활 > 곡류': 34,
            '식생활 > 과일': 35,
            '식생활 > 음료': 36,
            '식생활 > 식재료': 37,
            '식생활 > 조리 도구': 38,
            '식생활 > 식생활 관련 장소': 39,
            '식생활 > 맛': 40,
            '식생활 > 식사 및 조리 행위': 41,
            '의생활 > 전체': 42,
            '의생활 > 옷 종류': 43,
            '의생활 > 옷감': 44,
            '의생활 > 옷의 부분': 45,
            '의생활 > 모자, 신발, 장신구': 46,
            '의생활 > 의생활 관련 장소': 47,
            '의생활 > 의복 착용 상태': 48,
            '의생활 > 의복 착용 행위': 49,
            '의생활 > 미용 행위': 50,
            '주생활 > 전체': 51,
            '주생활 > 건물 종류': 52,
            '주생활 > 주거 형태': 53,
            '주생활 > 주거 지역': 54,
            '주생활 > 생활 용품': 55,
            '주생활 > 주택 구성': 56,
            '주생활 > 주거 상태': 57,
            '주생활 > 주거 행위': 58,
            '주생활 > 가사 행위': 59,
            '사회 생활 > 전체': 60,
            '사회 생활 > 인간관계': 61,
            '사회 생활 > 소통 수단': 62,
            '사회 생활 > 교통 수단': 63,
            '사회 생활 > 교통 이용 장소': 64,
            '사회 생활 > 매체': 65,
            '사회 생활 > 직장': 66,
            '사회 생활 > 직위': 67,
            '사회 생활 > 직업': 68,
            '사회 생활 > 사회 행사': 69,
            '사회 생활 > 사회 생활 상태': 70,
            '사회 생활 > 사회 활동': 71,
            '사회 생활 > 교통 이용 행위': 72,
            '사회 생활 > 직장 생활': 73,
            '사회 생활 > 언어 행위': 74,
            '사회 생활 > 통신 행위': 75,
            '사회 생활 > 말': 76,
            '경제 생활 > 전체': 77,
            '경제 생활 > 경제 행위 주체': 78,
            '경제 생활 > 경제 행위 장소': 79,
            '경제 생활 > 경제 수단': 80,
            '경제 생활 > 경제 산물': 81,
            '경제 생활 > 경제 상태': 82,
            '경제 생활 > 경제 행위': 83,
            '교육 > 전체': 84,
            '교육 > 교수 학습 주체': 85,
            '교육 > 전공과 교과목': 86,
            '교육 > 교육 기관': 87,
            '교육 > 학교 시설': 88,
            '교육 > 학습 관련 사물': 89,
            '교육 > 학문 용어': 90,
            '교육 > 교수 학습 행위': 91,
            '교육 > 학문 행위': 92,
            '종교 > 전체': 93,
            '종교 > 종교 유형': 94,
            '종교 > 종교 활동 장소': 95,
            '종교 > 종교인': 96,
            '종교 > 종교어': 97,
            '종교 > 신앙 대상': 98,
            '종교 > 종교 활동 도구': 99,
            '종교 > 종교 행위': 100,
            '문화 > 전체': 101,
            '문화 > 문화 활동 주체': 102,
            '문화 > 음악': 103,
            '문화 > 미술': 104,
            '문화 > 문학': 105,
            '문화 > 예술': 106,
            '문화 > 대중 문화': 107,
            '문화 > 전통 문화': 108,
            '문화 > 문화 생활 장소': 109,
            '문화 > 문화 활동': 110,
            '정치와 행정 > 전체': 111,
            '정치와 행정 > 공공 기관': 112,
            '정치와 행정 > 사법 및 치안 주체': 113,
            '정치와 행정 > 무기': 114,
            '정치와 행정 > 정치 및 치안 상태': 115,
            '정치와 행정 > 정치 및 행정 행위': 116,
            '정치와 행정 > 사법 및 치안 행위': 117,
            '정치와 행정 > 정치 및 행정 주체': 118,
            '자연 > 전체': 119,
            '자연 > 지형': 120,
            '자연 > 지표면 사물': 121,
            '자연 > 천체': 122,
            '자연 > 자원': 123,
            '자연 > 재해': 124,
            '자연 > 기상 및 기후': 125,
            '동식물 > 전체': 126,
            '동식물 > 동물류': 127,
            '동식물 > 곤충류': 128,
            '동식물 > 식물류': 129,
            '동식물 > 동물의 부분': 130,
            '동식물 > 식물의 부분': 131,
            '동식물 > 동식물 행위': 132,
            '동식물 > 동물 소리': 133,
            '개념 > 전체': 134,
            '개념 > 모양': 135,
            '개념 > 성질': 136,
            '개념 > 속도': 137,
            '개념 > 밝기': 138,
            '개념 > 온도': 139,
            '개념 > 색깔': 140,
            '개념 > 수': 141,
            '개념 > 세는 말': 142,
            '개념 > 양': 143,
            '개념 > 정도': 144,
            '개념 > 순서': 145,
            '개념 > 빈도': 146,
            '개념 > 시간': 147,
            '개념 > 위치 및 방향': 148,
            '개념 > 지역': 149,
            '개념 > 지시': 150,
            '개념 > 접속': 151,
            '개념 > 의문': 152,
            '개념 > 인칭': 153,
            'all': 0,
            'human > all': 1,
            'human > types of people': 2,
            'human > body parts': 3,
            'human > health status': 4,
            'human > physiological phenomena': 5,
            'human > senses': 6,
            'human > emotion': 7,
            'human > personality': 8,
            'human > attitude': 9,
            'human > features': 10,
            'human > ability': 11,
            'human > physical changes': 12,
            'human > physical activities': 13,
            'human > actions done to the body': 14,
            'human > cognitive behavior': 15,
            'human > sound': 16,
            'human > inner parts of the body': 17,
            'life > all': 18,
            'life > state of being': 19,
            'life > life activities': 20,
            'life > daily activities': 21,
            'life > kinship': 22,
            'life > family events': 23,
            'life > leisure tools': 24,
            'life > leisure facilities': 25,
            'life > leisure activities': 26,
            'life > diseases and symptoms': 27,
            'life > medical activities': 28,
            'life > medical facilities': 29,
            'life > medicine': 30,
            'dietary > all': 31,
            'dietary > food types': 32,
            'dietary > vegetables': 33,
            'dietary > grain': 34,
            'dietary > fruit': 35,
            'dietary > beverages': 36,
            'dietary > food ingredients': 37,
            'dietary > cooking appliances': 38,
            'dietary > eating places': 39,
            'dietary > taste': 40,
            'dietary > eating and cooking activities': 41,
            'clothing habits > all': 42,
            'clothing habits > types of clothing': 43,
            'clothing habits > fabric': 44,
            'clothing habits > parts of clothing': 45,
            'clothing habits > hats, shoes, accessories': 46,
            'clothing habits > places related to clothing': 47,
            'clothing habits > places related to clothing habits': 47,
            'clothing habits > state of clothing': 48,
            'clothing habits > activities related to clothing': 49,
            'clothing habits > activities related to wearing clothing': 49,
            'clothing habits > beauty and health': 50,
            'home life > all': 51,
            'home life > building types': 52,
            'home life > type of housing': 53,
            'home life > residential area': 54,
            'home life > household items': 55,
            'home life > housing structure': 56,
            'home life > residential status': 57,
            'home life > residential activities': 58,
            'home life > housing activities': 58,
            'home life > residential chores': 59,
            'home life > household chores': 59,
            'social life > all': 60,
            'social life > human relationships': 61,
            'social life > means of communication': 62,
            'social life > modes of transportation': 63,
            'social life > places of transportation usage': 64,
            'social life > places for transportation usage': 64,
            'social life > media': 65,
            'social life > workplace': 66,
            'social life > work title/position': 67,
            'social life > titles and positions': 67,
            'social life > occupation': 68,
            'social life > social events': 69,
            'social life > social life status': 70,
            'social life > conditions of social life': 70,
            'social life > social activities': 71,
            'social life > transportation usage': 72,
            'social life > workplace life': 73,
            'social life > life in the workplace': 73,
            'social life > language activities': 74,
            'social life > linguistic activities': 74,
            'social life > communication activities': 75,
            'social life > all communication activities': 75,
            'social life > grammar and speech': 76,
            'economic activities > all': 77,
            'economic activities > people': 78,
            'economic activities > economic agents': 78,
            'economic activities > places': 79,
            'economic activities > economic places': 79,
            'economic activities > places of economic activity': 79,
            'economic activities > means': 80,
            'economic activities > economic means': 80,
            'economic activities > products': 81,
            'economic activities > commercial products': 81,
            'economic activities > status': 82,
            'economic activities > economic situation': 82,
            'economic activities > activities': 83,
            'economic activities > economic activities': 83,
            'education > all': 84,
            'education > people': 85,
            'education > education personnel & students': 85,
            'education > majors & subjects': 86,
            'education > educational institutions': 87,
            'education > school facilities': 88,
            'education > objects': 89,
            'education > objects related to education': 89,
            'education > academic terms': 90,
            'education > teaching and learning activities': 91,
            'education > academic activities': 92,
            'religion > all': 93,
            'religion > types of religion': 94,
            'religion > places': 95,
            'religion > places for religious activities': 95,
            'religion > people': 96,
            'religion > religious people': 96,
            'religion > religious words': 97,
            'religion > religious language': 97,
            'religion > major figures': 98,
            'religion > major figures of religions': 98,
            'religion > objects': 99,
            'religion > objects for religious activities': 99,
            'religion > practices': 100,
            'religion > religious practices': 100,
            'culture > all': 101,
            'culture > cultural activity participants': 102,
            'culture > participants in cultural activities': 102,
            'culture > music': 103,
            'culture > fine art': 104,
            'culture > fine and/or visual art': 104,
            'culture > literature': 105,
            'culture > art': 106,
            'culture > the arts': 106,
            'culture > pop culture': 107,
            'culture > traditional culture': 108,
            'culture > cultural activity places': 109,
            'culture > places of cultural activities': 109,
            'culture > cultural activities': 110,
            'politics and administration > all': 111,
            'politics and administration > public institutions': 112,
            'politics and administration > judicial & security personnel': 113,
            'politics and administration > judicial and security personnel': 113,
            'politics and administration > weapons': 114,
            'politics and administration > politics & security': 115,
            'politics and administration > politics and security': 115,
            'politics and administration > political acts': 116,
            'politics and administration > political and administrative activity': 116,
            'politics and administration > law & security': 117,
            'politics and administration > law and security acts': 117,
            'politics and administration > political and administrative personnel': 118,
            'politics and administration > all people involved in political activity': 118,
            'nature > all': 119,
            'nature > topography': 120,
            'nature > geographical topography': 120,
            'nature > surface objects': 121,
            'nature > geographical surface objects': 121,
            'nature > celestial bodies': 122,
            'nature > extraterrestrial bodies': 122,
            'nature > natural resources': 123,
            'nature > disasters': 124,
            'nature > weather and climate': 125,
            'animals and plants > all': 126,
            'animals and plants > animals': 127,
            'animals and plants > insects': 128,
            'animals and plants > plants': 129,
            'animals and plants > parts of animals': 130,
            'animals and plants > parts of plants': 131,
            'animals and plants > behaviors': 132,
            'animals and plants > actions and/or stages of animals and plants': 132,
            'animals and plants > sounds': 133,
            'animals and plants > animal sounds': 133,
            'concepts > all': 134,
            'concepts > shape': 135,
            'concepts > property': 136,
            'concepts > speed': 137,
            'concepts > brightness': 138,
            'concepts > temperature': 139,
            'concepts > colors': 140,
            'concepts > number': 141,
            'concepts > numbers': 141,
            'concepts > counters': 142,
            'concepts > counting words': 142,
            'concepts > amount': 143,
            'concepts > degree': 144,
            'concepts > order': 145,
            'concepts > frequency': 146,
            'concepts > time': 147,
            'concepts > location and direction': 148,
            'concepts > area': 149,
            'concepts > instructions': 150,
            'concepts > connection': 151,
            'concepts > question words': 152,
            'concepts > pronouns': 153,
            'concepts > person nouns and pronouns': 153,
        }
    },
    'subject_category': {
        'name': 'subject_cat',
        'value': {
            '전체': 0,
            '인사하기': 1,
            '소개하기 (자기소개)': 2,
            '소개하기 (가족소개)': 3,
            '개인 정보 교환하기 (초급)': 4,
            '위치 표현하기': 5,
            '길찾기': 6,
            '교통 이용하기 (초금)': 7,
            '물건 사기 (초금)': 8,
            '음식 주문하기': 9,
            '요리 설명하기 (초금)': 10,
            '시간 표현하기': 11,
            '날짜 표현하기': 12,
            '요일 표현하기': 13,
            '날씨와 계절 (초금)': 14,
            '하루 생활': 15,
            '학교생활 (초금)': 16,
            '한국 생활 (초금)': 17,
            '약속하기': 18,
            '전화하기': 19,
            '감사하기': 20,
            '사과하기': 21,
            '여행 (초금)': 22,
            '주말 및 휴가 (초금)': 23,
            '취미 (초금)': 24,
            '가족 행사 (초금)': 25,
            '건강 (초금)': 26,
            '병원 이용하기': 27,
            '약국 이용하기': 28,
            '약국 이용하기 (초금)': 28,
            '공공 기관 이용하기 (도서관)': 29,
            '공공 기관 이용하기 (우체국)': 30,
            '공공 기관 이용하기 (출입국 관리 사무소)': 31,
            '초대와 방문 (초금)': 32,
            '집 구하기 (초금)': 33,
            '집안일 (초금)': 34,
            '감정, 기분 표현하기 (초금)': 35,
            '성격 표현하기 (초금)': 36,
            '복장 표현하기 (초금)': 37,
            '외모 표현하기 (초금)': 38,
            '영화 보기': 39,
            '개인 정보 교환하기 (중급)': 40,
            '교통 이용하기 (중급)': 41,
            '지리 정보 (중급)': 42,
            '물건 사기 (중급)': 43,
            '음식 설명하기': 44,
            '요리 설명하기 (중급)': 45,
            '날씨와 계절 (중급)': 46,
            '학교생활 (중급)': 47,
            '한국 생활 (중급)': 48,
            '직업과 진로 (중급)': 49,
            '직장 생활 (중급)': 50,
            '여행 (중급)': 51,
            '주말 및 휴가 (중급)': 52,
            '취미 (중급)': 53,
            '가족 행사 (중급)': 54,
            '가족 행사 (명절)': 55,
            '건강 (중급)': 56,
            '공공기관 이용하기': 57,
            '초대와 방문 (중급)': 58,
            '집 구하기 (중급)': 59,
            '집안일 (중급)': 60,
            '감정, 기분 표현하기 (중급)': 61,
            '성격 표현하기 (중급)': 62,
            '복장 표현하기 (중급)': 63,
            '외모 표현하기 (중급)': 64,
            '공연과 감상': 65,
            '대중 매체': 66,
            '컴퓨터와 인터넷 (중급)': 67,
            '사건, 사고, 재해 기술하기': 68,
            '환경 문제 (중급)': 69,
            '문화 비교하기': 70,
            '인간관계 (중급)': 71,
            '한국의 문학': 72,
            '문제 해결하기 (분실 및 고장)': 73,
            '실수담 말하기': 74,
            '연애와 결혼': 75,
            '언어 (중급)': 76,
            '지리 정보 (고급)': 77,
            '경제∙경영': 78,
            '경제-경영': 78,
            '식문화': 79,
            '기후': 80,
            '교육': 81,
            '직업과 진로 (고급)': 82,
            '직장 생활 (고급)': 83,
            '여가 생활': 84,
            '보건과 의료': 85,
            '주거 생활': 86,
            '심리': 87,
            '외양': 88,
            '대중문화': 89,
            '컴퓨터와 인터넷 (고급)': 90,
            '사회 문제': 91,
            '환경 문제 (고급)': 92,
            '사회 제도': 93,
            '문화 차이': 94,
            '인간관계 (고급)': 95,
            '예술': 96,
            '건축': 97,
            '과학과 기술': 98,
            '법': 99,
            '스포츠': 100,
            '언론': 101,
            '언어 (고급)': 102,
            '역사': 103,
            '정치': 104,
            '종교': 105,
            '철학∙윤리': 106,
            '철학-윤리': 106,
            'all': 0,
            'greeting': 1,
            'introducing oneself': 2,
            'introducing (introducing oneself)': 2,
            'introducing family': 3,
            'introducing (introducing family)': 3,
            'exchanging personal information (elementary)': 4,
            'describing location': 5,
            'directions': 6,
            'using transportation (elementary)': 7,
            'purchasing goods (elementary)': 8,
            'ordering food': 9,
            'describing a dish (elementary)': 10,
            'describing dishes (elementary)': 10,
            'expressing time': 11,
            'expressing date': 12,
            'expressing day of the week': 13,
            'weather and season (elementary)': 14,
            'daily life': 15,
            'school life (elementary)': 16,
            'life in korea (elementary)': 17,
            'making promises': 18,
            'making a promise': 18,
            'making phone calls': 19,
            'making a phone call': 19,
            'expressing gratitude': 20,
            'apologizing': 21,
            'travel (elementary)': 22,
            'weekends and holidays (elementary)': 23,
            'hobby (elementary)': 24,
            'hobbies (elementary)': 24,
            'family events (elementary)': 25,
            'health (elementary)': 26,
            'using the hospital': 27,
            'using a pharmacy': 28,
            'using the pharmacy': 28,
            'using the library': 29,
            'using public institutions (library)': 29,
            'using the post office': 30,
            'using public institutions (post office)': 30,
            'using the immigration office': 31,
            'using public institutions (immigration office)': 31,
            'inviting and visiting (elementary)': 32,
            'finding a house (elementary)': 33,
            'housework (elementary)': 34,
            'expressing emotions (elementary)': 35,
            'expressing emotion/feelings (elementary)': 35,
            'describing personality (elementary)': 36,
            'describing clothes (elementary)': 37,
            'describing physical features (elementary)': 38,
            'watching movies': 39,
            'watching a movie': 39,
            'exchanging personal information (intermediate)': 40,
            'using transportation (intermediate)': 41,
            'geological information (intermediate)': 42,
            'purchasing goods (intermediate)': 43,
            'describing food': 44,
            'describing a dish (intermediate)': 45,
            'describing dishes (intermediate)': 45,
            'weather and season (intermediate)': 46,
            'school life (intermediate)': 47,
            'life in korea (intermediate)': 48,
            'jobs and careers (intermediate)': 49,
            'occupation & future path (intermediate)': 49,
            'workplace life (intermediate)': 50,
            'life in the workplace (intermediate)': 50,
            'travel (intermediate)': 51,
            'weekends and holidays (intermediate)': 52,
            'hobby (intermediate)': 53,
            'hobbies (intermediate)': 53,
            'family events (intermediate)': 54,
            'family events during holidays': 55,
            'family events (during national holidays)': 55,
            'health (intermediate)': 56,
            'using public institutions': 57,
            'using public institutions (library, post office, etc.)': 57,
            'inviting and visiting (intermediate)': 58,
            'finding a house (intermediate)': 59,
            'housework (intermediate)': 60,
            'expressing emotions (intermediate)': 61,
            'expressing emotion/feelings (intermediate)': 61,
            'describing personality (intermediate)': 62,
            'describing clothes (intermediate)': 63,
            'describing physical features (intermediate)': 64,
            'performance & appreciation': 65,
            'performances and appreciation': 65,
            'mass media': 66,
            'computer & internet (intermediate)': 67,
            'computers and the internet (intermediate)': 67,
            'describing events and disasters': 68,
            'describing events, accidents, disasters': 68,
            'environmental issues (intermediate)': 69,
            'comapring cultures': 70,
            'human relationships (intermediate)': 71,
            'korean literature': 72,
            'solving problems': 73,
            'solving problems (loss or malfunction)': 73,
            'talking about mistakes': 74,
            'talking about one\'s mistakes': 74,
            'dating and marriage': 75,
            'dating and getting married': 75,
            'language (intermediate)': 76,
            'geological information (advanced)': 77,
            'economics and administration': 78,
            'economics and business administration': 78,
            'dietary culture': 79,
            'climate': 80,
            'education': 81,
            'jobs and careers (advanced)': 82,
            'occupation & future path (advanced)': 82,
            'workplace life (advanced)': 83,
            'life in the workplace (advanced)': 83,
            'hobby (advanced)': 84,
            'hobbies (advanced)': 84,
            'health and medical treatment': 85,
            'residential area': 86,
            'psychology': 87,
            'mentality': 87,
            'appearance': 88,
            'pop culture': 89,
            'computer & internet (advanced)': 90,
            'computers and the internet (advanced)': 90,
            'social issues': 91,
            'environmental issues (advanced)': 92,
            'social system': 93,
            'cultural differences': 94,
            'human relationships (advanced)': 95,
            'art': 96,
            'the arts': 96,
            'architecture': 97,
            'science & technology': 98,
            'science and technology': 98,
            'law': 99,
            'sports': 100,
            'press': 101,
            'language (advanced)': 102,
            'history': 103,
            'politics': 104,
            'religion': 105,
            'philosophy, ethics': 106,
            'philosophy and ethics': 106
        }
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
