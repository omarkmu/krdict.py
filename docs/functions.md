A summary of the provided functions in the `krdict` module and the arguments they expect.
With the exception of [`set_key`](#set_key) and [`set_default`](#set_default),
all of the functions listed below expect keyword arguments.

---
## advanced_search

Performs an advanced search on the Korean Learner's Dictionary API.

```python
def advanced_search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: SearchType = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    search_target: SearchTarget = None,
    target_language: TargetLanguage = None,
    search_method: SearchMethod = None,
    classification: Classification | List[Classification] = None,
    origin_type: OriginType | List[OriginType] = None,
    vocabulary_grade: VocabularyGrade | List[VocabularyGrade] = None,
    part_of_speech: PartOfSpeech | List[PartOfSpeech] = None,
    multimedia_info: MultimediaType | List[MultimediaType] = None,
    min_syllables: int = None,
    max_syllables: int = None,
    meaning_category: MeaningCategory | int = None,
    subject_category: SubjectCategory | int | List[SubjectCategory | int] = None,
    options: OptionsDict = None
) -> SearchResponse | KRDictError: ...
```
!!! warning
    Use of any value other than `'word'` or `None` for the `search_type` parameter with advanced search is
    undefined behavior. It is likely that incomplete or empty results will be returned.
    The parameter is included for completeness, but is not recommended for usage.

**Parameters:**

- query: The search query.
- raise_api_errors: Sets whether a [`KRDictException`](exceptions.md#krdictexception) will be raised if an API error occurs.
This guarantees that the result is not an error object.
- key: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- page: The page at which the search should start `[1, 1000]` (default `1`).
- per_page: The maximum number of search results to return `[10, 100]` (default `10`).
- sort ([`SortMethod`](parameters.md#sortmethod)): The sort method that should be used (default `'alphabetical'`).
- search_type ([`SearchType`](parameters.md#searchtype)): The type of search to perform (default `'word'`).
- translation_language ([`TranslationLanguage`](parameters.md#translationlanguage)): A language to include translations for.
- search_target ([`SearchTarget`](parameters.md#searchtarget)): The target field of the search query (default `'headword'`).
- target_language ([`TargetLanguage`](parameters.md#targetlanguage)): The original language to search by. If `search_target`
is set to any value other than `'original_language'`, this parameter has no effect (default `'all'`).
- search_method ([`SearchMethod`](parameters.md#searchmethod)): The method used to match against the query (default `'exact'`).
    - `'exact'`: Returns entries that are an exact match of the query.
    - `'include'`: Returns entries that include the query.
    - `'start'`: Returns entries that start with the query.
    - `'end'`: Returns entries that end with the query.
- classification ([`Classification`](parameters.md#classification)): An entry classification to filter by (default `'all'`).
- origin_type ([`OriginType`](parameters.md#origintype)): A word origin type to filter by (default `'all'`).
- vocabulary_grade ([`VocabularyGrade`](parameters.md#vocabularygrade)): A vocabulary level to filter by (default `'all'`).
- part_of_speech ([`PartOfSpeech`](parameters.md#partofspeech)): A part of speech to filter by (default `'all'`).
- multimedia_info ([`MultimediaType`](parameters.md#multimediatype)): A multimedia type to filter by (default `'all'`).
- min_syllables: The minimum number of syllables in result words `[1, inf)` (default `1`).
- max_syllables: The maximum number of syllables in results words. A value of `0` denotes no maximum `[0, inf)` (default `0`).
- meaning_category ([`MeaningCategory`](parameters.md#meaningcategory)): The meaning category to filter by (default `'all'`).
- subject_category ([`SubjectCategory`](parameters.md#subjectcategory)): A subject category to filter by (default `'all'`).
- options ([`OptionsDict`](parameters.md#optionsdict)): Additional options to apply.


**Returns**:

Depending on the value of `search_type` and whether an error occurred, returns one of:

- [`WordSearchResponse`](return_types.md#wordsearchresponse)
- [`DefinitionSearchResponse`](return_types.md#definitionsearchresponse)
- [`ExampleSearchResponse`](return_types.md#examplesearchresponse)
- [`IdiomProverbSearchResponse`](return_types.md#idiomproverbsearchresponse)
- [`KRDictError`](return_types.md#krdicterror)

---

## search

Performs a basic search on the Korean Learner's Dictionary API.

```python
def search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    search_type: SearchType = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> SearchResponse | KRDictError: ...
```

**Parameters:**

- query: The search query.
- raise_api_errors: Sets whether a [`KRDictException`](exceptions.md#krdictexception) will be raised if an API error occurs.
This guarantees that the result is not an error object.
- key: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- page: The page at which the search should start `[1, 1000]` (default `1`).
- per_page: The maximum number of search results to return `[10, 100]` (default `10`).
- sort ([`SortMethod`](parameters.md#sortmethod)): The sort method that should be used (default `'alphabetical'`).
- search_type ([`SearchType`](parameters.md#searchtype)): The type of search to perform (default `'word'`).
- translation_language ([`TranslationLanguage`](parameters.md#translationlanguage)): A language to include translations for.
- options ([`OptionsDict`](parameters.md#optionsdict)): Additional options to apply.


**Returns**:

Depending on the value of `search_type` and whether an error occurred, returns one of:

- [`WordSearchResponse`](return_types.md#wordsearchresponse)
- [`DefinitionSearchResponse`](return_types.md#definitionsearchresponse)
- [`ExampleSearchResponse`](return_types.md#examplesearchresponse)
- [`IdiomProverbSearchResponse`](return_types.md#idiomproverbsearchresponse)
- [`KRDictError`](return_types.md#krdicterror)

---

## set_default

Sets a default value for a library [option](parameters.md#optionsdict).

```python
def set_default(name: Option, value: bool) -> None: ...
```

**Parameters:**

- name: The name of the option to set. Accepted values:
    - `'fetch_multimedia'`: Controls whether multimedia is scraped during view queries. No effect unless the `'use_scraper'` option is `True`.
    - `'fetch_page_data'`: Controls whether pronunciation URLS and extended language information are scraped. No effect unless the `'use_scraper'` option is `True`.
    - `'raise_scraper_errors'`: Controls whether errors that occur during scraping are raised. No effect unless the `'use_scraper'` option is `True`.
    - `'use_scraper'`: Controls whether the scraper should be used to fetch more information.
- value: The new default value of the option.

---

## set_key

Sets a default API key to use, if one is not provided in a query.

```python
def set_key(key: str | None) -> None: ...
```

**Parameters:**

- key: The Korean Learner's Dictionary API key. To unset a key, use `None`.

---

## view

Performs a view query, which retrieves information about a particular entry, on the Korean Learner's Dictionary API.

```python
def view(*,
    query: str,
    raise_api_errors: bool = False,
    homograph_num: int = None,
    key: str = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> ViewResponse | KRDictError: ...

def view(*,
    target_code: int,
    raise_api_errors: bool = False,
    key: str = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None,
    options: OptionsDict = None
) -> ViewResponse | KRDictError: ...
```

**Parameters:**

- query: The search query.
- raise_api_errors: Sets whether a [`KRDictException`](exceptions.md#krdictexception) will be raised if an API error occurs.
This guarantees that the result is not an error object.
- homograph_num: The superscript number used to distinguish homographs (default `0`).
- target_code: The target code of the desired result.
- key: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- translation_language ([`TranslationLanguage`](parameters.md#translationlanguage)): A language or list of
languages to include translations for.
- options ([`OptionsDict`](parameters.md#optionsdict)): Additional options to apply.


**Returns:**

Depending on whether an error occurred, returns [`ViewResponse`](return_types.md#viewresponse) or
[`KRDictError`](return_types.md#krdicterror).
