"""
Contains enumeration class for handling subject categories.
"""

# pylint: disable=invalid-name,too-few-public-methods,too-many-instance-attributes

from .base import IntEnum, EnumProxy

class SubjectCategory(IntEnum):
    """Enumeration class that contains subject category values."""

    __aliases__ = {
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

    class __PROXY_ELEMENTARY__(EnumProxy):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.GREETING = SubjectCategory.ELEMENTARY_GREETING
            self.INTRODUCING_ONESELF = SubjectCategory.ELEMENTARY_INTRODUCING_ONESELF
            self.INTRODUCING_FAMILY = SubjectCategory.ELEMENTARY_INTRODUCING_FAMILY
            self.EXCHANGING_PERSONAL_INFORMATION = \
                SubjectCategory.ELEMENTARY_EXCHANGING_PERSONAL_INFORMATION
            self.DESCRIBING_LOCATION = SubjectCategory.ELEMENTARY_DESCRIBING_LOCATION
            self.DIRECTIONS = SubjectCategory.ELEMENTARY_DIRECTIONS
            self.USING_TRANSPORTATION = SubjectCategory.ELEMENTARY_USING_TRANSPORTATION
            self.PURCHASING_GOODS = SubjectCategory.ELEMENTARY_PURCHASING_GOODS
            self.ORDERING_FOOD = SubjectCategory.ELEMENTARY_ORDERING_FOOD
            self.DESCRIBING_DISHES = SubjectCategory.ELEMENTARY_DESCRIBING_DISHES
            self.EXPRESSING_TIME = SubjectCategory.ELEMENTARY_EXPRESSING_TIME
            self.EXPRESSING_DATE = SubjectCategory.ELEMENTARY_EXPRESSING_DATE
            self.EXPRESSING_DAY_OF_THE_WEEK = SubjectCategory.ELEMENTARY_EXPRESSING_DAY_OF_THE_WEEK
            self.WEATHER_AND_SEASON = SubjectCategory.ELEMENTARY_WEATHER_AND_SEASON
            self.DAILY_LIFE = SubjectCategory.ELEMENTARY_DAILY_LIFE
            self.SCHOOL_LIFE = SubjectCategory.ELEMENTARY_SCHOOL_LIFE
            self.LIFE_IN_KOREA = SubjectCategory.ELEMENTARY_LIFE_IN_KOREA
            self.MAKING_PROMISES = SubjectCategory.ELEMENTARY_MAKING_PROMISES
            self.MAKING_PHONE_CALLS = SubjectCategory.ELEMENTARY_MAKING_PHONE_CALLS
            self.EXPRESSING_GRATITUDE = SubjectCategory.ELEMENTARY_EXPRESSING_GRATITUDE
            self.APOLOGIZING = SubjectCategory.ELEMENTARY_APOLOGIZING
            self.TRAVEL = SubjectCategory.ELEMENTARY_TRAVEL
            self.WEEKENDS_AND_HOLIDAYS = SubjectCategory.ELEMENTARY_WEEKENDS_AND_HOLIDAYS
            self.HOBBIES = SubjectCategory.ELEMENTARY_HOBBIES
            self.FAMILY_EVENTS = SubjectCategory.ELEMENTARY_FAMILY_EVENTS
            self.HEALTH = SubjectCategory.ELEMENTARY_HEALTH
            self.USING_THE_HOSPITAL = SubjectCategory.ELEMENTARY_USING_THE_HOSPITAL
            self.USING_THE_PHARMACY = SubjectCategory.ELEMENTARY_USING_THE_PHARMACY
            self.USING_THE_LIBRARY = SubjectCategory.ELEMENTARY_USING_THE_LIBRARY
            self.USING_THE_POST_OFFICE = SubjectCategory.ELEMENTARY_USING_THE_POST_OFFICE
            self.USING_THE_IMMIGRATION_OFFICE = \
                SubjectCategory.ELEMENTARY_USING_THE_IMMIGRATION_OFFICE
            self.INVITING_AND_VISITING = SubjectCategory.ELEMENTARY_INVITING_AND_VISITING
            self.FINDING_A_HOUSE = SubjectCategory.ELEMENTARY_FINDING_A_HOUSE
            self.HOUSEWORK = SubjectCategory.ELEMENTARY_HOUSEWORK
            self.EXPRESSING_EMOTIONS = SubjectCategory.ELEMENTARY_EXPRESSING_EMOTIONS
            self.DESCRIBING_PERSONALITY = SubjectCategory.ELEMENTARY_DESCRIBING_PERSONALITY
            self.DESCRIBING_CLOTHES = SubjectCategory.ELEMENTARY_DESCRIBING_CLOTHES
            self.DESCRIBING_PHYSICAL_FEATURES = \
                SubjectCategory.ELEMENTARY_DESCRIBING_PHYSICAL_FEATURES
            self.WATCHING_MOVIES = SubjectCategory.ELEMENTARY_WATCHING_MOVIES

    class __PROXY_INTERMEDIATE__(EnumProxy):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.EXCHANGING_PERSONAL_INFORMATION = \
                SubjectCategory.INTERMEDIATE_EXCHANGING_PERSONAL_INFORMATION
            self.USING_TRANSPORTATION = SubjectCategory.INTERMEDIATE_USING_TRANSPORTATION
            self.GEOLOGICAL_INFORMATION = SubjectCategory.INTERMEDIATE_GEOLOGICAL_INFORMATION
            self.PURCHASING_GOODS = SubjectCategory.INTERMEDIATE_PURCHASING_GOODS
            self.DESCRIBING_FOOD = SubjectCategory.INTERMEDIATE_DESCRIBING_FOOD
            self.DESCRIBING_DISHES = SubjectCategory.INTERMEDIATE_DESCRIBING_DISHES
            self.WEATHER_AND_SEASON = SubjectCategory.INTERMEDIATE_WEATHER_AND_SEASON
            self.SCHOOL_LIFE = SubjectCategory.INTERMEDIATE_SCHOOL_LIFE
            self.LIFE_IN_KOREA = SubjectCategory.INTERMEDIATE_LIFE_IN_KOREA
            self.JOBS_AND_CAREERS = SubjectCategory.INTERMEDIATE_JOBS_AND_CAREERS
            self.WORKPLACE_LIFE = SubjectCategory.INTERMEDIATE_WORKPLACE_LIFE
            self.TRAVEL = SubjectCategory.INTERMEDIATE_TRAVEL
            self.WEEKENDS_AND_HOLIDAYS = SubjectCategory.INTERMEDIATE_WEEKENDS_AND_HOLIDAYS
            self.HOBBIES = SubjectCategory.INTERMEDIATE_HOBBIES
            self.FAMILY_EVENTS = SubjectCategory.INTERMEDIATE_FAMILY_EVENTS
            self.FAMILY_EVENTS_DURING_HOLIDAYS = \
                SubjectCategory.INTERMEDIATE_FAMILY_EVENTS_DURING_HOLIDAYS
            self.HEALTH = SubjectCategory.INTERMEDIATE_HEALTH
            self.USING_PUBLIC_INSTITUTIONS = SubjectCategory.INTERMEDIATE_USING_PUBLIC_INSTITUTIONS
            self.INVITING_AND_VISITING = SubjectCategory.INTERMEDIATE_INVITING_AND_VISITING
            self.FINDING_A_HOUSE = SubjectCategory.INTERMEDIATE_FINDING_A_HOUSE
            self.HOUSEWORK = SubjectCategory.INTERMEDIATE_HOUSEWORK
            self.EXPRESSING_EMOTIONS = SubjectCategory.INTERMEDIATE_EXPRESSING_EMOTIONS
            self.DESCRIBING_PERSONALITY = SubjectCategory.INTERMEDIATE_DESCRIBING_PERSONALITY
            self.DESCRIBING_CLOTHES = SubjectCategory.INTERMEDIATE_DESCRIBING_CLOTHES
            self.DESCRIBING_PHYSICAL_FEATURES = \
                SubjectCategory.INTERMEDIATE_DESCRIBING_PHYSICAL_FEATURES
            self.PERFORMANCES_AND_APPRECIATION = \
                SubjectCategory.INTERMEDIATE_PERFORMANCES_AND_APPRECIATION
            self.MASS_MEDIA = SubjectCategory.INTERMEDIATE_MASS_MEDIA
            self.COMPUTERS_AND_THE_INTERNET = \
                SubjectCategory.INTERMEDIATE_COMPUTERS_AND_THE_INTERNET
            self.DESCRIBING_EVENTS_AND_DISASTERS = \
                SubjectCategory.INTERMEDIATE_DESCRIBING_EVENTS_AND_DISASTERS
            self.ENVIRONMENTAL_ISSUES = SubjectCategory.INTERMEDIATE_ENVIRONMENTAL_ISSUES
            self.COMPARING_CULTURES = SubjectCategory.INTERMEDIATE_COMPARING_CULTURES
            self.HUMAN_RELATIONSHIPS = SubjectCategory.INTERMEDIATE_HUMAN_RELATIONSHIPS
            self.KOREAN_LITERATURE = SubjectCategory.INTERMEDIATE_KOREAN_LITERATURE
            self.SOLVING_PROBLEMS = SubjectCategory.INTERMEDIATE_SOLVING_PROBLEMS
            self.TALKING_ABOUT_MISTAKES = SubjectCategory.INTERMEDIATE_TALKING_ABOUT_MISTAKES
            self.DATING_AND_MARRIAGE = SubjectCategory.INTERMEDIATE_DATING_AND_MARRIAGE
            self.LANGUAGE = SubjectCategory.INTERMEDIATE_LANGUAGE

    class __PROXY_ADVANCED__(EnumProxy):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.GEOLOGICAL_INFORMATION = SubjectCategory.ADVANCED_GEOLOGICAL_INFORMATION
            self.ECONOMICS_AND_ADMINISTRATION = \
                SubjectCategory.ADVANCED_ECONOMICS_AND_ADMINISTRATION
            self.DIETARY_CULTURE = SubjectCategory.ADVANCED_DIETARY_CULTURE
            self.CLIMATE = SubjectCategory.ADVANCED_CLIMATE
            self.EDUCATION = SubjectCategory.ADVANCED_EDUCATION
            self.JOBS_AND_CAREERS = SubjectCategory.ADVANCED_JOBS_AND_CAREERS
            self.WORKPLACE_LIFE = SubjectCategory.ADVANCED_WORKPLACE_LIFE
            self.HOBBIES = SubjectCategory.ADVANCED_HOBBIES
            self.HEALTH_AND_MEDICAL_TREATMENT = \
                SubjectCategory.ADVANCED_HEALTH_AND_MEDICAL_TREATMENT
            self.RESIDENTIAL_AREA = SubjectCategory.ADVANCED_RESIDENTIAL_AREA
            self.PSYCHOLOGY = SubjectCategory.ADVANCED_PSYCHOLOGY
            self.APPEARANCE = SubjectCategory.ADVANCED_APPEARANCE
            self.POP_CULTURE = SubjectCategory.ADVANCED_POP_CULTURE
            self.COMPUTERS_AND_THE_INTERNET = SubjectCategory.ADVANCED_COMPUTERS_AND_THE_INTERNET
            self.SOCIAL_ISSUES = SubjectCategory.ADVANCED_SOCIAL_ISSUES
            self.ENVIRONMENTAL_ISSUES = SubjectCategory.ADVANCED_ENVIRONMENTAL_ISSUES
            self.SOCIAL_SYSTEM = SubjectCategory.ADVANCED_SOCIAL_SYSTEM
            self.CULTURAL_DIFFERENCES = SubjectCategory.ADVANCED_CULTURAL_DIFFERENCES
            self.HUMAN_RELATIONSHIPS = SubjectCategory.ADVANCED_HUMAN_RELATIONSHIPS
            self.ART = SubjectCategory.ADVANCED_ART
            self.ARCHITECTURE = SubjectCategory.ADVANCED_ARCHITECTURE
            self.SCIENCE_AND_TECHNOLOGY = SubjectCategory.ADVANCED_SCIENCE_AND_TECHNOLOGY
            self.LAW = SubjectCategory.ADVANCED_LAW
            self.SPORTS = SubjectCategory.ADVANCED_SPORTS
            self.PRESS = SubjectCategory.ADVANCED_PRESS
            self.LANGUAGE = SubjectCategory.ADVANCED_LANGUAGE
            self.HISTORY = SubjectCategory.ADVANCED_HISTORY
            self.POLITICS = SubjectCategory.ADVANCED_POLITICS
            self.RELIGION = SubjectCategory.ADVANCED_RELIGION
            self.PHILOSOPHY_AND_ETHICS = SubjectCategory.ADVANCED_PHILOSOPHY_AND_ETHICS


    __ELEMENTARY__: __PROXY_ELEMENTARY__ = __PROXY_ELEMENTARY__(False)
    __INTERMEDIATE__: __PROXY_INTERMEDIATE__ = __PROXY_INTERMEDIATE__(False)
    __ADVANCED__: __PROXY_ADVANCED__ = __PROXY_ADVANCED__(False)


    @classmethod
    @property
    def ELEMENTARY(cls):
        """Proxy for elementary subject categories."""
        if not cls.__ELEMENTARY__.__populated__:
            cls.__ELEMENTARY__ = SubjectCategory.__PROXY_ELEMENTARY__(True)
        return cls.__ELEMENTARY__

    @classmethod
    @property
    def INTERMEDIATE(cls):
        """Proxy for intermediate subject categories."""
        if not cls.__INTERMEDIATE__.__populated__:
            cls.__INTERMEDIATE__ = SubjectCategory.__PROXY_INTERMEDIATE__(True)
        return cls.__INTERMEDIATE__

    @classmethod
    @property
    def ADVANCED(cls):
        """Proxy for advanced subject categories."""
        if not cls.__ADVANCED__.__populated__:
            cls.__ADVANCED__ = SubjectCategory.__PROXY_ADVANCED__(True)
        return cls.__ADVANCED__
