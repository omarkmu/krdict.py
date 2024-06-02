A package that helps to query the [API](https://krdict.korean.go.kr/openApi/openApiInfo) of the
[Korean Learners' Dictionary](https://krdict.korean.go.kr/mainAction), provided by the National Institute of Korean Language.

## Installation

To install the package via pip, run:

```
pip install krdict.py
```

You can also install from one of the [GitHub releases](https://github.com/omarkmu/krdict.py/releases).

## Usage
To use most of the functionality provided by this package, you'll need to generate an API key via
[the portal](https://krdict.korean.go.kr/openApi/openApiRegister) (requires login).

A minimal example query that assumes the `KRDICT_KEY` environment variable is set:

```python
import os
import json
import krdict

krdict.set_key(os.getenv('KRDICT_KEY'))
response = krdict.search(query='나무', raise_api_errors=True)

print(json.dumps(response.asdict(), indent=2, ensure_ascii=False))
```

Assuming an error does not occur, the output will be similar to:

```json
{
  "data": {
    ...
    "results": [
      {
        "target_code": 32750,
        "word": "나무",
        "pronunciation": "나무",
        ...
        "definitions": [
          {
            "order": 1,
            "definition": "단단한 줄기에 가지와 잎이 달린, 여러 해 동안 자라는 식물."
          },
          ...
        ]
      },
      ...
    ]
  },
  "request_params": {
    "q": "나무",
    "key": "YOUR_API_KEY"
  }
}
```

For more information and usage examples, please check the [documentation](https://krdictpy.readthedocs.io/en/v3.0.2).
