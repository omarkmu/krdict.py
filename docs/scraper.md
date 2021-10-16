In addition to API bindings, krdict.py provides a scraper module that extends
the results of word search queries, advanced search queries, and view queries.

These extensions can be applied directly to results during query calls with the `use_scraper`
[option](parameters.md#optionsdict), but are also accessible via the `krdict.scraper` module.

---
## extend_advanced_search

Extends advanced word search results with pronunciation URLs.

```python
def extend_advanced_search(
    response: WordSearchResponse,
    raise_errors: bool
) -> WordSearchResponse: ...
```

**Parameters:**

- response: The word search results to extend.
- raise_errors: Whether errors that occur during scraping should be raised or ignored.

**Returns:**

Returns an extended [`WordSearchResponse`](return_types.md#wordsearchresponse) object.

---
## extend_search

Extends word search results with pronunciation URLs.

```python
def extend_search(
    response: WordSearchResponse,
    raise_errors: bool
) -> WordSearchResponse: ...
```

**Parameters:**

- response: The word search results to extend.
- raise_errors: Whether errors that occur during scraping should be raised or ignored.

**Returns:**

Returns an extended [`WordSearchResponse`](return_types.md#wordsearchresponse) object.

---
## extend_view

Extends view query results with pronunciation URLs, multimedia information, and extended hanja
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

- response: The word search results to extend.
- fetch_page_data: Whether page data (URLs and hanja information) should be scraped.
- fetch_multimedia: Whether multimedia URLs should be scraped.
- raise_errors: Whether errors that occur during scraping should be raised or ignored.

**Returns:**

Returns an extended [`ViewResponse`](return_types.md#viewresponse) object.

---
## fetch_daily_word

Fetches the Korean word of the day by scraping the dictionary website.

```python
def fetch_daily_word() -> WordOfTheDayResponse: ...
```

**Returns:**

Returns a [`WordOfTheDayResponse`](return_types.md#wordofthedayresponse) object.

---
## fetch_meaning_category_words

Fetches words that belong to the provided meaning category.

```python
def fetch_meaning_category_words(*,
    category: MeaningCategory | int,
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    translation_language: ScraperTranslationLanguage = None
) -> ScrapedWordSearchResponse: ...
```

!!! note
    The `'전체'` MeaningCategory option is **not supported** and will return zero results.

**Parameters:**

- category: The meaning category to fetch.
- page: The page at which the search should start `[1, 1000]` (default `1`).
- per_page: The maximum number of search results to return `[10, 100]` (default `10`).
- sort ([`SortMethod`](parameters.md#sortmethod)): The sort method that should be used (default `'alphabetical'`).
- translation_language ([`ScraperTranslationLanguage`](parameters.md#scrapertranslationlanguage)): A language to include translations for.

**Returns:**

Returns a [`ScrapedWordSearchResponse`](return_types.md#scrapedwordsearchresponse) object.

---
## fetch_subject_category_words

Fetches words that belong to one of the provided subject categories.

```python
def fetch_subject_category_words(*,
    category: SubjectCategory | int | List[SubjectCategory | int],
    page: int = None,
    per_page: int = None,
    sort: SortMethod = None,
    translation_language: ScraperTranslationLanguage = None
) -> ScrapedWordSearchResponse: ...
```

**Parameters:**

- category: The subject category to fetch.
- page: The page at which the search should start `[1, 1000]` (default `1`).
- per_page: The maximum number of search results to return `[10, 100]` (default `10`).
- sort ([`SortMethod`](parameters.md#sortmethod)): The sort method that should be used (default `'alphabetical'`).
- translation_language ([`ScraperTranslationLanguage`](parameters.md#scrapertranslationlanguage)): A language to include translations for.

**Returns:**

Returns a [`ScrapedWordSearchResponse`](return_types.md#scrapedwordsearchresponse) object.
