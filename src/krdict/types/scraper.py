"""
Contains types defined by the krdict.scraper package.
"""

from typing import Literal
from .base import IntEnum
from .main import _ResponseEntity, _SearchTranslation

# pylint: disable=too-few-public-methods,too-many-instance-attributes


class _ScrapedSearchDefinition(_ResponseEntity):
    def __init__(self, raw):
        self.order: int = raw['sense_order']
        self.definition: str = raw['definition']
        self.translations = (
            [_SearchTranslation(raw['translation'])]
            if 'translation' in raw else []
        )

class _ScrapedSearchItem(_ResponseEntity):
    def __init__(self, raw):
        self.target_code: int = raw['target_code']
        self.word: str = raw['word']
        self.url: str = raw['link']
        self.translated_url: str = raw.get('trans_link', '')

class _ScrapedResponseData(_ResponseEntity):
    def __init__(self, raw):
        self.url: str = raw['link']
        self.translated_url: str = raw.get('trans_link', '')
        self.page: int = raw['start']
        self.per_page: int = raw['num']
        self.total_results: int = raw['total']


class _ScrapedWordSearchItem(_ScrapedSearchItem):
    def __init__(self, raw):
        super().__init__(raw)
        self.part_of_speech: str = raw.get('pos', '')
        self.homograph_num: int = raw['sup_no']
        self.origin: str = raw.get('origin', '')
        self.vocabulary_level: str = raw.get('word_grade', '')
        self.pronunciation: str = raw.get('pronunciation', '')
        self.pronunciation_urls: list[str] = raw.get('pronunciation_urls', [])
        self.definitions = list(map(_ScrapedSearchDefinition, raw['sense']))

class _ScrapedWordResponseData(_ScrapedResponseData):
    def __init__(self, raw):
        super().__init__(raw)
        self.results = list(map(_ScrapedWordSearchItem, raw['item']))


class _ScrapedExampleSearchItem(_ScrapedSearchItem):
    def __init__(self, raw):
        super().__init__(raw)
        self.homograph_num: int = raw['sup_no']
        self.example: str = raw['example']

class _ScrapedExampleResponseData(_ScrapedResponseData):
    def __init__(self, raw):
        super().__init__(raw)
        self.results = list(map(_ScrapedExampleSearchItem, raw['item']))


class _WordOfTheDayData(_ResponseEntity):
    def __init__(self, raw):
        self.target_code: int = raw['target_code']
        self.word: str = raw['word']
        self.url: str = raw['link']
        self.translated_url: str = raw.get('trans_link', '')
        self.part_of_speech: str = raw.get('pos', '')
        self.homograph_num: int = raw['sup_no']
        self.origin: str = raw.get('origin', '')
        self.vocabulary_level: str = raw.get('word_grade', '')
        self.pronunciation: str = raw.get('pronunciation', '')
        self.pronunciation_urls: list[str] = raw.get('pronunciation_urls', [])
        self.definition: str = raw['definition']
        self.translation = _SearchTranslation(raw['translation']) if 'translation' in raw else None



class WordOfTheDayResponse(_ResponseEntity):
    """
    Contains information about the word of the day.
    """

    def __init__(self, raw):
        self.data = _WordOfTheDayData(raw)
        self.response_type: Literal['word_of_the_day'] = 'word_of_the_day'
        self.raw: dict = raw

class ScrapedWordResponse(_ResponseEntity):
    """
    Contains information about a scraped word search response.
    """

    def __init__(self, raw):
        self.data = _ScrapedWordResponseData(raw)
        self.response_type: Literal['scraped_word'] = 'scraped_word'
        self.raw: dict = raw

class ScrapedExampleResponse(_ResponseEntity):
    """
    Contains information about a scraped example search response.
    """

    def __init__(self, raw):
        self.data = _ScrapedExampleResponseData(raw)
        self.response_type: Literal['scraped_exam'] = 'scraped_exam'
        self.raw: dict = raw

class ScraperTranslationLanguage(IntEnum):
    """Enumeration class that contains translation languages that can be used by the scraper."""

    __aliases__ = {
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
