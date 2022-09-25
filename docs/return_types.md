A summary of response types of various [API](main.md) and [scraper](scraper.md) functions.
Each of these describes the structure of a class that has an `asdict` method which returns a dict.

Only types that are re-exported from the main `krdict` module are documented here; sub-types can be
accessed from within `krdict.types`.

## WordResponse

The results of a word [search](main.md#search).

```python
{
    "data": {
        "title": "한국어기초사전 오픈 API - 사전 검색",
        "url": "https://krdict.korean.go.kr",
        "description": "한국어기초사전 오픈 API – 사전 검색 결과",
        "last_build_date": str,
        "page": int,
        "per_page": int,
        "total_results": int,
        "results": [
            {
                "target_code": int,
                "word": str,
                "url": str,
                "part_of_speech": str,
                "homograph_num": str,
                "origin": str,
                "pronunciation": str,
                "vocabulary_level": str,
                "definitions": [
                    {
                        "definition": str,
                        "order": int,
                        "translations": [
                            {
                                "definition": str,
                                "word": str,
                                "language": str
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "request_params": { ... },
    "response_type": "word"
}
```

| Container      | Attribute          | Type | Description
| ---------      | -----              | :--: | -----------
| -              | data               | dict | Container for search results.
| data           | title              | str  | The title of the Korean Learners' Dictionary Open API (constant).
| data           | url                | str  | The URL of the Korean Learners' Dictionary (constant).
| data           | description        | str  | The description of the Korean Learners' Dictionary Open API (constant).
| data           | last_build_date    | str  | The time the search results were generated.
| data           | page               | int  | The page at which the search results begin.
| data           | per_page           | int  | The number of results per page. Does not necessarily correspond to the length of `results`.
| data           | total_results      | int  | The total number of results, including the returned results.
| data           | results            | list | A list of search result objects.
| results        | target_code        | int  | An entry's identification code.
| results        | word               | str  | An entry's headword.
| results        | url                | str  | A URL of a dictionary entry.
| results        | part_of_speech     | str  | The Korean part of speech of the entry.
| results        | homograph_num      | int  | A superscript number used to distinguish homographs.
| results        | origin             | str  | The origin (original language) of the entry.
| results        | pronunciation      | str  | The 한글 pronunciation of the entry.
| results        | vocabulary_level   | str  | The vocabulary level of the entry.
| results        | definitions        | list | A list of definitions associated with an entry.
| definitions    | definition         | str  | A definition associated with an entry.
| definitions    | translations       | list | A list of translations of a definition.
| translations   | definition         | str  | A translation of the definition.
| definitions    | order              | int  | The order of the definition in the list.
| translations   | word               | str  | A translation of the word.
| translations   | language           | str  | The translation language.
| -              | request_params     | dict | The request parameters which were sent to the API.
| -              | response_type      | str  | The identifying value of the response. (constant)

## DefinitionResponse

The results of a definition [search](main.md#search).

```python
{
    "data": {
        "title": "한국어기초사전 오픈 API - 사전 검색",
        "url": "https://krdict.korean.go.kr",
        "description": "한국어기초사전 오픈 API – 사전 검색 결과",
        "last_build_date": str,
        "page": int,
        "per_page": int,
        "total_results": int,
        "results": [
            {
                "target_code": int,
                "word": str,
                "url": str,
                "homograph_num": int,
                "definition_info": {
                    "definition": str,
                    "translations": [
                        {
                            "definition": str,
                            "word": str,
                            "language": str
                        }
                    ]
                }
            }
        ]
    },
    "request_params": { ... },
    "response_type": "dfn"
}
```

| Container       | Attribute       | Type | Description
| ---------       | -----           | :--: | -----------
| -               | data            | dict | Container for search results.
| data            | title           | str  | The title of the Korean Learners' Dictionary Open API (constant).
| data            | url             | str  | The URL of the Korean Learners' Dictionary (constant).
| data            | description     | str  | The description of the Korean Learners' Dictionary Open API (constant).
| data            | last_build_date | str  | The time the search results were generated.
| data            | page            | int  | The page at which the search results begin.
| data            | per_page        | int  | The number of results per page. Does not necessarily correspond to the length of `results`.
| data            | total_results   | int  | The total number of results, including the returned results.
| data            | results         | list | A list of search result objects.
| results         | target_code     | int  | An entry's identification code.
| results         | word            | str  | An entry's headword.
| results         | url             | str  | A URL of a dictionary entry.
| results         | homograph_num   | int  | A superscript number used to distinguish homographs.
| results         | definition_info | dict | Information about the definition associated with the entry.
| definition_info | definition      | str  | A definition associated with an entry.
| definition_info | translations    | list | A list of translations of a definition.
| translations    | definition      | str  | A translation of the definition.
| translations    | word            | str  | A translation of the word.
| translations    | language        | str  | The translation language.
| -               | request_params  | dict | The request parameters which were sent to the API.
| -               | response_type   | str  | The identifying value of the response. (constant)

## ExampleResponse

The results of an example [search](main.md#search).

```python
{
    "data": {
        "title": "한국어기초사전 오픈 API - 사전 검색",
        "url": "https://krdict.korean.go.kr",
        "description": "한국어기초사전 오픈 API – 사전 검색 결과",
        "last_build_date": str,
        "page": int,
        "per_page": int,
        "total_results": int,
        "results": [
            {
                "target_code": int,
                "word": str,
                "url": str,
                "homograph_num": int,
                "example": str
            }
        ]
    },
    "request_params": { ... },
    "response_type": "exam"
}
```

| Container  | Attribute       | Type | Description
| ---------  | -----           | :--: | -----------
| -          | data            | dict | Container for search results.
| data       | title           | str  | The title of the Korean Learners' Dictionary Open API (constant).
| data       | url             | str  | The URL of the Korean Learners' Dictionary (constant).
| data       | description     | str  | The description of the Korean Learners' Dictionary Open API (constant).
| data       | last_build_date | str  | The time the search results were generated.
| data       | page            | int  | The page at which the search results begin.
| data       | per_page        | int  | The number of results per page. Does not necessarily correspond to the length of `results`.
| data       | total_results   | int  | The total number of results, including the returned results.
| data       | results         | list | A list of search result objects.
| results    | target_code     | int  | An entry's identification code.
| results    | word            | str  | An entry's headword.
| results    | url             | str  | A URL of a dictionary entry.
| results    | homograph_num   | int  | A superscript number used to distinguish homographs.
| results    | example         | str  | An entry's example.
| -          | request_params  | dict | The request parameters which were sent to the API.
| -          | response_type   | str  | The identifying value of the response. (constant)


## IdiomProverbResponse

The results of an idiom/proverb [search](main.md#search).

```python
{
    "data": {
        "title": "한국어기초사전 오픈 API - 사전 검색",
        "url": "https://krdict.korean.go.kr",
        "description": "한국어기초사전 오픈 API – 사전 검색 결과",
        "last_build_date": str,
        "page": int,
        "per_page": int,
        "total_results": int,
        "results": [
            {
                "target_code": int,
                "word": str,
                "url": str,
                "definitions": [
                    {
                        "definition": str,
                        "order": int,
                        "translations": [
                            {
                                "definition": str,
                                "word": str,
                                "language": str
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "request_params": { ... },
    "response_type": "ip"
}
```

| Container      | Attribute       | Type | Description
| ---------      | -----           | :--: | -----------
| -              | data            | dict | Container for search results.
| data           | title           | str  | The title of the Korean Learners' Dictionary Open API (constant).
| data           | url             | str  | The URL of the Korean Learners' Dictionary (constant).
| data           | description     | str  | The description of the Korean Learners' Dictionary Open API (constant).
| data           | last_build_date | str  | The time the search results were generated.
| data           | page            | int  | The page at which the search results begin.
| data           | per_page        | int  | The number of results per page. Does not necessarily correspond to the length of `results`.
| data           | total_results   | int  | The total number of results, including the returned results.
| data           | results         | list | A list of search result objects.
| results        | target_code     | int  | An entry's identification code.
| results        | word            | str  | An idiom or proverb.
| results        | url             | str  | A URL of a dictionary entry.
| results        | homograph_num   | int  | A superscript number used to distinguish homographs.
| results        | definitions     | list | A list of definitions associated with an entry.
| definitions    | definition      | str  | A definition associated with an entry.
| definitions    | order           | int  | The order of the definition in the list.
| definitions    | translations    | list | A list of translations of a definition.
| translations   | definition      | str  | A translation of the definition.
| translations   | word            | str  | A translation of the idiom or proverb.
| translations   | language        | str  | The translation language.
| -              | request_params  | dict | The request parameters which were sent to the API.
| -              | response_type   | str  | The identifying value of the response. (constant)

## ViewResponse

The results of a [view](main.md#view) query.

```python
{
    "data": {
        "title": "한국어기초사전 오픈 API - 사전 검색",
        "url": str,
        "description": "한국어기초사전 오픈 API – 사전 검색 결과",
        "last_build_date": str,
        "total_results": int,
        "results": [ # contains 0 or 1 result
            {
                "target_code": int,
                "word_info": {
                    "word": str,
                    "word_unit": str,
                    "word_type": str,
                    "part_of_speech": str,
                    "homograph_num": int,
                    "vocabulary_level": str,
                    "allomorph": str,
                    "reference": str,
                    "origin": str,
                    "definition_info": [
                        {
                            "definition": str,
                            "reference": str,
                            "translations": [
                                {
                                    "definition": str,
                                    "word": str,
                                    "language": str
                                }
                            ],
                            "example_info": [
                                {
                                    "type": str,
                                    "example": str
                                }
                            ],
                            "pattern_info": [
                                {
                                    "pattern": str,
                                    "pattern_reference": str
                                }
                            ],
                            "related_info": [
                                {
                                    "type": str,
                                    "word": str,
                                    "url": str,
                                    "has_target_code": bool,
                                    "target_code": int
                                }
                            ],
                            "multimedia_info": [
                                {
                                    "label": str,
                                    "type": str,
                                    "url": str
                                }
                            ]
                        }
                    ],
                    "original_language_info": [
                        {
                            "original_language": str,
                            "language_type": str
                        }
                    ],
                    "pronunciation_info": [
                        {
                            "pronunciation": str
                        }
                    ],
                    "conjugation_info": [
                        {
                            "conjugation": str,
                            "pronunciation_info": [
                                {
                                    "pronunciation": str
                                }
                            ],
                            "abbreviation_info": [
                                {
                                    "abbreviation": str,
                                    "pronunciation_info": [
                                        {
                                            "pronunciation": str
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "derivative_info": [
                        {
                            "word": str,
                            "url": str,
                            "has_target_code": bool,
                            "target_code": int
                        }
                    ],
                    "reference_info": [
                        {
                            "word": str,
                            "url": str,
                            "has_target_code": bool,
                            "target_code": int
                        }
                    ],
                    "category_info": [
                        {
                            "type": str,
                            "name": str
                        }
                    ],
                    "subword_info": [
                        {
                            "subword": str,
                            "subword_type": str,
                            "subdefinition_info": [
                                {
                                    "definition": str,
                                    "reference": str,
                                    "translations": [
                                        {
                                            "definition": str,
                                            "reference": str,
                                            "word": str,
                                            "language": str
                                        }
                                    ],
                                    "example_info": [
                                        {
                                            "type": str,
                                            "example": str
                                        }
                                    ],
                                    "pattern_info": [
                                        {
                                            "pattern": str,
                                        }
                                    ],
                                    "related_info": [
                                        {
                                            "type": str,
                                            "word": str
                                        }
                                    ],
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    },
    "request_params": { ... },
    "response_type": "view"
}
```

| Container              | Attribute              | Type | Description
| ---------              | -----                  | :--: | -----------
| -                      | data                   | dict | Container for view query results.
| data                   | title                  | str  | The title of the Korean Learners' Dictionary Open API (constant).
| data                   | url                    | str  | The URL of the search result page.
| data                   | description            | str  | The description of the Korean Learners' Dictionary Open API (constant).
| data                   | last_build_date        | str  | The time the view results were generated.
| data                   | total_results          | int  | The total number of results, including the returned results.
| data                   | results                | list | A list of 0 or 1 view result objects.
| results                | target_code            | int  | The entry's identification code.
| results                | word_info              | dict | Container for word information.
| word_info              | word                   | str  | The entry's headword.
| word_info              | word_unit              | str  | The composition unit of the headword.
| word_info              | word_type              | str  | The origin type of the headword.
| word_info              | part_of_speech         | str  | The Korean part of speech of the headword.
| word_info              | homograph_num          | int  | A superscript number used to distinguish homographs.
| word_info              | vocabulary_level       | str  | The vocabulary level of the entry.
| word_info              | allomorph              | str  | The allomorph of the headword.
| word_info              | origin                 | str  | The original language of the entry.
| word_info              | reference              | str  | The reference of the word.
| word_info              | definition_info        | list | Contains information about the entry's definitions.
| definition_info        | definition             | str  | A definition of the entry.
| definition_info        | reference              | str  | The reference of the definition.
| definition_info        | translations           | list | A list of translations of a definition.
| translations           | definition             | str  | A translation of the definition.
| translations           | word                   | str  | A translation of the word.
| translations           | language               | str  | The translation language.
| definition_info        | example_info           | list | A list of example objects.
| example_info           | type                   | str  | The type of the example.
| example_info           | example                | str  | An example associated with the definition.
| definition_info        | pattern_info           | list | A list of pattern objects.
| pattern_info           | pattern                | str  | A pattern associated with the definition.
| pattern_info           | pattern_reference      | str  | A reference associated with the pattern.
| definition_info        | related_info           | list | A list of related word objects.
| related_info           | type                   | str  | The type of the related word.
| related_info           | word                   | str  | The related word.
| related_info           | url                    | str  | The URL of the related word.
| related_info           | has_target_code        | bool | Whether a target code is included.
| related_info           | target_code            | str  | The target code of the related word.
| definition_info        | multimedia_info        | list | A list of multimedia objects.
| multimedia_info        | label                  | str  | The label of the multimedia object.
| multimedia_info        | type                   | str  | The type of the multimedia object.
| multimedia_info        | url                    | str  | The URL of the multimedia object.
| word_info              | original_language_info | list | Contains information about the entry's original language.
| original_language_info | original_language      | str  | The origin of the word.
| original_language_info | language_type          | str  | The language type of the word origin.
| word_info              | pronunciation_info     | list | Contains information about the entry's pronunciation.
| pronunciation_info     | pronunciation          | str  | The 한글 pronunciation of the entry.
| word_info              | conjugation_info       | list | Contains information about the entry's conjugations.
| conjugation_info       | conjugation            | str  | The conjugation of the word.
| conjugation_info       | pronunciation_info     | list | Contains information about the conjugation's pronunciation.
| pronunciation_info     | pronunciation          | str  | The 한글 pronunciation of the conjugation.
| conjugation_info       | abbreviation_info      | list | Contains information about the conjugation's abbreviations.
| abbreviation_info      | abbreviation           | str  | The abbreviation of the conjugation.
| abbreviation_info      | pronunciation_info     | list | Contains information about the abbreviation's pronunciation.
| pronunciation_info     | pronunciation          | str  | The 한글 pronunciation of the abbreviation.
| word_info              | derivative_info        | list | Contains information about the entry's derivatives.
| derivative_info        | word                   | str  | The derivative word.
| derivative_info        | url                    | str  | The URL of the derivative word.
| derivative_info        | has_target_code        | bool | Whether a target code is included.
| derivative_info        | target_code            | str  | The target code of the derivative word.
| word_info              | reference_info         | list | Contains information about the entry's references.
| reference_info         | word                   | str  | The reference word.
| reference_info         | url                    | str  | The URL of the reference word.
| reference_info         | has_target_code        | bool | Whether a target code is included.
| reference_info         | target_code            | str  | The target code of the reference word.
| word_info              | category_info          | list | Contains information about the entry's categories.
| category_info          | type                   | str  | The category type.
| category_info          | name                   | str  | The category name.
| word_info              | subword_info           | list | Contains information about the entry's subwords.
| subword_info           | subword                | str  | The subword text.
| subword_info           | subword_type           | str  | The type of the subword.
| subword_info           | subdefinition_info     | list | Contains information about the subword's definitions.
| subdefinition_info     | definition             | str  | A definition of the subword.
| subdefinition_info     | reference              | str  | The reference of the subword.
| subdefinition_info     | translations           | list | A list of translations of a subword definition.
| translations           | definition             | str  | A translation of the subword definition.
| translations           | word                   | str  | A translation of the subword word.
| translations           | language               | str  | The translation language.
| subdefinition_info     | example_info           | list | A list of subdefinition example objects.
| example_info           | type                   | str  | The type of the example.
| example_info           | example                | str  | An example associated with the subword definition.
| subdefinition_info     | pattern_info           | list | A list of pattern objects.
| pattern_info           | pattern                | str  | A pattern associated with the subword definition.
| subdefinition_info     | related_info           | list | A list of related word objects.
| related_info           | type                   | str  | The type of the related word.
| related_info           | word                   | str  | The related word.
| -                      | request_params         | dict | The request parameters which were sent to the API.
| -                      | response_type          | str  | The identifying value of the response. (constant)

## ErrorResponse

Information about an API error. For a list of error codes, please see the
[API reference](https://krdict.korean.go.kr/openApi/openApiInfo).

```python
{
    "error_code": int,
    "message": str,
    "request_params": { ... },
    "response_type": "error"
}
```

| Attribute      | Type | Description
| -----          | :--: | -----------
| error_code     | int  | The error code supplied by the API.
| message        | str  | The error message supplied by the API.
| request_params | dict | The request parameters which were sent to the API.
| response_type  | str  | The identifying value of the response. (constant)

## WordOfTheDayResponse

Information about the [word of the day](scraper.md#fetch_word_of_the_day).

```python
{
    "data": {
        "target_code": int,
        "word": str,
        "definition": str,
        "url": str,
        "translation_urls": List[str],
        "homograph_num": int,
        "part_of_speech": str,
        "vocabulary_level": str,
        "origin": str,
        "pronunciation": str,
        "pronunciation_urls": List[str],
        "translations": [
            {
                "definition": str,
                "word": str,
                "language": str
            }
        ]
    },
    "response_type": "word_of_the_day"
}
```

| Container        | Attribute          | Type | Description
| ---------        | -----              | :--: | -----------
| -                | data               | dict | Container for results.
| data             | target_code        | int  | The entry's identification code.
| data             | word               | str  | The entry's headword.
| data             | definition         | str  | A definition of the entry.
| data             | url                | str  | The URL of the dictionary entry.
| results          | translation_urls   | list | Container for information about URLs that can be used to view a translated entry.
| translation_urls | url                | str  | The translation URL.
| translation_urls | language           | str  | The language of the translation URL.
| data             | homograph_num      | int  | A superscript number used to distinguish homographs.
| data             | part_of_speech     | str  | The Korean part of speech of the headword.
| data             | vocabulary_level   | str  | The vocabulary level of the entry.
| data             | origin             | str  | The origin (original language) of the word.
| data             | pronunciation      | str  | The 한글 pronunciation of the entry.
| data             | pronunciation_urls | list | A list of pronunciation audio URLs.
| data             | translation        | dict | Container for a translation of a definition. Not included if a translation language is not specified.
| translations     | definition         | str  | A translation of the definition.
| translations     | word               | str  | A translation of the word.
| translations     | language           | str  | The translation language.
| -                | response_type      | str  | The identifying value of the response. (constant)

## ScrapedWordResponse

The results of a scraped word [search](scraper.md#search).

```python
{
    "data": {
        "url": str,
        "translation_urls": [
            {
                "url": str,
                "language": str
            }
        ],
        "page": int,
        "per_page": int,
        "total_results": int,
        "results": [
            {
                "target_code": int,
                "word": str,
                "url": str,
                "translation_urls": [
                    {
                        "url": str,
                        "language": str
                    }
                ],
                "part_of_speech": str,
                "homograph_num": str,
                "origin": str,
                "vocabulary_level": str,
                "pronunciation": str,
                "pronunciation_urls": List[str],
                "definitions": [
                    {
                        "definition": str,
                        "order": int,
                        "translations": [
                            {
                                "definition": str,
                                "word": str,
                                "language": str
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "response_type": "scraped_word"
}
```

| Container        | Attribute          | Type | Description
| ---------        | -----              | :--: | -----------
| -                | data               | dict | Container for search results.
| data             | url                | str  | The Korean Learners' Dictionary URL that can be used to view the results.
| data             | translation_urls   | list | Container for information about URLs that can be used to view the translated results.
| translation_urls | url                | str  | The translation URL.
| translation_urls | language           | str  | The language of the translation URL.
| data             | page               | int  | The page at which the search results begin.
| data             | per_page           | int  | The number of results per page. Does not necessarily correspond to the length of `results`.
| data             | total_results      | int  | The total number of results, including the returned results.
| data             | results            | list | A list of search result objects.
| results          | target_code        | int  | An entry's identification code.
| results          | word               | str  | An entry's headword.
| results          | url                | str  | A URL of a dictionary entry.
| results          | translation_urls   | list | Container for information about URLs that can be used to view a translated entry.
| translation_urls | url                | str  | The translation URL.
| translation_urls | language           | str  | The language of the translation URL.
| results          | part_of_speech     | str  | The Korean part of speech of the entry.
| results          | homograph_num      | int  | A superscript number used to distinguish homographs.
| results          | origin             | str  | The origin (original language) of the entry.
| results          | vocabulary_level   | str  | The vocabulary level of the entry.
| results          | pronunciation      | str  | The 한글 pronunciation of the entry.
| results          | pronunciation_urls | list | A list of pronunciation audio URLs.
| results          | definitions        | list | A list of definitions associated with an entry.
| definitions      | definition         | str  | A definition associated with an entry.
| definitions      | order              | int  | The order of a definition in the list.
| definitions      | translation        | dict | Container for a translation of a definition. Not included if a translation language is not specified.
| translation      | definition         | str  | A translation of the definition.
| translation      | word               | str  | A translation of the word.
| translation      | language           | str  | The translation language.
| -                | response_type      | str  | The identifying value of the response. (constant)

## ScrapedDefinitionResponse

The results of a scraped definition [search](scraper.md#search).

```python
{
    "data": {
        "url": str,
        "translation_urls": [
            {
                "url": str,
                "language": str
            }
        ],
        "page": int,
        "per_page": int,
        "total_results": int,
        "results": [
            {
                "target_code": int,
                "word": str,
                "url": str,
                "translation_urls": [
                    {
                        "url": str,
                        "language": str
                    }
                ],
                "homograph_num": int,
                "definition_info": {
                    "definition": str,
                    "translations": [
                        {
                            "definition": str,
                            "word": str,
                            "language": str
                        }
                    ]
                }
            }
        ]
    },
    "response_type": "scraped_dfn"
}
```

| Container        | Attribute        | Type | Description
| ---------        | -----            | :--: | -----------
| -                | data             | dict | Container for search results.
| data             | url              | str  | The Korean Learners' Dictionary URL that can be used to view the results.
| data             | translation_urls | list | Container for information about URLs that can be used to view the translated results.
| translation_urls | url              | str  | The translation URL.
| translation_urls | language         | str  | The language of the translation URL.
| data             | page             | int  | The page at which the search results begin.
| data             | per_page         | int  | The number of results per page. Does not necessarily correspond to the length of `results`.
| data             | total_results    | int  | The total number of results, including the returned results.
| data             | results          | list | A list of search result objects.
| results          | target_code      | int  | An entry's identification code.
| results          | word             | str  | An entry's headword.
| results          | url              | str  | A URL of a dictionary entry.
| results          | translation_urls | list | Container for information about URLs that can be used to view a translated entry.
| translation_urls | url              | str  | The translation URL.
| translation_urls | language         | str  | The language of the translation URL.
| results          | homograph_num    | int  | A superscript number used to distinguish homographs.
| results          | definition_info  | dict | Information about the definition associated with the entry.
| definition_info  | definition       | str  | A definition associated with an entry.
| definition_info  | translations     | list | A list of translations of a definition.
| translations     | definition       | str  | A translation of the definition.
| translations     | word             | str  | A translation of the word.
| translations     | language         | str  | The translation language.
| -                | response_type    | str  | The identifying value of the response. (constant)

## ScrapedExampleResponse

The results of a scraped example [search](scraper.md#search).

```python
{
    "data": {
        "url": str,
        "translation_urls": [
            {
                "url": str,
                "language": str
            }
        ],
        "page": int,
        "per_page": int,
        "total_results": int,
        "results": [
            {
                "target_code": int,
                "word": str,
                "url": str,
                "homograph_num": int,
                "example": str
            }
        ]
    },
    "response_type": "scraped_exam"
}
```

| Container        | Attribute        | Type | Description
| ---------        | -----            | :--: | -----------
| -                | data             | dict | Container for search results.
| data             | url              | str  | The Korean Learners' Dictionary URL that can be used to view the results.
| data             | translation_urls | list | Container for information about URLs that can be used to view the translated results.
| translation_urls | url              | str  | The translation URL.
| translation_urls | language         | str  | The language of the translation URL.
| data             | page             | int  | The page at which the search results begin.
| data             | per_page         | int  | The number of results per page. Does not necessarily correspond to the length of `results`.
| data             | total_results    | int  | The total number of results, including the returned results.
| data             | results          | list | A list of search result objects.
| results          | target_code      | int  | An entry's identification code.
| results          | word             | str  | An entry's headword.
| results          | url              | str  | A URL of a dictionary entry.
| results          | homograph_num    | int  | A superscript number used to distinguish homographs.
| results          | example          | str  | An entry's example.
| -                | response_type    | str  | The identifying value of the response. (constant)


## ScrapedIdiomProverbResponse

The results of a scraped idiom/proverb [search](scraper.md#search).

```python
{
    "data": {
        "url": str,
        "translation_urls": [
            {
                "url": str,
                "language": str
            }
        ],
        "page": int,
        "per_page": int,
        "total_results": int,
        "results": [
            {
                "target_code": int,
                "word": str,
                "url": str,
                "definitions": [
                    {
                        "definition": str,
                        "order": int,
                        "translations": [
                            {
                                "definition": str,
                                "word": str,
                                "language": str
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "response_type": "scraped_ip"
}
```

| Container        | Attribute        | Type | Description
| ---------        | -----            | :--: | -----------
| -                | data             | dict | Container for search results.
| data             | title            | str  | The title of the Korean Learners' Dictionary Open API (constant).
| data             | url              | str  | The Korean Learners' Dictionary URL that can be used to view the results.
| data             | translation_urls | list | Container for information about URLs that can be used to view the translated results.
| translation_urls | url              | str  | The translation URL.
| translation_urls | language         | str  | The language of the translation URL.
| data             | page             | int  | The page at which the search results begin.
| data             | per_page         | int  | The number of results per page. Does not necessarily correspond to the length of `results`.
| data             | total_results    | int  | The total number of results, including the returned results.
| data             | results          | list | A list of search result objects.
| results          | target_code      | int  | An entry's identification code.
| results          | word             | str  | An idiom or proverb.
| results          | url              | str  | A URL of a dictionary entry.
| results          | homograph_num    | int  | A superscript number used to distinguish homographs.
| results          | definitions      | list | A list of definitions associated with an entry.
| definitions      | definition       | str  | A definition associated with an entry.
| definitions      | order            | int  | The order of the definition in the list.
| definitions      | translations     | list | A list of translations of a definition.
| translations     | definition       | str  | A translation of the definition.
| translations     | word             | str  | A translation of the idiom or proverb.
| translations     | language         | str  | The translation language.
| -                | response_type    | str  | The identifying value of the response. (constant)

## ScrapedViewResponse

The results of a scraped [view](scraper.md#view) query.

```python
{
    "data": {
        "url": str,
        "translation_urls": [
            {
                "url": str,
                "language": str
            }
        ],
        "total_results": int,
        "results": [ # contains 0 or 1 result
            {
                "target_code": int,
                "word_info": {
                    "word": str,
                    "part_of_speech": str,
                    "homograph_num": int,
                    "vocabulary_level": str,
                    "allomorph": str,
                    "reference": str,
                    "origin": str,
                    "definition_info": [
                        {
                            "definition": str,
                            "reference": str,
                            "pattern_reference": str,
                            "translations": [
                                {
                                    "definition": str,
                                    "word": str,
                                    "language": str
                                }
                            ],
                            "example_info": [
                                {
                                    "example": str
                                }
                            ],
                            "pattern_info": [
                                {
                                    "pattern": str,
                                }
                            ],
                            "related_info": [
                                {
                                    "type": str,
                                    "word": str,
                                    "url": str,
                                    "translation_urls": [
                                        {
                                            "url": str,
                                            "language": str
                                        }
                                    ],
                                    "has_target_code": bool,
                                    "target_code": int
                                }
                            ],
                            "multimedia_info": [
                                {
                                    "label": str,
                                    "type": str,
                                    "file_number": int,
                                    "url": str,
                                    "thumbnail_urls": List[str],
                                    "content_urls": List[str]
                                }
                            ]
                        }
                    ],
                    "original_language_info": [
                        {
                            "original_language": str,
                            "language_type": str,
                            "hanja_info": [
                                {
                                    "hanja": str,
                                    "radical": str,
                                    "stroke_count": int,
                                    "readings": List[str]
                                }
                            ]
                        }
                    ],
                    "pronunciation_info": [
                        {
                            "pronunciation": str,
                            "url": str
                        }
                    ],
                    "conjugation_info": [
                        {
                            "conjugation": str,
                            "pronunciation_info": [
                                {
                                    "pronunciation": str,
                                    "url": str
                                }
                            ],
                            "abbreviation_info": [
                                {
                                    "abbreviation": str,
                                    "pronunciation_info": [
                                        {
                                            "pronunciation": str,
                                            "url": str
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "derivative_info": [
                        {
                            "word": str,
                            "url": str,
                            "translation_urls": [
                                {
                                    "url": str,
                                    "language": str
                                }
                            ],
                            "has_target_code": bool,
                            "target_code": int
                        }
                    ],
                    "subword_info": [
                        {
                            "subword": str,
                            "subword_type": str,
                            "subdefinition_info": [
                                {
                                    "definition": str,
                                    "reference": str,
                                    "pattern_reference": str,
                                    "translations": [
                                        {
                                            "definition": str,
                                            "word": str,
                                            "language": str
                                        }
                                    ],
                                    "example_info": [
                                        {
                                            "type": str,
                                            "example": str
                                        }
                                    ],
                                    "pattern_info": [
                                        {
                                            "pattern": str,
                                        }
                                    ],
                                    "related_info": [
                                        {
                                            "type": str,
                                            "word": str
                                        }
                                    ],
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    },
    "response_type": "scraped_view"
}
```

| Container              | Attribute              | Type | Description
| ---------              | -----                  | :--: | -----------
| -                      | data                   | dict | Container for view query results.
| data                   | url                    | str  | The URL of the search result page.
| data                   | translation_urls       | list | Container for information about URLs that can be used to view the translated results.
| translation_urls       | url                    | str  | The translation URL.
| translation_urls       | language               | str  | The language of the translation URL.
| data                   | description            | str  | The description of the Korean Learners' Dictionary Open API (constant).
| data                   | last_build_date        | str  | The time the view results were generated.
| data                   | total_results          | int  | The total number of results, including the returned results.
| data                   | results                | list | A list of 0 or 1 view result objects.
| results                | target_code            | int  | The entry's identification code.
| results                | word_info              | dict | Container for word information.
| word_info              | word                   | str  | The entry's headword.
| word_info              | part_of_speech         | str  | The Korean part of speech of the headword.
| word_info              | homograph_num          | int  | A superscript number used to distinguish homographs.
| word_info              | vocabulary_level       | str  | The vocabulary level of the entry.
| word_info              | allomorph              | str  | The allomorph of the headword.
| word_info              | reference              | str  | The reference of the entry.
| word_info              | origin                 | str  | The original language of the entry.
| word_info              | definition_info        | list | Contains information about the entry's definitions.
| definition_info        | definition             | str  | A definition of the entry.
| definition_info        | reference              | str  | The reference of the definition.
| definition_info        | pattern_reference      | str  | A reference associated with a pattern.
| definition_info        | translations           | list | A list of translations of a definition.
| translations           | definition             | str  | A translation of the definition.
| translations           | word                   | str  | A translation of the word.
| translations           | language               | str  | The translation language.
| definition_info        | example_info           | list | A list of example objects.
| example_info           | example                | str  | An example associated with the definition.
| definition_info        | pattern_info           | list | A list of pattern objects.
| pattern_info           | pattern                | str  | A pattern associated with the definition.
| definition_info        | related_info           | list | A list of related word objects.
| related_info           | translation_urls       | list | Container for information about URLs that can be used to view translations of the related entry.
| translation_urls       | url                    | str  | The translation URL.
| translation_urls       | language               | str  | The language of the translation URL.
| related_info           | type                   | str  | The type of the related word.
| related_info           | word                   | str  | The related word.
| related_info           | url                    | str  | The URL of the related word.
| related_info           | has_target_code        | bool | Whether a target code is included.
| related_info           | target_code            | str  | The target code of the related word.
| definition_info        | multimedia_info        | list | A list of multimedia objects.
| multimedia_info        | label                  | str  | The label of the multimedia object.
| multimedia_info        | type                   | str  | The type of the multimedia object.
| multimedia_info        | file_number            | str  | The file number of the multimedia object.
| multimedia_info        | url                    | str  | The URL of the multimedia object.
| multimedia_info        | thumbnail_url          | list | The URL of the multimedia object's thumbnail.
| multimedia_info        | content_urls           | list | A list of multimedia URLs.
| word_info              | original_language_info | list | Contains information about the entry's original language.
| original_language_info | original_language      | str  | The origin of the word.
| original_language_info | language_type          | str  | The language type of the word origin.
| original_language_info | hanja_info             | list | Contains information about hanja.
| hanja_info             | hanja                  | str  | The hanja character described by the object.
| hanja_info             | radical                | str  | The radical (부수) of the character.
| hanja_info             | stroke_count           | int  | The amount of strokes that the character is composed of.
| hanja_info             | readings               | list | The readings (음훈) of the character.
| word_info              | pronunciation_info     | list | Contains information about the entry's pronunciation.
| pronunciation_info     | pronunciation          | str  | The 한글 pronunciation of the entry.
| pronunciation_info     | url                    | str  | The audio URL of the pronunciation.
| word_info              | conjugation_info       | list | Contains information about the entry's conjugations.
| conjugation_info       | conjugation            | str  | The conjugation of the word.
| conjugation_info       | pronunciation_info     | list | Contains information about the conjugation's pronunciation.
| pronunciation_info     | pronunciation          | str  | The 한글 pronunciation of the conjugation.
| pronunciation_info     | url                    | str  | The audio URL of the pronunciation.
| conjugation_info       | abbreviation_info      | list | Contains information about the conjugation's abbreviations.
| abbreviation_info      | abbreviation           | str  | The abbreviation of the conjugation.
| abbreviation_info      | pronunciation_info     | list | Contains information about the abbreviation's pronunciation.
| pronunciation_info     | pronunciation          | str  | The 한글 pronunciation of the abbreviation.
| pronunciation_info     | url                    | str  | The audio URL of the pronunciation.
| word_info              | derivative_info        | list | Contains information about the entry's derivatives.
| derivative_info        | word                   | str  | The derivative word.
| derivative_info        | url                    | str  | The URL of the derivative word.
| derivative_info        | translation_urls       | list | Container for information about URLs that can be used to view translations of the derivative entry.
| translation_urls       | url                    | str  | The translation URL.
| translation_urls       | language               | str  | The language of the translation URL.
| derivative_info        | has_target_code        | bool | Whether a target code is included.
| derivative_info        | target_code            | str  | The target code of the derivative word.
| word_info              | subword_info           | list | Contains information about the entry's subwords.
| subword_info           | subword                | str  | The subword text.
| subword_info           | subword_type           | str  | The type of the subword.
| subword_info           | subdefinition_info     | list | Contains information about the subword's definitions.
| subdefinition_info     | definition             | str  | A definition of the subword.
| subdefinition_info     | reference              | str  | The reference of the subword.
| subdefinition_info     | pattern_reference      | str  | A reference associated with a pattern.
| subdefinition_info     | translations           | list | A list of translations of a subword definition.
| translations           | definition             | str  | A translation of the subword definition.
| translations           | word                   | str  | A translation of the subword word.
| translations           | language               | str  | The translation language.
| subdefinition_info     | example_info           | list | A list of subdefinition example objects.
| example_info           | type                   | str  | The type of the example.
| example_info           | example                | str  | An example associated with the subword definition.
| subdefinition_info     | pattern_info           | list | A list of pattern objects.
| pattern_info           | pattern                | str  | A pattern associated with the subword definition.
| subdefinition_info     | related_info           | list | A list of related word objects.
| related_info           | type                   | str  | The type of the related word.
| related_info           | word                   | str  | The related word.
| -                      | response_type          | str  | The identifying value of the response. (constant)


---
