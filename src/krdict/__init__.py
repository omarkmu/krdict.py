"""
Provides functions that query the Korean Learners' Dictionary API.
"""

from . import scraper
from .request import send_request, set_default, set_key
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

def advanced_search(**kwargs):
    """
    Performs an advanced search on the Korean Learners' Dictionary API.
    Returns a dict with contents dependent on the value of the ``search_type``
    parameter and whether an error occurred.

    See the [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/)
    for details about return types.

    - ``query``: The search query.
    - ``raise_api_errors``: Sets whether a ``KRDictException`` will be raised if an API error
    occurs. A value of ``True`` guarantees that the result is not an error object.
    - ``guarantee_keys``: Sets whether keys that are missing from the response should be inserted
    with default values. A value of ``True`` guarantees that every key that is not required
    is included, including keys set by the scraper. Default values:
        - The empty string `""` for string values.
        - Zero `0` for integer values.
        - An empty list `[]` for list values.
    - ``key``: The API key. If a key was set with ``set_key``, this can be omitted.
    - ``page``: The page at which the search should start ``[1, 1000]``.
    - ``per_page``: The maximum number of search results to return ``[10, 100]``.
    - ``sort``: The sort method that should be used ``'alphabetical' | 'dict'``.
    - ``search_type``: The type of search to perform
    ``'word' | 'idiom_proverb' | 'definition' | 'example'``.
        - Note: Values other than ``'word'`` are unsupported and not recommended for use.
    - ``translation_language``: A language or list of languages to include translations for.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#translationlanguage).
    - ``search_target``: The target field of the search query.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#searchtarget).
    - ``target_language``: The original language to search by. If ``search_target``
    is set to any value other than ``'original_language'``, this parameter has no effect.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#targetlanguage).
    - ``search_method``: The method used to match against the query.
    ``'exact' |'include' |'start' |'end'``
    - ``classification``: An entry classification to filter by.
    ``'all' | 'word' | 'phrase' | 'expression'``
    - ``origin_type``: A word origin type to filter by.
    ``'all' | 'native' | 'hanja' | 'loanword' | 'hybrid'``
    - ``vocabulary_grade``: A vocabulary level to filter by.
    ``'all' | 'beginner' | 'intermediate' | 'advanced'``
    - ``part_of_speech``: A part of speech to filter by.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#partofspeech).
    - ``multimedia_info``: A multimedia type to filter by.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#multimediatype).
    - ``min_syllables``: The minimum number of syllables in result words ``[1, 80]``.
    - ``max_syllables``: The maximum number of syllables in results words. A value of ``0`` denotes
    no maximum ``[0, 80]``.
    - ``meaning_category``: The meaning category to filter by.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#meaningcategory).
    - ``subject_category``: A subject category to filter by.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#subjectcategory).
    - ``options``: Additional options to apply.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#optionsdict).

    """

    kwargs = kwargs.copy()
    kwargs['advanced'] = 'y'
    return send_request(kwargs)

def search(**kwargs):
    """
    Performs a search on the Korean Learners' Dictionary API.
    Returns a dict with contents dependent on the value of the ``search_type``
    parameter and whether an error occurred.

    See the [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/)
    for details about return types.

    - ``query``: The search query.
    - ``raise_api_errors``: Sets whether a ``KRDictException`` will be raised if an API error
    occurs. A value of ``True`` guarantees that the result is not an error object.
    - ``guarantee_keys``: Sets whether keys that are missing from the response should be inserted
    with default values. A value of ``True`` guarantees that every key that is not required
    is included, including keys set by the scraper. Default values:
        - The empty string `""` for string values.
        - Zero `0` for integer values.
        - An empty list `[]` for list values.
    - ``key``: The API key. If a key was set with ``set_key``, this can be omitted.
    - ``page``: The page at which the search should start ``[1, 1000]``.
    - ``per_page``: The maximum number of search results to return ``[10, 100]``.
    - ``sort``: The sort method that should be used ``'alphabetical' | 'dict'``.
    - ``search_type``: The type of search to perform
    ``'word' | 'idiom_proverb' | 'definition' | 'example'``.
    - ``translation_language``: A language or list of languages to include translations for.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#translationlanguage).
    - ``options``: Additional options to apply.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#optionsdict).

    """

    return send_request(kwargs)

def view(**kwargs):
    """
    Performs a view query on the Korean Learners' Dictionary API.
    Returns either a dict with information about a dictionary entry, or an error object
    if an error occurred.

    See the [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/)
    for details about return types.

    - ``query``: The search query.
    - ``homograph_num``: The superscript number used to distinguish homographs.
    - ``target_code``: The target code of the desired result.
    - ``raise_api_errors``: Sets whether a KRDictException will be raised if an API error occurs.
    A value of ``True`` guarantees that the result is not an error object.
    - ``guarantee_keys``: Sets whether keys that are missing from the response should be inserted
    with default values. A value of ``True`` guarantees that every key that is not required
    is included, including keys set by the scraper. Default values:
        - The empty string `""` for string values.
        - Zero `0` for integer values.
        - An empty list `[]` for list values.
    - ``key``: The API key. If a key was set with set_key, this can be omitted.
    - ``translation_language``: A language or list of languages to include translations for.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#translationlanguage).
    - ``options``: Additional options to apply.
    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/parameters/#optionsdict).

    """

    return send_request(kwargs, 'view')


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
