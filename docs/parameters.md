A summary of expected parameter types for various [functions](main.md).

Functions which expect any of the enumeration types below also accept their underlying string or integer
value, the enumeration name, or a string alias. The [methods and properties](#enumeration-methods)
available on all enumeration types are also detailed below.

---

## Enumerations

### Classification

The word classification of a dictionary entry.
```python
class Classification:
    ALL = 'all'
    WORD = 'word'
    PHRASE = 'phrase'
    EXPRESSION = 'expression'
```

### MeaningCategory

A meaning category which a dictionary entry may belong to.

See [Meaning Category](meaning_category.md) for details.

### MultimediaType

A type of multimedia file.
```python
class MultimediaType:
    ALL = 0
    PHOTO = 1
    ILLUSTRATION = 2
    VIDEO = 3
    ANIMATION = 4
    SOUND = 5
    NONE = 6
```

Aliases:
```bash
'all': 0
'photo': 1
'illustration': 2
'video': 3
'animation': 4
'sound': 5
'none': 6
```

### OriginType

The classification of a dictionary entry's origin.
```python
class OriginType:
    ALL = 'all'
    NATIVE = 'native'
    HANJA = 'chinese'
    LOANWORD = 'loanword'
    HYBRID = 'hybrid'
```

Aliases:
```bash
'hanja': 'chinese'
```

### PartOfSpeech

The Korean part of speech of a dictionary entry.
```python
class PartOfSpeech:
    ALL = 0
    NOUN = 1
    PRONOUN = 2
    NUMERAL = 3
    PARTICLE = 4
    VERB = 5
    ADJECTIVE = 6
    DETERMINER = 7
    ADVERB = 8
    INTERJECTION = 9
    AFFIX = 10
    BOUND_NOUN = 11
    AUXILIARY_VERB = 12
    AUXILIARY_ADJECTIVE = 13
    ENDING = 14
    NONE = 15
```

Aliases:
```bash
'all': 0
'noun': 1
'pronoun': 2
'numeral': 3
'particle': 4
'verb': 5
'adjective': 6
'determiner': 7
'adverb': 8
'interjection': 9
'affix': 10
'bound noun': 11
'bound_noun': 11
'auxiliary verb': 12
'auxiliary_verb': 12
'auxiliary adjective': 13
'auxiliary_adjective': 13
'ending': 14
'none': 15
```

### SubjectCategory

A subject category (themes and situations) which a dictionary entry may belong to.

See [Subject Category](subject_category.md) for details.

### ScraperTranslationLanguage

A language for which translations should be included during a scraper fetch.
```python
class ScraperTranslationLanguage:
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
```

Aliases:
```bash
'all': 0
'english': 1
'japanese': 2
'french': 3
'spanish': 4
'arabic': 5
'mongolian': 6
'vietnamese': 7
'thai': 8
'indonesian': 9
'russian': 10
'chinese': 11
```

### SearchMethod

The method to use when searching.

- `'exact'`: Returns entries that are an exact match of the query.
- `'include'`: Returns entries that include the query.
- `'start'`: Returns entries that start with the query.
- `'end'`: Returns entries that end with the query.

```python
class SearchMethod(StrEnumBase):
    EXACT = 'exact'
    INCLUDE = 'include'
    START = 'start'
    END = 'end'
```

### SearchTarget

The target of the search query; what to search by.
```python
class SearchTarget(IntEnumBase):
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
```

Aliases:
```bash
'headword': 1
'definition': 2
'example': 3
'original language': 4
'original_language': 4
'pronunciation': 5
'application': 6
'application shorthand': 7
'application_shorthand': 7
'idiom': 8
'proverb': 9
'reference info': 10
'reference_info': 10
```

### SearchType

The type of search to perform.
```python
class SearchType:
    IDIOM_PROVERB = 'ip'
    DEFINITION = 'dfn'
    EXAMPLE = 'exam'
    WORD = 'word'
```

Aliases:
```bash
'idiom/proverb': 'ip'
'idiom_proverb': 'ip'
'definition': 'dfn'
'example': 'exam'
```

### SortMethod

A sorting method to use for search results.
```python
class SortMethod(StrEnumBase):
    ALPHABETICAL = 'dict'
    POPULAR = 'popular'
```

Aliases:
```bash
'alphabetical': 'dict'
```

### TargetLanguage

A target original language to search by.
```python
class TargetLanguage(IntEnumBase):
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
    MAORI = 12
    MALAY = 13
    MONGOLIAN = 14
    BASQUE = 15
    BURMESE = 16
    VIETNAMESE = 17
    BULGARIAN = 18
    SANSKRIT = 19
    SERBO_CROATIAN = 20
    SWAHILI = 21
    SWEDISH = 22
    ARABIC = 23
    IRISH = 24
    SPANISH = 25
    UZBEK = 26
    UKRAINIAN = 27
    ITALIAN = 28
    INDONESIAN = 29
    JAPANESE = 30
    CHINESE = 31
    CZECH = 32
    CAMBODIAN = 33
    QUECHUA = 34
    TAGALOG = 35
    THAI = 36
    TURKISH = 37
    TIBETAN = 38
    PERSIAN = 39
    PORTUGUESE = 40
    POLISH = 41
    FRENCH = 42
    PROVENCAL = 43
    FINNISH = 44
    HUNGARIAN = 45
    HEBREW = 46
    HINDI = 47
    OTHER = 48
    DANISH = 49
```

Aliases:
```bash
'all': 0
'native_word': 1
'sino-korean': 2
'sino_korean': 2
'unknown': 3
'english': 4
'greek': 5
'dutch': 6
'norwegian': 7
'german': 8
'latin': 9
'russian': 10
'romanian': 11
'maori': 12
'malay': 13
'mongolian': 14
'basque': 15
'burmese': 16
'vietnamese': 17
'bulgarian': 18
'sanskrit': 19
'serbo-croatian': 20
'serbo_croatian': 20
'swahili': 21
'swedish': 22
'arabic': 23
'irish': 24
'spanish': 25
'uzbek': 26
'ukrainian': 27
'italian': 28
'indonesian': 29
'japanese': 30
'chinese': 31
'czech': 32
'cambodian': 33
'quechua': 34
'tagalog': 35
'thai': 36
'turkish': 37
'tibetan': 38
'persian': 39
'portuguese': 40
'polish': 41
'french': 42
'provencal': 43
'finnish': 44
'hungarian': 45
'hebrew': 46
'hindi': 47
'other': 48
'danish': 49
```

### TranslationLanguage

A language for which translations should be included.
```python
class TranslationLanguage:
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
```

Aliases:
```bash
'all': 0
'english': 1
'japanese': 2
'french': 3
'spanish': 4
'arabic': 5
'mongolian': 6
'vietnamese': 7
'thai': 8
'indonesian': 9
'russian': 10
```

### VocabularyLevel

The vocabulary level of a dictionary entry.
```python
class VocabularyLevel(StrEnumBase):
    ALL = 'all'
    BEGINNER = 'level1'
    INTERMEDIATE = 'level2'
    ADVANCED = 'level3'
```

Aliases:
```bash
'beginner': 'level1'
'intermediate': 'level2'
'advanced': 'level3'
```

## Enumeration Methods

All of the enumeration types in the module define the following:

### aliases

A property that allows access to enumeration aliases via a read-only dictionary.
These aliases, which are documented under each of the types above, can be used
with [`get`](#get) to retrieve an enumeration value.

```python
@property
@staticmethod
def aliases() -> Mapping: ...
```

### get

Returns the enumeration instance associated with a string or integer, or 
`default` if the value is not associated with any enumeration value.

A string key can be the name of an enumeration value, an [alias](#aliases), or
the value of the enumeration in the case of string enumerations.

```python
@staticmethod
def get(key: str | int, default: T = None) -> EnumType | T: ...
```

### get_value

Returns the enumeration value associated with a string or integer, or
`default` if the value is not associated with any enumeration value.

Accepts the same `key` values as [`get`](#get) and returns either a string
or an integer depending on the underlying type of the enumeration type.

```python
@staticmethod
def get_value(key: str | int, default: T = None) -> int | str | T: ...
```

## Other Types

### OptionsDict

Additional options to apply to a query. All of the keys are not required.
```python
{
    'fetch_multimedia': bool, # default: False
    'fetch_page_data': bool, # default: True
    'raise_scraper_errors': bool, # default: False
    'use_scraper': bool # default: False
}
```

- `'fetch_multimedia'`: Controls whether multimedia is scraped during view queries. No effect unless the `'use_scraper'` option is `True`.
- `'fetch_page_data'`: Controls whether pronunciation URLs and extended language information are scraped. No effect unless the `'use_scraper'` option is `True`.
- `'raise_scraper_errors'`: Controls whether errors that occur during scraping are raised. No effect unless the `'use_scraper'` option is `True`.
- `'use_scraper'`: Controls whether the scraper should be used to fetch more information.

See also: [`set_default`](main.md#set_default).


