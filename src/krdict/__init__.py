"""
Provides functions that query the Korean Learners' Dictionary API.
"""

from . import scraper
from .request import set_key
from .response import set_default
from .main import advanced_search, search, view
from .types import (
    Classification,
    KRDictException,
    MeaningCategory,
    MultimediaType,
    OriginType,
    PartOfSpeech,
    SearchMethod,
    SearchTarget,
    SearchType,
    SortMethod,
    SubjectCategory,
    TargetLanguage,
    TranslationLanguage,
    VocabularyLevel
)

__all__ = [
    'scraper',
    'advanced_search',
    'search',
    'set_default',
    'set_key',
    'view',
    'Classification',
    'KRDictException',
    'MeaningCategory',
    'MultimediaType',
    'OriginType',
    'PartOfSpeech',
    'SearchMethod',
    'SearchTarget',
    'SearchType',
    'SortMethod',
    'SubjectCategory',
    'TargetLanguage',
    'TranslationLanguage',
    'VocabularyLevel'
]
