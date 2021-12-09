"""
Retrieves information from the krdict website via scraping.
"""

from ..types.scraper import ScrapedWordResponse, ScraperTranslationLanguage, WordOfTheDayResponse
from .fetch import fetch_meaning_category_words, fetch_subject_category_words, fetch_today_word

__all__ = [
    'fetch_today_word',
    'fetch_meaning_category_words',
    'fetch_subject_category_words',
    'ScrapedWordResponse',
    'ScraperTranslationLanguage',
    'WordOfTheDayResponse'
]
