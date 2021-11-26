"""
Contains enumeration class for handling meaning categories.
"""

# pylint: disable=invalid-name,too-few-public-methods,too-many-instance-attributes

from .base import IntEnumBase, EnumProxyBase

class MeaningCategory(IntEnumBase):
    """Enumeration class that contains meaning category values."""

    __aliases__ = {
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

    class __PROXY_HUMAN__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.HUMAN_ALL
            self.TYPES_OF_PEOPLE = MeaningCategory.HUMAN_TYPES_OF_PEOPLE
            self.BODY_PARTS = MeaningCategory.HUMAN_BODY_PARTS
            self.HEALTH_STATUS = MeaningCategory.HUMAN_HEALTH_STATUS
            self.PHYSIOLOGICAL_PHENOMENA = MeaningCategory.HUMAN_PHYSIOLOGICAL_PHENOMENA
            self.SENSES = MeaningCategory.HUMAN_SENSES
            self.EMOTION = MeaningCategory.HUMAN_EMOTION
            self.PERSONALITY = MeaningCategory.HUMAN_PERSONALITY
            self.ATTITUDE = MeaningCategory.HUMAN_ATTITUDE
            self.FEATURES = MeaningCategory.HUMAN_FEATURES
            self.ABILITY = MeaningCategory.HUMAN_ABILITY
            self.PHYSICAL_CHANGES = MeaningCategory.HUMAN_PHYSICAL_CHANGES
            self.PHYSICAL_ACTIVITIES = MeaningCategory.HUMAN_PHYSICAL_ACTIVITIES
            self.ACTIONS_DONE_TO_THE_BODY = MeaningCategory.HUMAN_ACTIONS_DONE_TO_THE_BODY
            self.COGNITIVE_BEHAVIOR = MeaningCategory.HUMAN_COGNITIVE_BEHAVIOR
            self.SOUND = MeaningCategory.HUMAN_SOUND
            self.INNER_PARTS_OF_THE_BODY = MeaningCategory.HUMAN_INNER_PARTS_OF_THE_BODY

    class __PROXY_LIFE__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.LIFE_ALL
            self.STATE_OF_BEING = MeaningCategory.LIFE_STATE_OF_BEING
            self.LIFE_ACTIVIES = MeaningCategory.LIFE_LIFE_ACTIVIES
            self.DAILY_ACTIVITIES = MeaningCategory.LIFE_DAILY_ACTIVITIES
            self.KINSHIP = MeaningCategory.LIFE_KINSHIP
            self.FAMILY_EVENTS = MeaningCategory.LIFE_FAMILY_EVENTS
            self.LEISURE_TOOLS = MeaningCategory.LIFE_LEISURE_TOOLS
            self.LEISURE_FACILITIES = MeaningCategory.LIFE_LEISURE_FACILITIES
            self.LEISURE_ACTIVITIES = MeaningCategory.LIFE_LEISURE_ACTIVITIES
            self.DISEASES_AND_SYMPTOMS = MeaningCategory.LIFE_DISEASES_AND_SYMPTOMS
            self.MEDICAL_ACTIVITIES = MeaningCategory.LIFE_MEDICAL_ACTIVITIES
            self.MEDICAL_FACILITIES = MeaningCategory.LIFE_MEDICAL_FACILITIES
            self.MEDICINE = MeaningCategory.LIFE_MEDICINE

    class __PROXY_DIETARY__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.DIETARY_ALL
            self.FOOD_TYPES = MeaningCategory.DIETARY_FOOD_TYPES
            self.VEGETABLES = MeaningCategory.DIETARY_VEGETABLES
            self.GRAIN = MeaningCategory.DIETARY_GRAIN
            self.FRUIT = MeaningCategory.DIETARY_FRUIT
            self.BEVERAGES = MeaningCategory.DIETARY_BEVERAGES
            self.FOOD_INGREDIENTS = MeaningCategory.DIETARY_FOOD_INGREDIENTS
            self.COOKING_APPLIANCES = MeaningCategory.DIETARY_COOKING_APPLIANCES
            self.EATING_PLACES = MeaningCategory.DIETARY_EATING_PLACES
            self.TASTE = MeaningCategory.DIETARY_TASTE
            self.EATING_AND_COOKING_ACTIVITIES = \
                MeaningCategory.DIETARY_EATING_AND_COOKING_ACTIVITIES

    class __PROXY_CLOTHING__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.CLOTHING_ALL
            self.TYPES_OF_CLOTHING = MeaningCategory.CLOTHING_TYPES_OF_CLOTHING
            self.FABRIC = MeaningCategory.CLOTHING_FABRIC
            self.PARTS_OF_CLOTHING = MeaningCategory.CLOTHING_PARTS_OF_CLOTHING
            self.HATS_SHOES_ACCESSORIES = MeaningCategory.CLOTHING_HATS_SHOES_ACCESSORIES
            self.PLACES_RELATED_TO_CLOTHING = MeaningCategory.CLOTHING_PLACES_RELATED_TO_CLOTHING
            self.STATE_OF_CLOTHING = MeaningCategory.CLOTHING_STATE_OF_CLOTHING
            self.ACTIVITIES_RELATED_TO_CLOTHING = \
                MeaningCategory.CLOTHING_ACTIVITIES_RELATED_TO_CLOTHING
            self.BEAUTY_AND_HEALTH = MeaningCategory.CLOTHING_BEAUTY_AND_HEALTH

    class __PROXY_HOME_LIFE__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.HOME_LIFE_ALL
            self.BUILDING_TYPES = MeaningCategory.HOME_LIFE_BUILDING_TYPES
            self.TYPE_OF_HOUSING = MeaningCategory.HOME_LIFE_TYPE_OF_HOUSING
            self.RESIDENTIAL_AREA = MeaningCategory.HOME_LIFE_RESIDENTIAL_AREA
            self.HOUSEHOLD_ITEMS = MeaningCategory.HOME_LIFE_HOUSEHOLD_ITEMS
            self.HOUSING_STRUCTURE = MeaningCategory.HOME_LIFE_HOUSING_STRUCTURE
            self.RESIDENTIAL_STATUS = MeaningCategory.HOME_LIFE_RESIDENTIAL_STATUS
            self.RESIDENTIAL_ACTIVITIES = MeaningCategory.HOME_LIFE_RESIDENTIAL_ACTIVITIES
            self.RESIDENTIAL_CHORES = MeaningCategory.HOME_LIFE_RESIDENTIAL_CHORES

    class __PROXY_SOCIAL_LIFE__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.SOCIAL_LIFE_ALL
            self.HUMAN_RELATIONSHIPS = MeaningCategory.SOCIAL_LIFE_HUMAN_RELATIONSHIPS
            self.MEANS_OF_COMMUNICATION = MeaningCategory.SOCIAL_LIFE_MEANS_OF_COMMUNICATION
            self.MODES_OF_TRANSPORTATION = MeaningCategory.SOCIAL_LIFE_MODES_OF_TRANSPORTATION
            self.PLACES_FOR_TRANSPORTATION_USAGE = \
                MeaningCategory.SOCIAL_LIFE_PLACES_FOR_TRANSPORTATION_USAGE
            self.MEDIA = MeaningCategory.SOCIAL_LIFE_MEDIA
            self.WORKPLACE = MeaningCategory.SOCIAL_LIFE_WORKPLACE
            self.TITLES_AND_POSITIONS = MeaningCategory.SOCIAL_LIFE_TITLES_AND_POSITIONS
            self.OCCUPATION = MeaningCategory.SOCIAL_LIFE_OCCUPATION
            self.SOCIAL_EVENTS = MeaningCategory.SOCIAL_LIFE_SOCIAL_EVENTS
            self.SOCIAL_LIFE_STATUS = MeaningCategory.SOCIAL_LIFE_SOCIAL_LIFE_STATUS
            self.SOCIAL_ACTIVITIES = MeaningCategory.SOCIAL_LIFE_SOCIAL_ACTIVITIES
            self.TRANSPORTATION_USAGE = MeaningCategory.SOCIAL_LIFE_TRANSPORTATION_USAGE
            self.WORKPLACE_LIFE = MeaningCategory.SOCIAL_LIFE_WORKPLACE_LIFE
            self.LANGUAGE_ACTIVITIES = MeaningCategory.SOCIAL_LIFE_LANGUAGE_ACTIVITIES
            self.COMMUNICATION_ACTIVITIES = MeaningCategory.SOCIAL_LIFE_COMMUNICATION_ACTIVITIES
            self.GRAMMAR_AND_SPEECH = MeaningCategory.SOCIAL_LIFE_GRAMMAR_AND_SPEECH

    class __PROXY_ECONOMIC__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.ECONOMIC_ALL
            self.PEOPLE = MeaningCategory.ECONOMIC_PEOPLE
            self.PLACES = MeaningCategory.ECONOMIC_PLACES
            self.MEANS = MeaningCategory.ECONOMIC_MEANS
            self.PRODUCTS = MeaningCategory.ECONOMIC_PRODUCTS
            self.STATUS = MeaningCategory.ECONOMIC_STATUS
            self.ACTIVITIES = MeaningCategory.ECONOMIC_ACTIVITIES

    class __PROXY_EDUCATION__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.EDUCATION_ALL
            self.PEOPLE = MeaningCategory.EDUCATION_PEOPLE
            self.MAJORS_AND_SUBJECTS = MeaningCategory.EDUCATION_MAJORS_AND_SUBJECTS
            self.EDUCATIONAL_INSTITUTIONS = MeaningCategory.EDUCATION_EDUCATIONAL_INSTITUTIONS
            self.SCHOOL_FACILITIES = MeaningCategory.EDUCATION_SCHOOL_FACILITIES
            self.OBJECTS = MeaningCategory.EDUCATION_OBJECTS
            self.ACADEMIC_TERMS = MeaningCategory.EDUCATION_ACADEMIC_TERMS
            self.TEACHING_AND_LEARNING_ACTIVITIES = \
                MeaningCategory.EDUCATION_TEACHING_AND_LEARNING_ACTIVITIES
            self.ACADEMIC_ACTIVITIES = MeaningCategory.EDUCATION_ACADEMIC_ACTIVITIES

    class __PROXY_RELIGION__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.RELIGION_ALL
            self.TYPES_OF_RELIGION = MeaningCategory.RELIGION_TYPES_OF_RELIGION
            self.PLACES = MeaningCategory.RELIGION_PLACES
            self.PEOPLE = MeaningCategory.RELIGION_PEOPLE
            self.RELIGIOUS_WORDS = MeaningCategory.RELIGION_RELIGIOUS_WORDS
            self.MAJOR_FIGURES = MeaningCategory.RELIGION_MAJOR_FIGURES
            self.OBJECTS = MeaningCategory.RELIGION_OBJECTS
            self.PRACTICES = MeaningCategory.RELIGION_PRACTICES

    class __PROXY_CULTURE__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.CULTURE_ALL
            self.CULTURAL_ACTIVITY_PARTICIPANTS = \
                MeaningCategory.CULTURE_CULTURAL_ACTIVITY_PARTICIPANTS
            self.MUSIC = MeaningCategory.CULTURE_MUSIC
            self.FINE_ART = MeaningCategory.CULTURE_FINE_ART
            self.LITERATURE = MeaningCategory.CULTURE_LITERATURE
            self.ART = MeaningCategory.CULTURE_ART
            self.POP_CULTURE = MeaningCategory.CULTURE_POP_CULTURE
            self.TRADITIONAL_CULTURE = MeaningCategory.CULTURE_TRADITIONAL_CULTURE
            self.CULTURAL_ACTIVITY_PLACES = MeaningCategory.CULTURE_CULTURAL_ACTIVITY_PLACES
            self.CULTURAL_ACTIVITIES = MeaningCategory.CULTURE_CULTURAL_ACTIVITIES

    class __PROXY_POLITICS_AND_ADMINISTRATION__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.POLITICS_AND_ADMINISTRATION_ALL
            self.PUBLIC_INSTITUTIONS = \
                MeaningCategory.POLITICS_AND_ADMINISTRATION_PUBLIC_INSTITUTIONS
            self.JUDICIAL_AND_SECURITY_PERSONNEL = \
                MeaningCategory.POLITICS_AND_ADMINISTRATION_JUDICIAL_AND_SECURITY_PERSONNEL
            self.WEAPONS = MeaningCategory.POLITICS_AND_ADMINISTRATION_WEAPONS
            self.POLITICS_AND_SECURITY = \
                MeaningCategory.POLITICS_AND_ADMINISTRATION_POLITICS_AND_SECURITY
            self.POLITICAL_ACTS = MeaningCategory.POLITICS_AND_ADMINISTRATION_POLITICAL_ACTS
            self.LAW_AND_SECURITY_ACTS = \
                MeaningCategory.POLITICS_AND_ADMINISTRATION_LAW_AND_SECURITY_ACTS
            self.POLITICAL_AND_ADMINISTRATIVE_PERSONNEL = \
                MeaningCategory.POLITICS_AND_ADMINISTRATION_POLITICAL_AND_ADMINISTRATIVE_PERSONNEL

    class __PROXY_NATURE__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.NATURE_ALL
            self.TOPOGRAPHY = MeaningCategory.NATURE_TOPOGRAPHY
            self.SURFACE_OBJECTS = MeaningCategory.NATURE_SURFACE_OBJECTS
            self.CELESTIAL_BODIES = MeaningCategory.NATURE_CELESTIAL_BODIES
            self.NATURAL_RESOURCES = MeaningCategory.NATURE_NATURAL_RESOURCES
            self.DISASTERS = MeaningCategory.NATURE_DISASTERS
            self.WEATHER_AND_CLIMATE = MeaningCategory.NATURE_WEATHER_AND_CLIMATE

    class __PROXY_ANIMALS_AND_PLANTS__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.ANIMALS_AND_PLANTS_ALL
            self.ANIMALS = MeaningCategory.ANIMALS_AND_PLANTS_ANIMALS
            self.INSECTS = MeaningCategory.ANIMALS_AND_PLANTS_INSECTS
            self.PLANTS = MeaningCategory.ANIMALS_AND_PLANTS_PLANTS
            self.PARTS_OF_ANIMALS = MeaningCategory.ANIMALS_AND_PLANTS_PARTS_OF_ANIMALS
            self.PARTS_OF_PLANTS = MeaningCategory.ANIMALS_AND_PLANTS_PARTS_OF_PLANTS
            self.BEHAVIORS = MeaningCategory.ANIMALS_AND_PLANTS_BEHAVIORS
            self.SOUNDS = MeaningCategory.ANIMALS_AND_PLANTS_SOUNDS

    class __PROXY_CONCEPTS__(EnumProxyBase):
        def __init__(self, populate):
            super().__init__(populate)
            if not populate:
                return

            self.ALL = MeaningCategory.CONCEPTS_ALL
            self.SHAPE = MeaningCategory.CONCEPTS_SHAPE
            self.PROPERTY = MeaningCategory.CONCEPTS_PROPERTY
            self.SPEED = MeaningCategory.CONCEPTS_SPEED
            self.BRIGHTNESS = MeaningCategory.CONCEPTS_BRIGHTNESS
            self.TEMPERATURE = MeaningCategory.CONCEPTS_TEMPERATURE
            self.COLORS = MeaningCategory.CONCEPTS_COLORS
            self.NUMBERS = MeaningCategory.CONCEPTS_NUMBERS
            self.COUNTERS = MeaningCategory.CONCEPTS_COUNTERS
            self.AMOUNT = MeaningCategory.CONCEPTS_AMOUNT
            self.DEGREE = MeaningCategory.CONCEPTS_DEGREE
            self.ORDER = MeaningCategory.CONCEPTS_ORDER
            self.FREQUENCY = MeaningCategory.CONCEPTS_FREQUENCY
            self.TIME = MeaningCategory.CONCEPTS_TIME
            self.LOCATION_AND_DIRECTION = MeaningCategory.CONCEPTS_LOCATION_AND_DIRECTION
            self.AREA = MeaningCategory.CONCEPTS_AREA
            self.INSTRUCTIONS = MeaningCategory.CONCEPTS_INSTRUCTIONS
            self.CONNECTION = MeaningCategory.CONCEPTS_CONNECTION
            self.QUESTION_WORDS = MeaningCategory.CONCEPTS_QUESTION_WORDS
            self.PRONOUNS = MeaningCategory.CONCEPTS_PRONOUNS


    __HUMAN__: __PROXY_HUMAN__ = __PROXY_HUMAN__(False)
    __LIFE__: __PROXY_LIFE__ = __PROXY_LIFE__(False)
    __DIETARY__: __PROXY_DIETARY__ = __PROXY_DIETARY__(False)
    __CLOTHING__: __PROXY_CLOTHING__ = __PROXY_CLOTHING__(False)
    __HOME_LIFE__: __PROXY_HOME_LIFE__ = __PROXY_HOME_LIFE__(False)
    __SOCIAL_LIFE__: __PROXY_SOCIAL_LIFE__ = __PROXY_SOCIAL_LIFE__(False)
    __ECONOMIC__: __PROXY_ECONOMIC__ = __PROXY_ECONOMIC__(False)
    __EDUCATION__: __PROXY_EDUCATION__ = __PROXY_EDUCATION__(False)
    __RELIGION__: __PROXY_RELIGION__ = __PROXY_RELIGION__(False)
    __CULTURE__: __PROXY_CULTURE__ = __PROXY_CULTURE__(False)
    __POLITICS_AND_ADMINISTRATION__: __PROXY_POLITICS_AND_ADMINISTRATION__ = \
        __PROXY_POLITICS_AND_ADMINISTRATION__(False)
    __NATURE__: __PROXY_NATURE__ = __PROXY_NATURE__(False)
    __ANIMALS_AND_PLANTS__: __PROXY_ANIMALS_AND_PLANTS__ = __PROXY_ANIMALS_AND_PLANTS__(False)
    __CONCEPTS__: __PROXY_CONCEPTS__ = __PROXY_CONCEPTS__(False)


    @classmethod
    @property
    def HUMAN(cls):
        """Proxy for human meaning categories."""
        if not cls.__HUMAN__.__populated__:
            cls.__HUMAN__ = MeaningCategory.__PROXY_HUMAN__(True)
        return cls.__HUMAN__

    @classmethod
    @property
    def LIFE(cls):
        """Proxy for life meaning categories."""
        if not cls.__LIFE__.__populated__:
            cls.__LIFE__ = MeaningCategory.__PROXY_LIFE__(True)
        return cls.__LIFE__

    @classmethod
    @property
    def DIETARY(cls):
        """Proxy for dietary meaning categories."""
        if not cls.__DIETARY__.__populated__:
            cls.__DIETARY__ = MeaningCategory.__PROXY_DIETARY__(True)
        return cls.__DIETARY__

    @classmethod
    @property
    def CLOTHING(cls):
        """Proxy for clothing meaning categories."""
        if not cls.__CLOTHING__.__populated__:
            cls.__CLOTHING__ = MeaningCategory.__PROXY_CLOTHING__(True)
        return cls.__CLOTHING__

    @classmethod
    @property
    def HOME_LIFE(cls):
        """Proxy for home life meaning categories."""
        if not cls.__HOME_LIFE__.__populated__:
            cls.__HOME_LIFE__ = MeaningCategory.__PROXY_HOME_LIFE__(True)
        return cls.__HOME_LIFE__

    @classmethod
    @property
    def SOCIAL_LIFE(cls):
        """Proxy for social life meaning categories."""
        if not cls.__SOCIAL_LIFE__.__populated__:
            cls.__SOCIAL_LIFE__ = MeaningCategory.__PROXY_SOCIAL_LIFE__(True)
        return cls.__SOCIAL_LIFE__

    @classmethod
    @property
    def ECONOMIC(cls):
        """Proxy for economic meaning categories."""
        if not cls.__ECONOMIC__.__populated__:
            cls.__ECONOMIC__ = MeaningCategory.__PROXY_ECONOMIC__(True)
        return cls.__ECONOMIC__

    @classmethod
    @property
    def EDUCATION(cls):
        """Proxy for education meaning categories."""
        if not cls.__EDUCATION__.__populated__:
            cls.__EDUCATION__ = MeaningCategory.__PROXY_EDUCATION__(True)
        return cls.__EDUCATION__

    @classmethod
    @property
    def RELIGION(cls):
        """Proxy for religion meaning categories."""
        if not cls.__RELIGION__.__populated__:
            cls.__RELIGION__ = MeaningCategory.__PROXY_RELIGION__(True)
        return cls.__RELIGION__

    @classmethod
    @property
    def CULTURE(cls):
        """Proxy for culture meaning categories."""
        if not cls.__CULTURE__.__populated__:
            cls.__CULTURE__ = MeaningCategory.__PROXY_CULTURE__(True)
        return cls.__CULTURE__

    @classmethod
    @property
    def POLITICS_AND_ADMINISTRATION(cls):
        """Proxy for politics and administration meaning categories."""
        if not cls.__POLITICS_AND_ADMINISTRATION__.__populated__:
            cls.__POLITICS_AND_ADMINISTRATION__ = \
                MeaningCategory.__PROXY_POLITICS_AND_ADMINISTRATION__(True)
        return cls.__POLITICS_AND_ADMINISTRATION__

    @classmethod
    @property
    def NATURE(cls):
        """Proxy for nature meaning categories."""
        if not cls.__NATURE__.__populated__:
            cls.__NATURE__ = MeaningCategory.__PROXY_NATURE__(True)
        return cls.__NATURE__

    @classmethod
    @property
    def ANIMALS_AND_PLANTS(cls):
        """Proxy for animals and plants meaning categories."""
        if not cls.__ANIMALS_AND_PLANTS__.__populated__:
            cls.__ANIMALS_AND_PLANTS__ = MeaningCategory.__PROXY_ANIMALS_AND_PLANTS__(True)
        return cls.__ANIMALS_AND_PLANTS__

    @classmethod
    @property
    def CONCEPTS(cls):
        """Proxy for concept meaning categories."""
        if not cls.__CONCEPTS__.__populated__:
            cls.__CONCEPTS__ = MeaningCategory.__PROXY_CONCEPTS__(True)
        return cls.__CONCEPTS__
