"""
Contains types defined by the krdict.scraper module.
"""

from typing import Literal
from .base import IntEnum, StrEnum
from .main import (
    _PartialSearchDefinition,
    _ResponseEntity,
    _SearchDefinition,
    _SearchItem,
    _SearchTranslation
)

# pylint: disable=too-few-public-methods,too-many-instance-attributes


class _ScrapedTranslationURLInfo(_ResponseEntity):
    def __init__(self, raw):
        self.url: str = raw['url']
        self.language: str = raw['language']

class _ScrapedSearchItem(_SearchItem):
    def __init__(self, raw):
        super().__init__(raw)
        self.translation_urls = list(map(_ScrapedTranslationURLInfo, raw.get('trans_link', [])))

class _ScrapedResponseData(_ResponseEntity):
    def __init__(self, raw):
        self.url: str = raw['link']
        self.translation_urls = list(map(_ScrapedTranslationURLInfo, raw.get('trans_link', [])))
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
        self.definitions = list(map(_SearchDefinition, raw['sense']))

class _ScrapedWordResponseData(_ScrapedResponseData):
    def __init__(self, raw):
        super().__init__(raw)
        self.results = list(map(_ScrapedWordSearchItem, raw['item']))


class _ScrapedDefinitionSearchItem(_ScrapedSearchItem):
    def __init__(self, raw):
        super().__init__(raw)
        self.homograph_num: int = raw['sup_no']
        self.definition_info = _PartialSearchDefinition(raw['sense'][0])

class _ScrapedDefinitionResponseData(_ScrapedResponseData):
    def __init__(self, raw):
        super().__init__(raw)
        self.results = list(map(_ScrapedDefinitionSearchItem, raw['item']))


class _ScrapedExampleSearchItem(_ScrapedSearchItem):
    def __init__(self, raw):
        super().__init__(raw)
        self.homograph_num: int = raw['sup_no']
        self.example: str = raw['example']

class _ScrapedExampleResponseData(_ScrapedResponseData):
    def __init__(self, raw):
        super().__init__(raw)
        self.results = list(map(_ScrapedExampleSearchItem, raw['item']))


class _ScrapedIdiomProverbSearchItem(_ScrapedSearchItem):
    def __init__(self, raw):
        super().__init__(raw)
        self.definitions = list(map(_SearchDefinition, raw['sense']))

class _ScrapedIdiomProverbResponseData(_ScrapedResponseData):
    def __init__(self, raw):
        super().__init__(raw)
        self.results = list(map(_ScrapedIdiomProverbSearchItem, raw['item']))


class _WordOfTheDayData(_ResponseEntity):
    def __init__(self, raw):
        self.target_code: int = raw['target_code']
        self.word: str = raw['word']
        self.url: str = raw['link']
        self.translation_urls = list(map(_ScrapedTranslationURLInfo, raw.get('trans_link', [])))
        self.part_of_speech: str = raw.get('pos', '')
        self.homograph_num: int = raw['sup_no']
        self.origin: str = raw.get('origin', '')
        self.vocabulary_level: str = raw.get('word_grade', '')
        self.pronunciation: str = raw.get('pronunciation', '')
        self.pronunciation_urls: list[str] = raw.get('pronunciation_urls', [])
        self.definition: str = raw['definition']
        self.translations = list(map(_SearchTranslation, raw.get('translation', [])))


class _ViewHanjaInfo(_ResponseEntity):
    def __init__(self, raw):
        self.hanja: str = raw['hanja']
        self.radical: str = raw['radical']
        self.stroke_count: int = raw['stroke_count']
        self.readings: list[str] = raw['readings']

class _ViewOriginalLanguageInfo(_ResponseEntity):
    def __init__(self, raw):
        self.original_language: str = raw['original_language']
        self.language_type: str = raw['language_type']
        self.hanja_info = list(map(_ViewHanjaInfo, raw.get('hanja_info', [])))

class _ScrapedViewPronunciationInfo(_ResponseEntity):
    def __init__(self, raw):
        self.pronunciation: str = raw['pronunciation']
        self.url: str = raw.get('link', '')

class _ScrapedViewAbbreviationInfo(_ResponseEntity):
    def __init__(self, raw):
        self.abbreviation: str = raw['abbreviation']
        self.pronunciation_info = list(
            map(_ScrapedViewPronunciationInfo, raw.get('pronunciation_info', [])))

class _ScrapedViewConjugationInfo(_ResponseEntity):
    def __init__(self, raw):
        info = raw.get('conjugation_info', {})

        self.conjugation: str = info.get('conjugation', '')
        self.pronunciation_info = list(map(
            _ScrapedViewPronunciationInfo, info.get('pronunciation_info', [])))
        self.abbreviation_info = list(map(
            _ScrapedViewAbbreviationInfo, raw.get('abbreviation_info', [])))

class _ScrapedViewDerivativeInfo(_ResponseEntity):
    def __init__(self, raw):
        self.word: str = raw['word']
        self.target_code: int = raw.get('link_target_code', 0)
        self.url: str = raw.get('link', '')
        self.has_target_code: bool = raw.get('link_type') == 'C'

class _ScrapedViewPatternInfo(_ResponseEntity):
    def __init__(self, raw):
        self.pattern: str = raw['pattern']

class _ScrapedViewExampleInfo(_ResponseEntity):
    def __init__(self, raw):
        self.example: str = raw['example']

class _ScrapedViewRelatedInfo(_ScrapedViewDerivativeInfo):
    def __init__(self, raw):
        super().__init__(raw)
        self.type: str = raw['type']

class _ScrapedViewMultimediaInfo(_ResponseEntity):
    def __init__(self, raw):
        self.label: str = raw['label']
        self.type: str = raw['type']
        self.file_number: int = raw['file_no']
        self.url: str = raw['link']
        self.thumbnail_url: str = raw['thumb_link']
        self.content_urls: list[str] = raw.get('content_urls', [])

class _ScrapedPartialViewDefinitionInfo(_ResponseEntity):
    def __init__(self, raw):
        self.definition: str = raw['definition']
        self.reference: str = raw.get('reference', '')
        self.translations = list(map(_SearchTranslation, raw.get('translation', [])))
        self.example_info = list(map(_ScrapedViewExampleInfo, raw.get('example_info', [])))
        self.pattern_info = list(map(_ScrapedViewPatternInfo, raw.get('pattern_info', [])))
        self.pattern_reference: str = raw.get('pattern_reference', '')
        self.related_info = list(map(_ScrapedViewRelatedInfo, raw.get('rel_info', [])))

class _ScrapedViewDefinitionInfo(_ScrapedPartialViewDefinitionInfo):
    def __init__(self, raw):
        super().__init__(raw)
        self.multimedia_info = list(map(_ScrapedViewMultimediaInfo, raw.get('multimedia_info', [])))

class _ScrapedViewSubwordInfo(_ResponseEntity):
    def __init__(self, raw):
        self.subword: str = raw['subword']
        self.subword_type: str = raw['subword_unit']
        self.subdefinition_info = list(map(_ScrapedPartialViewDefinitionInfo, raw['subsense_info']))

class _ScrapedViewWordInfo(_ResponseEntity):
    def __init__(self, raw):
        self.word: str = raw['word']
        self.part_of_speech: str = raw.get('pos', '')
        self.homograph_num: int = raw['sup_no']
        self.vocabulary_level: str = raw['word_grade']
        self.allomorph: str = raw.get('allomorph', '')
        self.reference: str = raw.get('reference', '')

        self.definition_info = list(map(_ScrapedViewDefinitionInfo, raw['sense_info']))
        self.original_language_info = list(map(
            _ViewOriginalLanguageInfo, raw.get('original_language_info', [])))
        self.pronunciation_info = list(map(
            _ScrapedViewPronunciationInfo, raw.get('pronunciation_info', [])))
        self.conjugation_info = list(map(_ScrapedViewConjugationInfo, raw.get('conju_info', [])))
        self.derivative_info = list(map(_ScrapedViewDerivativeInfo, raw.get('der_info', [])))
        self.subword_info = list(map(_ScrapedViewSubwordInfo, raw.get('subword_info', [])))

class _ScrapedViewItem(_ResponseEntity):
    def __init__(self, raw):
        self.target_code: int = raw['target_code']
        self.word_info = _ScrapedViewWordInfo(raw['word_info'])

class _ScrapedViewResponseData(_ResponseEntity):
    def __init__(self, raw):
        self.url: str = raw['link']
        self.translation_urls = list(map(_ScrapedTranslationURLInfo, raw.get('trans_link', [])))
        self.total_results: int = raw['total']
        self.results = list(map(_ScrapedViewItem, raw['item']))


class WordOfTheDayResponse(_ResponseEntity):
    """
    Contains information about the word of the day.
    """

    def __init__(self, raw):
        self.data = _WordOfTheDayData(raw['item'])
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

class ScrapedDefinitionResponse(_ResponseEntity):
    """
    Contains information about a scraped definition search response.
    """

    def __init__(self, raw):
        self.data = _ScrapedDefinitionResponseData(raw)
        self.response_type: Literal['scraped_dfn'] = 'scraped_dfn'
        self.raw: dict = raw

class ScrapedExampleResponse(_ResponseEntity):
    """
    Contains information about a scraped example search response.
    """

    def __init__(self, raw):
        self.data = _ScrapedExampleResponseData(raw)
        self.response_type: Literal['scraped_exam'] = 'scraped_exam'
        self.raw: dict = raw

class ScrapedIdiomProverbResponse(_ResponseEntity):
    """
    Contains information about a scraped idiom/proverb search response.
    """

    def __init__(self, raw):
        self.data = _ScrapedIdiomProverbResponseData(raw)
        self.response_type: Literal['scraped_ip'] = 'scraped_ip'
        self.raw: dict = raw

class ScrapedViewResponse(_ResponseEntity):
    """
    Contains information about a scraped view response.
    """

    def __init__(self, raw):
        self.data = _ScrapedViewResponseData(raw)
        self.response_type: Literal['scraped_view'] = 'scraped_view'
        self.raw: dict = raw

class ScraperSearchTarget(IntEnum):
    """Enumeration class that contains scraper search targets."""

    __aliases__ = {
        'headword': 1,
        'definition': 2,
        'example': 3,
        'original language': 4,
        'original_language': 4,
        'pronunciation': 5,
        'application': 6,
        'application shorthand': 7,
        'application_shorthand': 7,
        'idiom': 8,
        'proverb': 9,
        'reference info': 10,
        'reference_info': 10,
        'translation_headword': 11,
        'translation_definition': 12,
        'translation_idiom_proverb': 13
    }

    HEADWORD = 1
    DEFINITION = 2
    EXAMPLE = 3
    ORIGINAL_LANGUAGE = 4
    PRONUNCIATION = 5
    APPLICATION = 6
    APPLICATION_SHORTHAND = 7
    IDIOM = 8
    PROVERB = 9
    REFERENCE_INFO = 10
    TRANSLATION_HEADWORD = 11
    TRANSLATION_DEFINITION = 12
    TRANSLATION_IDIOM_PROVERB= 13

class ScraperTargetLanguage(IntEnum):
    """Enumeration class that contains scraper target languages."""

    __aliases__ = {
        'all': 0,
        'native_word': 1,
        'sino-korean': 2,
        'sino_korean': 2,
        'unknown': 3,
        'english': 4,
        'greek': 5,
        'dutch': 6,
        'norwegian': 7,
        'german': 8,
        'latin': 9,
        'russian': 10,
        'romanian': 11,
        'malay': 13,
        'mongolian': 14,
        'vietnamese': 17,
        'bulgarian': 18,
        'sanskrit': 19,
        'serbo-croatian': 20,
        'serbo_croatian': 20,
        'swedish': 22,
        'arabic': 23,
        'spanish': 25,
        'italian': 28,
        'indonesian': 29,
        'japanese': 30,
        'chinese': 31,
        'czech': 32,
        'thai': 36,
        'turkish': 37,
        'persian': 39,
        'portuguese': 40,
        'polish': 41,
        'french': 42,
        'hungarian': 45,
        'hebrew': 46,
        'hindi': 47,
        'other': 48
    }

    ALL = 0
    NATIVE_WORD = 1
    SINO_KOREAN = 2
    UNKNOWN = 3
    ENGLISH = 4
    GREEK = 5
    DUTCH = 6
    NORWEGIAN = 7
    GERMAN = 8
    LATIN = 9
    RUSSIAN = 10
    ROMANIAN = 11
    MALAY = 13
    MONGOLIAN = 14
    VIETNAMESE = 17
    BULGARIAN = 18
    SANSKRIT = 19
    SERBO_CROATIAN = 20
    SWEDISH = 22
    ARABIC = 23
    SPANISH = 25
    ITALIAN = 28
    INDONESIAN = 29
    JAPANESE = 30
    CHINESE = 31
    CZECH = 32
    THAI = 36
    TURKISH = 37
    PERSIAN = 39
    PORTUGUESE = 40
    POLISH = 41
    FRENCH = 42
    HUNGARIAN = 45
    HEBREW = 46
    HINDI = 47
    OTHER = 48

class ScraperTranslationLanguage(IntEnum):
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

class ScraperVocabularyLevel(StrEnum):
    """Enumeration class that contains scraper vocabulary levels."""

    __aliases__ = {
        'beginner': 'level1',
        'intermediate': 'level2',
        'advanced': 'level3'
    }

    ALL = 'all'
    BEGINNER = 'level1'
    INTERMEDIATE = 'level2'
    ADVANCED = 'level3'
    NONE = 'none'
