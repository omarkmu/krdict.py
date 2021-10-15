from typing import List, TypedDict
from . import WordSearchResults, ViewResult

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
    link: str
    homograph_num: int

class DailyWordResponse(TypedDict):
    data: DailyWordData

def extend_advanced_search(
    response: WordSearchResults,
    raise_errors: bool
) -> WordSearchResults: ...

def extend_search(
    response: WordSearchResults,
    raise_errors: bool
) -> WordSearchResults: ...

def extend_view(
    response: ViewResult,
    fetch_page_data: bool,
    fetch_multimedia: bool,
    raise_errors: bool
) -> ViewResult: ...

def fetch_daily_word() -> DailyWordResponse: ...
