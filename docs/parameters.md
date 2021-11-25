A summary of expected parameter types for various [functions](functions.md).

---

## Classification

The classification of a dictionary entry.
```bash
'all' | 'word' | 'phrase' | 'expression'
```

## MultimediaType

A type of multimedia file.
```bash
'all' | 'photo' | 'illustration' | 'video' | 'animation' | 'sound' | 'none'
```

## OptionsDict

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

See also: [`set_default`](functions.md#set_default).

## OriginType

The classification of a dictionary entry's origin.
```bash
'all' | 'native' | 'hanja' | 'loanword' | 'hybrid'
```

## PartOfSpeech

A Korean part of speech.
```bash
| 'all'
| 'noun'
| 'pronoun'
| 'numeral'
| 'particle'
| 'verb'
| 'adjective'
| 'determiner'
| 'adverb'
| 'interjection'
| 'affix'
| 'bound noun'
| 'auxiliary verb'
| 'auxiliary adjective'
| 'ending'
| 'none'
```

## ScraperTranslationLanguage

A language to include translations for during a scraper fetch.
```bash
| 'chinese'
| 'english'
| 'japanese'
| 'french'
| 'spanish'
| 'arabic'
| 'mongolian'
| 'vietnamese'
| 'thai'
| 'indonesian'
| 'russian'
```

## SearchMethod

The method to use when searching.

- `'exact'`: Returns entries that are an exact match of the query.
- `'include'`: Returns entries that include the query.
- `'start'`: Returns entries that start with the query.
- `'end'`: Returns entries that end with the query.

```bash
'exact' | 'include' | 'start' | 'end'
```

## SearchTarget

The target of the search query; what to search by.
```bash
| 'headword'
| 'definition'
| 'example'
| 'original_language'
| 'pronunciation'
| 'application'
| 'application_shorthand'
| 'idiom'
| 'proverb'
| 'reference_info'
```

## SearchType

The type of search to perform.
```bash
'word' | 'idiom_proverb' | 'definition' | 'example'
```

## SortMethod

A sorting method to use for search results.
```bash
'alphabetical' | 'popular'
```

## TargetLanguage

A target original language to search by.
```bash
| 'all'
| 'native_word'
| 'sino-korean'
| 'unknown'
| 'english'
| 'greek'
| 'dutch'
| 'norwegian'
| 'german'
| 'latin'
| 'russian'
| 'romanian'
| 'maori'
| 'malay'
| 'mongolian'
| 'basque'
| 'burmese'
| 'vietnamese'
| 'bulgarian'
| 'sanskrit'
| 'serbo-croatian'
| 'swahili'
| 'swedish'
| 'arabic'
| 'irish'
| 'spanish'
| 'uzbek'
| 'ukrainian'
| 'italian'
| 'indonesian'
| 'japanese'
| 'chinese'
| 'czech'
| 'cambodian'
| 'quechua'
| 'tagalog'
| 'thai'
| 'turkish'
| 'tibetan'
| 'persian'
| 'portuguese'
| 'polish'
| 'french'
| 'provencal'
| 'finnish'
| 'hungarian'
| 'hebrew'
| 'hindi'
| 'other'
| 'danish'
```

## TranslationLanguage

A language to include translations for.
```bash
| 'all'
| 'english'
| 'japanese'
| 'french'
| 'spanish'
| 'arabic'
| 'mongolian'
| 'vietnamese'
| 'thai'
| 'indonesian'
| 'russian'
```

## VocabularyGrade

The vocabulary level of a dictionary entry.
```bash
'all' | 'beginner' | 'intermediate' | 'advanced'
```

## MeaningCategory

A meaning category which a dictionary entry may belong to.
Accepts a meaning category enumeration, integer, or string alias.  

See [Meaning Category](meaning_category.md) for details.

## SubjectCategory

A subject category (themes and situations) which a dictionary entry may belong to.
Accepts a subject category enumeration, integer, or string alias.  

See [Subject Category](subject_category.md) for details.
