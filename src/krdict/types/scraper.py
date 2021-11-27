"""
Contains types defined by the krdict.scraper module.
"""

from .base import IntEnumBase

class ScraperTranslationLanguage(IntEnumBase):
    """Enumeration class that contains translation languages that can be used by the scraper."""

    __aliases__ = {
        'all': 0,
        'english': 1,
        'japanese': 2,
        'french': 3,
        'spanish': 4,
        'arabic': 5,
        'mongolian': 6,
        'vietnamese': 7,
        'thai': 8,
        'indonesian': 9,
        'russian': 10,
        'chinese': 11
    }

    ALL = 0
    ENGLISH = 1
    JAPANESE = 2
    FRENCH = 3
    SPANISH = 4
    ARABIC = 5
    MONGOLIAN = 6
    VIETNAMESE = 7
    THAI = 8
    INDONESIAN = 9
    RUSSIAN = 10
    CHINESE = 11
