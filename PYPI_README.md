A module that helps to query the [API](https://krdict.korean.go.kr/openApi/openApiInfo) of the
[Korean Learner's Dictionary](https://krdict.korean.go.kr), provided by the National Institute of Korean Language.

## Installation

To install the module via pip, run:

```
pip install krdict.py
```

To use this module, you'll need to generate an API key via [krdict](https://krdict.korean.go.kr/openApi/openApiRegister) (requires login).

## Usage
A minimal example query that assumes the `KRDICT_KEY` environment variable is set:

```python
import os
import json
import krdict

krdict.set_key(os.getenv('KRDICT_KEY'))
response = krdict.search(query='나무', raise_api_errors=True)

print(json.dumps(response, indent=2, ensure_ascii=False))
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

For more information, please check the [documentation](https://krdictpy.readthedocs.io/en/v1.1.0).
