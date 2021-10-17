from typing import List, Literal, TypedDict
from . import MeaningCategory, SearchTranslation, SortMethod, SubjectCategory, WordSearchResponse, ViewResponse

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


def extend_advanced_search(
    response: WordSearchResponse,
    raise_errors: bool
) -> WordSearchResponse: ...

def extend_search(
    response: WordSearchResponse,
    raise_errors: bool
) -> WordSearchResponse: ...

def extend_view(
    response: ViewResponse,
    fetch_page_data: bool,
    fetch_multimedia: bool,
    raise_errors: bool
) -> ViewResponse: ...

def fetch_today_word(
    translation_language: ScraperTranslationLanguage = None
) -> WordOfTheDayResponse: ...

def fetch_meaning_category_words(*,
    category: MeaningCategory | int,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    translation_language: ScraperTranslationLanguage = None
) -> ScrapedWordSearchResponse: ...

def fetch_subject_category_words(*,
    category: SubjectCategory | int | List[SubjectCategory | int],
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    translation_language: ScraperTranslationLanguage = None
) -> ScrapedWordSearchResponse: ...
