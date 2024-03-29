A summary of the provided functions in the `krdict` package and the arguments they expect.
With the exception of [`set_key`](#set_key),
all of the functions listed below expect keyword arguments.

The `krdict` package also directly exports all of the enumerations described in
the [parameter types](enums.md) of the functions below.

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
    semantic_category: SemanticCategory = SemanticCategory.ALL,
    subject_category: SubjectCategory | Iterable[SubjectCategory] = SubjectCategory.ALL,
    search_conditions: Iterable[SearchCondition] = None
) -> WordResponse | DefinitionResponse | ExampleResponse | IdiomProverbResponse | ErrorResponse: ...
```
!!! warning
    Use of any search type other than `SearchType.WORD` for the `search_type` parameter with advanced search is
    undefined behavior. It is likely that incomplete or empty results will be returned.
    The parameter is included for completeness, but is not recommended for usage.

**Parameters:**

- `query`: The search query.
- `raise_api_errors`: Sets whether a [`KRDictException`](other.md#krdictexception) will be raised if an API error occurs.
A value of `True` guarantees that the result is not an [`ErrorResponse`](return_types.md#errorresponse).
- `key`: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- `page`: The page at which the search should start `[1, 1000]`.
- `per_page`: The maximum number of search results to return `[10, 100]`.
- `sort`: The sort method that should be used.
- `search_type`: The type of search to perform.
- `translation_language`: A language for which translations should be included.
- `search_target`: The target field of the search query.
- `target_language`: The original language to search by. If `search_target`
is set to any value other than `'original_language'`, this parameter has no effect.
- `search_method`: The method used to match against the query.
- `classification`: An entry classification to filter by.
- `origin_type`: A word origin type to filter by.
- `vocabulary_level`: A vocabulary level to filter by.
- `part_of_speech`: A part of speech to filter by.
- `multimedia_type`: A multimedia type to filter by.
- `min_syllables`: The minimum number of syllables in result words `[1, 80]`.
- `max_syllables`: The maximum number of syllables in result words. A value of `0` denotes no maximum `[0, 80]`.
- `semantic_category`: The semantic category to filter by.
- `subject_category`: A subject category to filter by.
- `search_conditions`: A list of dicts describing additional search conditions for the search.


**Returns**:

Depending on the value of `search_type` and whether an error occurred, returns one of:

- [`WordResponse`](return_types.md#wordresponse)
- [`DefinitionResponse`](return_types.md#definitionresponse) **(potentially empty or incomplete)**
- [`ExampleResponse`](return_types.md#exampleresponse) **(potentially empty or incomplete)**
- [`IdiomProverbResponse`](return_types.md#idiomproverbresponse) **(potentially empty or incomplete)**
- [`ErrorResponse`](return_types.md#errorresponse)

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
) -> WordResponse | DefinitionResponse | ExampleResponse | IdiomProverbResponse | ErrorResponse: ...
```

**Parameters:**

- `query`: The search query.
- `raise_api_errors`: Sets whether a [`KRDictException`](other.md#krdictexception) will be raised if an API error occurs.
A value of `True` guarantees that the result is not an [`ErrorResponse`](return_types.md#errorresponse).
- `key`: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- `page`: The page at which the search should start `[1, 1000]`.
- `per_page`: The maximum number of search results to return `[10, 100]`.
- `sort`: The sort method that should be used.
- `search_type`: The type of search to perform.
- `translation_language`: A language
for which translations should be included.


**Returns**:

Depending on the value of `search_type` and whether an error occurred, returns one of:

- [`WordResponse`](return_types.md#wordresponse)
- [`DefinitionResponse`](return_types.md#definitionresponse)
- [`ExampleResponse`](return_types.md#exampleresponse)
- [`IdiomProverbResponse`](return_types.md#idiomproverbresponse)
- [`ErrorResponse`](return_types.md#errorresponse)

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

Performs a view query, which retrieves information about a particular entry on the Korean Learners' Dictionary API.

```python
def view(*,
    query: str,
    homograph_num: int = 0,
    raise_api_errors: bool = False,
    key: str = None,
    translation_language: TranslationLanguage | Iterable[TranslationLanguage] = None
) -> ViewResponse | ErrorResponse: ...

def view(*,
    target_code: int,
    raise_api_errors: bool = False,
    key: str = None,
    translation_language: TranslationLanguage | Iterable[TranslationLanguage] = None
) -> ViewResponse | ErrorResponse: ...
```

**Parameters:**

- `query`: The search query.
- `homograph_num`: The superscript number used to distinguish homographs.
- `target_code`: The target code of the desired result.
- `raise_api_errors`: Sets whether a [`KRDictException`](other.md#krdictexception) will be raised if an API error occurs.
A value of `True` guarantees that the result is not an [`ErrorResponse`](return_types.md#errorresponse).
- `key`: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- `translation_language`: A language for which translations
should be included.
