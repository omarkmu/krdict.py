In addition to API bindings, krdict.py provides a scraper module that offers functions that
fetch information from the dictionary website and extend the results of word search queries,
advanced search queries, and view queries.

The extensions can be applied directly to the results of the main module's functions with the `use_scraper`
[option](parameters.md#optionsdict), but are also accessible via the `krdict.scraper` module.

!!! warning
    Because this module utilizes scraping, the reliability of results cannot be guaranteed.
    At any time, functions may break entirely and remain broken until a patch is released. If there
    are errors or improper results, please submit an
    [issue](https://github.com/omarkmu/krdict.py/issues/new).

---
## extend_advanced_search

Extends advanced word search responses with pronunciation URLs.

```python
def extend_advanced_search(
    response: WordSearchResponse,
    raise_errors: bool
) -> WordSearchResponse: ...
```

**Parameters:**

- `response`: The word search responses to extend.
- `raise_errors`: Whether errors that occur during scraping should be raised or ignored.

**Returns:**

Returns an extended [`WordSearchResponse`](return_types.md#wordsearchresponse) object.

---
## extend_search

Extends word search responses with pronunciation URLs.

```python
def extend_search(
    response: WordSearchResponse,
    raise_errors: bool
) -> WordSearchResponse: ...
```

**Parameters:**

- `response`: The word search responses to extend.
- `raise_errors`: Whether errors that occur during scraping should be raised or ignored.

**Returns:**

Returns an extended [`WordSearchResponse`](return_types.md#wordsearchresponse) object.

---
## extend_view

Extends view query responses with pronunciation URLs, multimedia information, and extended hanja
information.

```python
def extend_view(
    response: ViewResponse,
    fetch_page_data: bool,
    fetch_multimedia: bool,
    raise_errors: bool
) -> ViewResponse: ...
```

**Parameters:**

- `response`: The word search responses to extend.
- `fetch_page_data`: Whether page data (URLs and hanja information) should be scraped.
- `fetch_multimedia`: Whether multimedia URLs should be scraped.
- `raise_errors`: Whether errors that occur during scraping should be raised or ignored.

**Returns:**

Returns an extended [`ViewResponse`](return_types.md#viewresponse) object.

---
## fetch_today_word

Fetches the Korean word of the day by scraping the dictionary website.

```python
def fetch_today_word(*,
    guarantee_keys: bool = False,
    translation_language: ScraperTranslationLanguage = None
) -> WordOfTheDayResponse: ...
```

**Parameters:**

- `guarantee_keys`: Sets whether keys that are missing from the response should be inserted with default values.
A value of `True` guarantees that every key that is not required is included, including keys set by the scraper. Default values:
    - The empty string `""` for string values.
    - Zero `0` for integer values.
    - An empty list `[]` for list values.
    - `None` for dictionary values. This only applies to the `translation` field.
- `translation_language` ([`ScraperTranslationLanguage`](parameters.md#scrapertranslationlanguage)): A language to include a translation for.

**Returns:**

Returns a [`WordOfTheDayResponse`](return_types.md#wordofthedayresponse) object.

---
## fetch_meaning_category_words

Fetches words that belong to the provided meaning category.

```python
def fetch_meaning_category_words(*,
    guarantee_keys: bool = False,
    category: MeaningCategory,
    page: int = 1,
    per_page: int = 10,
    sort: SortMethod = SortMethod.ALPHABETICAL,
    translation_language: ScraperTranslationLanguage = None
) -> ScrapedWordSearchResponse: ...
```

!!! warning
    The `MeaningCategory.ALL` option is **not supported** and will return zero results.
    This also applies for calls that do not supply `category`.

**Parameters:**

- `guarantee_keys`: Sets whether keys that are missing from the response should be inserted with default values.
A value of `True` guarantees that every key that is not required is included, including keys set by the scraper. Default values:
    - The empty string `""` for string values.
    - Zero `0` for integer values.
    - An empty list `[]` for list values.
    - `None` for dictionary values. This only applies to the `translation` field.
- `category` ([`MeaningCategory`](parameters.md#meaningcategory)): The meaning category to fetch.
- `page`: The page at which the search should start `[1, 1000]`.
- `per_page`: The maximum number of search results to return `[10, 100]`.
- `sort` ([`SortMethod`](parameters.md#sortmethod)): The sort method that should be used.
- `translation_language` ([`ScraperTranslationLanguage`](parameters.md#scrapertranslationlanguage)): A language for which translations should be included.

**Returns:**

Returns a [`ScrapedWordSearchResponse`](return_types.md#scrapedwordsearchresponse) object.

---
## fetch_subject_category_words

Fetches words that belong to one of the provided subject categories.

```python
def fetch_subject_category_words(*,
    guarantee_keys: bool = False,
    category: SubjectCategory | List[SubjectCategory] = SubjectCategory.ALL,
    page: int = 1,
    per_page: int = 0,
    sort: SortMethod = SortMethod.ALPHABETICAL,
    translation_language: ScraperTranslationLanguage = None
) -> ScrapedWordSearchResponse: ...
```

**Parameters:**

- `guarantee_keys`: Sets whether keys that are missing from the response should be inserted with default values.
A value of `True` guarantees that every key that is not required is included, including keys set by the scraper. Default values:
    - The empty string `""` for string values.
    - Zero `0` for integer values.
    - An empty list `[]` for list values.
    - `None` for dictionary values. This only applies to the `translation` field.
- `category` ([`SubjectCategory`](parameters.md#subjectcategory)): The subject category to fetch.
- `page`: The page at which the search should start `[1, 1000]`.
- `per_page`: The maximum number of search results to return `[10, 100]`.
- `sort` ([`SortMethod`](parameters.md#sortmethod)): The sort method that should be used.
- `translation_language` ([`ScraperTranslationLanguage`](parameters.md#scrapertranslationlanguage)): A language for which translations should be included.

**Returns:**

Returns a [`ScrapedWordSearchResponse`](return_types.md#scrapedwordsearchresponse) object.
