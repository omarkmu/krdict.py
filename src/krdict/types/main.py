"""
Contains response types defined by the krdict package.
"""

from typing import Literal

# pylint: disable=too-few-public-methods,too-many-instance-attributes


def _to_dict(obj):
    if isinstance(obj, _ResponseEntity):
        return obj.asdict()

    if isinstance(obj, list):
        return list(map(_to_dict, obj))

    return obj


class _ResponseEntity:
    def __contains__(self, key):
        return key in self.__dict__

    def __repr__(self):
        attrs = vars(self).copy()

        if 'raw' in attrs:
            del attrs['raw']

        return repr(attrs)

    def asdict(self):
        """
        Converts the response object to a dict and returns the created dict.
        """

        attrs = {
            k: _to_dict(v)
            for k, v in vars(self).items()
        }

        if 'raw' in attrs:
            del attrs['raw']

        return attrs

class _SearchItem(_ResponseEntity):
    def __init__(self, raw):
        self.target_code: int = raw['target_code']
        self.word: str = raw['word']
        self.url: str = raw['link']

class _ResponseData(_ResponseEntity):
    def __init__(self, raw):
        self.title: str = raw['title']
        self.url: str = raw['link']
        self.description: str = raw['description']
        self.last_build_date: str = raw['lastBuildDate']
        self.page: int = raw['start']
        self.per_page: int = raw['num']
        self.total_results: int = raw['total']

class _SearchTranslation(_ResponseEntity):
    def __init__(self, raw):
        self.word: str = raw.get('trans_word', '')
        self.definition: str = raw['trans_dfn']
        self.language: str = raw['trans_lang']

class _PartialSearchDefinition(_ResponseEntity):
    def __init__(self, raw):
        self.definition: str = raw['definition']
        self.translations = list(map(_SearchTranslation, raw.get('translation', [])))

class _SearchDefinition(_PartialSearchDefinition):
    def __init__(self, raw):
        self.order: int = raw['sense_order']
        super().__init__(raw)


class _WordSearchItem(_SearchItem):
    def __init__(self, raw):
        super().__init__(raw)
        self.part_of_speech: str = raw['pos']
        self.homograph_num: int = raw['sup_no']
        self.origin: str = raw.get('origin', '')
        self.pronunciation: str = raw.get('pronunciation', '')
        self.vocabulary_level: str = raw.get('word_grade', '')
        self.definitions = list(map(_SearchDefinition, raw['sense']))

class _WordResponseData(_ResponseData):
    def __init__(self, raw):
        super().__init__(raw)
        self.results = list(map(_WordSearchItem, raw['item']))


class _DefinitionSearchItem(_SearchItem):
    def __init__(self, raw):
        super().__init__(raw)
        self.homograph_num: int = raw['sup_no']
        self.definition_info = _PartialSearchDefinition(raw['sense'][0])

class _DefinitionResponseData(_ResponseData):
    def __init__(self, raw):
        super().__init__(raw)
        self.results = list(map(_DefinitionSearchItem, raw['item']))


class _ExampleSearchItem(_SearchItem):
    def __init__(self, raw):
        super().__init__(raw)
        self.homograph_num: int = raw['sup_no']
        self.example: str = raw['example']

class _ExampleResponseData(_ResponseData):
    def __init__(self, raw):
        super().__init__(raw)
        self.results = list(map(_ExampleSearchItem, raw['item']))


class _IdiomProverbSearchItem(_SearchItem):
    def __init__(self, raw):
        super().__init__(raw)
        self.definitions = list(map(_SearchDefinition, raw['sense']))

class _IdiomProverbResponseData(_ResponseData):
    def __init__(self, raw):
        super().__init__(raw)
        self.results = list(map(_IdiomProverbSearchItem, raw['item']))


class _ViewOriginalLanguageInfo(_ResponseEntity):
    def __init__(self, raw):
        self.original_language: str = raw['original_language']
        self.language_type: str = raw['language_type']

class _ViewPronunciationInfo(_ResponseEntity):
    def __init__(self, raw):
        self.pronunciation: str = raw['pronunciation']

class _ViewAbbreviationInfo(_ResponseEntity):
    def __init__(self, raw):
        self.abbreviation: str = raw['abbreviation']
        self.pronunciation_info = list(
            map(_ViewPronunciationInfo, raw.get('pronunciation_info', [])))

class _ViewConjugationInfo(_ResponseEntity):
    def __init__(self, raw):
        self.conjugation: str = raw['conjugation']
        info = raw.get('conjugation_info', {})

        self.pronunciation_info = list(map(
            _ViewPronunciationInfo, info.get('pronunciation_info', [])))
        self.abbreviation_info = list(map(
            _ViewAbbreviationInfo, info.get('abbreviation_info', [])))

class _ViewReferenceInfo(_ResponseEntity):
    def __init__(self, raw):
        self.word: str = raw['word']
        self.target_code: int = raw.get('link_target_code', 0)
        self.url: str = raw['link']
        self.has_target_code: bool = raw.get('link_type') == 'C'

class _ViewCategoryInfo(_ResponseEntity):
    def __init__(self, raw):
        self.type: str = raw['type']
        self.name: str = raw['written_form']

class _ViewPatternInfo(_ResponseEntity):
    def __init__(self, raw):
        self.pattern: str = raw['pattern']
        self.pattern_referebce: str = raw.get('pattern_reference', '')

class _ViewExampleInfo(_ResponseEntity):
    def __init__(self, raw):
        self.type: str = raw['type']
        self.example: str = raw['example']

class _ViewRelatedInfo(_ViewReferenceInfo):
    def __init__(self, raw):
        super().__init__(raw)
        self.type: str = raw['type']

class _ViewMultimediaInfo(_ResponseEntity):
    def __init__(self, raw):
        self.label: str = raw['label']
        self.type: str = raw['type']
        self.url: str = raw['link']

class _ViewPartialRelatedInfo(_ResponseEntity):
    def __init__(self, raw):
        self.word: str = raw['word']
        self.type: str = raw['type']

class _ViewSubdefinitionInfo(_ResponseEntity):
    def __init__(self, raw):
        self.definition: str = raw['definition']
        self.translations = list(map(_SearchTranslation, raw.get('translation', [])))
        self.example_info = list(map(_ViewExampleInfo, raw.get('example_info', [])))
        self.related_info = list(map(_ViewPartialRelatedInfo, raw.get('rel_info', [])))

class _ViewSubwordInfo(_ResponseEntity):
    def __init__(self, raw):
        self.subword: str = raw['subword']
        self.subword_unit: str = raw['subword_unit']
        self.subdefinition_info = list(map(_ViewSubdefinitionInfo, raw['subsense_info']))

class _ViewDefinitionInfo(_ResponseEntity):
    def __init__(self, raw):
        self.definition: str = raw['definition']
        self.reference: str = raw.get('reference', '')
        self.translations = list(map(_SearchTranslation, raw.get('translation', [])))
        self.example_info = list(map(_ViewExampleInfo, raw.get('example_info', [])))
        self.pattern_info = list(map(_ViewPatternInfo, raw.get('pattern_info', [])))
        self.related_info = list(map(_ViewRelatedInfo, raw.get('rel_info', [])))
        self.multimedia_info = list(map(_ViewMultimediaInfo, raw.get('multimedia_info', [])))

class _ViewWordInfo(_ResponseEntity):
    def __init__(self, raw):
        self.word: str = raw['word']
        self.word_unit: str = raw['word_unit']
        self.word_type: str = raw['word_type']
        self.part_of_speech: str = raw['pos']
        self.homograph_num: int = raw['sup_no']
        self.vocabulary_level: str = raw['word_grade']
        self.allomorph: str = raw.get('allomorph', '')

        self.definition_info = list(map(_ViewDefinitionInfo, raw['sense_info']))
        self.original_language_info = list(map(
            _ViewOriginalLanguageInfo, raw.get('original_language_info', [])))
        self.pronunciation_info = list(map(
            _ViewPronunciationInfo, raw.get('pronunciation_info', [])))
        self.conjugation_info = list(map(_ViewConjugationInfo, raw.get('conju_info', [])))
        self.derivative_info = list(map(_ViewReferenceInfo, raw.get('der_info', [])))
        self.reference_info = list(map(_ViewReferenceInfo, raw.get('ref_info', [])))
        self.category_info = list(map(_ViewCategoryInfo, raw.get('category_info', [])))
        self.subword_info = list(map(_ViewSubwordInfo, raw.get('subword_info', [])))

class _ViewItem(_ResponseEntity):
    def __init__(self, raw):
        self.target_code: int = raw['target_code']
        self.word_info = _ViewWordInfo(raw['word_info'])

class _ViewResponseData(_ResponseEntity):
    def __init__(self, raw):
        self.title: str = raw['title']
        self.url: str = raw['link']
        self.description: str = raw['description']
        self.last_build_date: str = raw['lastBuildDate']
        self.total_results: int = raw['total']
        self.results = list(map(_ViewItem, raw['item']))



class ErrorResponse(_ResponseEntity):
    """
    Contains information about an error response.
    """

    def __init__(self, raw, request_params):
        self.error_code: int = raw['error']['error_code']
        self.message: str = raw['error']['message']
        self.request_params: dict = request_params
        self.response_type: Literal['error'] = 'error'
        self.raw: dict = raw

class WordResponse(_ResponseEntity):
    """
    Contains information about a word search response.
    """

    def __init__(self, raw, request_params):
        self.data = _WordResponseData(raw['channel'])
        self.request_params: dict = request_params
        self.response_type: Literal['word'] = 'word'
        self.raw: dict = raw

class DefinitionResponse(_ResponseEntity):
    """
    Contains information about a definition search response.
    """

    def __init__(self, raw, request_params):
        self.data = _DefinitionResponseData(raw['channel'])
        self.request_params: dict = request_params
        self.response_type: Literal['dfn'] = 'dfn'
        self.raw: dict = raw

class ExampleResponse(_ResponseEntity):
    """
    Contains information about an example search response.
    """

    def __init__(self, raw, request_params):
        self.data = _ExampleResponseData(raw['channel'])
        self.request_params: dict = request_params
        self.response_type: Literal['exam'] = 'exam'
        self.raw: dict = raw

class IdiomProverbResponse(_ResponseEntity):
    """
    Contains information about an idiom/proverb search response.
    """

    def __init__(self, raw, request_params):
        self.data = _IdiomProverbResponseData(raw['channel'])
        self.request_params: dict = request_params
        self.response_type: Literal['ip'] = 'ip'
        self.raw: dict = raw

class ViewResponse(_ResponseEntity):
    """
    Contains information about a view query response.
    """

    def __init__(self, raw, request_params):
        self.data = _ViewResponseData(raw['channel'])
        self.request_params: dict = request_params
        self.response_type: Literal['view'] = 'view'
        self.raw: dict = raw
