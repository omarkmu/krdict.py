Exceptions that should be expected to be thrown from the library.  
If you encounter any other type of error, or an unexpected error, please submit an
[issue](https://github.com/omarkmu/krdict.py/issues/new)!

## KRDictException

An exception that contains information about an API error. This only occurs if the argument passed to the
`raise_api_errors` parameter of a query function is `True`.  
For a list of error codes, please see the
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

## RequestException

If an error occurs while performing the request, a
[`RequestException`](https://docs.python-requests.org/en/master/api/#requests.RequestException) is raised.  
Note that an exception is also thrown if the status code of the response falls between 400 and 600.
