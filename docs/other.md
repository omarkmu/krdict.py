A summary of other types provided by the package.

---

# Exceptions

Exceptions that should be expected to be thrown from the library.  
If you encounter any other type of exception, or an unexpected error, please submit an
[issue](https://github.com/omarkmu/krdict.py/issues/new)!

## KRDictException

An exception that contains information about an API error. This only occurs if the argument passed to the
`raise_api_errors` parameter of a query function is `True`. For a list of error codes, please see the
[API reference](https://krdict.korean.go.kr/openApi/openApiInfo).

```python
class KRDictException(Exception):
    message: str
    error_code: int
    request_params: dict
```

| Attribute      | Type | Description
| -----          | :--: | -----------
| error_code     | int  | The error code supplied by the API.
| message        | str  | The error message supplied by the API.
| request_params | dict | The request parameters that were sent to the API.

## Request Exceptions

If an error occurs while performing the request, one of a few different
types of [exceptions](https://requests.readthedocs.io/en/latest/api/#exceptions) may be raised.  
Note that an exception is also thrown if the status code of the response falls between 400 and 600.

---

# Miscellaneous

## SearchCondition

A dict that describes a search condition for an advanced search. All keys are optional.
See [advanced_search](main.md#advanced_search).

- `'query'`: The search query.
- `'exclude'`: If set to True, this condition will *exclude* results from the search rather than
including them.
- `'search_target'`: The target field of the search query.
- `'target_language'`: The original language to search by. If `search_target`
is set to any value other than `'original_language'`, this has no effect.
- `'search_method'`: The method used to match against the query.

```python
{
    'query': str,
    'exclude': bool,
    'search_target': SearchTarget,
    'target_language': TargetLanguage,
    'search_method': SearchMethod
}
```
