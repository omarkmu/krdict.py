from typing import List, TypedDict
from . import WordSearchResponse, ViewResponse

class _DailyWordData(TypedDict, total=False):
    part_of_speech: str
    vocabulary_grade: str
    original_language: str
    pronunciation: str
    pronunciation_urls: List[str]
class DailyWordData(_DailyWordData):
    target_code: int
    word: str
    definition: str
    url: str
    homograph_num: int

class DailyWordResponse(TypedDict):
    data: DailyWordData

def extend_advanced_search(
    response: WordSearchResponse,
    raise_errors: bool
) -> WordSearchResponse: ...

def extend_search(
    response: WordSearchResponse,
    raise_errors: bool
) -> WordSearchResponse: ...

def extend_view(
    response: ViewResponse,
    fetch_page_data: bool,
    fetch_multimedia: bool,
    raise_errors: bool
) -> ViewResponse: ...

def fetch_daily_word() -> DailyWordResponse: ...
