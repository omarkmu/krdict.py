The `SubjectCategory` class provided by `krdict` acts as a proxy
for an underlying enumeration class, to allow nested indexing operations.

This means that `SubjectCategory.ELEMENTARY.GREETING`, `SubjectCategory['ELEMENTARY_GREETING']`,
and `SubjectCategory(1)` all map to `<SubjectCategory.ELEMENTARY_GREETING: 1>`.

The `enum` property can be used to access the underlying enumeration class.

---

## Enumeration Values

The following non-standard syntax represents access via indexing.

```python
class SubjectCategory:
    ALL = 0
    ELEMENTARY.GREETING = 1
    ELEMENTARY.INTRODUCING_ONESELF = 2
    ELEMENTARY.INTRODUCING_FAMILY = 3
    ELEMENTARY.EXCHANGING_PERSONAL_INFORMATION = 4
    ELEMENTARY.DESCRIBING_LOCATION = 5
    ELEMENTARY.DIRECTIONS = 6
    ELEMENTARY.USING_TRANSPORTATION = 7
    ELEMENTARY.PURCHASING_GOODS = 8
    ELEMENTARY.ORDERING_FOOD = 9
    ELEMENTARY.DESCRIBING_DISHES = 10
    ELEMENTARY.EXPRESSING_TIME = 11
    ELEMENTARY.EXPRESSING_DATE = 12
    ELEMENTARY.EXPRESSING_DAY_OF_THE_WEEK = 13
    ELEMENTARY.WEATHER_AND_SEASON = 14
    ELEMENTARY.DAILY_LIFE = 15
    ELEMENTARY.SCHOOL_LIFE = 16
    ELEMENTARY.LIFE_IN_KOREA = 17
    ELEMENTARY.MAKING_PROMISES = 18
    ELEMENTARY.MAKING_PHONE_CALLS = 19
    ELEMENTARY.EXPRESSING_GRATITUDE = 20
    ELEMENTARY.APOLOGIZING = 21
    ELEMENTARY.TRAVEL = 22
    ELEMENTARY.WEEKENDS_AND_HOLIDAYS = 23
    ELEMENTARY.HOBBIES = 24
    ELEMENTARY.FAMILY_EVENTS = 25
    ELEMENTARY.HEALTH = 26
    ELEMENTARY.USING_THE_HOSPITAL = 27
    ELEMENTARY.USING_THE_PHARMACY = 28
    ELEMENTARY.USING_THE_LIBRARY = 29
    ELEMENTARY.USING_THE_POST_OFFICE = 30
    ELEMENTARY.USING_THE_IMMIGRATION_OFFICE = 31
    ELEMENTARY.INVITING_AND_VISITING = 32
    ELEMENTARY.FINDING_A_HOUSE = 33
    ELEMENTARY.HOUSEWORK = 34
    ELEMENTARY.EXPRESSING_EMOTIONS = 35
    ELEMENTARY.DESCRIBING_PERSONALITY = 36
    ELEMENTARY.DESCRIBING_CLOTHES = 37
    ELEMENTARY.DESCRIBING_PHYSICAL_FEATURES = 38
    ELEMENTARY.WATCHING_MOVIES = 39
    INTERMEDIATE.EXCHANGING_PERSONAL_INFORMATION = 40
    INTERMEDIATE.USING_TRANSPORTATION = 41
    INTERMEDIATE.GEOLOGICAL_INFORMATION = 42
    INTERMEDIATE.PURCHASING_GOODS = 43
    INTERMEDIATE.DESCRIBING_FOOD = 44
    INTERMEDIATE.DESCRIBING_DISHES = 45
    INTERMEDIATE.WEATHER_AND_SEASON = 46
    INTERMEDIATE.SCHOOL_LIFE = 47
    INTERMEDIATE.LIFE_IN_KOREA = 48
    INTERMEDIATE.JOBS_AND_CAREERS = 49
    INTERMEDIATE.WORKPLACE_LIFE = 50
    INTERMEDIATE.TRAVEL = 51
    INTERMEDIATE.WEEKENDS_AND_HOLIDAYS = 52
    INTERMEDIATE.HOBBIES = 53
    INTERMEDIATE.FAMILY_EVENTS = 54
    INTERMEDIATE.FAMILY_EVENTS_DURING_HOLIDAYS = 55
    INTERMEDIATE.HEALTH = 56
    INTERMEDIATE.USING_PUBLIC_INSTITUTIONS = 57
    INTERMEDIATE.INVITING_AND_VISITING = 58
    INTERMEDIATE.FINDING_A_HOUSE = 59
    INTERMEDIATE.HOUSEWORK = 60
    INTERMEDIATE.EXPRESSING_EMOTIONS = 61
    INTERMEDIATE.DESCRIBING_PERSONALITY = 62
    INTERMEDIATE.DESCRIBING_CLOTHES = 63
    INTERMEDIATE.DESCRIBING_PHYSICAL_FEATURES = 64
    INTERMEDIATE.PERFORMANCES_AND_APPRECIATION = 65
    INTERMEDIATE.MASS_MEDIA = 66
    INTERMEDIATE.COMPUTERS_AND_THE_INTERNET = 67
    INTERMEDIATE.DESCRIBING_EVENTS_AND_DISASTERS = 68
    INTERMEDIATE.ENVIRONMENTAL_ISSUES = 69
    INTERMEDIATE.COMPARING_CULTURES = 70
    INTERMEDIATE.HUMAN_RELATIONSHIPS = 71
    INTERMEDIATE.KOREAN_LITERATURE = 72
    INTERMEDIATE.SOLVING_PROBLEMS = 73
    INTERMEDIATE.TALKING_ABOUT_MISTAKES = 74
    INTERMEDIATE.DATING_AND_MARRIAGE = 75
    INTERMEDIATE.LANGUAGE = 76
    ADVANCED.GEOLOGICAL_INFORMATION = 77
    ADVANCED.ECONOMICS_AND_ADMINISTRATION = 78
    ADVANCED.DIETARY_CULTURE = 79
    ADVANCED.CLIMATE = 80
    ADVANCED.EDUCATION = 81
    ADVANCED.JOBS_AND_CAREERS = 82
    ADVANCED.WORKPLACE_LIFE = 83
    ADVANCED.HOBBIES = 84
    ADVANCED.HEALTH_AND_MEDICAL_TREATMENT = 85
    ADVANCED.RESIDENTIAL_AREA = 86
    ADVANCED.PSYCHOLOGY = 87
    ADVANCED.APPEARANCE = 88
    ADVANCED.POP_CULTURE = 89
    ADVANCED.COMPUTERS_AND_THE_INTERNET = 90
    ADVANCED.SOCIAL_ISSUES = 91
    ADVANCED.ENVIRONMENTAL_ISSUES = 92
    ADVANCED.SOCIAL_SYSTEM = 93
    ADVANCED.CULTURAL_DIFFERENCES = 94
    ADVANCED.HUMAN_RELATIONSHIPS = 95
    ADVANCED.ART = 96
    ADVANCED.ARCHITECTURE = 97
    ADVANCED.SCIENCE_AND_TECHNOLOGY = 98
    ADVANCED.LAW = 99
    ADVANCED.SPORTS = 100
    ADVANCED.PRESS = 101
    ADVANCED.LANGUAGE = 102
    ADVANCED.HISTORY = 103
    ADVANCED.POLITICS = 104
    ADVANCED.RELIGION = 105
    ADVANCED.PHILOSOPHY_AND_ETHICS = 106
```

## Aliases

The following values are aliases for subject categories.
A read-only dictionary of these aliases can be accessed with
the [`aliases`](parameters.md#aliases) property.

These strings and the integer values they map to can be used directly
in functions which expect subject categories, and return the expected
enumeration value when used as the argument to [`get`](parameters.md#get).

```bash
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
"talking about one's mistakes": 74,
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
```
