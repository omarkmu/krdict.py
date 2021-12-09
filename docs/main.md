A summary of the provided functions in the `krdict` package and the arguments they expect.
With the exception of [`set_key`](#set_key),
all of the functions listed below expect keyword arguments.

The `krdict` package also exports all of the enumerations described in
the [parameter types](#parameters) of the functions below.

---
## advanced_search

Performs an advanced search on the Korean Learners' Dictionary API.

```python
def advanced_search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    page: int = 1,
    per_page: int = 10,
    sort: SortMethod = SortMethod.ALPHABETICAL,
    search_type: SearchType = SearchType.WORD,
    translation_language: TranslationLanguage | Iterable[TranslationLanguage] = None,
    search_target: SearchTarget = SearchTarget.HEADWORD,
    target_language: TargetLanguage = TargetLanguage.ALL,
    search_method: SearchMethod = SearchMethod.EXACT,
    classification: Classification | Iterable[Classification] = Classification.ALL,
    origin_type: OriginType | Iterable[OriginType] = OriginType.ALL,
    vocabulary_level: VocabularyLevel | Iterable[VocabularyLevel] = VocabularyLevel.ALL,
    part_of_speech: PartOfSpeech | Iterable[PartOfSpeech] = PartOfSpeech.ALL,
    multimedia_type: MultimediaType | Iterable[MultimediaType] = MultimediaType.ALL,
    min_syllables: int = 1,
    max_syllables: int = 0,
    meaning_category: MeaningCategory = MeaningCategory.ALL,
    subject_category: SubjectCategory | Iterable[SubjectCategory] = SubjectCategory.ALL
) -> SearchResponse | KRDictError: ...
```
!!! warning
    Use of any search type other than `SearchType.WORD` for the `search_type` parameter with advanced search is
    undefined behavior. It is likely that incomplete or empty results will be returned.
    The parameter is included for completeness, but is not recommended for usage.

**Parameters:**

- `query`: The search query.
- `raise_api_errors`: Sets whether a [`KRDictException`](exceptions.md#krdictexception) will be raised if an API error occurs.
A value of `True` guarantees that the result is not an error object.
    - The empty string `""` for string values.
    - Zero `0` for integer values.
    - An empty list `[]` for list values.
- `key`: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- `page`: The page at which the search should start `[1, 1000]`.
- `per_page`: The maximum number of search results to return `[10, 100]`.
- `sort` ([`SortMethod`](parameters.md#sortmethod)): The sort method that should be used.
- `search_type` ([`SearchType`](parameters.md#searchtype)): The type of search to perform.
- `translation_language` ([`TranslationLanguage`](parameters.md#translationlanguage)): A language for which translations should be included.
- `search_target` ([`SearchTarget`](parameters.md#searchtarget)): The target field of the search query.
- `target_language` ([`TargetLanguage`](parameters.md#targetlanguage)): The original language to search by. If `search_target`
is set to any value other than `'original_language'`, this parameter has no effect.
- `search_method` ([`SearchMethod`](parameters.md#searchmethod)): The method used to match against the query.
- `classification` ([`Classification`](parameters.md#classification)): An entry classification to filter by.
- `origin_type` ([`OriginType`](parameters.md#origintype)): A word origin type to filter by.
- `vocabulary_level` ([`VocabularyLevel`](parameters.md#vocabularylevel)): A vocabulary level to filter by.
- `part_of_speech` ([`PartOfSpeech`](parameters.md#partofspeech)): A part of speech to filter by.
- `multimedia_type` ([`MultimediaType`](parameters.md#multimediatype)): A multimedia type to filter by.
- `min_syllables`: The minimum number of syllables in result words `[1, 80]`.
- `max_syllables`: The maximum number of syllables in results words. A value of `0` denotes no maximum `[0, 80]`.
- `meaning_category` ([`MeaningCategory`](parameters.md#meaningcategory)): The meaning category to filter by.
- `subject_category` ([`SubjectCategory`](parameters.md#subjectcategory)): A subject category to filter by.


**Returns**:

Depending on the value of `search_type` and whether an error occurred, returns one of:

- [`WordSearchResponse`](return_types.md#wordsearchresponse)
- [`DefinitionSearchResponse`](return_types.md#definitionsearchresponse) **(potentially empty or incomplete)**
- [`ExampleSearchResponse`](return_types.md#examplesearchresponse) **(potentially empty or incomplete)**
- [`IdiomProverbSearchResponse`](return_types.md#idiomproverbsearchresponse) **(potentially empty or incomplete)**
- [`KRDictError`](return_types.md#krdicterror)

---

## search

Performs a basic search on the Korean Learners' Dictionary API.

```python
def search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    page: int = 1,
    per_page: int = 10,
    sort: SortMethod = SortMethod.ALPHABETICAL,
    search_type: SearchType = SearchType.WORD,
    translation_language: TranslationLanguage | Iterable[TranslationLanguage] = None
) -> SearchResponse | KRDictError: ...
```

**Parameters:**

- `query`: The search query.
- `raise_api_errors`: Sets whether a [`KRDictException`](exceptions.md#krdictexception) will be raised if an API error occurs.
A value of `True` guarantees that the result is not an error object.
    - The empty string `""` for string values.
    - Zero `0` for integer values.
    - An empty list `[]` for list values.
- `key`: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- `page`: The page at which the search should start `[1, 1000]`.
- `per_page`: The maximum number of search results to return `[10, 100]`.
- `sort` ([`SortMethod`](parameters.md#sortmethod)): The sort method that should be used.
- `search_type` ([`SearchType`](parameters.md#searchtype)): The type of search to perform.
- `translation_language` ([`TranslationLanguage`](parameters.md#translationlanguage)): A language for which translations should be included.


**Returns**:

Depending on the value of `search_type` and whether an error occurred, returns one of:

- [`WordSearchResponse`](return_types.md#wordsearchresponse)
- [`DefinitionSearchResponse`](return_types.md#definitionsearchresponse)
- [`ExampleSearchResponse`](return_types.md#examplesearchresponse)
- [`IdiomProverbSearchResponse`](return_types.md#idiomproverbsearchresponse)
- [`KRDictError`](return_types.md#krdicterror)

---

## set_key

Sets a default API key to use, if one is not provided in a query.

```python
def set_key(key: str | None) -> None: ...
```

**Parameters:**

- key: The Korean Learners' Dictionary API key. To unset a key, use `None`.

---

## view

Performs a view query, which retrieves information about a particular entry, on the Korean Learners' Dictionary API.

```python
def view(*,
    query: str,
    homograph_num: int = 0,
    raise_api_errors: bool = False,
    key: str = None,
    translation_language: TranslationLanguage | Iterable[TranslationLanguage] = None
) -> ViewResponse | KRDictError: ...

def view(*,
    target_code: int,
    raise_api_errors: bool = False,
    key: str = None,
    translation_language: TranslationLanguage | Iterable[TranslationLanguage] = None
) -> ViewResponse | KRDictError: ...
```

**Parameters:**

- `query`: The search query.
- `homograph_num`: The superscript number used to distinguish homographs.
- `target_code`: The target code of the desired result.
- `raise_api_errors`: Sets whether a [`KRDictException`](exceptions.md#krdictexception) will be raised if an API error occurs.
A value of `True` guarantees that the result is not an error object.
    - The empty string `""` for string values.
    - Zero `0` for integer values.
    - An empty list `[]` for list values.
- `key`: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- `translation_language` ([`TranslationLanguage`](parameters.md#translationlanguage)): A language for which translations
should be included.


**Returns:**

Depending on whether an error occurred, returns [`ViewResponse`](return_types.md#viewresponse) or
[`KRDictError`](return_types.md#krdicterror).
