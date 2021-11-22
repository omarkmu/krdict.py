"""
Contains helper classes.
"""

# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods

from enum import Enum

_MEANING_CATEGORY_STRINGS = {
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
_SUBJECT_CATEGORY_STRINGS = {
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

class MeaningCategory(Enum):
    """Enumeration class that contains meaning category values."""
    ALL = 0
    HUMAN_ALL = 1
    HUMAN_TYPES_OF_PEOPLE = 2
    HUMAN_BODY_PARTS = 3
    HUMAN_HEALTH_STATUS = 4
    HUMAN_PHYSIOLOGICAL_PHENOMENA = 5
    HUMAN_SENSES = 6
    HUMAN_EMOTION = 7
    HUMAN_PERSONALITY = 8
    HUMAN_ATTITUDE = 9
    HUMAN_FEATURES = 10
    HUMAN_ABILITY = 11
    HUMAN_PHYSICAL_CHANGES = 12
    HUMAN_PHYSICAL_ACTIVITIES = 13
    HUMAN_ACTIONS_DONE_TO_THE_BODY = 14
    HUMAN_COGNITIVE_BEHAVIOR = 15
    HUMAN_SOUND = 16
    HUMAN_INNER_PARTS_OF_THE_BODY = 17
    LIFE_ALL = 18
    LIFE_STATE_OF_BEING = 19
    LIFE_LIFE_ACTIVIES = 20
    LIFE_DAILY_ACTIVITIES = 21
    LIFE_KINSHIP = 22
    LIFE_FAMILY_EVENTS = 23
    LIFE_LEISURE_TOOLS = 24
    LIFE_LEISURE_FACILITIES = 25
    LIFE_LEISURE_ACTIVITIES = 26
    LIFE_DISEASES_AND_SYMPTOMS = 27
    LIFE_MEDICAL_ACTIVITIES = 28
    LIFE_MEDICAL_FACILITIES = 29
    LIFE_MEDICINE = 30
    DIETARY_ALL = 31
    DIETARY_FOOD_TYPES = 32
    DIETARY_VEGETABLES = 33
    DIETARY_GRAIN = 34
    DIETARY_FRUIT = 35
    DIETARY_BEVERAGES = 36
    DIETARY_FOOD_INGREDIENTS = 37
    DIETARY_COOKING_APPLIANCES = 38
    DIETARY_EATING_PLACES = 39
    DIETARY_TASTE = 40
    DIETARY_EATING_AND_COOKING_ACTIVITIES = 41
    CLOTHING_ALL = 42
    CLOTHING_TYPES_OF_CLOTHING = 43
    CLOTHING_FABRIC = 44
    CLOTHING_PARTS_OF_CLOTHING = 45
    CLOTHING_HATS_SHOES_ACCESSORIES = 46
    CLOTHING_PLACES_RELATED_TO_CLOTHING = 47
    CLOTHING_STATE_OF_CLOTHING = 48
    CLOTHING_ACTIVITIES_RELATED_TO_CLOTHING = 49
    CLOTHING_BEAUTY_AND_HEALTH = 50
    HOME_LIFE_ALL = 51
    HOME_LIFE_BUILDING_TYPES = 52
    HOME_LIFE_TYPE_OF_HOUSING = 53
    HOME_LIFE_RESIDENTIAL_AREA = 54
    HOME_LIFE_HOUSEHOLD_ITEMS = 55
    HOME_LIFE_HOUSING_STRUCTURE = 56
    HOME_LIFE_RESIDENTIAL_STATUS = 57
    HOME_LIFE_RESIDENTIAL_ACTIVITIES = 58
    HOME_LIFE_RESIDENTIAL_CHORES = 59
    SOCIAL_LIFE_ALL = 60
    SOCIAL_LIFE_HUMAN_RELATIONSHIPS = 61
    SOCIAL_LIFE_MEANS_OF_COMMUNICATION = 62
    SOCIAL_LIFE_MODES_OF_TRANSPORTATION = 63
    SOCIAL_LIFE_PLACES_FOR_TRANSPORTATION_USAGE = 64
    SOCIAL_LIFE_MEDIA = 65
    SOCIAL_LIFE_WORKPLACE = 66
    SOCIAL_LIFE_TITLES_AND_POSITIONS = 67
    SOCIAL_LIFE_OCCUPATION = 68
    SOCIAL_LIFE_SOCIAL_EVENTS = 69
    SOCIAL_LIFE_SOCIAL_LIFE_STATUS = 70
    SOCIAL_LIFE_SOCIAL_ACTIVITIES = 71
    SOCIAL_LIFE_TRANSPORTATION_USAGE = 72
    SOCIAL_LIFE_WORKPLACE_LIFE = 73
    SOCIAL_LIFE_LANGUAGE_ACTIVITIES = 74
    SOCIAL_LIFE_COMMUNICATION_ACTIVITIES = 75
    SOCIAL_LIFE_GRAMMAR_AND_SPEECH = 76
    ECONOMIC_ALL = 77
    ECONOMIC_PEOPLE = 78
    ECONOMIC_PLACES = 79
    ECONOMIC_MEANS = 80
    ECONOMIC_PRODUCTS = 81
    ECONOMIC_STATUS = 82
    ECONOMIC_ACTIVITIES = 83
    EDUCATION_ALL = 84
    EDUCATION_PEOPLE = 85
    EDUCATION_MAJORS_AND_SUBJECTS = 86
    EDUCATION_EDUCATIONAL_INSTITUTIONS = 87
    EDUCATION_SCHOOL_FACILITIES = 88
    EDUCATION_OBJECTS = 89
    EDUCATION_ACADEMIC_TERMS = 90
    EDUCATION_TEACHING_AND_LEARNING_ACTIVITIES = 91
    EDUCATION_ACADEMIC_ACTIVITIES = 92
    RELIGION_ALL = 93
    RELIGION_TYPES_OF_RELIGION = 94
    RELIGION_PLACES = 95
    RELIGION_PEOPLE = 96
    RELIGION_RELIGIOUS_WORDS = 97
    RELIGION_MAJOR_FIGURES = 98
    RELIGION_OBJECTS = 99
    RELIGION_PRACTICES = 100
    CULTURE_ALL = 101
    CULTURE_CULTURAL_ACTIVITY_PARTICIPANTS = 102
    CULTURE_MUSIC = 103
    CULTURE_FINE_ART = 104
    CULTURE_LITERATURE = 105
    CULTURE_ART = 106
    CULTURE_POP_CULTURE = 107
    CULTURE_TRADITIONAL_CULTURE = 108
    CULTURE_CULTURAL_ACTIVITY_PLACES = 109
    CULTURE_CULTURAL_ACTIVITIES = 110
    POLITICS_AND_ADMINISTRATION_ALL = 111
    POLITICS_AND_ADMINISTRATION_PUBLIC_INSTITUTIONS = 112
    POLITICS_AND_ADMINISTRATION_JUDICIAL_AND_SECURITY_PERSONNEL = 113
    POLITICS_AND_ADMINISTRATION_WEAPONS = 114
    POLITICS_AND_ADMINISTRATION_POLITICS_AND_SECURITY = 115
    POLITICS_AND_ADMINISTRATION_POLITICAL_ACTS = 116
    POLITICS_AND_ADMINISTRATION_LAW_AND_SECURITY_ACTS = 117
    POLITICS_AND_ADMINISTRATION_POLITICAL_AND_ADMINISTRATIVE_PERSONNEL = 118
    NATURE_ALL = 119
    NATURE_TOPOGRAPHY = 120
    NATURE_SURFACE_OBJECTS = 121
    NATURE_CELESTIAL_BODIES = 122
    NATURE_NATURAL_RESOURCES = 123
    NATURE_DISASTERS = 124
    NATURE_WEATHER_AND_CLIMATE = 125
    ANIMALS_AND_PLANTS_ALL = 126
    ANIMALS_AND_PLANTS_ANIMALS = 127
    ANIMALS_AND_PLANTS_INSECTS = 128
    ANIMALS_AND_PLANTS_PLANTS = 129
    ANIMALS_AND_PLANTS_PARTS_OF_ANIMALS = 130
    ANIMALS_AND_PLANTS_PARTS_OF_PLANTS = 131
    ANIMALS_AND_PLANTS_BEHAVIORS = 132
    ANIMALS_AND_PLANTS_SOUNDS = 133
    CONCEPTS_ALL = 134
    CONCEPTS_SHAPE = 135
    CONCEPTS_PROPERTY = 136
    CONCEPTS_SPEED = 137
    CONCEPTS_BRIGHTNESS = 138
    CONCEPTS_TEMPERATURE = 139
    CONCEPTS_COLORS = 140
    CONCEPTS_NUMBERS = 141
    CONCEPTS_COUNTERS = 142
    CONCEPTS_AMOUNT = 143
    CONCEPTS_DEGREE = 144
    CONCEPTS_ORDER = 145
    CONCEPTS_FREQUENCY = 146
    CONCEPTS_TIME = 147
    CONCEPTS_LOCATION_AND_DIRECTION = 148
    CONCEPTS_AREA = 149
    CONCEPTS_INSTRUCTIONS = 150
    CONCEPTS_CONNECTION = 151
    CONCEPTS_QUESTION_WORDS = 152
    CONCEPTS_PRONOUNS = 153

class SubjectCategory(Enum):
    """Enumeration class that contains subject category values."""
    ALL = 0
    ELEMENTARY_GREETING = 1
    ELEMENTARY_INTRODUCING_ONESELF = 2
    ELEMENTARY_INTRODUCING_FAMILY = 3
    ELEMENTARY_EXCHANGING_PERSONAL_INFORMATION = 4
    ELEMENTARY_DESCRIBING_LOCATION = 5
    ELEMENTARY_DIRECTIONS = 6
    ELEMENTARY_USING_TRANSPORTATION = 7
    ELEMENTARY_PURCHASING_GOODS = 8
    ELEMENTARY_ORDERING_FOOD = 9
    ELEMENTARY_DESCRIBING_DISHES = 10
    ELEMENTARY_EXPRESSING_TIME = 11
    ELEMENTARY_EXPRESSING_DATE = 12
    ELEMENTARY_EXPRESSING_DAY_OF_THE_WEEK = 13
    ELEMENTARY_WEATHER_AND_SEASON = 14
    ELEMENTARY_DAILY_LIFE = 15
    ELEMENTARY_SCHOOL_LIFE = 16
    ELEMENTARY_LIFE_IN_KOREA = 17
    ELEMENTARY_MAKING_PROMISES = 18
    ELEMENTARY_MAKING_PHONE_CALLS = 19
    ELEMENTARY_EXPRESSING_GRATITUDE = 20
    ELEMENTARY_APOLOGIZING = 21
    ELEMENTARY_TRAVEL = 22
    ELEMENTARY_WEEKENDS_AND_HOLIDAYS = 23
    ELEMENTARY_HOBBIES = 24
    ELEMENTARY_FAMILY_EVENTS = 25
    ELEMENTARY_HEALTH = 26
    ELEMENTARY_USING_THE_HOSPITAL = 27
    ELEMENTARY_USING_THE_PHARMACY = 28
    ELEMENTARY_USING_THE_LIBRARY = 29
    ELEMENTARY_USING_THE_POST_OFFICE = 30
    ELEMENTARY_USING_THE_IMMIGRATION_OFFICE = 31
    ELEMENTARY_INVITING_AND_VISITING = 32
    ELEMENTARY_FINDING_A_HOUSE = 33
    ELEMENTARY_HOUSEWORK = 34
    ELEMENTARY_EXPRESSING_EMOTIONS = 35
    ELEMENTARY_DESCRIBING_PERSONALITY = 36
    ELEMENTARY_DESCRIBING_CLOTHES = 37
    ELEMENTARY_DESCRIBING_PHYSICAL_FEATURES = 38
    ELEMENTARY_WATCHING_MOVIES = 39
    INTERMEDIATE_EXCHANGING_PERSONAL_INFORMATION = 40
    INTERMEDIATE_USING_TRANSPORTATION = 41
    INTERMEDIATE_GEOLOGICAL_INFORMATION = 42
    INTERMEDIATE_PURCHASING_GOODS = 43
    INTERMEDIATE_DESCRIBING_FOOD = 44
    INTERMEDIATE_DESCRIBING_DISHES = 45
    INTERMEDIATE_WEATHER_AND_SEASON = 46
    INTERMEDIATE_SCHOOL_LIFE = 47
    INTERMEDIATE_LIFE_IN_KOREA = 48
    INTERMEDIATE_JOBS_AND_CAREERS = 49
    INTERMEDIATE_WORKPLACE_LIFE = 50
    INTERMEDIATE_TRAVEL = 51
    INTERMEDIATE_WEEKENDS_AND_HOLIDAYS = 52
    INTERMEDIATE_HOBBIES = 53
    INTERMEDIATE_FAMILY_EVENTS = 54
    INTERMEDIATE_FAMILY_EVENTS_DURING_HOLIDAYS = 55
    INTERMEDIATE_HEALTH = 56
    INTERMEDIATE_USING_PUBLIC_INSTITUTIONS = 57
    INTERMEDIATE_INVITING_AND_VISITING = 58
    INTERMEDIATE_FINDING_A_HOUSE = 59
    INTERMEDIATE_HOUSEWORK = 60
    INTERMEDIATE_EXPRESSING_EMOTIONS = 61
    INTERMEDIATE_DESCRIBING_PERSONALITY = 62
    INTERMEDIATE_DESCRIBING_CLOTHES = 63
    INTERMEDIATE_DESCRIBING_PHYSICAL_FEATURES = 64
    INTERMEDIATE_PERFORMANCES_AND_APPRECIATION = 65
    INTERMEDIATE_MASS_MEDIA = 66
    INTERMEDIATE_COMPUTERS_AND_THE_INTERNET = 67
    INTERMEDIATE_DESCRIBING_EVENTS_AND_DISASTERS = 68
    INTERMEDIATE_ENVIRONMENTAL_ISSUES = 69
    INTERMEDIATE_COMPARING_CULTURES = 70
    INTERMEDIATE_HUMAN_RELATIONSHIPS = 71
    INTERMEDIATE_KOREAN_LITERATURE = 72
    INTERMEDIATE_SOLVING_PROBLEMS = 73
    INTERMEDIATE_TALKING_ABOUT_MISTAKES = 74
    INTERMEDIATE_DATING_AND_MARRIAGE = 75
    INTERMEDIATE_LANGUAGE = 76
    ADVANCED_GEOLOGICAL_INFORMATION = 77
    ADVANCED_ECONOMICS_AND_ADMINISTRATION = 78
    ADVANCED_DIETARY_CULTURE = 79
    ADVANCED_CLIMATE = 80
    ADVANCED_EDUCATION = 81
    ADVANCED_JOBS_AND_CAREERS = 82
    ADVANCED_WORKPLACE_LIFE = 83
    ADVANCED_HOBBIES = 84
    ADVANCED_HEALTH_AND_MEDICAL_TREATMENT = 85
    ADVANCED_RESIDENTIAL_AREA = 86
    ADVANCED_PSYCHOLOGY = 87
    ADVANCED_APPEARANCE = 88
    ADVANCED_POP_CULTURE = 89
    ADVANCED_COMPUTERS_AND_THE_INTERNET = 90
    ADVANCED_SOCIAL_ISSUES = 91
    ADVANCED_ENVIRONMENTAL_ISSUES = 92
    ADVANCED_SOCIAL_SYSTEM = 93
    ADVANCED_CULTURAL_DIFFERENCES = 94
    ADVANCED_HUMAN_RELATIONSHIPS = 95
    ADVANCED_ART = 96
    ADVANCED_ARCHITECTURE = 97
    ADVANCED_SCIENCE_AND_TECHNOLOGY = 98
    ADVANCED_LAW = 99
    ADVANCED_SPORTS = 100
    ADVANCED_PRESS = 101
    ADVANCED_LANGUAGE = 102
    ADVANCED_HISTORY = 103
    ADVANCED_POLITICS = 104
    ADVANCED_RELIGION = 105
    ADVANCED_PHILOSOPHY_AND_ETHICS = 106


class MeaningCategoryHelper:
    """Helper class for meaning categories."""

    def __new__(cls, value):
        return MeaningCategory(value)

    @staticmethod
    def enum():
        """Returns the underlying enumeration type."""
        return MeaningCategory

    @staticmethod
    def from_literal(value):
        """
        Returns the meaning category associated with a string or integer,
        raising an error if the value is not associated with any meaning category.
        """

        if isinstance(value, str):
            value = _MEANING_CATEGORY_STRINGS.get(value, value)

        return MeaningCategory(value)

    @staticmethod
    def from_literal_safe(value):
        """
        Returns the meaning category associated with a string or integer,
        or None if the value is not associated with any meaning category.
        """

        if isinstance(value, str):
            numeric_value = _MEANING_CATEGORY_STRINGS.get(value)
            if numeric_value is None:
                return None

            value = numeric_value

        if not isinstance(value, int) or not 0 <= value <= 153:
            return None

        return MeaningCategory(value)

    ALL = MeaningCategory.ALL

    class HUMAN:
        """Helper class for human meaning categories."""
        ALL = MeaningCategory.HUMAN_ALL
        TYPES_OF_PEOPLE = MeaningCategory.HUMAN_TYPES_OF_PEOPLE
        BODY_PARTS = MeaningCategory.HUMAN_BODY_PARTS
        HEALTH_STATUS = MeaningCategory.HUMAN_HEALTH_STATUS
        PHYSIOLOGICAL_PHENOMENA = MeaningCategory.HUMAN_PHYSIOLOGICAL_PHENOMENA
        SENSES = MeaningCategory.HUMAN_SENSES
        EMOTION = MeaningCategory.HUMAN_EMOTION
        PERSONALITY = MeaningCategory.HUMAN_PERSONALITY
        ATTITUDE = MeaningCategory.HUMAN_ATTITUDE
        FEATURES = MeaningCategory.HUMAN_FEATURES
        ABILITY = MeaningCategory.HUMAN_ABILITY
        PHYSICAL_CHANGES = MeaningCategory.HUMAN_PHYSICAL_CHANGES
        PHYSICAL_ACTIVITIES = MeaningCategory.HUMAN_PHYSICAL_ACTIVITIES
        ACTIONS_DONE_TO_THE_BODY = MeaningCategory.HUMAN_ACTIONS_DONE_TO_THE_BODY
        COGNITIVE_BEHAVIOR = MeaningCategory.HUMAN_COGNITIVE_BEHAVIOR
        SOUND = MeaningCategory.HUMAN_SOUND
        INNER_PARTS_OF_THE_BODY = MeaningCategory.HUMAN_INNER_PARTS_OF_THE_BODY

    class LIFE:
        """Helper class for life meaning categories."""
        ALL = MeaningCategory.LIFE_ALL
        STATE_OF_BEING = MeaningCategory.LIFE_STATE_OF_BEING
        LIFE_ACTIVIES = MeaningCategory.LIFE_LIFE_ACTIVIES
        DAILY_ACTIVITIES = MeaningCategory.LIFE_DAILY_ACTIVITIES
        KINSHIP = MeaningCategory.LIFE_KINSHIP
        FAMILY_EVENTS = MeaningCategory.LIFE_FAMILY_EVENTS
        LEISURE_TOOLS = MeaningCategory.LIFE_LEISURE_TOOLS
        LEISURE_FACILITIES = MeaningCategory.LIFE_LEISURE_FACILITIES
        LEISURE_ACTIVITIES = MeaningCategory.LIFE_LEISURE_ACTIVITIES
        DISEASES_AND_SYMPTOMS = MeaningCategory.LIFE_DISEASES_AND_SYMPTOMS
        MEDICAL_ACTIVITIES = MeaningCategory.LIFE_MEDICAL_ACTIVITIES
        MEDICAL_FACILITIES = MeaningCategory.LIFE_MEDICAL_FACILITIES
        MEDICINE = MeaningCategory.LIFE_MEDICINE

    class DIETARY:
        """Helper class for dietary meaning categories."""
        ALL = MeaningCategory.DIETARY_ALL
        FOOD_TYPES = MeaningCategory.DIETARY_FOOD_TYPES
        VEGETABLES = MeaningCategory.DIETARY_VEGETABLES
        GRAIN = MeaningCategory.DIETARY_GRAIN
        FRUIT = MeaningCategory.DIETARY_FRUIT
        BEVERAGES = MeaningCategory.DIETARY_BEVERAGES
        FOOD_INGREDIENTS = MeaningCategory.DIETARY_FOOD_INGREDIENTS
        COOKING_APPLIANCES = MeaningCategory.DIETARY_COOKING_APPLIANCES
        EATING_PLACES = MeaningCategory.DIETARY_EATING_PLACES
        TASTE = MeaningCategory.DIETARY_TASTE
        EATING_AND_COOKING_ACTIVITIES = MeaningCategory.DIETARY_EATING_AND_COOKING_ACTIVITIES

    class CLOTHING:
        """Helper class for clothing meaning categories."""
        ALL = MeaningCategory.CLOTHING_ALL
        TYPES_OF_CLOTHING = MeaningCategory.CLOTHING_TYPES_OF_CLOTHING
        FABRIC = MeaningCategory.CLOTHING_FABRIC
        PARTS_OF_CLOTHING = MeaningCategory.CLOTHING_PARTS_OF_CLOTHING
        HATS_SHOES_ACCESSORIES = MeaningCategory.CLOTHING_HATS_SHOES_ACCESSORIES
        PLACES_RELATED_TO_CLOTHING = MeaningCategory.CLOTHING_PLACES_RELATED_TO_CLOTHING
        STATE_OF_CLOTHING = MeaningCategory.CLOTHING_STATE_OF_CLOTHING
        ACTIVITIES_RELATED_TO_CLOTHING = MeaningCategory.CLOTHING_ACTIVITIES_RELATED_TO_CLOTHING
        BEAUTY_AND_HEALTH = MeaningCategory.CLOTHING_BEAUTY_AND_HEALTH

    class HOME_LIFE:
        """Helper class for home life meaning categories."""
        ALL = MeaningCategory.HOME_LIFE_ALL
        BUILDING_TYPES = MeaningCategory.HOME_LIFE_BUILDING_TYPES
        TYPE_OF_HOUSING = MeaningCategory.HOME_LIFE_TYPE_OF_HOUSING
        RESIDENTIAL_AREA = MeaningCategory.HOME_LIFE_RESIDENTIAL_AREA
        HOUSEHOLD_ITEMS = MeaningCategory.HOME_LIFE_HOUSEHOLD_ITEMS
        HOUSING_STRUCTURE = MeaningCategory.HOME_LIFE_HOUSING_STRUCTURE
        RESIDENTIAL_STATUS = MeaningCategory.HOME_LIFE_RESIDENTIAL_STATUS
        RESIDENTIAL_ACTIVITIES = MeaningCategory.HOME_LIFE_RESIDENTIAL_ACTIVITIES
        RESIDENTIAL_CHORES = MeaningCategory.HOME_LIFE_RESIDENTIAL_CHORES

    class SOCIAL_LIFE:
        """Helper class for social life meaning categories."""
        ALL = MeaningCategory.SOCIAL_LIFE_ALL
        HUMAN_RELATIONSHIPS = MeaningCategory.SOCIAL_LIFE_HUMAN_RELATIONSHIPS
        MEANS_OF_COMMUNICATION = MeaningCategory.SOCIAL_LIFE_MEANS_OF_COMMUNICATION
        MODES_OF_TRANSPORTATION = MeaningCategory.SOCIAL_LIFE_MODES_OF_TRANSPORTATION
        PLACES_FOR_TRANSPORTATION_USAGE = \
            MeaningCategory.SOCIAL_LIFE_PLACES_FOR_TRANSPORTATION_USAGE
        MEDIA = MeaningCategory.SOCIAL_LIFE_MEDIA
        WORKPLACE = MeaningCategory.SOCIAL_LIFE_WORKPLACE
        TITLES_AND_POSITIONS = MeaningCategory.SOCIAL_LIFE_TITLES_AND_POSITIONS
        OCCUPATION = MeaningCategory.SOCIAL_LIFE_OCCUPATION
        SOCIAL_EVENTS = MeaningCategory.SOCIAL_LIFE_SOCIAL_EVENTS
        SOCIAL_LIFE_STATUS = MeaningCategory.SOCIAL_LIFE_SOCIAL_LIFE_STATUS
        SOCIAL_ACTIVITIES = MeaningCategory.SOCIAL_LIFE_SOCIAL_ACTIVITIES
        TRANSPORTATION_USAGE = MeaningCategory.SOCIAL_LIFE_TRANSPORTATION_USAGE
        WORKPLACE_LIFE = MeaningCategory.SOCIAL_LIFE_WORKPLACE_LIFE
        LANGUAGE_ACTIVITIES = MeaningCategory.SOCIAL_LIFE_LANGUAGE_ACTIVITIES
        COMMUNICATION_ACTIVITIES = MeaningCategory.SOCIAL_LIFE_COMMUNICATION_ACTIVITIES
        GRAMMAR_AND_SPEECH = MeaningCategory.SOCIAL_LIFE_GRAMMAR_AND_SPEECH

    class ECONOMIC:
        """Helper class for economic meaning categories."""
        ALL = MeaningCategory.ECONOMIC_ALL
        PEOPLE = MeaningCategory.ECONOMIC_PEOPLE
        PLACES = MeaningCategory.ECONOMIC_PLACES
        MEANS = MeaningCategory.ECONOMIC_MEANS
        PRODUCTS = MeaningCategory.ECONOMIC_PRODUCTS
        STATUS = MeaningCategory.ECONOMIC_STATUS
        ACTIVITIES = MeaningCategory.ECONOMIC_ACTIVITIES

    class EDUCATION:
        """Helper class for education meaning categories."""
        ALL = MeaningCategory.EDUCATION_ALL
        PEOPLE = MeaningCategory.EDUCATION_PEOPLE
        MAJORS_AND_SUBJECTS = MeaningCategory.EDUCATION_MAJORS_AND_SUBJECTS
        EDUCATIONAL_INSTITUTIONS = MeaningCategory.EDUCATION_EDUCATIONAL_INSTITUTIONS
        SCHOOL_FACILITIES = MeaningCategory.EDUCATION_SCHOOL_FACILITIES
        OBJECTS = MeaningCategory.EDUCATION_OBJECTS
        ACADEMIC_TERMS = MeaningCategory.EDUCATION_ACADEMIC_TERMS
        TEACHING_AND_LEARNING_ACTIVITIES = \
            MeaningCategory.EDUCATION_TEACHING_AND_LEARNING_ACTIVITIES
        ACADEMIC_ACTIVITIES = MeaningCategory.EDUCATION_ACADEMIC_ACTIVITIES

    class RELIGION:
        """Helper class for religion meaning categories."""
        ALL = MeaningCategory.RELIGION_ALL
        TYPES_OF_RELIGION = MeaningCategory.RELIGION_TYPES_OF_RELIGION
        PLACES = MeaningCategory.RELIGION_PLACES
        PEOPLE = MeaningCategory.RELIGION_PEOPLE
        RELIGIOUS_WORDS = MeaningCategory.RELIGION_RELIGIOUS_WORDS
        MAJOR_FIGURES = MeaningCategory.RELIGION_MAJOR_FIGURES
        OBJECTS = MeaningCategory.RELIGION_OBJECTS
        PRACTICES = MeaningCategory.RELIGION_PRACTICES

    class CULTURE:
        """Helper class for culture meaning categories."""
        ALL = MeaningCategory.CULTURE_ALL
        CULTURAL_ACTIVITY_PARTICIPANTS = MeaningCategory.CULTURE_CULTURAL_ACTIVITY_PARTICIPANTS
        MUSIC = MeaningCategory.CULTURE_MUSIC
        FINE_ART = MeaningCategory.CULTURE_FINE_ART
        LITERATURE = MeaningCategory.CULTURE_LITERATURE
        ART = MeaningCategory.CULTURE_ART
        POP_CULTURE = MeaningCategory.CULTURE_POP_CULTURE
        TRADITIONAL_CULTURE = MeaningCategory.CULTURE_TRADITIONAL_CULTURE
        CULTURAL_ACTIVITY_PLACES = MeaningCategory.CULTURE_CULTURAL_ACTIVITY_PLACES
        CULTURAL_ACTIVITIES = MeaningCategory.CULTURE_CULTURAL_ACTIVITIES

    class POLITICS_AND_ADMINISTRATION:
        """Helper class for politics and administration meaning categories."""
        ALL = MeaningCategory.POLITICS_AND_ADMINISTRATION_ALL
        PUBLIC_INSTITUTIONS = MeaningCategory.POLITICS_AND_ADMINISTRATION_PUBLIC_INSTITUTIONS
        JUDICIAL_AND_SECURITY_PERSONNEL = \
            MeaningCategory.POLITICS_AND_ADMINISTRATION_JUDICIAL_AND_SECURITY_PERSONNEL
        WEAPONS = MeaningCategory.POLITICS_AND_ADMINISTRATION_WEAPONS
        POLITICS_AND_SECURITY = MeaningCategory.POLITICS_AND_ADMINISTRATION_POLITICS_AND_SECURITY
        POLITICAL_ACTS = MeaningCategory.POLITICS_AND_ADMINISTRATION_POLITICAL_ACTS
        LAW_AND_SECURITY_ACTS = MeaningCategory.POLITICS_AND_ADMINISTRATION_LAW_AND_SECURITY_ACTS
        POLITICAL_AND_ADMINISTRATIVE_PERSONNEL = \
            MeaningCategory.POLITICS_AND_ADMINISTRATION_POLITICAL_AND_ADMINISTRATIVE_PERSONNEL

    class NATURE:
        """Helper class for nature meaning categories."""
        ALL = MeaningCategory.NATURE_ALL
        TOPOGRAPHY = MeaningCategory.NATURE_TOPOGRAPHY
        SURFACE_OBJECTS = MeaningCategory.NATURE_SURFACE_OBJECTS
        CELESTIAL_BODIES = MeaningCategory.NATURE_CELESTIAL_BODIES
        NATURAL_RESOURCES = MeaningCategory.NATURE_NATURAL_RESOURCES
        DISASTERS = MeaningCategory.NATURE_DISASTERS
        WEATHER_AND_CLIMATE = MeaningCategory.NATURE_WEATHER_AND_CLIMATE

    class ANIMALS_AND_PLANTS:
        """Helper class for animals and plants meaning categories."""
        ALL = MeaningCategory.ANIMALS_AND_PLANTS_ALL
        ANIMALS = MeaningCategory.ANIMALS_AND_PLANTS_ANIMALS
        INSECTS = MeaningCategory.ANIMALS_AND_PLANTS_INSECTS
        PLANTS = MeaningCategory.ANIMALS_AND_PLANTS_PLANTS
        PARTS_OF_ANIMALS = MeaningCategory.ANIMALS_AND_PLANTS_PARTS_OF_ANIMALS
        PARTS_OF_PLANTS = MeaningCategory.ANIMALS_AND_PLANTS_PARTS_OF_PLANTS
        BEHAVIORS = MeaningCategory.ANIMALS_AND_PLANTS_BEHAVIORS
        SOUNDS = MeaningCategory.ANIMALS_AND_PLANTS_SOUNDS

    class CONCEPTS:
        """Helper class for concept meaning categories."""
        ALL = MeaningCategory.CONCEPTS_ALL
        SHAPE = MeaningCategory.CONCEPTS_SHAPE
        PROPERTY = MeaningCategory.CONCEPTS_PROPERTY
        SPEED = MeaningCategory.CONCEPTS_SPEED
        BRIGHTNESS = MeaningCategory.CONCEPTS_BRIGHTNESS
        TEMPERATURE = MeaningCategory.CONCEPTS_TEMPERATURE
        COLORS = MeaningCategory.CONCEPTS_COLORS
        NUMBERS = MeaningCategory.CONCEPTS_NUMBERS
        COUNTERS = MeaningCategory.CONCEPTS_COUNTERS
        AMOUNT = MeaningCategory.CONCEPTS_AMOUNT
        DEGREE = MeaningCategory.CONCEPTS_DEGREE
        ORDER = MeaningCategory.CONCEPTS_ORDER
        FREQUENCY = MeaningCategory.CONCEPTS_FREQUENCY
        TIME = MeaningCategory.CONCEPTS_TIME
        LOCATION_AND_DIRECTION = MeaningCategory.CONCEPTS_LOCATION_AND_DIRECTION
        AREA = MeaningCategory.CONCEPTS_AREA
        INSTRUCTIONS = MeaningCategory.CONCEPTS_INSTRUCTIONS
        CONNECTION = MeaningCategory.CONCEPTS_CONNECTION
        QUESTION_WORDS = MeaningCategory.CONCEPTS_QUESTION_WORDS
        PRONOUNS = MeaningCategory.CONCEPTS_PRONOUNS

class SubjectCategoryHelper:
    """Helper class for subject categories."""

    def __new__(cls, value):
        return SubjectCategory(value)

    @staticmethod
    def enum():
        """Returns the underlying enumeration type."""
        return SubjectCategory

    ALL = SubjectCategory.ALL

    class ELEMENTARY:
        """Helper class for elementary subject categories."""
        GREETING = SubjectCategory.ELEMENTARY_GREETING
        INTRODUCING_ONESELF = SubjectCategory.ELEMENTARY_INTRODUCING_ONESELF
        INTRODUCING_FAMILY = SubjectCategory.ELEMENTARY_INTRODUCING_FAMILY
        EXCHANGING_PERSONAL_INFORMATION = SubjectCategory.ELEMENTARY_EXCHANGING_PERSONAL_INFORMATION
        DESCRIBING_LOCATION = SubjectCategory.ELEMENTARY_DESCRIBING_LOCATION
        DIRECTIONS = SubjectCategory.ELEMENTARY_DIRECTIONS
        USING_TRANSPORTATION = SubjectCategory.ELEMENTARY_USING_TRANSPORTATION
        PURCHASING_GOODS = SubjectCategory.ELEMENTARY_PURCHASING_GOODS
        ORDERING_FOOD = SubjectCategory.ELEMENTARY_ORDERING_FOOD
        DESCRIBING_DISHES = SubjectCategory.ELEMENTARY_DESCRIBING_DISHES
        EXPRESSING_TIME = SubjectCategory.ELEMENTARY_EXPRESSING_TIME
        EXPRESSING_DATE = SubjectCategory.ELEMENTARY_EXPRESSING_DATE
        EXPRESSING_DAY_OF_THE_WEEK = SubjectCategory.ELEMENTARY_EXPRESSING_DAY_OF_THE_WEEK
        WEATHER_AND_SEASON = SubjectCategory.ELEMENTARY_WEATHER_AND_SEASON
        DAILY_LIFE = SubjectCategory.ELEMENTARY_DAILY_LIFE
        SCHOOL_LIFE = SubjectCategory.ELEMENTARY_SCHOOL_LIFE
        LIFE_IN_KOREA = SubjectCategory.ELEMENTARY_LIFE_IN_KOREA
        MAKING_PROMISES = SubjectCategory.ELEMENTARY_MAKING_PROMISES
        MAKING_PHONE_CALLS = SubjectCategory.ELEMENTARY_MAKING_PHONE_CALLS
        EXPRESSING_GRATITUDE = SubjectCategory.ELEMENTARY_EXPRESSING_GRATITUDE
        APOLOGIZING = SubjectCategory.ELEMENTARY_APOLOGIZING
        TRAVEL = SubjectCategory.ELEMENTARY_TRAVEL
        WEEKENDS_AND_HOLIDAYS = SubjectCategory.ELEMENTARY_WEEKENDS_AND_HOLIDAYS
        HOBBIES = SubjectCategory.ELEMENTARY_HOBBIES
        FAMILY_EVENTS = SubjectCategory.ELEMENTARY_FAMILY_EVENTS
        HEALTH = SubjectCategory.ELEMENTARY_HEALTH
        USING_THE_HOSPITAL = SubjectCategory.ELEMENTARY_USING_THE_HOSPITAL
        USING_THE_PHARMACY = SubjectCategory.ELEMENTARY_USING_THE_PHARMACY
        USING_THE_LIBRARY = SubjectCategory.ELEMENTARY_USING_THE_LIBRARY
        USING_THE_POST_OFFICE = SubjectCategory.ELEMENTARY_USING_THE_POST_OFFICE
        USING_THE_IMMIGRATION_OFFICE = SubjectCategory.ELEMENTARY_USING_THE_IMMIGRATION_OFFICE
        INVITING_AND_VISITING = SubjectCategory.ELEMENTARY_INVITING_AND_VISITING
        FINDING_A_HOUSE = SubjectCategory.ELEMENTARY_FINDING_A_HOUSE
        HOUSEWORK = SubjectCategory.ELEMENTARY_HOUSEWORK
        EXPRESSING_EMOTIONS = SubjectCategory.ELEMENTARY_EXPRESSING_EMOTIONS
        DESCRIBING_PERSONALITY = SubjectCategory.ELEMENTARY_DESCRIBING_PERSONALITY
        DESCRIBING_CLOTHES = SubjectCategory.ELEMENTARY_DESCRIBING_CLOTHES
        DESCRIBING_PHYSICAL_FEATURES = SubjectCategory.ELEMENTARY_DESCRIBING_PHYSICAL_FEATURES
        WATCHING_MOVIES = SubjectCategory.ELEMENTARY_WATCHING_MOVIES

    class INTERMEDIATE:
        """Helper class for intermediate subject categories."""
        EXCHANGING_PERSONAL_INFORMATION = \
            SubjectCategory.INTERMEDIATE_EXCHANGING_PERSONAL_INFORMATION
        USING_TRANSPORTATION = SubjectCategory.INTERMEDIATE_USING_TRANSPORTATION
        GEOLOGICAL_INFORMATION = SubjectCategory.INTERMEDIATE_GEOLOGICAL_INFORMATION
        PURCHASING_GOODS = SubjectCategory.INTERMEDIATE_PURCHASING_GOODS
        DESCRIBING_FOOD = SubjectCategory.INTERMEDIATE_DESCRIBING_FOOD
        DESCRIBING_DISHES = SubjectCategory.INTERMEDIATE_DESCRIBING_DISHES
        WEATHER_AND_SEASON = SubjectCategory.INTERMEDIATE_WEATHER_AND_SEASON
        SCHOOL_LIFE = SubjectCategory.INTERMEDIATE_SCHOOL_LIFE
        LIFE_IN_KOREA = SubjectCategory.INTERMEDIATE_LIFE_IN_KOREA
        JOBS_AND_CAREERS = SubjectCategory.INTERMEDIATE_JOBS_AND_CAREERS
        WORKPLACE_LIFE = SubjectCategory.INTERMEDIATE_WORKPLACE_LIFE
        TRAVEL = SubjectCategory.INTERMEDIATE_TRAVEL
        WEEKENDS_AND_HOLIDAYS = SubjectCategory.INTERMEDIATE_WEEKENDS_AND_HOLIDAYS
        HOBBIES = SubjectCategory.INTERMEDIATE_HOBBIES
        FAMILY_EVENTS = SubjectCategory.INTERMEDIATE_FAMILY_EVENTS
        FAMILY_EVENTS_DURING_HOLIDAYS = SubjectCategory.INTERMEDIATE_FAMILY_EVENTS_DURING_HOLIDAYS
        HEALTH = SubjectCategory.INTERMEDIATE_HEALTH
        USING_PUBLIC_INSTITUTIONS = SubjectCategory.INTERMEDIATE_USING_PUBLIC_INSTITUTIONS
        INVITING_AND_VISITING = SubjectCategory.INTERMEDIATE_INVITING_AND_VISITING
        FINDING_A_HOUSE = SubjectCategory.INTERMEDIATE_FINDING_A_HOUSE
        HOUSEWORK = SubjectCategory.INTERMEDIATE_HOUSEWORK
        EXPRESSING_EMOTIONS = SubjectCategory.INTERMEDIATE_EXPRESSING_EMOTIONS
        DESCRIBING_PERSONALITY = SubjectCategory.INTERMEDIATE_DESCRIBING_PERSONALITY
        DESCRIBING_CLOTHES = SubjectCategory.INTERMEDIATE_DESCRIBING_CLOTHES
        DESCRIBING_PHYSICAL_FEATURES = SubjectCategory.INTERMEDIATE_DESCRIBING_PHYSICAL_FEATURES
        PERFORMANCES_AND_APPRECIATION = SubjectCategory.INTERMEDIATE_PERFORMANCES_AND_APPRECIATION
        MASS_MEDIA = SubjectCategory.INTERMEDIATE_MASS_MEDIA
        COMPUTERS_AND_THE_INTERNET = SubjectCategory.INTERMEDIATE_COMPUTERS_AND_THE_INTERNET
        DESCRIBING_EVENTS_AND_DISASTERS = \
            SubjectCategory.INTERMEDIATE_DESCRIBING_EVENTS_AND_DISASTERS
        ENVIRONMENTAL_ISSUES = SubjectCategory.INTERMEDIATE_ENVIRONMENTAL_ISSUES
        COMPARING_CULTURES = SubjectCategory.INTERMEDIATE_COMPARING_CULTURES
        HUMAN_RELATIONSHIPS = SubjectCategory.INTERMEDIATE_HUMAN_RELATIONSHIPS
        KOREAN_LITERATURE = SubjectCategory.INTERMEDIATE_KOREAN_LITERATURE
        SOLVING_PROBLEMS = SubjectCategory.INTERMEDIATE_SOLVING_PROBLEMS
        TALKING_ABOUT_MISTAKES = SubjectCategory.INTERMEDIATE_TALKING_ABOUT_MISTAKES
        DATING_AND_MARRIAGE = SubjectCategory.INTERMEDIATE_DATING_AND_MARRIAGE
        LANGUAGE = SubjectCategory.INTERMEDIATE_LANGUAGE

    class ADVANCED:
        """Helper class for advanced subject categories."""
        GEOLOGICAL_INFORMATION = SubjectCategory.ADVANCED_GEOLOGICAL_INFORMATION
        ECONOMICS_AND_ADMINISTRATION = SubjectCategory.ADVANCED_ECONOMICS_AND_ADMINISTRATION
        DIETARY_CULTURE = SubjectCategory.ADVANCED_DIETARY_CULTURE
        CLIMATE = SubjectCategory.ADVANCED_CLIMATE
        EDUCATION = SubjectCategory.ADVANCED_EDUCATION
        JOBS_AND_CAREERS = SubjectCategory.ADVANCED_JOBS_AND_CAREERS
        WORKPLACE_LIFE = SubjectCategory.ADVANCED_WORKPLACE_LIFE
        HOBBIES = SubjectCategory.ADVANCED_HOBBIES
        HEALTH_AND_MEDICAL_TREATMENT = SubjectCategory.ADVANCED_HEALTH_AND_MEDICAL_TREATMENT
        RESIDENTIAL_AREA = SubjectCategory.ADVANCED_RESIDENTIAL_AREA
        PSYCHOLOGY = SubjectCategory.ADVANCED_PSYCHOLOGY
        APPEARANCE = SubjectCategory.ADVANCED_APPEARANCE
        POP_CULTURE = SubjectCategory.ADVANCED_POP_CULTURE
        COMPUTERS_AND_THE_INTERNET = SubjectCategory.ADVANCED_COMPUTERS_AND_THE_INTERNET
        SOCIAL_ISSUES = SubjectCategory.ADVANCED_SOCIAL_ISSUES
        ENVIRONMENTAL_ISSUES = SubjectCategory.ADVANCED_ENVIRONMENTAL_ISSUES
        SOCIAL_SYSTEM = SubjectCategory.ADVANCED_SOCIAL_SYSTEM
        CULTURAL_DIFFERENCES = SubjectCategory.ADVANCED_CULTURAL_DIFFERENCES
        HUMAN_RELATIONSHIPS = SubjectCategory.ADVANCED_HUMAN_RELATIONSHIPS
        ART = SubjectCategory.ADVANCED_ART
        ARCHITECTURE = SubjectCategory.ADVANCED_ARCHITECTURE
        SCIENCE_AND_TECHNOLOGY = SubjectCategory.ADVANCED_SCIENCE_AND_TECHNOLOGY
        LAW = SubjectCategory.ADVANCED_LAW
        SPORTS = SubjectCategory.ADVANCED_SPORTS
        PRESS = SubjectCategory.ADVANCED_PRESS
        LANGUAGE = SubjectCategory.ADVANCED_LANGUAGE
        HISTORY = SubjectCategory.ADVANCED_HISTORY
        POLITICS = SubjectCategory.ADVANCED_POLITICS
        RELIGION = SubjectCategory.ADVANCED_RELIGION
        PHILOSOPHY_AND_ETHICS = SubjectCategory.ADVANCED_PHILOSOPHY_AND_ETHICS
