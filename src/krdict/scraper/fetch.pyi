from typing import Iterable, List, Literal, TypedDict, overload
from ..types import SortMethod, SubjectCategory
from ..types.scraper import ScraperTranslationLanguage
from ..main import TMeaningCategory, SearchTranslation, TSortMethod, TSubjectCategory

TScraperTranslationLanguage = ScraperTranslationLanguage | int | Literal[
    'english',
    'japanese',
    'french',
    'spanish',
    'arabic',
    'mongolian',
    'vietnamese',
    'thai',
    'indonesian',
    'russian',
    'chinese'
]


class _WordOfTheDayData(TypedDict, total=False):
    part_of_speech: str
    vocabulary_level: str
    origin: str
    pronunciation: str
    pronunciation_urls: List[str]
class WordOfTheDayData(_WordOfTheDayData):
    target_code: int
    word: str
    definition: str
    url: str
    homograph_num: int
    translation: SearchTranslation

class WordOfTheDayResponse(TypedDict):
    response_type: Literal['word_of_the_day']
    data: WordOfTheDayData


class TotalWordOfTheDayData(TypedDict):
    part_of_speech: str
    vocabulary_level: str
    origin: str
    pronunciation: str
    pronunciation_urls: List[str]
    target_code: int
    word: str
    definition: str
    url: str
    homograph_num: int
    translation: SearchTranslation | None

class TotalWordOfTheDayResponse(TypedDict):
    response_type: Literal['word_of_the_day']
    data: TotalWordOfTheDayData


class _ScrapedSearchDefinition(TypedDict, total=False):
    translation: SearchTranslation
class ScrapedSearchDefinition(_ScrapedSearchDefinition):
    definition: str
    order: int

class _ScrapedSearchItem(TypedDict, total=False):
    part_of_speech: str
    origin: str
    vocabulary_level: str
class ScrapedSearchItem(_ScrapedSearchItem):
    target_code: int
    word: str
    url: str
    homograph_num: int
    definitions: List[ScrapedSearchDefinition]

class ScrapedWordSearchData(TypedDict):
    search_url: str
    page: int
    per_page: int
    total_results: int
    results: List[ScrapedSearchItem]

class ScrapedWordSearchResponse(TypedDict):
    response_type: Literal['scraped_word']
    data: ScrapedWordSearchData


class TotalScrapedSearchDefinition(TypedDict):
    translation: SearchTranslation | None
    definition: str
    order: int

class TotalScrapedSearchItem(TypedDict):
    part_of_speech: str
    origin: str
    vocabulary_level: str
    target_code: int
    word: str
    url: str
    homograph_num: int
    definitions: List[TotalScrapedSearchDefinition]

class TotalScrapedWordSearchData(TypedDict):
    search_url: str
    page: int
    per_page: int
    total_results: int
    results: List[TotalScrapedSearchItem]

class TotalScrapedWordSearchResponse(TypedDict):
    response_type: Literal['scraped_word']
    data: TotalScrapedWordSearchData


@overload
def fetch_today_word(*,
    guarantee_keys: Literal[True],
    translation_language: TScraperTranslationLanguage = None
) -> TotalWordOfTheDayResponse: ...
@overload
def fetch_today_word(*,
    guarantee_keys: bool = False,
    translation_language: TScraperTranslationLanguage = None
) -> WordOfTheDayResponse: ...


@overload
def fetch_meaning_category_words(*,
    guarantee_keys: Literal[True],
    category: TMeaningCategory,
    page: int = 1,
    per_page: int = 10,
    sort: TSortMethod = SortMethod.ALPHABETICAL,
    translation_language: TScraperTranslationLanguage = None
) -> TotalScrapedWordSearchResponse: ...
@overload
def fetch_meaning_category_words(*,
    guarantee_keys: bool = False,
    category: TMeaningCategory,
    page: int = 1,
    per_page: int = 10,
    sort: TSortMethod = SortMethod.ALPHABETICAL,
    translation_language: TScraperTranslationLanguage = None
) -> ScrapedWordSearchResponse: ...


@overload
def fetch_subject_category_words(*,
    guarantee_keys: Literal[True],
    category: TSubjectCategory | Iterable[TSubjectCategory] = SubjectCategory.ALL,
    page: int = 1,
    per_page: int = 10,
    sort: TSortMethod = SortMethod.ALPHABETICAL,
    translation_language: TScraperTranslationLanguage = None
) -> TotalScrapedWordSearchResponse: ...
@overload
def fetch_subject_category_words(*,
    guarantee_keys: bool = False,
    category: TSubjectCategory | Iterable[TSubjectCategory] = SubjectCategory.ALL,
    page: int = 1,
    per_page: int = 10,
    sort: TSortMethod = SortMethod.ALPHABETICAL,
    translation_language: TScraperTranslationLanguage = None
) -> ScrapedWordSearchResponse: ...
