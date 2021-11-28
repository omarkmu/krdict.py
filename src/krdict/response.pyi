from typing import Any, Literal, Optional, Tuple, Union
from requests import Response
from . import SearchResponse, TotalSearchResponse, TotalViewResponse, ViewResponse

TOption = Literal[
    'fetch_multimedia',
    'fetch_page_data',
    'raise_scraper_errors',
    'use_scraper'
]

def parse_response(
    kwargs: dict[str, Any],
    api_response: Response,
    request_params: dict[str, Any],
    search_type: str
) -> Union[SearchResponse, ViewResponse, TotalSearchResponse, TotalViewResponse]: ...

def postprocessor(
    key: str, 
    value: Any,
    search_type: str,
    guarantee_keys: bool
) -> Optional[Tuple[str, Any]]: ...

def set_default(option: TOption, value: bool) -> None: ...
