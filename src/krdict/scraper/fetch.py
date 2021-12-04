"""
Handles fetching and reading information from the krdict website.
"""

from .request import send_request, map_advanced_param
from ..types import (
    isiterable,
    SortMethod,
    MeaningCategory,
    SubjectCategory,
    ScraperTranslationLanguage
)
from .utils import (
    extract_href,
    read_search_results,
    read_wotd_details
)

_BASE_URL = 'https://krdict.korean.go.kr/{}mainAction'
_TRANSLATED_VIEW_URL = 'https://krdict.korean.go.kr/{}dicSearch/SearchView?ParaWordNo={}{}'
_SUBJECT_URL = (
    'https://krdict.korean.go.kr/{}dicSearchDetail/searchDetailActCategoryResult?'
    'searchFlag=Y{}&currentPage={}&blockCount={}&sort={}{}')
_SENSE_URL = (
    'https://krdict.korean.go.kr/{}dicSearchDetail/searchDetailSenseCategoryResult?'
    'searchFlag=Y{}&currentPage={}&blockCount={}&sort={}{}')

_LANG_INFO = [
    ['eng', 6, '영어'],
    ['jpn', 7, '일본어'],
    ['fra', 8, '프랑스어'],
    ['spa', 9, '스페인어'],
    ['ara', 10, '아랍어'],
    ['mon', 1, '몽골어'],
    ['vie', 2, '베트남어'],
    ['tha', 3, '타이어'],
    ['ind', 4, '인도네시아어'],
    ['rus', 5, '러시아어'],
    ['chn', 11, '중국어']
]
_SENSE_CAT_MAX = [
    17,
    30,
    41,
    50,
    59,
    76,
    83,
    92,
    100,
    110,
    118,
    125,
    133,
    153
]


def _build_language_query(lang):
    lang = ScraperTranslationLanguage.get_value(lang)
    [nation, code, exo] = _LANG_INFO[lang - 1] if lang and lang != 0 else [None, 0, None]

    if code == 0:
        return '', '', None

    return f'&nation={nation}&nationCode={code}', f'{nation}/', exo

def _build_sense_category_query(category):
    category = MeaningCategory.get_value(category, category)

    if category <= 0 or category > 153:
        return '&lgCategoryCode=0&miCategoryCode=-1'

    if category == 1:
        return '&lgCategoryCode=1&miCategoryCode=-1'

    code_large = 0
    code_mid = 1000 + category if category < 129 else 1100 + category

    for idx, cat_max in enumerate(_SENSE_CAT_MAX):
        if category == cat_max + 1:
            code_large = idx + 2
            code_mid = -1
            break

        if category <= cat_max:
            code_large = idx + 1
            break

    return f'&lgCategoryCode={code_large}&miCategoryCode={code_mid}'

def _build_subject_category_query(category):
    if not isiterable(category, exclude=(str,)):
        category = (category,)

    value = []

    for cat in category:
        cat_value = SubjectCategory.get_value(cat, cat)

        if cat_value == '0':
            value = []

            for i in range(1, 107):
                value.append(f'&actCategory={map_advanced_param("subject_cat", i)}')

            return ''.join(value)

        value.append(f'&actCategory={map_advanced_param("subject_cat", cat_value)}')

    return ''.join(value)


def fetch_today_word(**kwargs):
    """
    Fetches information about the word of the day by scraping the dictionary website.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/return_types/#wordofthedayresponse)
    for details.

    - ``guarantee_keys``: Sets whether keys that are missing from the response should be inserted
    with default values. A value of ``True`` guarantees that every key that is not required
    is included, including keys set by the scraper.
    - ``translation_language``: The language for which translations should be included.
    """

    [lang_query, nation, exonym] = _build_language_query(kwargs.get('translation_language'))
    doc = send_request(_BASE_URL.format(nation), True)
    if doc is None:
        return None

    dt_elem = doc.cssselect('dl.today_word > dt')[0]
    dd_elems = doc.cssselect('dl.today_word > dd')
    word_elem = dt_elem.cssselect('a')[0]
    strong_elem = word_elem.cssselect('strong')[0]
    sup_elems = word_elem.cssselect('strong > sup')

    dfn_idx = 0 if not nation and len(dd_elems) < 3 else 1
    result = {
        'target_code': int(extract_href(word_elem) or 0),
        'word': strong_elem.text.strip(),
        'definition': dd_elems[dfn_idx].text_content().strip()
    }

    result['url'] = _TRANSLATED_VIEW_URL.format(nation, result['target_code'], lang_query)
    result['homograph_num'] = int(sup_elems[0].text_content() or 0 if len(sup_elems) > 0 else 0)

    read_wotd_details(
        result,
        dt_elem,
        dd_elems,
        exonym,
        kwargs.get('guarantee_keys', False)
    )

    return {'data': result, 'response_type': 'word_of_the_day'}

def fetch_meaning_category_words(**kwargs):
    """
    Fetches words that belong to the provided meaning category.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/scraper/#fetch_meaning_category_words)
    for details.

    - ``guarantee_keys``: Sets whether keys that are missing from the response should be inserted
    with default values. A value of ``True`` guarantees that every key that is not required
    is included, including keys set by the scraper.
    - ``category``: The meaning category to fetch.
    - ``page``: The page at which the search should start ``[1, 1000]``.
    - ``per_page``: The maximum number of search results to return ``[10, 100]``.
    - ``sort``: The sort method that should be used.
    - ``translation_language``: A language for which translations should be included.
    """

    page = kwargs.get('page', 1)
    per_page = kwargs.get('per_page', 10)
    [lang, nation, exonym] = _build_language_query(kwargs.get('translation_language'))
    url = _SENSE_URL.format(
        nation,
        lang,
        page,
        per_page,
        'C' if SortMethod.get_value(kwargs.get('sort')) == 'popular' else 'W',
        _build_sense_category_query(kwargs.get('category', 0)))

    doc = send_request(url, True)
    [results, total] = read_search_results(doc, exonym, kwargs.get('guarantee_keys', False))

    return {
        'data': {
            'search_url': url,
            'page': int(page),
            'per_page': int(per_page),
            'total_results': total,
            'results': results
        },
        'response_type': 'scraped_word'
    }

def fetch_subject_category_words(**kwargs):
    """
    Fetches words that belong to one of the provided subject categories.

    See the
    [documentation](https://krdictpy.readthedocs.io/en/stable/scraper/#fetch_subject_category_words)
    for details.

    - ``guarantee_keys``: Sets whether keys that are missing from the response should be inserted
    with default values. A value of ``True`` guarantees that every key that is not required
    is included, including keys set by the scraper.
    - ``category``: The subject category to fetch.
    - ``page``: The page at which the search should start ``[1, 1000]``.
    - ``per_page``: The maximum number of search results to return ``[10, 100]``.
    - ``sort``: The sort method that should be used.
    - ``translation_language``: A language for which translations should be included.
    """

    page = kwargs.get('page', 1)
    per_page = kwargs.get('per_page', 10)
    [lang, nation, exonym] = _build_language_query(kwargs.get('translation_language'))
    url = _SUBJECT_URL.format(
        nation,
        lang,
        page,
        per_page,
        'C' if SortMethod.get_value(kwargs.get('sort')) == 'popular' else 'W',
        _build_subject_category_query(kwargs.get('category', 0)))

    doc = send_request(url, True)
    [results, total] = read_search_results(doc, exonym, kwargs.get('guarantee_keys', False))

    return {
        'data': {
            'search_url': url,
            'page': int(page),
            'per_page': int(per_page),
            'total_results': total,
            'results': results
        },
        'response_type': 'scraped_word'
    }
