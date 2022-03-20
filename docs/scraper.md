In addition to API bindings, krdict.py provides a scraper package that offers functions that
fetch information from the dictionary website and extend the results of word search queries,
advanced search queries, and view queries.

The extensions can be applied directly to the results of the main package's functions with the `use_scraper`
[option](parameters.md#optionsdict), but are also accessible via the `krdict.scraper` package.

!!! warning
    Because this package utilizes scraping, the reliability of results cannot be guaranteed.
    At any time, functions may break entirely and remain broken until a patch is released. If there
    are errors or improper results, please submit an
    [issue](https://github.com/omarkmu/krdict.py/issues/new).

---
## fetch_today_word

Fetches the Korean word of the day by scraping the dictionary website.

```python
def fetch_today_word(*,
    translation_language: ScraperTranslationLanguage = None
) -> WordOfTheDayResponse: ...
```

**Parameters:**

- `translation_language` ([`ScraperTranslationLanguage`](parameters.md#scrapertranslationlanguage)): A language to include a translation for.

**Returns:**

Returns a [`WordOfTheDayResponse`](return_types.md#wordofthedayresponse) object.

---
## fetch_meaning_category_words

Fetches words that belong to the provided meaning category.

```python
def fetch_meaning_category_words(*,
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
    category: SubjectCategory | List[SubjectCategory] = SubjectCategory.ALL,
    page: int = 1,
    per_page: int = 0,
    sort: SortMethod = SortMethod.ALPHABETICAL,
    translation_language: ScraperTranslationLanguage = None
) -> ScrapedWordSearchResponse: ...
```

**Parameters:**

- `category` ([`SubjectCategory`](parameters.md#subjectcategory)): The subject category to fetch.
- `page`: The page at which the search should start `[1, 1000]`.
- `per_page`: The maximum number of search results to return `[10, 100]`.
- `sort` ([`SortMethod`](parameters.md#sortmethod)): The sort method that should be used.
- `translation_language` ([`ScraperTranslationLanguage`](parameters.md#scrapertranslationlanguage)): A language for which translations should be included.

**Returns:**

Returns a [`ScrapedWordSearchResponse`](return_types.md#scrapedwordsearchresponse) object.
