"""
Contains potential usage examples of the library.
"""

import os
import sys
import json
import requests
import krdict

try:
    # try to load environment variables from .env file
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

krdict.set_key(os.getenv('KRDICT_KEY'))


def _display_results(response):
    data = response['data']
    print(f'Total Results: {data["total_results"]}')

    for idx, result in enumerate(data['results']):
        first_dfn = result['definitions'][0]

        # note: get is used instead of indexing because 'origin' is not a required key.
        # the same is true for the below calls to get.
        # this can be avoided using the guarantee_keys parameter (see example 12).
        origin = result.get('origin')
        origin_info = f' ({origin})' if origin else ''
        print(f'{idx + 1}. {result["word"]}{origin_info}: {first_dfn["definition"]}')

        for translation in first_dfn.get('translations', []):
            print(f'   {translation.get("word")}: {translation["definition"]}')

        # scraped word responses (e.g. from category scraping) return only one translation.
        if 'translation' in first_dfn:
            translation = first_dfn['translation']
            print(f'   {translation.get("word")}: {translation["definition"]}')


def _display_view_results(response):
    data = response['data']
    result = data['results'][0]

    origin = ''
    for origin_obj in result['word_info'].get('original_language_info', []):
        origin += origin_obj['original_language']

    pronunciation = ''
    for pronunciation_obj in result['word_info'].get('pronunciation_info', []):
        if pronunciation:
            pronunciation += '/'

        pronunciation += pronunciation_obj['pronunciation']
        if 'url' in pronunciation_obj:
            pronunciation += f' ({pronunciation_obj["url"]})'

    print(f'{result["word_info"]["word"]}'
        + f' 「{result["word_info"]["part_of_speech"]}」'
        + (f' ({origin})' if origin else '')
        + (f' [{pronunciation}]' if pronunciation else ''))
    print(data['url'])

    for idx, dfn in enumerate(result['word_info']['definition_info']):
        lines = dfn['definition']

        # present if at least one translation language is specified.
        if 'translations' in dfn:
            translation = dfn['translations'][0]
            lines = translation['word'] if 'word' in translation else ''
            lines += f'\n   {dfn["definition"]}'
            lines += f'\n   {dfn["translations"][0]["definition"]}'

        print(f'{idx + 1}. {lines}')

        for i, example in enumerate(dfn.get('example_info', [])):
            if i == 5:
                print('   • ...')
                break
            print(f'   • {example["example"]}')

        for i, multimedia in enumerate(dfn.get('multimedia_info', [])):
            if i == 5:
                print('   ► ...')
                break

            # present if scraping is enabled and the fetch_multimedia option is set to True.
            if 'media_urls' in multimedia:
                print(f'   ► {",".join(multimedia["media_urls"])} ({multimedia["type"]})')
            else:
                print(f'   ► {multimedia["url"]} ({multimedia["type"]})')


# Example 1
def pagination():
    """
    Collects results from multiple API calls using pagination.
    """

    page = 1
    results = []
    has_next = True
    total_results = 0

    while has_next:
        response = krdict.search(query='나무', page=page, per_page=20, raise_api_errors=True)
        data = response['data']
        total_results = data['total_results']

        page += 1
        results += data['results']
        has_next = data['per_page'] * data['page'] < total_results

        print(f'Collected {len(data["results"])} results from page {page - 1}. '
            + f'{"Querying next page." if has_next else "All results collected."}')

    print(f'{len(results)} results collected. Total results: {total_results}.')

# Example 2
def search_definitions():
    """
    Performs a search for definitions containing the word 나무.
    """

    response = krdict.search(
        query='나무',
        # if you're using type checking,
        # setting the search_type parameter in a keyword
        # arguments call will define the search result.
        # when calling with an unpacked dictionary (**{...}),
        # the more specific type cannot be inferred.
        search_type='definition',
        translation_language='english',
        raise_api_errors=True
    )

    _display_results(response)

# Example 3
def search_examples():
    """
    Performs a search for examples containing the word 나무.
    """

    response = krdict.search(
        query='나무',
        search_type='example',
        raise_api_errors=True
    )

    for result in response['data']['results']:
        print(f'• {result["example"]} (Word: {result["word"]})')

# Example 4
def search_idioms():
    """
    Performs a search for idioms and proverbs containing the word 나무.
    """

    response = krdict.search(
        query='나무',
        search_type='idiom_proverb',
        translation_language='english',
        raise_api_errors=True
    )

    _display_results(response)

# Example 5
def search_beginner_words_with_multimedia():
    """
    Displays the first 10 results which are beginner grade words and contain multimedia.
    """

    response = krdict.advanced_search(
        # the API lacks a supported way to search without a query,
        # but because most definitions contain a period, it's possible to
        # achieve near-perfect results using the query '.' and the 'definition'
        # search target. in this example, all matches are returned.
        query='.',
        search_type='word',
        search_target='definition',
        vocabulary_grade='beginner',
        multimedia_info=['photo', 'illustration', 'video', 'animation', 'sound'],
        # the search method must be set to 'include' for the desired behavior;
        # the default value is 'exact', which returns only exact matches.
        search_method='include',
        translation_language='english',
        raise_api_errors=True
    )

    _display_results(response)

# Example 6
def search_words_with_hanja():
    """
    Displays the first 10 results which contain the 한자 機.
    """

    response = krdict.advanced_search(
        query='機',
        search_type='word',
        search_target='original_language',
        search_method='include',
        translation_language='english',
        raise_api_errors=True
    )

    _display_results(response)

# Example 7
def view_query():
    """
    Displays the results of a view query for the word 단풍나무.
    """

    response = krdict.view(
        query='단풍나무',
        # the homograph_num parameter defaults to 0.
        # it is included here for completeness.
        homograph_num=0,
        translation_language='english',
        raise_api_errors=True
    )

    # or, equivalently:
    # response = krdict.view(
    #     target_code=42075,
    #     translation_language='english',
    #     raise_api_errors=True
    # )

    _display_view_results(response)

# Example 8
def view_query_enhanced():
    """
    Displays the results of a view query for the word 단풍나무
    with results enhanced from scraping.
    """

    response = krdict.view(
        query='단풍나무',
        homograph_num=0,
        translation_language='english',
        raise_api_errors=True,
        # the scraper can be applied to the search and advanced_search
        # functions similarly; for those functions, the only
        # additional information retrieved is pronunciation URLs.
        options={'use_scraper': True, 'fetch_multimedia': True}
    )

    _display_view_results(response)

# Example 9
def word_of_the_day():
    """
    Fetches the word of the day, then fetches extended information
    about the word of the day using the result.
    """

    wotd_response = krdict.scraper.fetch_today_word(translation_language='english')
    wotd_translation = ''

    if 'translation' in wotd_response['data']:
        wotd_translation = f' ({wotd_response["data"]["translation"].get("word", "")})'

    print(f'Word of the Day: {wotd_response["data"]["word"]}{wotd_translation}'
        + f'\n{wotd_response["data"]["definition"]}'
        + f'\n{wotd_response["data"]["url"]}')

    response = krdict.view(
        # with the target code from the scraped word of the day response,
        # we can use the API and the scraper to get extended information.
        target_code=wotd_response['data']['target_code'],
        translation_language='english',
        raise_api_errors=True,
        options={'use_scraper': True, 'fetch_multimedia': True}
    )

    print('\nExtended Info:')
    _display_view_results(response)

# Example 10
def fetch_meaning_category():
    """
    Fetches words in the 인간 > 신체 부위 meaning category.
    """

    response = krdict.scraper.fetch_meaning_category_words(
        category='인간 > 신체 부위',
        translation_language='english'
    )

    # or, equivalently:
    # response = krdict.scraper.fetch_meaning_category_words(
    #     category=3,
    #     translation_language='english'
    # )

    _display_results(response)

# Example 11
def fetch_subject_category():
    """
    Fetches words in the 인사하기 subject category.
    """

    response = krdict.scraper.fetch_subject_category_words(
        # category also accepts an array of multiple categories,
        # or '전체'/0 to retrieve all categories' words.
        category='인사하기',
        translation_language='english'
    )

    # or, equivalently:
    # response = krdict.scraper.fetch_subject_category_words(
    #     category=1,
    #     translation_language='english'
    # )

    _display_results(response)

# Example 12
def guarantee_keys():
    """
    Compares results without and with guaranteed keys.
    """

    print('Default word_info:')
    response = krdict.view(
        target_code=57557,
        raise_api_errors=True
    )

    # prints a result with plenty of "not required" keys missing.
    print(json.dumps(response['data']['results'][0]['word_info'], indent=2, ensure_ascii=False))


    print('\nWith guarantee_keys:')
    # same call as above, with guarantee_keys set to True.
    response = krdict.view(
        target_code=57557,
        guarantee_keys=True,
        raise_api_errors=True
    )

    # prints a result with all "not required" keys included as default values,
    # including keys which can only be obtained from scraping, such as "hanja_info",
    # "url", and "media_urls".
    print(json.dumps(response['data']['results'][0]['word_info'], indent=2, ensure_ascii=False))

# Example 13
def hanja_info():
    """
    Displays information about hanja in an
    extended view response.
    """

    response = krdict.view(
        query='가감승제',
        homograph_num=0,
        raise_api_errors=True,
        guarantee_keys=True,
        options={'use_scraper': True}
    )

    # without guarantee_keys, a check for original_language_info would be necessary.
    # the length of response['data']['results'] should also be checked in careful code.
    lang_info = response['data']['results'][0]['word_info']['original_language_info']

    idx = 0
    for info in lang_info:
        # filter out non-한자
        if info['language_type'] != '한자':
            continue

        for h_info in info['hanja_info']:
            print(f'Hanja {idx + 1}: {h_info["hanja"]}')
            print(f'Radical: {h_info["radical"]}')
            print(f'Stroke Count: {h_info["stroke_count"]}')
            print('Readings:')

            for reading in h_info['readings']:
                print(f'   {reading}')

            print()
            idx += 1


_EXAMPLE_FUNCS = [
    pagination,
    search_definitions,
    search_examples,
    search_idioms,
    search_beginner_words_with_multimedia,
    search_words_with_hanja,
    view_query,
    view_query_enhanced,
    word_of_the_day,
    fetch_meaning_category,
    fetch_subject_category,
    guarantee_keys,
    hanja_info
]

def _run_examples():
    pad = '═' * 39
    pad_line = '═' * 90

    for idx, example_func in enumerate(_EXAMPLE_FUNCS):
        print(f'{pad} Example {idx+1:02d} {pad}')
        print(example_func.__doc__)

        example_func()
        print()

    print(pad_line)


if __name__ == '__main__':
    try:
        _run_examples()
    except (krdict.KRDictException, requests.RequestException) as exc:
        sys.exit(exc)
