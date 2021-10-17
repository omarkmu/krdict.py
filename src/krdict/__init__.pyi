from typing import Dict, List, Literal, TypedDict, Union, overload

Classification = Literal[
    'all',
    'word',
    'phrase',
    'expression'
]
MeaningCategory = Literal[
    '전체',
    '인간 > 전체',
    '인간 > 사람의 종류',
    '인간 > 신체 부위',
    '인간 > 체력 상태',
    '인간 > 생리 현상',
    '인간 > 감각',
    '인간 > 감정',
    '인간 > 성격',
    '인간 > 태도',
    '인간 > 용모',
    '인간 > 능력',
    '인간 > 신체 변화',
    '인간 > 신체 행위',
    '인간 > 신체에 가하는 행위',
    '인간 > 인지 행위',
    '인간 > 소리',
    '인간 > 신체 내부 구성',
    '삶 > 전체',
    '삶 > 삶의 상태',
    '삶 > 삶의 행위',
    '삶 > 일상 행위',
    '삶 > 친족 관계',
    '삶 > 가족 행사',
    '삶 > 여가 도구',
    '삶 > 여가 시설',
    '삶 > 여가 활동',
    '삶 > 병과 증상',
    '삶 > 치료 행위',
    '삶 > 치료 시설',
    '삶 > 약품류',
    '식생활 > 전체',
    '식생활 > 음식',
    '식생활 > 채소',
    '식생활 > 곡류',
    '식생활 > 과일',
    '식생활 > 음료',
    '식생활 > 식재료',
    '식생활 > 조리 도구',
    '식생활 > 식생활 관련 장소',
    '식생활 > 맛',
    '식생활 > 식사 및 조리 행위',
    '의생활 > 전체',
    '의생활 > 옷 종류',
    '의생활 > 옷감',
    '의생활 > 옷의 부분',
    '의생활 > 모자, 신발, 장신구',
    '의생활 > 의생활 관련 장소',
    '의생활 > 의복 착용 상태',
    '의생활 > 의복 착용 행위',
    '의생활 > 미용 행위',
    '주생활 > 전체',
    '주생활 > 건물 종류',
    '주생활 > 주거 형태',
    '주생활 > 주거 지역',
    '주생활 > 생활 용품',
    '주생활 > 주택 구성',
    '주생활 > 주거 상태',
    '주생활 > 주거 행위',
    '주생활 > 가사 행위',
    '사회 생활 > 전체',
    '사회 생활 > 인간관계',
    '사회 생활 > 소통 수단',
    '사회 생활 > 교통 수단',
    '사회 생활 > 교통 이용 장소',
    '사회 생활 > 매체',
    '사회 생활 > 직장',
    '사회 생활 > 직위',
    '사회 생활 > 직업',
    '사회 생활 > 사회 행사',
    '사회 생활 > 사회 생활 상태',
    '사회 생활 > 사회 활동',
    '사회 생활 > 교통 이용 행위',
    '사회 생활 > 직장 생활',
    '사회 생활 > 언어 행위',
    '사회 생활 > 통신 행위',
    '사회 생활 > 말',
    '경제 생활 > 전체',
    '경제 생활 > 경제 행위 주체',
    '경제 생활 > 경제 행위 장소',
    '경제 생활 > 경제 수단',
    '경제 생활 > 경제 산물',
    '경제 생활 > 경제 상태',
    '경제 생활 > 경제 행위',
    '교육 > 전체',
    '교육 > 교수 학습 주체',
    '교육 > 전공과 교과목',
    '교육 > 교육 기관',
    '교육 > 학교 시설',
    '교육 > 학습 관련 사물',
    '교육 > 학문 용어',
    '교육 > 교수 학습 행위',
    '교육 > 학문 행위',
    '종교 > 전체',
    '종교 > 종교 유형',
    '종교 > 종교 활동 장소',
    '종교 > 종교인',
    '종교 > 종교어',
    '종교 > 신앙 대상',
    '종교 > 종교 활동 도구',
    '종교 > 종교 행위',
    '문화 > 전체',
    '문화 > 문화 활동 주체',
    '문화 > 음악',
    '문화 > 미술',
    '문화 > 문학',
    '문화 > 예술',
    '문화 > 대중 문화',
    '문화 > 전통 문화',
    '문화 > 문화 생활 장소',
    '문화 > 문화 활동',
    '정치와 행정 > 전체',
    '정치와 행정 > 공공 기관',
    '정치와 행정 > 사법 및 치안 주체',
    '정치와 행정 > 무기',
    '정치와 행정 > 정치 및 치안 상태',
    '정치와 행정 > 정치 및 행정 행위',
    '정치와 행정 > 사법 및 치안 행위',
    '정치와 행정 > 정치 및 행정 주체',
    '자연 > 전체',
    '자연 > 지형',
    '자연 > 지표면 사물',
    '자연 > 천체',
    '자연 > 자원',
    '자연 > 재해',
    '자연 > 기상 및 기후',
    '동식물 > 전체',
    '동식물 > 동물류',
    '동식물 > 곤충류',
    '동식물 > 식물류',
    '동식물 > 동물의 부분',
    '동식물 > 식물의 부분',
    '동식물 > 동식물 행위',
    '동식물 > 동물 소리',
    '개념 > 전체',
    '개념 > 모양',
    '개념 > 성질',
    '개념 > 속도',
    '개념 > 밝기',
    '개념 > 온도',
    '개념 > 색깔',
    '개념 > 수',
    '개념 > 세는 말',
    '개념 > 양',
    '개념 > 정도',
    '개념 > 순서',
    '개념 > 빈도',
    '개념 > 시간',
    '개념 > 위치 및 방향',
    '개념 > 지역',
    '개념 > 지시',
    '개념 > 접속',
    '개념 > 의문',
    '개념 > 인칭'
]
MultimediaType = Literal[
    'all',
    'photo',
    'illustration',
    'video',
    'animation',
    'sound',
    'none'
]
PartOfSpeech = Literal[
    'all',
    'noun',
    'pronoun',
    'numeral',
    'particle',
    'verb',
    'adjective',
    'determiner',
    'adverb',
    'interjection',
    'affix',
    'bound noun',
    'auxiliary verb',
    'auxiliary adjective',
    'ending',
    'none'
]
SearchMethod = Literal[
    'exact',
    'include',
    'start',
    'end'
]
SearchTarget = Literal[
    'headword',
    'definition',
    'example',
    'original_language',
    'pronunciation',
    'application',
    'application_shorthand',
    'idiom',
    'proverb',
    'reference_info'
]
SearchType = Literal[
    'word',
    'idiom_proverb',
    'definition',
    'example'
]
SortMethod = Literal[
    'alphabetical',
    'popular'
]
SubjectCategory = Literal[
    '전체',
    '인사하기',
    '소개하기 (자기소개)',
    '소개하기 (가족소개)',
    '개인 정보 교환하기 (초급)',
    '위치 표현하기',
    '길찾기',
    '교통 이용하기 (초금)',
    '물건 사기 (초금)',
    '음식 주문하기',
    '요리 설명하기 (초금)',
    '시간 표현하기',
    '날짜 표현하기',
    '요일 표현하기',
    '날씨와 계절 (초금)',
    '하루 생활',
    '학교생활 (초금)',
    '한국 생활 (초금)',
    '약속하기',
    '전화하기',
    '감사하기',
    '사과하기',
    '여행 (초금)',
    '주말 및 휴가 (초금)',
    '취미 (초금)',
    '가족 행사 (초금)',
    '건강 (초금)',
    '병원 이용하기',
    '약국 이용하기 (초금)',
    '공공 기관 이용하기 (도서관)',
    '공공 기관 이용하기 (우체국)',
    '공공 기관 이용하기 (출입국 관리 사무소)',
    '초대와 방문 (초금)',
    '집 구하기 (초금)',
    '집안일 (초금)',
    '감정, 기분 표현하기 (초금)',
    '성격 표현하기 (초금)',
    '복장 표현하기 (초금)',
    '외모 표현하기 (초금)',
    '영화 보기',
    '개인 정보 교환하기 (중급)',
    '교통 이용하기 (중급)',
    '지리 정보 (중급)',
    '물건 사기 (중급)',
    '음식 설명하기',
    '요리 설명하기 (중급)',
    '날씨와 계절 (중급)',
    '학교생활 (중급)',
    '한국 생활 (중급)',
    '직업과 진로 (중급)',
    '직장 생활 (중급)',
    '여행 (중급)',
    '주말 및 휴가 (중급)',
    '취미 (중급)',
    '가족 행사 (중급)',
    '가족 행사 (명절)',
    '건강 (중급)',
    '공공기관 이용하기',
    '초대와 방문 (중급)',
    '집 구하기 (중급)',
    '집안일 (중급)',
    '감정, 기분 표현하기 (중급)',
    '성격 표현하기 (중급)',
    '복장 표현하기 (중급)',
    '외모 표현하기 (중급)',
    '공연과 감상',
    '대중 매체',
    '컴퓨터와 인터넷 (중급)',
    '사건, 사고, 재해 기술하기',
    '환경 문제 (중급)',
    '문화 비교하기',
    '인간관계 (중급)',
    '한국의 문학',
    '문제 해결하기 (분실 및 고장)',
    '실수담 말하기',
    '연애와 결혼',
    '언어 (중급)',
    '지리 정보 (고급)',
    '경제∙경영',
    '경제-경영',
    '식문화',
    '기후',
    '교육',
    '직업과 진로 (고급)',
    '직장 생활 (고급)',
    '여가 생활',
    '보건과 의료',
    '주거 생활',
    '심리',
    '외양',
    '대중문화',
    '컴퓨터와 인터넷 (고급)',
    '사회 문제',
    '환경 문제 (고급)',
    '사회 제도',
    '문화 차이',
    '인간관계 (고급)',
    '예술',
    '건축',
    '과학과 기술',
    '법',
    '스포츠',
    '언론',
    '언어 (고급)',
    '역사',
    '정치',
    '종교',
    '철학∙윤리',
    '철학-윤리'
]
TargetLanguage = Literal[
    'all',
    'native_word',
    'sino-korean',
    'unknown',
    'english',
    'greek',
    'dutch',
    'norwegian',
    'german',
    'latin',
    'russian',
    'romanian',
    'maori',
    'malay',
    'mongolian',
    'basque',
    'burmese',
    'vietnamese',
    'bulgarian',
    'sanskrit',
    'serbo-croatian',
    'swahili',
    'swedish',
    'arabic',
    'irish',
    'spanish',
    'uzbek',
    'ukrainian',
    'italian',
    'indonesian',
    'japanese',
    'chinese',
    'czech',
    'cambodian',
    'quechua',
    'tagalog',
    'thai',
    'turkish',
    'tibetan',
    'persian',
    'portuguese',
    'polish',
    'french',
    'provencal',
    'finnish',
    'hungarian',
    'hebrew',
    'hindi',
    'other',
    'danish'
]
TranslationLanguage = Literal[
    'all',
    'english',
    'japanese',
    'french',
    'spanish',
    'arabic',
    'mongolian',
    'vietnamese',
    'thai',
    'indonesian',
    'russian'
]
OriginType = Literal[
    'all',
    'native',
    'hanja',
    'loanword',
    'hybrid'
]
VocabularyGrade = Literal[
    'all',
    'beginner',
    'intermediate',
    'advanced'
]
Option = Literal[
    'fetch_multimedia',
    'fetch_page_data',
    'raise_scraper_errors',
    'use_scraper'
]

class OptionsDict(TypedDict, total=False):
    use_scraper: bool
    raise_scraper_errors: bool
    fetch_multimedia: bool
    fetch_page_data: bool


class KRDictErrorInfo(TypedDict):
    error_code: int
    message: str
class KRDictError(TypedDict):
    response_type: Literal['error']
    request_params: Dict[str, str]
    error: KRDictErrorInfo

class _SearchTranslation(TypedDict, total=False):
    word: str
class SearchTranslation(_SearchTranslation):
    definition: str
    language: str

class _BaseSearchDefinition(TypedDict, total=False):
    translations: List[SearchTranslation]
class PartialSearchDefinition(_BaseSearchDefinition):
    definition: str
class SearchDefinition(PartialSearchDefinition):
    order: int


class _BaseSearchItem(TypedDict):
    target_code: int
    word: str
    url: str

class _WordSearchItem(TypedDict, total=False):
    origin: str
    pronunciation: str
    vocabulary_grade: str
    pronunciation_urls: List[str]
class WordSearchItem(_WordSearchItem, _BaseSearchItem):
    part_of_speech: str
    homograph_num: int
    definitions: List[SearchDefinition]

class DefinitionSearchItem(_BaseSearchItem):
    homograph_num: int
    definitions: List[PartialSearchDefinition]

class ExampleSearchItem(_BaseSearchItem):
    homograph_num: int
    example: str

class IdiomProverbSearchItem(_BaseSearchItem):
    definitions: List[SearchDefinition]


class _BaseSearchResponseData(TypedDict):
    title: str
    url: str
    description: str
    last_build_date: str
    page: int
    per_page: int
    total_results: int
class WordSearchResponseData(_BaseSearchResponseData):
    results: List[WordSearchItem]
class DefinitionSearchResponseData(_BaseSearchResponseData):
    results: List[DefinitionSearchItem]
class ExampleSearchResponseData(_BaseSearchResponseData):
    results: List[ExampleSearchItem]
class IdiomProverbSearchResponseData(_BaseSearchResponseData):
    results: List[IdiomProverbSearchItem]

class WordSearchResponse(TypedDict):
    response_type: Literal['word']
    request_params: Dict[str, str]
    data: WordSearchResponseData
class DefinitionSearchResponse(TypedDict):
    response_type: Literal['definition']
    request_params: Dict[str, str]
    data: DefinitionSearchResponseData
class ExampleSearchResponse(TypedDict):
    response_type: Literal['example']
    request_params: Dict[str, str]
    data: ExampleSearchResponseData
class IdiomProverbSearchResponse(TypedDict):
    response_type: Literal['idiom_proverb']
    request_params: Dict[str, str]
    data: IdiomProverbSearchResponseData

SearchResponse = Union[
    WordSearchResponse,
    DefinitionSearchResponse,
    ExampleSearchResponse,
    IdiomProverbSearchResponse
]

class HanjaInfo(TypedDict):
    hanja: str
    radical: str
    stroke_count: int
    readings: List[str]

class _ViewOriginalLanguageInfo(TypedDict, total=False):
    hanja_info: List[HanjaInfo]
class ViewOriginalLanguageInfo(_ViewOriginalLanguageInfo):
    original_language: str
    language_type: str

class _ViewPronunciationInfo(TypedDict, total=False):
    url: str
class ViewPronunciationInfo(_ViewPronunciationInfo):
    pronunciation: str

class _ViewAbbreviationInfo(TypedDict, total=False):
    pronunciation_info: List[ViewPronunciationInfo]
class ViewAbbreviationInfo(_ViewAbbreviationInfo):
    abbreviation: str

class _ViewConjugationInfo(TypedDict, total=False):
    pronunciation_info: List[ViewPronunciationInfo]
    abbreviation_info: List[ViewAbbreviationInfo]
class ViewConjugationInfo(_ViewConjugationInfo):
    conjugation: str

class _ViewReferenceInfo(TypedDict, total=False):
    target_code: int
class ViewReferenceInfo(_ViewReferenceInfo):
    word: str
    url: str
    has_target_code: bool

class ViewCategoryInfo(TypedDict):
    type: str
    name: str

class _ViewPatternInfo(TypedDict, total=False):
    pattern_reference: str
class ViewPatternInfo(_ViewPatternInfo):
    pattern: str

class ViewExampleInfo(TypedDict):
    type: str
    example: str

class ViewRelatedInfo(ViewReferenceInfo):
    type: str

class _ViewMultimediaInfo(TypedDict, total=False):
    media_urls: List[str]
class ViewMultimediaInfo(_ViewMultimediaInfo):
    label: str
    type: str
    url: str

class ViewPartialRelatedInfo(TypedDict):
    word: str
    type: str

class _ViewSubdefinitionInfo(TypedDict, total=False):
    translations: List[SearchTranslation]
    example_info: List[ViewExampleInfo]
    related_info: List[ViewPartialRelatedInfo]
class ViewSubdefinitionInfo(_ViewSubdefinitionInfo):
    definition: str

class ViewSubwordInfo(TypedDict):
    subword: str
    subword_unit: str
    subdefinition_info: List[ViewSubdefinitionInfo]

class _ViewDefinitionInfo(TypedDict):
    reference: str
    translations: List[SearchTranslation]
    example_info: List[ViewExampleInfo]
    pattern_info: List[ViewPatternInfo]
    related_info: List[ViewRelatedInfo]
    multimedia_info: List[ViewMultimediaInfo]
class ViewDefinitionInfo(_ViewDefinitionInfo):
    definition: str

class _ViewWordInfo(TypedDict):
    allomorph: str
    original_language_info: List[ViewOriginalLanguageInfo]
    pronunciation_info: List[ViewPronunciationInfo]
    conjugation_info: List[ViewConjugationInfo]
    derivative_info: List[ViewReferenceInfo]
    reference_info: List[ViewReferenceInfo]
    category_info: List[ViewCategoryInfo]
    subword_info: List[ViewSubwordInfo]
class ViewWordInfo(_ViewWordInfo):
    word: str
    word_unit: str
    word_type: str
    part_of_speech: str
    homograph_num: int
    vocabulary_grade: str
    definition_info: List[ViewDefinitionInfo]

class ViewItem(TypedDict):
    target_code: int
    word_info: ViewWordInfo

class ViewResponseData(TypedDict):
    title: str
    url: str
    description: str
    last_build_date: str
    total_results: int
    results: List[ViewItem]

class ViewResponse(TypedDict):
    response_type: Literal['view']
    data: ViewResponseData
    request_params: Dict[str, str]


class KRDictException(Exception):
    message: str
    error_code: str
    request_params: dict


@overload
def advanced_search(*,
    query: str,
    raise_api_errors: Literal[True],
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: Literal['word'],
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    search_target: SearchTarget = None,
    target_language: TargetLanguage = None,
    search_method: SearchMethod = None,
    classification: Classification | List[Classification] = None,
    origin_type: OriginType | List[OriginType] = None,
    vocabulary_grade: VocabularyGrade | List[VocabularyGrade] = None,
    part_of_speech: PartOfSpeech | List[PartOfSpeech] = None,
    multimedia_info: MultimediaType | List[MultimediaType] = None,
    min_syllables: int = None,
    max_syllables: int = None,
    meaning_category: MeaningCategory | int = None,
    subject_category: SubjectCategory | int | List[SubjectCategory | int] = None,
    options: OptionsDict = None
) -> WordSearchResponse: ...
@overload
def advanced_search(*,
    query: str,
    raise_api_errors: Literal[True],
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: SearchType = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    search_target: SearchTarget = None,
    target_language: TargetLanguage = None,
    search_method: SearchMethod = None,
    classification: Classification | List[Classification] = None,
    origin_type: OriginType | List[OriginType] = None,
    vocabulary_grade: VocabularyGrade | List[VocabularyGrade] = None,
    part_of_speech: PartOfSpeech | List[PartOfSpeech] = None,
    multimedia_info: MultimediaType | List[MultimediaType] = None,
    min_syllables: int = None,
    max_syllables: int = None,
    meaning_category: MeaningCategory | int = None,
    subject_category: SubjectCategory | int | List[SubjectCategory | int] = None,
    options: OptionsDict = None
) -> SearchResponse: ...

@overload
def advanced_search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: Literal['word'],
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    search_target: SearchTarget = None,
    target_language: TargetLanguage = None,
    search_method: SearchMethod = None,
    classification: Classification | List[Classification] = None,
    origin_type: OriginType | List[OriginType] = None,
    vocabulary_grade: VocabularyGrade | List[VocabularyGrade] = None,
    part_of_speech: PartOfSpeech | List[PartOfSpeech] = None,
    multimedia_info: MultimediaType | List[MultimediaType] = None,
    min_syllables: int = None,
    max_syllables: int = None,
    meaning_category: MeaningCategory | int = None,
    subject_category: SubjectCategory | int | List[SubjectCategory | int] = None,
    options: OptionsDict = None
) -> WordSearchResponse | KRDictError: ...
@overload
def advanced_search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: SearchType = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    search_target: SearchTarget = None,
    target_language: TargetLanguage = None,
    search_method: SearchMethod = None,
    classification: Classification | List[Classification] = None,
    origin_type: OriginType | List[OriginType] = None,
    vocabulary_grade: VocabularyGrade | List[VocabularyGrade] = None,
    part_of_speech: PartOfSpeech | List[PartOfSpeech] = None,
    multimedia_info: MultimediaType | List[MultimediaType] = None,
    min_syllables: int = None,
    max_syllables: int = None,
    meaning_category: MeaningCategory | int = None,
    subject_category: SubjectCategory | int | List[SubjectCategory | int] = None,
    options: OptionsDict = None
) -> SearchResponse | KRDictError: ...


@overload
def search(*,
    query: str,
    raise_api_errors: Literal[True],
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: Literal['word'],
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> WordSearchResponse: ...
@overload
def search(*,
    query: str,
    raise_api_errors: Literal[True],
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: Literal['definition'],
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> DefinitionSearchResponse: ...
@overload
def search(*,
    query: str,
    raise_api_errors: Literal[True],
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: Literal['example'],
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> ExampleSearchResponse: ...
@overload
def search(*,
    query: str,
    raise_api_errors: Literal[True],
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: Literal['idiom_proverb'],
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> IdiomProverbSearchResponse: ...
@overload
def search(*,
    query: str,
    raise_api_errors: Literal[True],
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: SearchType = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> SearchResponse: ...

@overload
def search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: Literal['word'],
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> WordSearchResponse | KRDictError: ...
@overload
def search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: Literal['definition'],
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> DefinitionSearchResponse | KRDictError: ...
@overload
def search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: Literal['example'],
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> ExampleSearchResponse | KRDictError: ...
@overload
def search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: Literal['idiom_proverb'],
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> IdiomProverbSearchResponse | KRDictError: ...
@overload
def search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: SearchType = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> SearchResponse | KRDictError: ...


def set_default(name: Option, value: bool) -> None: ...


def set_key(key: str | None) -> None: ...


@overload
def view(*,
    query: str,
    raise_api_errors: Literal[True],
    homograph_num: int = None,
    key: str = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> ViewResponse: ...
@overload
def view(*,
    query: str,
    raise_api_errors: bool = False,
    homograph_num: int = None,
    key: str = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> ViewResponse | KRDictError: ...

@overload
def view(*,
    target_code: int,
    raise_api_errors: Literal[True],
    key: str = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> ViewResponse: ...
@overload
def view(*,
    target_code: int,
    raise_api_errors: bool = False,
    key: str = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> ViewResponse | KRDictError: ...
