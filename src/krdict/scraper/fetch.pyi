from typing import Iterable, Literal, overload
from ..types import SearchType, SortMethod, SubjectCategory
from ..types.scraper import ScrapedExampleResponse, ScrapedWordResponse, ScraperTranslationLanguage, WordOfTheDayResponse
from ..main import TMeaningCategory, TSortMethod, TSubjectCategory

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

def fetch_today_word(*,
    translation_language: TScraperTranslationLanguage = None
) -> WordOfTheDayResponse: ...


def fetch_meaning_category_words(*,
    category: TMeaningCategory,
    page: int = 1,
    per_page: int = 10,
    sort: TSortMethod = SortMethod.ALPHABETICAL,
    translation_language: TScraperTranslationLanguage = None
) -> ScrapedWordResponse: ...

def fetch_subject_category_words(*,
    category: TSubjectCategory | Iterable[TSubjectCategory] = SubjectCategory.ALL,
    page: int = 1,
    per_page: int = 10,
    sort: TSortMethod = SortMethod.ALPHABETICAL,
    translation_language: TScraperTranslationLanguage = None
) -> ScrapedWordResponse: ...

@overload
def search(*,
    query: str,
    page: int = 1,
    per_page: int = 10,
    sort: TSortMethod = SortMethod.ALPHABETICAL,
    search_type: Literal[SearchType.WORD, 'word'],
    translation_language: TScraperTranslationLanguage | Iterable[TScraperTranslationLanguage] = None
) -> ScrapedWordResponse: ...
@overload
def search(*,
    query: str,
    page: int = 1,
    per_page: int = 10,
    sort: TSortMethod = SortMethod.ALPHABETICAL,
    search_type: Literal[SearchType.EXAMPLE, 'example', 'exam'],
    translation_language: TScraperTranslationLanguage | Iterable[TScraperTranslationLanguage] = None
) -> ScrapedExampleResponse: ...
