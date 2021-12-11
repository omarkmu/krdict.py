"""
Retrieves information from the krdict website via scraping.
"""

from ..types.scraper import ScrapedWordResponse, ScraperTranslationLanguage, WordOfTheDayResponse
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
    'ScraperTranslationLanguage',
    'WordOfTheDayResponse'
]
