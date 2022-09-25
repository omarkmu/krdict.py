In addition to API bindings, krdict.py provides a scraper package that offers functions that
fetch information directly from the dictionary website. These are accessible via the `krdict.scraper` package.

!!! warning
    Because this package utilizes scraping, the reliability of results cannot be guaranteed.
    At any time, functions may break entirely and remain broken until a patch is released. If there
    are errors or improper results, please submit an
    [issue](https://github.com/omarkmu/krdict.py/issues/new).

---
## advanced_search

Performs an advanced search on the Korean Learners' Dictionary.

```python
def advanced_search(*,
    query: str,
    page: int = 1,
    per_page: int = 10,
    sort: SortMethod = SortMethod.ALPHABETICAL,
    translation_language: ScraperTranslationLanguage | Iterable[ScraperTranslationLanguage] = None,
    search_target: ScraperSearchTarget = ScraperSearchTarget.HEADWORD,
    target_language: ScraperTargetLanguage = ScraperTargetLanguage.ALL,
    search_method: SearchMethod = SearchMethod.INCLUDE,
    classification: Classification | Iterable[Classification] = Classification.ALL,
    origin_type: OriginType | Iterable[OriginType] = OriginType.ALL,
    vocabulary_level: ScraperVocabularyLevel | Iterable[ScraperVocabularyLevel] = ScraperVocabularyLevel.ALL,
    part_of_speech: PartOfSpeech | Iterable[PartOfSpeech] = PartOfSpeech.ALL,
    multimedia_type: MultimediaType | Iterable[MultimediaType] = MultimediaType.ALL,
    min_syllables: int = 1,
    max_syllables: int = 0,
    semantic_category: SemanticCategory = SemanticCategory.ALL,
    subject_category: SubjectCategory | Iterable[SubjectCategory] = SubjectCategory.ALL,
    search_conditions: Iterable[SearchCondition] = None
) -> ScrapedWordResponse: ...
```
!!! note
    Unlike its counterpart in the main module, the default of the `search_method` parameter
    of this function is `SearchMethod.INCLUDE` rather than `SearchMethod.EXACT`.
    This is to more closely match the search function on the website.

**Parameters:**

- `query`: The search query.
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

---
## fetch_semantic_category_words

Fetches words that belong to the provided semantic category.

```python
def fetch_semantic_category_words(*,
    category: SemanticCategory,
    page: int = 1,
    per_page: int = 10,
    sort: SortMethod = SortMethod.ALPHABETICAL,
    translation_language: ScraperTranslationLanguage = None
) -> ScrapedWordResponse: ...
```

!!! warning
    The `SemanticCategory.ALL` option is **not supported** and will return zero results.
    This also applies for calls that do not supply `category`.

**Parameters:**

- `category`: The semantic category to fetch.
- `page`: The page at which the search should start `[1, 1000]`.
- `per_page`: The maximum number of search results to return `[10, 100]`.
- `sort`: The sort method that should be used.
- `translation_language`: A language for which translations should be included.

---
## fetch_subject_category_words

Fetches words that belong to one of the provided subject categories.

```python
def fetch_subject_category_words(*,
    category: SubjectCategory | List[SubjectCategory] = SubjectCategory.ALL,
    page: int = 1,
    per_page: int = 10,
    sort: SortMethod = SortMethod.ALPHABETICAL,
    translation_language: ScraperTranslationLanguage = None
) -> ScrapedWordResponse: ...
```

**Parameters:**

- `category`: The subject category to fetch.
- `page`: The page at which the search should start `[1, 1000]`.
- `per_page`: The maximum number of search results to return `[10, 100]`.
- `sort`: The sort method that should be used.
- `translation_language`: A language for which translations should be included.

---
## fetch_word_of_the_day

Fetches the Korean word of the day by scraping the dictionary website.

```python
def fetch_word_of_the_day(*,
    translation_language: ScraperTranslationLanguage | Iterable[ScraperTranslationLanguage] = None
) -> WordOfTheDayResponse: ...
```

**Parameters:**

- `translation_language`: A language for which a translation should be included.

---

## search

Performs a basic search on the Korean Learners' Dictionary.

```python
def search(*,
    query: str,
    key: str = None,
    page: int = 1,
    per_page: int = 10,
    sort: SortMethod = SortMethod.ALPHABETICAL,
    search_type: SearchType = SearchType.WORD,
    translation_language: ScraperTranslationLanguage | Iterable[ScraperTranslationLanguage] = None
) -> ScrapedWordResponse | ScrapedDefinitionResponse | ScrapedExampleResponse | ScrapedIdiomProverbResponse: ...
```

**Parameters:**

- `query`: The search query.
- `page`: The page at which the search should start `[1, 1000]`.
- `per_page`: The maximum number of search results to return `[10, 100]`.
- `sort`: The sort method that should be used.
- `search_type`: The type of search to perform.
- `translation_language`: A language
for which translations should be included.


**Returns**:

Depending on the value of `search_type`, returns one of:

- [`ScrapedWordResponse`](return_types.md#scrapedwordresponse)
- [`ScrapedDefinitionResponse`](return_types.md#scrapeddefinitionresponse)
- [`ScrapedExampleResponse`](return_types.md#scrapedexampleresponse)
- [`ScrapedIdiomProverbResponse`](return_types.md#scrapedidiomproverbresponse)

---

## view

Performs a view query, which retrieves information about a particular entry on the Korean Learners' Dictionary.

```python
def view(*,
    target_code: int,
    fetch_multimedia: bool = False,
    translation_language: TranslationLanguage | Iterable[TranslationLanguage] = None
) -> ScrapedViewResponse: ...
```

**Parameters:**

- `target_code`: The target code of the desired result.
- `translation_language`: A language
for which translations should be included.
