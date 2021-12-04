from typing import overload
from ..main import TotalViewResponse, TotalWordSearchResponse, WordSearchResponse, ViewResponse

@overload
def extend_advanced_search(
    response: TotalWordSearchResponse,
    raise_errors: bool
) -> TotalWordSearchResponse: ...
@overload
def extend_advanced_search(
    response: WordSearchResponse,
    raise_errors: bool
) -> WordSearchResponse: ...


@overload
def extend_search(
    response: TotalWordSearchResponse,
    raise_errors: bool
) -> TotalWordSearchResponse: ...
@overload
def extend_search(
    response: WordSearchResponse,
    raise_errors: bool
) -> WordSearchResponse: ...


@overload
def extend_view(
    response: TotalViewResponse,
    fetch_page_data: bool,
    fetch_multimedia: bool,
    raise_errors: bool
) -> TotalViewResponse: ...
@overload
def extend_view(
    response: ViewResponse,
    fetch_page_data: bool,
    fetch_multimedia: bool,
    raise_errors: bool
) -> ViewResponse: ...
