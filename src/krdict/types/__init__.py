"""
Contains types defined by the krdict module.
"""

from .enum import (
    Classification,
    MultimediaType,
    OriginType,
    PartOfSpeech,
    SearchMethod,
    SearchTarget,
    SearchType,
    SortMethod,
    TargetLanguage,
    TranslationLanguage,
    VocabularyLevel
)
from .meaning_category import MeaningCategory
from .subject_category import SubjectCategory
from .exceptions import KRDictException
from .scraper import ScraperTranslationLanguage


def isiterable(obj, exclude=None):
    """
    Returns True if a type is iterable,
    or False otherwise.

    Types passed to ``exclude`` will be
    considered not iterable.
    """

    if any(isinstance(obj, cls) for cls in exclude or ()):
        return False

    try:
        iter(obj)
        return True
    except TypeError:
        return False


__all__ = [
    'Classification',
    'KRDictException',
    'MeaningCategory',
    'MultimediaType',
    'OriginType',
    'PartOfSpeech',
    'ScraperTranslationLanguage',
    'SearchMethod',
    'SearchTarget',
    'SearchType',
    'SortMethod',
    'SubjectCategory',
    'TargetLanguage',
    'TranslationLanguage',
    'VocabularyLevel',
    'isiterable'
]
