A summary of enumeration types provided by the package.
Most of these types are expected parameter types for various functions in the [main](main.md)
and [scraper](scraper.md) modules.

Functions which expect any of the enumeration types below also accept their underlying string or integer
value, the enumeration name, or a string alias. The [methods and properties](#enumeration-methods)
available on all enumeration types are also detailed below.

### Classification

The word classification of a dictionary entry.
```python
class Classification:
    ALL = 'all'
    WORD = 'word'
    PHRASE = 'phrase'
    EXPRESSION = 'expression'
```

### MultimediaType

A type of multimedia file.
```python
class MultimediaType:
    ALL = 0
    PHOTO = 1
    ILLUSTRATION = 2
    VIDEO = 3
    ANIMATION = 4
    SOUND = 5
    NONE = 6
```

Aliases:
```bash
'all': 0
'photo': 1
'illustration': 2
'video': 3
'animation': 4
'sound': 5
'none': 6
```

### OriginType

The classification of a dictionary entry's origin.
```python
class OriginType:
    ALL = 'all'
    NATIVE = 'native'
    HANJA = 'chinese'
    LOANWORD = 'loanword'
    HYBRID = 'hybrid'
```

Aliases:
```bash
'hanja': 'chinese'
```

### PartOfSpeech

The Korean part of speech of a dictionary entry.
```python
class PartOfSpeech:
    ALL = 0
    NOUN = 1
    PRONOUN = 2
    NUMERAL = 3
    PARTICLE = 4
    VERB = 5
    ADJECTIVE = 6
    DETERMINER = 7
    ADVERB = 8
    INTERJECTION = 9
    AFFIX = 10
    BOUND_NOUN = 11
    AUXILIARY_VERB = 12
    AUXILIARY_ADJECTIVE = 13
    ENDING = 14
    NONE = 15
```

Aliases:
```bash
'all': 0
'noun': 1
'pronoun': 2
'numeral': 3
'particle': 4
'verb': 5
'adjective': 6
'determiner': 7
'adverb': 8
'interjection': 9
'affix': 10
'bound noun': 11
'bound_noun': 11
'auxiliary verb': 12
'auxiliary_verb': 12
'auxiliary adjective': 13
'auxiliary_adjective': 13
'ending': 14
'none': 15
```

### ResponseType

Descriptors for response types returned by the main module.
```python
class ResponseType:
    DEFINITION = 'dfn'
    ERROR = 'error'
    EXAMPLE = 'exam'
    IDIOM_PROVERB = 'ip'
    VIEW = 'view'
    WORD = 'word'
```

### ScrapedResponseType

Descriptors for response types returned by the scraper module.
```python
class ScrapedResponseType:
    DEFINITION = 'scraped_dfn'
    EXAMPLE = 'scraped_exam'
    IDIOM_PROVERB = 'scraped_ip'
    VIEW = 'scraped_view'
    WORD = 'scraped_word'
    WORD_OF_THE_DAY = 'word_of_the_day'
```

### ScraperSearchTarget

The target of the search query for a scraper request; what to search by.
```python
class ScraperSearchTarget:
    HEADWORD = 1
    DEFINITION = 2
    EXAMPLE = 3
    ORIGINAL_LANGUAGE = 4
    PRONUNCIATION = 5
    APPLICATION = 6
    APPLICATION_SHORTHAND = 7
    IDIOM = 8
    PROVERB = 9
    REFERENCE_INFO = 10
    TRANSLATION_HEADWORD = 11
    TRANSLATION_DEFINITION = 12
    TRANSLATION_IDIOM_PROVERB= 13
```

Aliases:
```bash
'headword': 1
'definition': 2
'example': 3
'original language': 4
'original_language': 4
'pronunciation': 5
'application': 6
'application shorthand': 7
'application_shorthand': 7
'idiom': 8
'proverb': 9
'reference info': 10
'reference_info': 10
'translation_headword': 11
'translation_definition': 12
'translation_idiom_proverb': 13
```

### ScraperTargetLanguage

A target original language to search by for a scraper request.
```python
class ScraperTargetLanguage:
    ALL = 0
    NATIVE_WORD = 1
    SINO_KOREAN = 2
    UNKNOWN = 3
    ENGLISH = 4
    GREEK = 5
    DUTCH = 6
    NORWEGIAN = 7
    GERMAN = 8
    LATIN = 9
    RUSSIAN = 10
    ROMANIAN = 11
    MALAY = 13
    MONGOLIAN = 14
    VIETNAMESE = 17
    BULGARIAN = 18
    SANSKRIT = 19
    SERBO_CROATIAN = 20
    SWEDISH = 22
    ARABIC = 23
    SPANISH = 25
    ITALIAN = 28
    INDONESIAN = 29
    JAPANESE = 30
    CHINESE = 31
    CZECH = 32
    THAI = 36
    TURKISH = 37
    PERSIAN = 39
    PORTUGUESE = 40
    POLISH = 41
    FRENCH = 42
    HUNGARIAN = 45
    HEBREW = 46
    HINDI = 47
    OTHER = 48
```

Aliases:
```bash
'all': 0
'native_word': 1
'sino-korean': 2
'sino_korean': 2
'unknown': 3
'english': 4
'greek': 5
'dutch': 6
'norwegian': 7
'german': 8
'latin': 9
'russian': 10
'romanian': 11
'malay': 13
'mongolian': 14
'vietnamese': 17
'bulgarian': 18
'sanskrit': 19
'serbo-croatian': 20
'serbo_croatian': 20
'swedish': 22
'arabic': 23
'spanish': 25
'italian': 28
'indonesian': 29
'japanese': 30
'chinese': 31
'czech': 32
'thai': 36
'turkish': 37
'persian': 39
'portuguese': 40
'polish': 41
'french': 42
'hungarian': 45
'hebrew': 46
'hindi': 47
'other': 48
```

### ScraperTranslationLanguage

A language for which translations should be included during a scraper request.
```python
class ScraperTranslationLanguage:
    ALL = 0
    ENGLISH = 1
    JAPANESE = 2
    FRENCH = 3
    SPANISH = 4
    ARABIC = 5
    MONGOLIAN = 6
    VIETNAMESE = 7
    THAI = 8
    INDONESIAN = 9
    RUSSIAN = 10
    CHINESE = 11
```

Aliases:
```bash
'all': 0
'english': 1
'japanese': 2
'french': 3
'spanish': 4
'arabic': 5
'mongolian': 6
'vietnamese': 7
'thai': 8
'indonesian': 9
'russian': 10
'chinese': 11
```

### ScraperVocabularyLevel

The vocabulary level of a dictionary entry, for use in a scraper request.
```python
class ScraperVocabularyLevel:
    ALL = 'all'
    BEGINNER = 'level1'
    INTERMEDIATE = 'level2'
    ADVANCED = 'level3'
    NONE = 'none'
```

Aliases:
```bash
'beginner': 'level1'
'intermediate': 'level2'
'advanced': 'level3'
```

### SearchMethod

The method to use when searching.

- `'exact'`: Returns entries that are an exact match of the query.
- `'include'`: Returns entries that include the query.
- `'start'`: Returns entries that start with the query.
- `'end'`: Returns entries that end with the query.

```python
class SearchMethod:
    EXACT = 'exact'
    INCLUDE = 'include'
    START = 'start'
    END = 'end'
```

### SearchTarget

The target of the search query; what to search by.
```python
class SearchTarget:
    HEADWORD = 1
    DEFINITION = 2
    EXAMPLE = 3
    ORIGINAL_LANGUAGE = 4
    PRONUNCIATION = 5
    APPLICATION = 6
    APPLICATION_SHORTHAND = 7
    IDIOM = 8
    PROVERB = 9
    REFERENCE_INFO = 10
```

Aliases:
```bash
'headword': 1
'definition': 2
'example': 3
'original language': 4
'original_language': 4
'pronunciation': 5
'application': 6
'application shorthand': 7
'application_shorthand': 7
'idiom': 8
'proverb': 9
'reference info': 10
'reference_info': 10
```

### SearchType

The type of search to perform.
```python
class SearchType:
    IDIOM_PROVERB = 'ip'
    DEFINITION = 'dfn'
    EXAMPLE = 'exam'
    WORD = 'word'
```

Aliases:
```bash
'idiom/proverb': 'ip'
'idiom_proverb': 'ip'
'definition': 'dfn'
'example': 'exam'
```

### SemanticCategory

A semantic category which a dictionary entry may belong to.

```python
class SemanticCategory:
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
```

Aliases:

```bash
'전체': 0
'인간 > 전체': 1
'인간 > 사람의 종류': 2
'인간 > 신체 부위': 3
'인간 > 체력 상태': 4
'인간 > 생리 현상': 5
'인간 > 감각': 6
'인간 > 감정': 7
'인간 > 성격': 8
'인간 > 태도': 9
'인간 > 용모': 10
'인간 > 능력': 11
'인간 > 신체 변화': 12
'인간 > 신체 행위': 13
'인간 > 신체에 가하는 행위': 14
'인간 > 인지 행위': 15
'인간 > 소리': 16
'인간 > 신체 내부 구성': 17
'삶 > 전체': 18
'삶 > 삶의 상태': 19
'삶 > 삶의 행위': 20
'삶 > 일상 행위': 21
'삶 > 친족 관계': 22
'삶 > 가족 행사': 23
'삶 > 여가 도구': 24
'삶 > 여가 시설': 25
'삶 > 여가 활동': 26
'삶 > 병과 증상': 27
'삶 > 치료 행위': 28
'삶 > 치료 시설': 29
'삶 > 약품류': 30
'식생활 > 전체': 31
'식생활 > 음식': 32
'식생활 > 채소': 33
'식생활 > 곡류': 34
'식생활 > 과일': 35
'식생활 > 음료': 36
'식생활 > 식재료': 37
'식생활 > 조리 도구': 38
'식생활 > 식생활 관련 장소': 39
'식생활 > 맛': 40
'식생활 > 식사 및 조리 행위': 41
'의생활 > 전체': 42
'의생활 > 옷 종류': 43
'의생활 > 옷감': 44
'의생활 > 옷의 부분': 45
'의생활 > 모자, 신발, 장신구': 46
'의생활 > 의생활 관련 장소': 47
'의생활 > 의복 착용 상태': 48
'의생활 > 의복 착용 행위': 49
'의생활 > 미용 행위': 50
'주생활 > 전체': 51
'주생활 > 건물 종류': 52
'주생활 > 주거 형태': 53
'주생활 > 주거 지역': 54
'주생활 > 생활 용품': 55
'주생활 > 주택 구성': 56
'주생활 > 주거 상태': 57
'주생활 > 주거 행위': 58
'주생활 > 가사 행위': 59
'사회 생활 > 전체': 60
'사회 생활 > 인간관계': 61
'사회 생활 > 소통 수단': 62
'사회 생활 > 교통 수단': 63
'사회 생활 > 교통 이용 장소': 64
'사회 생활 > 매체': 65
'사회 생활 > 직장': 66
'사회 생활 > 직위': 67
'사회 생활 > 직업': 68
'사회 생활 > 사회 행사': 69
'사회 생활 > 사회 생활 상태': 70
'사회 생활 > 사회 활동': 71
'사회 생활 > 교통 이용 행위': 72
'사회 생활 > 직장 생활': 73
'사회 생활 > 언어 행위': 74
'사회 생활 > 통신 행위': 75
'사회 생활 > 말': 76
'경제 생활 > 전체': 77
'경제 생활 > 경제 행위 주체': 78
'경제 생활 > 경제 행위 장소': 79
'경제 생활 > 경제 수단': 80
'경제 생활 > 경제 산물': 81
'경제 생활 > 경제 상태': 82
'경제 생활 > 경제 행위': 83
'교육 > 전체': 84
'교육 > 교수 학습 주체': 85
'교육 > 전공과 교과목': 86
'교육 > 교육 기관': 87
'교육 > 학교 시설': 88
'교육 > 학습 관련 사물': 89
'교육 > 학문 용어': 90
'교육 > 교수 학습 행위': 91
'교육 > 학문 행위': 92
'종교 > 전체': 93
'종교 > 종교 유형': 94
'종교 > 종교 활동 장소': 95
'종교 > 종교인': 96
'종교 > 종교어': 97
'종교 > 신앙 대상': 98
'종교 > 종교 활동 도구': 99
'종교 > 종교 행위': 100
'문화 > 전체': 101
'문화 > 문화 활동 주체': 102
'문화 > 음악': 103
'문화 > 미술': 104
'문화 > 문학': 105
'문화 > 예술': 106
'문화 > 대중 문화': 107
'문화 > 전통 문화': 108
'문화 > 문화 생활 장소': 109
'문화 > 문화 활동': 110
'정치와 행정 > 전체': 111
'정치와 행정 > 공공 기관': 112
'정치와 행정 > 사법 및 치안 주체': 113
'정치와 행정 > 무기': 114
'정치와 행정 > 정치 및 치안 상태': 115
'정치와 행정 > 정치 및 행정 행위': 116
'정치와 행정 > 사법 및 치안 행위': 117
'정치와 행정 > 정치 및 행정 주체': 118
'자연 > 전체': 119
'자연 > 지형': 120
'자연 > 지표면 사물': 121
'자연 > 천체': 122
'자연 > 자원': 123
'자연 > 재해': 124
'자연 > 기상 및 기후': 125
'동식물 > 전체': 126
'동식물 > 동물류': 127
'동식물 > 곤충류': 128
'동식물 > 식물류': 129
'동식물 > 동물의 부분': 130
'동식물 > 식물의 부분': 131
'동식물 > 동식물 행위': 132
'동식물 > 동물 소리': 133
'개념 > 전체': 134
'개념 > 모양': 135
'개념 > 성질': 136
'개념 > 속도': 137
'개념 > 밝기': 138
'개념 > 온도': 139
'개념 > 색깔': 140
'개념 > 수': 141
'개념 > 세는 말': 142
'개념 > 양': 143
'개념 > 정도': 144
'개념 > 순서': 145
'개념 > 빈도': 146
'개념 > 시간': 147
'개념 > 위치 및 방향': 148
'개념 > 지역': 149
'개념 > 지시': 150
'개념 > 접속': 151
'개념 > 의문': 152
'개념 > 인칭': 153
'all': 0
'human > all': 1
'human > types of people': 2
'human > body parts': 3
'human > health status': 4
'human > physiological phenomena': 5
'human > senses': 6
'human > emotion': 7
'human > personality': 8
'human > attitude': 9
'human > features': 10
'human > ability': 11
'human > physical changes': 12
'human > physical activities': 13
'human > actions done to the body': 14
'human > cognitive behavior': 15
'human > sound': 16
'human > inner parts of the body': 17
'life > all': 18
'life > state of being': 19
'life > life activities': 20
'life > daily activities': 21
'life > kinship': 22
'life > family events': 23
'life > leisure tools': 24
'life > leisure facilities': 25
'life > leisure activities': 26
'life > diseases and symptoms': 27
'life > medical activities': 28
'life > medical facilities': 29
'life > medicine': 30
'dietary > all': 31
'dietary > food types': 32
'dietary > vegetables': 33
'dietary > grain': 34
'dietary > fruit': 35
'dietary > beverages': 36
'dietary > food ingredients': 37
'dietary > cooking appliances': 38
'dietary > eating places': 39
'dietary > taste': 40
'dietary > eating and cooking activities': 41
'clothing habits > all': 42
'clothing habits > types of clothing': 43
'clothing habits > fabric': 44
'clothing habits > parts of clothing': 45
'clothing habits > hats, shoes, accessories': 46
'clothing habits > places related to clothing': 47
'clothing habits > places related to clothing habits': 47
'clothing habits > state of clothing': 48
'clothing habits > activities related to clothing': 49
'clothing habits > activities related to wearing clothing': 49
'clothing habits > beauty and health': 50
'home life > all': 51
'home life > building types': 52
'home life > type of housing': 53
'home life > residential area': 54
'home life > household items': 55
'home life > housing structure': 56
'home life > residential status': 57
'home life > residential activities': 58
'home life > housing activities': 58
'home life > residential chores': 59
'home life > household chores': 59
'social life > all': 60
'social life > human relationships': 61
'social life > means of communication': 62
'social life > modes of transportation': 63
'social life > places of transportation usage': 64
'social life > places for transportation usage': 64
'social life > media': 65
'social life > workplace': 66
'social life > work title/position': 67
'social life > titles and positions': 67
'social life > occupation': 68
'social life > social events': 69
'social life > social life status': 70
'social life > conditions of social life': 70
'social life > social activities': 71
'social life > transportation usage': 72
'social life > workplace life': 73
'social life > life in the workplace': 73
'social life > language activities': 74
'social life > linguistic activities': 74
'social life > communication activities': 75
'social life > all communication activities': 75
'social life > grammar and speech': 76
'economic activities > all': 77
'economic activities > people': 78
'economic activities > economic agents': 78
'economic activities > places': 79
'economic activities > economic places': 79
'economic activities > places of economic activity': 79
'economic activities > means': 80
'economic activities > economic means': 80
'economic activities > products': 81
'economic activities > commercial products': 81
'economic activities > status': 82
'economic activities > economic situation': 82
'economic activities > activities': 83
'economic activities > economic activities': 83
'education > all': 84
'education > people': 85
'education > education personnel & students': 85
'education > majors & subjects': 86
'education > educational institutions': 87
'education > school facilities': 88
'education > objects': 89
'education > objects related to education': 89
'education > academic terms': 90
'education > teaching and learning activities': 91
'education > academic activities': 92
'religion > all': 93
'religion > types of religion': 94
'religion > places': 95
'religion > places for religious activities': 95
'religion > people': 96
'religion > religious people': 96
'religion > religious words': 97
'religion > religious language': 97
'religion > major figures': 98
'religion > major figures of religions': 98
'religion > objects': 99
'religion > objects for religious activities': 99
'religion > practices': 100
'religion > religious practices': 100
'culture > all': 101
'culture > cultural activity participants': 102
'culture > participants in cultural activities': 102
'culture > music': 103
'culture > fine art': 104
'culture > fine and/or visual art': 104
'culture > literature': 105
'culture > art': 106
'culture > the arts': 106
'culture > pop culture': 107
'culture > traditional culture': 108
'culture > cultural activity places': 109
'culture > places of cultural activities': 109
'culture > cultural activities': 110
'politics and administration > all': 111
'politics and administration > public institutions': 112
'politics and administration > judicial & security personnel': 113
'politics and administration > judicial and security personnel': 113
'politics and administration > weapons': 114
'politics and administration > politics & security': 115
'politics and administration > politics and security': 115
'politics and administration > political acts': 116
'politics and administration > political and administrative activity': 116
'politics and administration > law & security': 117
'politics and administration > law and security acts': 117
'politics and administration > political and administrative personnel': 118
'politics and administration > all people involved in political activity': 118
'nature > all': 119
'nature > topography': 120
'nature > geographical topography': 120
'nature > surface objects': 121
'nature > geographical surface objects': 121
'nature > celestial bodies': 122
'nature > extraterrestrial bodies': 122
'nature > natural resources': 123
'nature > disasters': 124
'nature > weather and climate': 125
'animals and plants > all': 126
'animals and plants > animals': 127
'animals and plants > insects': 128
'animals and plants > plants': 129
'animals and plants > parts of animals': 130
'animals and plants > parts of plants': 131
'animals and plants > behaviors': 132
'animals and plants > actions and/or stages of animals and plants': 132
'animals and plants > sounds': 133
'animals and plants > animal sounds': 133
'concepts > all': 134
'concepts > shape': 135
'concepts > property': 136
'concepts > speed': 137
'concepts > brightness': 138
'concepts > temperature': 139
'concepts > colors': 140
'concepts > number': 141
'concepts > numbers': 141
'concepts > counters': 142
'concepts > counting words': 142
'concepts > amount': 143
'concepts > degree': 144
'concepts > order': 145
'concepts > frequency': 146
'concepts > time': 147
'concepts > location and direction': 148
'concepts > area': 149
'concepts > instructions': 150
'concepts > connection': 151
'concepts > question words': 152
'concepts > pronouns': 153
'concepts > person nouns and pronouns': 153
```

### SortMethod

A sorting method to use for search results.
```python
class SortMethod:
    ALPHABETICAL = 'dict'
    POPULAR = 'popular'
```

Aliases:
```bash
'alphabetical': 'dict'
```

### SubjectCategory

A subject category (themes and situations) which a dictionary entry may belong to.

```python
class SubjectCategory:
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
```

Aliases:

```bash
'전체': 0
'인사하기': 1
'소개하기 (자기소개)': 2
'소개하기 (가족소개)': 3
'개인 정보 교환하기 (초급)': 4
'위치 표현하기': 5
'길찾기': 6
'교통 이용하기 (초금)': 7
'물건 사기 (초금)': 8
'음식 주문하기': 9
'요리 설명하기 (초금)': 10
'시간 표현하기': 11
'날짜 표현하기': 12
'요일 표현하기': 13
'날씨와 계절 (초금)': 14
'하루 생활': 15
'학교생활 (초금)': 16
'한국 생활 (초금)': 17
'약속하기': 18
'전화하기': 19
'감사하기': 20
'사과하기': 21
'여행 (초금)': 22
'주말 및 휴가 (초금)': 23
'취미 (초금)': 24
'가족 행사 (초금)': 25
'건강 (초금)': 26
'병원 이용하기': 27
'약국 이용하기': 28
'약국 이용하기 (초금)': 28
'공공 기관 이용하기 (도서관)': 29
'공공 기관 이용하기 (우체국)': 30
'공공 기관 이용하기 (출입국 관리 사무소)': 31
'초대와 방문 (초금)': 32
'집 구하기 (초금)': 33
'집안일 (초금)': 34
'감정, 기분 표현하기 (초금)': 35
'성격 표현하기 (초금)': 36
'복장 표현하기 (초금)': 37
'외모 표현하기 (초금)': 38
'영화 보기': 39
'개인 정보 교환하기 (중급)': 40
'교통 이용하기 (중급)': 41
'지리 정보 (중급)': 42
'물건 사기 (중급)': 43
'음식 설명하기': 44
'요리 설명하기 (중급)': 45
'날씨와 계절 (중급)': 46
'학교생활 (중급)': 47
'한국 생활 (중급)': 48
'직업과 진로 (중급)': 49
'직장 생활 (중급)': 50
'여행 (중급)': 51
'주말 및 휴가 (중급)': 52
'취미 (중급)': 53
'가족 행사 (중급)': 54
'가족 행사 (명절)': 55
'건강 (중급)': 56
'공공기관 이용하기': 57
'초대와 방문 (중급)': 58
'집 구하기 (중급)': 59
'집안일 (중급)': 60
'감정, 기분 표현하기 (중급)': 61
'성격 표현하기 (중급)': 62
'복장 표현하기 (중급)': 63
'외모 표현하기 (중급)': 64
'공연과 감상': 65
'대중 매체': 66
'컴퓨터와 인터넷 (중급)': 67
'사건, 사고, 재해 기술하기': 68
'환경 문제 (중급)': 69
'문화 비교하기': 70
'인간관계 (중급)': 71
'한국의 문학': 72
'문제 해결하기 (분실 및 고장)': 73
'실수담 말하기': 74
'연애와 결혼': 75
'언어 (중급)': 76
'지리 정보 (고급)': 77
'경제∙경영': 78
'경제-경영': 78
'식문화': 79
'기후': 80
'교육': 81
'직업과 진로 (고급)': 82
'직장 생활 (고급)': 83
'여가 생활': 84
'보건과 의료': 85
'주거 생활': 86
'심리': 87
'외양': 88
'대중문화': 89
'컴퓨터와 인터넷 (고급)': 90
'사회 문제': 91
'환경 문제 (고급)': 92
'사회 제도': 93
'문화 차이': 94
'인간관계 (고급)': 95
'예술': 96
'건축': 97
'과학과 기술': 98
'법': 99
'스포츠': 100
'언론': 101
'언어 (고급)': 102
'역사': 103
'정치': 104
'종교': 105
'철학∙윤리': 106
'철학-윤리': 106
'all': 0
'greeting': 1
'introducing oneself': 2
'introducing (introducing oneself)': 2
'introducing family': 3
'introducing (introducing family)': 3
'exchanging personal information (elementary)': 4
'describing location': 5
'directions': 6
'using transportation (elementary)': 7
'purchasing goods (elementary)': 8
'ordering food': 9
'describing a dish (elementary)': 10
'describing dishes (elementary)': 10
'expressing time': 11
'expressing date': 12
'expressing day of the week': 13
'weather and season (elementary)': 14
'daily life': 15
'school life (elementary)': 16
'life in korea (elementary)': 17
'making promises': 18
'making a promise': 18
'making phone calls': 19
'making a phone call': 19
'expressing gratitude': 20
'apologizing': 21
'travel (elementary)': 22
'weekends and holidays (elementary)': 23
'hobby (elementary)': 24
'hobbies (elementary)': 24
'family events (elementary)': 25
'health (elementary)': 26
'using the hospital': 27
'using a pharmacy': 28
'using the pharmacy': 28
'using the library': 29
'using public institutions (library)': 29
'using the post office': 30
'using public institutions (post office)': 30
'using the immigration office': 31
'using public institutions (immigration office)': 31
'inviting and visiting (elementary)': 32
'finding a house (elementary)': 33
'housework (elementary)': 34
'expressing emotions (elementary)': 35
'expressing emotion/feelings (elementary)': 35
'describing personality (elementary)': 36
'describing clothes (elementary)': 37
'describing physical features (elementary)': 38
'watching movies': 39
'watching a movie': 39
'exchanging personal information (intermediate)': 40
'using transportation (intermediate)': 41
'geological information (intermediate)': 42
'purchasing goods (intermediate)': 43
'describing food': 44
'describing a dish (intermediate)': 45
'describing dishes (intermediate)': 45
'weather and season (intermediate)': 46
'school life (intermediate)': 47
'life in korea (intermediate)': 48
'jobs and careers (intermediate)': 49
'occupation & future path (intermediate)': 49
'workplace life (intermediate)': 50
'life in the workplace (intermediate)': 50
'travel (intermediate)': 51
'weekends and holidays (intermediate)': 52
'hobby (intermediate)': 53
'hobbies (intermediate)': 53
'family events (intermediate)': 54
'family events during holidays': 55
'family events (during national holidays)': 55
'health (intermediate)': 56
'using public institutions': 57
'using public institutions (library, post office, etc.)': 57
'inviting and visiting (intermediate)': 58
'finding a house (intermediate)': 59
'housework (intermediate)': 60
'expressing emotions (intermediate)': 61
'expressing emotion/feelings (intermediate)': 61
'describing personality (intermediate)': 62
'describing clothes (intermediate)': 63
'describing physical features (intermediate)': 64
'performance & appreciation': 65
'performances and appreciation': 65
'mass media': 66
'computer & internet (intermediate)': 67
'computers and the internet (intermediate)': 67
'describing events and disasters': 68
'describing events, accidents, disasters': 68
'environmental issues (intermediate)': 69
'comapring cultures': 70
'human relationships (intermediate)': 71
'korean literature': 72
'solving problems': 73
'solving problems (loss or malfunction)': 73
'talking about mistakes': 74
"talking about one's mistakes": 74
'dating and marriage': 75
'dating and getting married': 75
'language (intermediate)': 76
'geological information (advanced)': 77
'economics and administration': 78
'economics and business administration': 78
'dietary culture': 79
'climate': 80
'education': 81
'jobs and careers (advanced)': 82
'occupation & future path (advanced)': 82
'workplace life (advanced)': 83
'life in the workplace (advanced)': 83
'hobby (advanced)': 84
'hobbies (advanced)': 84
'health and medical treatment': 85
'residential area': 86
'psychology': 87
'mentality': 87
'appearance': 88
'pop culture': 89
'computer & internet (advanced)': 90
'computers and the internet (advanced)': 90
'social issues': 91
'environmental issues (advanced)': 92
'social system': 93
'cultural differences': 94
'human relationships (advanced)': 95
'art': 96
'the arts': 96
'architecture': 97
'science & technology': 98
'science and technology': 98
'law': 99
'sports': 100
'press': 101
'language (advanced)': 102
'history': 103
'politics': 104
'religion': 105
'philosophy, ethics': 106
'philosophy and ethics': 106
```

### TargetLanguage

A target original language to search by.
```python
class TargetLanguage:
    ALL = 0
    NATIVE_WORD = 1
    SINO_KOREAN = 2
    UNKNOWN = 3
    ENGLISH = 4
    GREEK = 5
    DUTCH = 6
    NORWEGIAN = 7
    GERMAN = 8
    LATIN = 9
    RUSSIAN = 10
    ROMANIAN = 11
    MAORI = 12
    MALAY = 13
    MONGOLIAN = 14
    BASQUE = 15
    BURMESE = 16
    VIETNAMESE = 17
    BULGARIAN = 18
    SANSKRIT = 19
    SERBO_CROATIAN = 20
    SWAHILI = 21
    SWEDISH = 22
    ARABIC = 23
    IRISH = 24
    SPANISH = 25
    UZBEK = 26
    UKRAINIAN = 27
    ITALIAN = 28
    INDONESIAN = 29
    JAPANESE = 30
    CHINESE = 31
    CZECH = 32
    CAMBODIAN = 33
    QUECHUA = 34
    TAGALOG = 35
    THAI = 36
    TURKISH = 37
    TIBETAN = 38
    PERSIAN = 39
    PORTUGUESE = 40
    POLISH = 41
    FRENCH = 42
    PROVENCAL = 43
    FINNISH = 44
    HUNGARIAN = 45
    HEBREW = 46
    HINDI = 47
    OTHER = 48
    DANISH = 49
```

Aliases:
```bash
'all': 0
'native_word': 1
'sino-korean': 2
'sino_korean': 2
'unknown': 3
'english': 4
'greek': 5
'dutch': 6
'norwegian': 7
'german': 8
'latin': 9
'russian': 10
'romanian': 11
'maori': 12
'malay': 13
'mongolian': 14
'basque': 15
'burmese': 16
'vietnamese': 17
'bulgarian': 18
'sanskrit': 19
'serbo-croatian': 20
'serbo_croatian': 20
'swahili': 21
'swedish': 22
'arabic': 23
'irish': 24
'spanish': 25
'uzbek': 26
'ukrainian': 27
'italian': 28
'indonesian': 29
'japanese': 30
'chinese': 31
'czech': 32
'cambodian': 33
'quechua': 34
'tagalog': 35
'thai': 36
'turkish': 37
'tibetan': 38
'persian': 39
'portuguese': 40
'polish': 41
'french': 42
'provencal': 43
'finnish': 44
'hungarian': 45
'hebrew': 46
'hindi': 47
'other': 48
'danish': 49
```

### TranslationLanguage

A language for which translations should be included.
```python
class TranslationLanguage:
    ALL = 0
    ENGLISH = 1
    JAPANESE = 2
    FRENCH = 3
    SPANISH = 4
    ARABIC = 5
    MONGOLIAN = 6
    VIETNAMESE = 7
    THAI = 8
    INDONESIAN = 9
    RUSSIAN = 10
```

Aliases:
```bash
'all': 0
'english': 1
'japanese': 2
'french': 3
'spanish': 4
'arabic': 5
'mongolian': 6
'vietnamese': 7
'thai': 8
'indonesian': 9
'russian': 10
```

### VocabularyLevel

The vocabulary level of a dictionary entry.
```python
class VocabularyLevel:
    ALL = 'all'
    BEGINNER = 'level1'
    INTERMEDIATE = 'level2'
    ADVANCED = 'level3'
```

Aliases:
```bash
'beginner': 'level1'
'intermediate': 'level2'
'advanced': 'level3'
```

## Enumeration Methods

All of the enumeration types in the package define the following:

### aliases

A property that allows access to enumeration aliases via a read-only dictionary.
These aliases, which are documented under each of the types above, can be used
with [`get`](#get) to retrieve an enumeration value.

```python
@property
@staticmethod
def aliases() -> Mapping: ...
```

### get

Returns the enumeration instance associated with a string or integer, or 
`default` if the value is not associated with any enumeration value.

If an enumeration value of the same type is used as the `key`, that
enumeration value is returned.

A string key can be the name of an enumeration value, an [alias](#aliases), or
the value of the enumeration in the case of string enumerations.

```python
@staticmethod
def get(key: EnumInstance | str | int, default: T = None) -> EnumType | T: ...
```

### get_value

Returns the enumeration value associated with a string or integer, or
`default` if the value is not associated with any enumeration value.

If an enumeration value of the same type is used as the `key`, the value associated with
that same enumeration value is returned.

Accepts the same `key` values as [`get`](#get) and returns either a string
or an integer depending on the underlying type of the enumeration type.

```python
@staticmethod
def get_value(key: EnumInstance | str | int, default: T = None) -> int | str | T: ...
```
