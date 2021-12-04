"""
Retrieves information from the krdict website via scraping.
"""

from ..types import ScraperTranslationLanguage
from .extend import extend_advanced_search, extend_search, extend_view
from .fetch import fetch_meaning_category_words, fetch_subject_category_words, fetch_today_word

__all__ = [
    'extend_advanced_search',
    'extend_search',
    'extend_view',
    'fetch_today_word',
    'fetch_meaning_category_words',
    'fetch_subject_category_words',
    'ScraperTranslationLanguage'
]
