"""
Retrieves information from the krdict website via scraping.
"""

from ..types import (
    ScrapedWordResponse,
    ScraperSearchTarget,
    ScraperTargetLanguage,
    ScraperTranslationLanguage,
    ScraperVocabularyLevel,
    WordOfTheDayResponse
)
from .fetch import (
    advanced_search,
    fetch_meaning_category_words,
    fetch_subject_category_words,
    fetch_today_word,
    search
)

__all__ = [
    'advanced_search',
    'fetch_today_word',
    'fetch_meaning_category_words',
    'fetch_subject_category_words',
    'search',
    'ScrapedWordResponse',
    'ScraperSearchTarget',
    'ScraperTargetLanguage',
    'ScraperTranslationLanguage',
    'ScraperVocabularyLevel',
    'WordOfTheDayResponse'
]
