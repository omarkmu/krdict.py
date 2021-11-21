from typing import List, Literal, TypedDict, overload
from ._helpers import MeaningCategory
from . import (
    MeaningCategoryLiteral, SearchTranslation, SortMethod, SubjectCategory,
    TotalViewResponse, TotalWordSearchResponse, WordSearchResponse, ViewResponse
)

ScraperTranslationLanguage = Literal[
    'chinese',
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


class _WordOfTheDayData(TypedDict, total=False):
    part_of_speech: str
    vocabulary_grade: str
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
    vocabulary_grade: str
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
    vocabulary_grade: str
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
    vocabulary_grade: str
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
def extend_advanced_search(
    response: TotalWordSearchResponse,
    raise_errors: bool
) -> TotalWordSearchResponse: ...
@overload
def extend_advanced_search(
    response: WordSearchResponse,
    raise_errors: bool
) -> WordSearchResponse: ...


@overload
def extend_search(
    response: TotalWordSearchResponse,
    raise_errors: bool
) -> TotalWordSearchResponse: ...
@overload
def extend_search(
    response: WordSearchResponse,
    raise_errors: bool
) -> WordSearchResponse: ...


@overload
def extend_view(
    response: TotalViewResponse,
    fetch_page_data: bool,
    fetch_multimedia: bool,
    raise_errors: bool
) -> TotalViewResponse: ...
@overload
def extend_view(
    response: ViewResponse,
    fetch_page_data: bool,
    fetch_multimedia: bool,
    raise_errors: bool
) -> ViewResponse: ...


@overload
def fetch_today_word(*,
    guarantee_keys: Literal[True],
    translation_language: ScraperTranslationLanguage = None
) -> TotalWordOfTheDayResponse: ...
@overload
def fetch_today_word(*,
    guarantee_keys: bool = False,
    translation_language: ScraperTranslationLanguage = None
) -> WordOfTheDayResponse: ...


@overload
def fetch_meaning_category_words(*,
    guarantee_keys: Literal[True],
    category: MeaningCategory | MeaningCategoryLiteral | int,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    translation_language: ScraperTranslationLanguage = None
) -> TotalScrapedWordSearchResponse: ...
@overload
def fetch_meaning_category_words(*,
    guarantee_keys: bool = False,
    category: MeaningCategory | MeaningCategoryLiteral | int,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    translation_language: ScraperTranslationLanguage = None
) -> ScrapedWordSearchResponse: ...


@overload
def fetch_subject_category_words(*,
    guarantee_keys: Literal[True],
    category: SubjectCategory | int | List[SubjectCategory | int],
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    translation_language: ScraperTranslationLanguage = None
) -> TotalScrapedWordSearchResponse: ...
@overload
def fetch_subject_category_words(*,
    guarantee_keys: bool = False,
    category: SubjectCategory | int | List[SubjectCategory | int],
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    translation_language: ScraperTranslationLanguage = None
) -> ScrapedWordSearchResponse: ...
