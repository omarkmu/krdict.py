A summary of return types of various [functions](functions.md).

## DefinitionSearchResponse

The results of a [definition search](functions.md#search).

```python
{
    "data": {
        "title": str,
        "url": str,
        "description": str,
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
                "definitions": [
                    {
                        "definition": str,
                        "translations": [ # not required
                            {
                                "definition": str,
                                "word": str, # not required
                                "language": str
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "request_params": {
        ...
    }
}
```

| Container      | Field           | Type | Required | Description
| ---------      | -----           | :--: | :------: | -----------
| -              | data            | dict |    ✓     | Container for search results.
| data           | title           | str  |    ✓     | The title of the Korean Leaner's Dictionary Open API (constant).
| data           | url             | str  |    ✓     | The URL of the Korean Leaner's Dictionary (constant).
| data           | description     | str  |    ✓     | The description of the Korean Learner's Dictionary Open API (constant).
| data           | last_build_date | str  |    ✓     | The time the search results were generated.
| data           | page            | int  |    ✓     | The page at which the search results begin.
| data           | per_page        | int  |    ✓     | The number of results per page. Does not necessarily correspond to the length of `results`.
| data           | total_results   | int  |    ✓     | The total number of results, including the returned results.
| data           | results         | list |    ✓     | A list of search result objects.
| results        | target_code     | int  |    ✓     | An entry's identification code.
| results        | word            | str  |    ✓     | An entry's headword.
| results        | url             | str  |    ✓     | A URL of a dictionary entry.
| results        | homograph_num   | int  |    ✓     | A superscript number used to distinguish homographs.
| results        | definitions     | list |    ✓     | A list of definitions associated with an entry.
| definitions    | definition      | str  |    ✓     | A definition associated with an entry.
| definitions    | translations    | list |    ✗     | A list of translations of a definition. Not included if no translation languages are specified.
| translations   | definition      | str  |    ✓     | A translation of the definition.
| translations   | word            | str  |    ✗     | A translation of the word.
| translations   | language        | str  |    ✓     | The translation language.
| -              | request_params  | dict |    ✓     | The request parameters which were sent to the API.

## ExampleSearchResponse

The results of an [example search](functions.md#search).

```python
{
    "data": {
        "title": str,
        "url": str,
        "description": str,
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
    "request_params": {
        ...
    }
}
```

| Container  | Field           | Type | Required | Description
| ---------  | -----           | :--: | :------: | -----------
| -          | data            | dict |    ✓     | Container for search results.
| data       | title           | str  |    ✓     | The title of the Korean Leaner's Dictionary Open API (constant).
| data       | url             | str  |    ✓     | The URL of the Korean Leaner's Dictionary (constant).
| data       | description     | str  |    ✓     | The description of the Korean Learner's Dictionary Open API (constant).
| data       | last_build_date | str  |    ✓     | The time the search results were generated.
| data       | page            | int  |    ✓     | The page at which the search results begin.
| data       | per_page        | int  |    ✓     | The number of results per page. Does not necessarily correspond to the length of `results`.
| data       | total_results   | int  |    ✓     | The total number of results, including the returned results.
| data       | results         | list |    ✓     | A list of search result objects.
| results    | target_code     | int  |    ✓     | An entry's identification code.
| results    | word            | str  |    ✓     | An entry's headword.
| results    | url             | str  |    ✓     | A URL of a dictionary entry.
| results    | homograph_num   | int  |    ✓     | A superscript number used to distinguish homographs.
| results    | example         | str  |    ✓     | An entry's example.
| -          | request_params  | dict |    ✓     | The request parameters which were sent to the API.


## IdiomProverbSearchResponse

The results of an [idiom/proverb search](functions.md#search).

```python
{
    "data": {
        "title": str,
        "url": str,
        "description": str,
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
                        "translations": [ # not required
                            {
                                "definition": str,
                                "word": str, # not required
                                "language": str
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "request_params": {
        ...
    }
}
```

| Container      | Field           | Type | Required | Description
| ---------      | -----           | :--: | :------: | -----------
| -              | data            | dict |    ✓     | Container for search results.
| data           | title           | str  |    ✓     | The title of the Korean Leaner's Dictionary Open API (constant).
| data           | url             | str  |    ✓     | The URL of the Korean Leaner's Dictionary (constant).
| data           | description     | str  |    ✓     | The description of the Korean Learner's Dictionary Open API (constant).
| data           | last_build_date | str  |    ✓     | The time the search results were generated.
| data           | page            | int  |    ✓     | The page at which the search results begin.
| data           | per_page        | int  |    ✓     | The number of results per page. Does not necessarily correspond to the length of `results`.
| data           | total_results   | int  |    ✓     | The total number of results, including the returned results.
| data           | results         | list |    ✓     | A list of search result objects.
| results        | target_code     | int  |    ✓     | An entry's identification code.
| results        | word            | str  |    ✓     | An idiom or proverb.
| results        | url             | str  |    ✓     | A URL of a dictionary entry.
| results        | homograph_num   | int  |    ✓     | A superscript number used to distinguish homographs.
| results        | definitions     | list |    ✓     | A list of definitions associated with an entry.
| definitions    | definition      | str  |    ✓     | A definition associated with an entry.
| definitions    | translations    | list |    ✗     | A list of translations of a definition. Not included if no translation languages are specified.
| translations   | definition      | str  |    ✓     | A translation of the definition.
| translations   | word            | str  |    ✗     | A translation of the idiom or proverb.
| translations   | language        | str  |    ✓     | The translation language.
| -              | request_params  | dict |    ✓     | The request parameters which were sent to the API.

## WordSearchResponse

The results of a [word search](functions.md#search).

```python
{
    "data": {
        "title": str,
        "url": str,
        "description": str,
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
                "origin": str, # not required
                "pronunciation": str, # not required
                "vocabulary_grade": str, # not required
                "pronunciation_urls": List[str], # not required
                "definitions": [
                    {
                        "definition": str,
                        "order": int,
                        "translations": [ # not required
                            {
                                "definition": str,
                                "word": str, # not required
                                "language": str
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "request_params": {
        ...
    }
}
```

| Container      | Field              | Type | Required | Description
| ---------      | -----              | :--: | :------: | -----------
| -              | data               | dict |    ✓     | Container for search results.
| data           | title              | str  |    ✓     | The title of the Korean Leaner's Dictionary Open API (constant).
| data           | url                | str  |    ✓     | The URL of the Korean Leaner's Dictionary (constant).
| data           | description        | str  |    ✓     | The description of the Korean Learner's Dictionary Open API (constant).
| data           | last_build_date    | str  |    ✓     | The time the search results were generated.
| data           | page               | int  |    ✓     | The page at which the search results begin.
| data           | per_page           | int  |    ✓     | The number of results per page. Does not necessarily correspond to the length of `results`.
| data           | total_results      | int  |    ✓     | The total number of results, including the returned results.
| data           | results            | list |    ✓     | A list of search result objects.
| results        | target_code        | int  |    ✓     | An entry's identification code.
| results        | word               | str  |    ✓     | An entry's headword.
| results        | url                | str  |    ✓     | A URL of a dictionary entry.
| results        | part_of_speech     | str  |    ✓     | The Korean part of speech of the entry.
| results        | homograph_num      | int  |    ✓     | A superscript number used to distinguish homographs.
| results        | origin             | str  |    ✗     | The origin (original language) of the entry.
| results        | pronunciation      | str  |    ✗     | The 한글 pronunciation of the entry.
| results        | vocabulary_grade   | str  |    ✗     | The vocabulary level of the entry.
| results        | pronunciation_urls | list |    ✗     | A list of pronunciation audio URLs. Included only if scraping is enabled and URLs are available.
| results        | definitions        | list |    ✓     | A list of definitions associated with an entry.
| definitions    | definition         | str  |    ✓     | A definition associated with an entry.
| definitions    | translations       | list |    ✗     | A list of translations of a definition. Not included if no translation languages are specified.
| translations   | definition         | str  |    ✓     | A translation of the definition.
| translations   | word               | str  |    ✗     | A translation of the word.
| translations   | language           | str  |    ✓     | The translation language.
| -              | request_params     | dict |    ✓     | The request parameters which were sent to the API.

## ViewResponse

The results of a [view query](functions.md#view).

```python
{
    "data": {
        "title": str,
        "url": str,
        "description": str,
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
                    "vocabulary_grade": str,
                    "allomorph": str, # not required
                    "definition_info": [
                        {
                            "definition": str,
                            "reference": str, # not required
                            "translations": [ # not required
                                {
                                    "definition": str,
                                    "word": str, # not required
                                    "language": str
                                }
                            ],
                            "example_info": [ # not required
                                {
                                    "type": str,
                                    "example": str
                                }
                            ],
                            "pattern_info": [ # not required
                                {
                                    "pattern": str,
                                    "pattern_reference": str # not required
                                }
                            ],
                            "related_info": [ # not required
                                {
                                    "type": str,
                                    "word": str,
                                    "url": str,
                                    "has_target_code": bool,
                                    "target_code": int # not required
                                }
                            ],
                            "multimedia_info": [ # not required
                                {
                                    "label": str,
                                    "type": str,
                                    "url": str,
                                    "media_urls": List[str]
                                }
                            ]
                        }
                    ],
                    "original_language_info": [ # not required
                        {
                            "original_language": str,
                            "language_type": str,
                            "hanja_info": [ # not required
                                {
                                    "hanja": str,
                                    "radical": str,
                                    "stroke_count": int,
                                    "readings": List[str]
                                }
                            ]
                        }
                    ],
                    "pronunciation_info": [ # not required
                        {
                            "pronunciation": str,
                            "url": str # not required
                        }
                    ],
                    "conjugation_info": [ # not required
                        {
                            "conjugation": str,
                            "pronunciation_info": [ # not required
                                {
                                    "pronunciation": str,
                                    "url": str # not required
                                }
                            ],
                            "abbreviation_info": [ # not required
                                {
                                    "abbreviation": str,
                                    "pronunciation_info": [ # not required
                                        {
                                            "pronunciation": str,
                                            "url": str # not required
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "derivative_info": [ # not required
                        {
                            "word": str,
                            "url": str,
                            "has_target_code": bool,
                            "target_code": int # not required
                        }
                    ],
                    "reference_info": [ # not required
                        {
                            "word": str,
                            "url": str,
                            "has_target_code": bool,
                            "target_code": int # not required
                        }
                    ],
                    "category_info": [ # not required
                        {
                            "type": str,
                            "name": str
                        }
                    ],
                    "subword_info": [ # not required
                        {
                            "subword": str,
                            "subword_unit": str,
                            "subdefinition_info": [
                                {
                                    "definition": str,
                                    "translations": [ # not required
                                        {
                                            "definition": str,
                                            "word": str, # not required
                                            "language": str
                                        }
                                    ],
                                    "example_info": [ # not required
                                        {
                                            "type": str,
                                            "example": str
                                        }
                                    ],
                                    "related_info": [ # not required
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
    "request_params": {
        ...
    }
}
```

| Container              | Field                  | Type | Required | Description
| ---------              | -----                  | :--: | :------: | -----------
| -                      | data                   | dict |    ✓     | Container for view query results.
| data                   | title                  | str  |    ✓     | The title of the Korean Leaner's Dictionary Open API (constant).
| data                   | url                    | str  |    ✓     | The URL of the search result page.
| data                   | description            | str  |    ✓     | The description of the Korean Learner's Dictionary Open API (constant).
| data                   | last_build_date        | str  |    ✓     | The time the view results were generated.
| data                   | total_results          | int  |    ✓     | The total number of results, including the returned results.
| data                   | results                | list |    ✓     | A list of 0 or 1 view result objects.
| results                | target_code            | int  |    ✓     | The entry's identification code.
| results                | word_info              | dict |    ✓     | Container for word information.
| word_info              | word                   | str  |    ✓     | The entry's headword.
| word_info              | word_unit              | str  |    ✓     | The composition unit of the headword.
| word_info              | word_type              | str  |    ✓     | The origin type of the headword.
| word_info              | part_of_speech         | str  |    ✓     | The Korean part of speech of the headword.
| word_info              | homograph_num          | int  |    ✓     | A superscript number used to distinguish homographs.
| word_info              | vocabulary_grade       | str  |    ✓     | The vocabulary level of the entry.
| word_info              | allomorph              | str  |    ✗     | The allomorph of the headword.
| word_info              | definition_info        | list |    ✓     | Contains information about the entry's definitions.
| definition_info        | definition             | str  |    ✓     | A definition of the entry.
| definition_info        | reference              | str  |    ✗     | The reference of the definition.
| definition_info        | translations           | list |    ✗     | A list of translations of a definition. Not included if no translation languages are specified.
| translations           | definition             | str  |    ✓     | A translation of the definition.
| translations           | word                   | str  |    ✗     | A translation of the word.
| translations           | language               | str  |    ✓     | The translation language.
| definition_info        | example_info           | list |    ✗     | A list of example objects.
| example_info           | type                   | str  |    ✓     | The type of the example.
| example_info           | example                | str  |    ✓     | An example associated with the definition.
| definition_info        | pattern_info           | list |    ✗     | A list of pattern objects.
| pattern_info           | pattern                | str  |    ✓     | A pattern associated with the definition.
| pattern_info           | pattern_reference      | str  |    ✗     | A reference associated with the pattern.
| definition_info        | related_info           | list |    ✗     | A list of related word objects.
| related_info           | type                   | str  |    ✓     | The type of the related word.
| related_info           | word                   | str  |    ✓     | The related word.
| related_info           | url                    | str  |    ✓     | The URL of the related word.
| related_info           | has_target_code        | bool |    ✓     | Whether a target code is included.
| related_info           | target_code            | str  |    ✗     | The target code of the related word.
| definition_info        | multimedia_info        | list |    ✗     | A list of multimedia objects.
| multimedia_info        | label                  | str  |    ✓     | The label of the multimedia object.
| multimedia_info        | type                   | str  |    ✓     | The type of the multimedia object.
| multimedia_info        | url                    | str  |    ✓     | The URL of the multimedia object.
| multimedia_info        | media_urls             | list |    ✗     | A list of multimedia URLs. Included only if scraping is enabled.
| word_info              | original_language_info | list |    ✗     | Contains information about the entry's original language.
| original_language_info | original_language      | str  |    ✓     | The origin of the word.
| original_language_info | language_type          | str  |    ✓     | The language type of the word origin.
| original_language_info | hanja_info             | list |    ✗     | Contains information about hanja. Included only if scraping is enabled and hanja information is available.
| hanja_info             | hanja                  | str  |    ✓     | The hanja character described by the object.
| hanja_info             | radical                | str  |    ✓     | The radical (부수) of the character.
| hanja_info             | stroke_count           | int  |    ✓     | The amount of strokes that the character is composed of.
| hanja_info             | readings               | list |    ✓     | The readings (음훈) of the character.
| word_info              | pronunciation_info     | list |    ✗     | Contains information about the entry's pronunciation.
| pronunciation_info     | pronunciation          | str  |    ✓     | The 한글 pronunciation of the entry.
| pronunciation_info     | url                    | str  |    ✗     | The audio URL of the pronunciation. Included only if scraping is enabled and audio is available.
| word_info              | conjugation_info       | list |    ✗     | Contains information about the entry's conjugations.
| conjugation_info       | conjugation            | str  |    ✓     | The conjugation of the word.
| conjugation_info       | pronunciation_info     | list |    ✗     | Contains information about the conjugation's pronunciation.
| pronunciation_info     | pronunciation          | str  |    ✓     | The 한글 pronunciation of the conjugation.
| pronunciation_info     | url                    | str  |    ✗     | The audio URL of the pronunciation. Included only if scraping is enabled and audio is available.
| conjugation_info       | abbreviation_info      | list |    ✗     | Contains information about the conjugation's abbreviations.
| abbreviation_info      | abbreviation           | str  |    ✓     | The abbreviation of the conjugation.
| abbreviation_info      | pronunciation_info     | list |    ✗     | Contains information about the abbreviation's pronunciation.
| pronunciation_info     | pronunciation          | str  |    ✓     | The 한글 pronunciation of the abbreviation.
| pronunciation_info     | url                    | str  |    ✗     | The audio URL of the pronunciation. Included only if scraping is enabled and audio is available.
| word_info              | derivative_info        | list |    ✗     | Contains information about the entry's derivatives.
| derivative_info        | word                   | str  |    ✓     | The derivative word.
| derivative_info        | url                    | str  |    ✓     | The URL of the derivative word.
| derivative_info        | has_target_code        | bool |    ✓     | Whether a target code is included.
| derivative_info        | target_code            | str  |    ✗     | The target code of the derivative word.
| word_info              | reference_info         | list |    ✗     | Contains information about the entry's references.
| reference_info         | word                   | str  |    ✓     | The reference word.
| reference_info         | url                    | str  |    ✓     | The URL of the reference word.
| reference_info         | has_target_code        | bool |    ✓     | Whether a target code is included.
| reference_info         | target_code            | str  |    ✗     | The target code of the reference word.
| word_info              | category_info          | list |    ✗     | Contains information about the entry's categories.
| category_info          | type                   | str  |    ✓     | The category type.
| category_info          | name                   | str  |    ✓     | The category name.
| word_info              | subword_info           | list |    ✗     | Contains information about the entry's subwords.
| subword_info           | subword                | str  |    ✓     | The subword text.
| subword_info           | subword_unit           | str  |    ✓     | The composition unit of the subword.
| subword_info           | subdefinition_info     | list |    ✓     | Contains information about the subword's definitions.
| subdefinition_info     | definition             | str  |    ✓     | A definition of the subword.
| subdefinition_info     | translations           | list |    ✗     | A list of translations of a subword definition. Not included if no translation languages are specified.
| translations           | definition             | str  |    ✓     | A translation of the subword definition.
| translations           | word                   | str  |    ✓     | A translation of the subword word.
| translations           | language               | str  |    ✓     | The translation language.
| subdefinition_info     | example_info           | list |    ✗     | A list of subdefinition example objects.
| example_info           | type                   | str  |    ✓     | The type of the example.
| example_info           | example                | str  |    ✓     | An example associated with the subword definition.
| subdefinition_info     | related_info           | list |    ✗     | A list of related word objects.
| related_info           | type                   | str  |    ✓     | The type of the related word.
| related_info           | word                   | str  |    ✓     | The related word.
| -                      | request_params         | dict |    ✓     | The request parameters which were sent to the API.

## KRDictError

Information about an API error. For a list of error codes, please see the
[API reference](https://krdict.korean.go.kr/openApi/openApiInfo).

```python
{
    "error": {
        "error_code": int,
        "message": str
    },
    "request_params": {
        ...
    }
}
```

| Container | Field          | Type | Required | Description
| --------- | -----          | :--: | :------: | -----------
| -         | error          | dict |    ✓     | Container for error information.
| error     | error_code     | int  |    ✓     | The error code supplied by the API.
| error     | message        | str  |    ✓     | The error message supplied by the API.
| -         | request_params | dict |    ✓     | The request parameters which were sent to the API.

## DailyWordResponse

Information about the word of the day.

```python
{
    "data": {
        "target_code": int,
        "word": str,
        "definition": str,
        "url": str,
        "homograph_num": int,
        "part_of_speech": str, # not required
        "vocabulary_grade": str, # not required
        "original_language": str, # not required
        "pronunciation": str, # not required
        "pronunciation_urls": List[str] # not required
    }
}
```

| Field              | Type | Required | Description
| -----              | :--: | :------: | -----------
| target_code        | int  |    ✓     | The entry's identification code.
| word               | str  |    ✓     | The entry's headword.
| definition         | str  |    ✓     | A definition of the entry.
| url                | str  |    ✓     | The URL of the dictionary entry.
| homograph_num      | int  |    ✓     | A superscript number used to distinguish homographs.
| part_of_speech     | str  |    ✗     | The Korean part of speech of the headword.
| vocabulary_grade   | str  |    ✗     | The vocabulary level of the entry.
| original_language  | str  |    ✗     | The origin of the word.
| pronunciation      | str  |    ✗     | The 한글 pronunciation of the entry.
| pronunciation_urls | list |    ✗     | A list of pronunciation audio URLs. Included only if scraping is enabled and URLs are available.

---
