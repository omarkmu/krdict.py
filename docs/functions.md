# Functions

A summary of provided functions and the arguments they expect.
With the exception of [`set_key`](#set_key), all of the functions listed below expect keyword arguments.

---
### advanced_search

Performs an advanced search on the Korean Learner's Dictionary API.

```python
def advanced_search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    start_index: int = None,
    num_results: int = None,
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
    subject_category: SubjectCategory | int | List[SubjectCategory | int] = None
) -> SearchResults | KRDictError: ...
```
!!! warning
    Use of any value other than `'word'` for the `search_type` parameter with advanced search is
    undefined behavior, and incomplete or empty results will likely be returned. The parameter is
    included for completeness, but is not recommended for usage.

**Parameters:**

- query: The search query.
- raise_api_errors: Sets whether a [`KRDictException`](../types#krdictexception) will be raised if an API error occurs.
This guarantees that the result is not an error object.
- key: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- start_index: The index at which the search should start `[1, 1000]` (default `1`).
- num_results: The maximum number of search results to return `[10, 100]` (default `10`).
- sort ([`SortMethod`](../types#sortmethod)): The sort method which should be used (default `'alphabetical'`).
- search_type ([`SearchType`](../types#searchtype)): The type of search to perform (default `'word'`).
- translation_language ([`TranslationLanguage`](../types#translationlanguage)): A language to include translations for.
- search_target ([`SearchTarget`](../types#searchtarget)): The target field of the search query (default `'headword'`).
- target_language ([`TargetLanguage`](../types#targetlanguage)): The original language to search by. If `search_target`
is set to any value other than `'original_language'`, this parameter has no effect (default `'all'`).
- search_method ([`SearchMethod`](../types#searchmethod)): The method used to match against the query (default `'exact'`).
    - `'exact'`: Returns entries that are an exact match of the query.
    - `'include'`: Returns entries that include the query.
    - `'start'`: Returns entries that start with the query.
    - `'end'`: Returns entries that end with the query.
- classification ([`Classification`](../types#classification)): An entry classification to filter by (default `'all'`).
- origin_type ([`OriginType`](../types#origintype)): A word origin type to filter by (default `'all'`).
- vocabulary_grade ([`VocabularyGrade`](../types#vocabularygrade)): A vocabulary level to filter by (default `'all'`).
- part_of_speech ([`PartOfSpeech`](../types#partofspeech)): A part of speech to filter by (default `'all'`).
- multimedia_info ([`MultimediaType`](../types#multimediatype)): A multimedia type to filter by (default `'all'`).
- min_syllables: The minimum number of syllables in result words `[1, inf)` (default `1`).
- max_syllables: The maximum number of syllables in results words. A value of `0` denotes no maximum `[0, inf)` (default `0`).
- meaning_category ([`MeaningCategory`](../types#meaningcategory)): The meaning category to filter by (default `'all'`).
- subject_category ([`SubjectCategory`](../types#subjectcategory)): A subject category to filter by (default `'all'`).


**Returns**:

Depending on the value of `search_type` and whether an error occurred, returns one of:

- [`WordSearchResults`](../types#wordsearchresults)
- [`DefinitionSearchResults`](../types#definitionsearchresults)
- [`ExampleSearchResults`](../types#examplesearchresults)
- [`IdiomProverbSearchResults`](../types#idiomproverbsearchresults)
- [`KRDictError`](../types#krdicterror)

---

### search

Performs a basic search on the Korean Learner's Dictionary API.

```python
def search(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    start_index: int = None,
    num_results: int = None,
    sort: SortMethod = None,
    search_type: SearchType = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None
) -> SearchResults | KRDictError: ...
```

!!! note
    If `search_type` is omitted, this function has the same behavior as
    [`search_words`](#search_words) by default.
    For a more specific return type with static typing, use [`search_words`](#search_words).

**Parameters:**

- query: The search query.
- raise_api_errors: Sets whether a [`KRDictException`](../types#krdictexception) will be raised if an API error occurs.
This guarantees that the result is not an error object.
- key: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- start_index: The index at which the search should start `[1, 1000]` (default `1`).
- num_results: The maximum number of search results to return `[10, 100]` (default `10`).
- sort ([`SortMethod`](../types#sortmethod)): The sort method which should be used (default `'alphabetical'`).
- search_type ([`SearchType`](../types#searchtype)): The type of search to perform (default `'word'`).
- translation_language ([`TranslationLanguage`](../types#translationlanguage)): A language to include translations for.


**Returns**:

Depending on the value of `search_type` and whether an error occurred, returns one of:

- [`WordSearchResults`](../types#wordsearchresults)
- [`DefinitionSearchResults`](../types#definitionsearchresults)
- [`ExampleSearchResults`](../types#examplesearchresults)
- [`IdiomProverbSearchResults`](../types#idiomproverbsearchresults)
- [`KRDictError`](../types#krdicterror)

---

### search_definitions

Performs a search for definitions on the Korean Learner's Dictionary API.  
This function is equivalent to using `'definition'` as the argument to the `search_type`
parameter in the [`search`](#search) function, but returns a more specific type for static typing.

```python
def search_definitions(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    start_index: int = None,
    num_results: int = None,
    sort: SortMethod = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None
) -> DefinitionSearchResults | KRDictError: ...
```

**Parameters:**

- query: The search query.
- raise_api_errors: Sets whether a [`KRDictException`](../types#krdictexception) will be raised if an API error occurs.
This guarantees that the result is not an error object.
- key: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- start_index: The index at which the search should start `[1, 1000]` (default `1`).
- num_results: The maximum number of search results to return `[10, 100]` (default `10`).
- sort ([`SortMethod`](../types#sortmethod)): The sort method which should be used (default `'alphabetical'`).
- translation_language ([`TranslationLanguage`](../types#translationlanguage)): A language to include translations for.


**Returns:**

Depending on whether an error occurred, returns [`DefinitionSearchResults`](../types#definitionsearchresults) or
[`KRDictError`](../types#krdicterror).

---

### search_examples

Performs a search for examples on the Korean Learner's Dictionary API.  
This function is equivalent to using `'example'` as the argument to the `search_type`
parameter in the [`search`](#search) function, but returns a more specific type for static typing.

```python
def search_examples(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    start_index: int = None,
    num_results: int = None,
    sort: SortMethod = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None
) -> ExampleSearchResults | KRDictError: ...
```

**Parameters:**

- query: The search query.
- raise_api_errors: Sets whether a [`KRDictException`](../types#krdictexception) will be raised if an API error occurs.
This guarantees that the result is not an error object.
- key: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- start_index: The index at which the search should start `[1, 1000]` (default `1`).
- num_results: The maximum number of search results to return `[10, 100]` (default `10`).
- sort ([`SortMethod`](../types#sortmethod)): The sort method which should be used (default `'alphabetical'`).
- translation_language ([`TranslationLanguage`](../types#translationlanguage)): A language to include translations for.


**Returns:**

Depending on whether an error occurred, returns [`ExampleSearchResults`](../types#examplesearchresults) or
[`KRDictError`](../types#krdicterror).

---

### search_idioms_proverbs

Performs a search for idioms and proverbs on the Korean Learner's Dictionary API.  
This function is equivalent to using `'idiom_proverb'` as the argument to the `search_type`
parameter in the [`search`](#search) function, but returns a more specific type for static typing.

```python
def search_idioms_proverbs(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    start_index: int = None,
    num_results: int = None,
    sort: SortMethod = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None
) -> IdiomProverbSearchResults | KRDictError: ...
```

**Parameters:**

- query: The search query.
- raise_api_errors: Sets whether a [`KRDictException`](../types#krdictexception) will be raised if an API error occurs.
This guarantees that the result is not an error object.
- key: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- start_index: The index at which the search should start `[1, 1000]` (default `1`).
- num_results: The maximum number of search results to return `[10, 100]` (default `10`).
- sort ([`SortMethod`](../types#sortmethod)): The sort method which should be used (default `'alphabetical'`).
- translation_language ([`TranslationLanguage`](../types#translationlanguage)): A language to include translations for.


**Returns:**

Depending on whether an error occurred, returns [`IdiomProverbSearchResults`](../types#idiomproverbsearchresults) or
[`KRDictError`](../types#krdicterror).

---

### search_words

Performs a search for definitions on the Korean Learner's Dictionary API.  
This function is equivalent to using `'word'` or `None` as the argument to the `search_type`
parameter in the [`search`](#search) function, but returns a more specific type for static typing.

```python
def search_words(*,
    query: str,
    raise_api_errors: bool = False,
    key: str = None,
    start_index: int = None,
    num_results: int = None,
    sort: SortMethod = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None
) -> WordSearchResults | KRDictError: ...
```

**Parameters:**

- query: The search query.
- raise_api_errors: Sets whether a [`KRDictException`](../types#krdictexception) will be raised if an API error occurs.
This guarantees that the result is not an error object.
- key: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- start_index: The index at which the search should start. `[1, 1000]` (default `1`).
- num_results: The maximum number of search results to return. `[10, 100]` (default `10`).
- sort ([`SortMethod`](../types#sortmethod)): The sort method which should be used (default `'alphabetical'`).
- translation_language ([`TranslationLanguage`](../types#translationlanguage)): A language to include translations for.


**Returns:**

Depending on whether an error occurred, returns [`WordSearchResults`](../types#wordsearchresults) or
[`KRDictError`](../types#krdicterror).

---

### set_key

Sets a default API key to use, if one is not provided in a query.

```python
def set_key(key: str | None) -> None: ...
```

**Parameters:**

- key: The KRDict API key. To unset a key, use `None`.

---

### view

Performs a view query, which retrieves information about a particular entry, on the Korean Learner's Dictionary API.

```python
def view(*,
    query: str,
    raise_api_errors: bool = False,
    homograph_num: int = None,
    key: str = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None
) -> ViewResult | KRDictError: ...

def view(*,
    target_code: int,
    raise_api_errors: bool = False,
    key: str = None,
    translation_language: TranslationLanguage | List[TranslationLanguage] = None
) -> ViewResult | KRDictError: ...
```

**Parameters:**

- query: The search query.
- raise_api_errors: Sets whether a [`KRDictException`](../types#krdictexception) will be raised if an API error occurs.
This guarantees that the result is not an error object.
- homograph_num: The superscript number used to distinguish homographs (default `0`).
- target_code: The target code of the desired result.
- key: The API key. If a key was set with [`set_key`](#set_key), this can be omitted.
- translation_language ([`TranslationLanguage`](../types#translationlanguage)): A language or list of
languages to include translations for.


**Returns:**

Depending on whether an error occurred, returns [`ViewResult`](../types#viewresult) or
[`KRDictError`](../types#krdicterror).
