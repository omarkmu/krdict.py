"""
Contains potential usage examples of the library.
"""

import os
import sys
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
    data = response.data
    print(f'Total Results: {data.total_results}')

    for idx, result in enumerate(data.results):
        first_dfn = (
            result.definition_info
            if isinstance(response, krdict.DefinitionResponse)
            else result.definitions[0]
        )

        origin_info = f' ({result.origin})' if 'origin' in result and result.origin else ''
        print(f'{idx + 1}. {result.word}{origin_info}: {first_dfn.definition}')

        for translation in first_dfn.translations:
            print(f'   {translation.word}: {translation.definition}')


def _display_view_results(response):
    data = response.data
    result = data.results[0]

    origin = []
    for origin_obj in result.word_info.original_language_info:
        origin.append(origin_obj.original_language)

    pronunciation = []
    for pronunciation_obj in result.word_info.pronunciation_info:
        if pronunciation:
            pronunciation.append('/')

        pronunciation.append(pronunciation_obj.pronunciation)
        if 'url' in pronunciation_obj:
            pronunciation.append(f' ({pronunciation_obj.url})')

    print(f'{result.word_info.word}'
        + f' 「{result.word_info.part_of_speech}」'
        + (f' ({"".join(origin)})' if origin else '')
        + (f' [{"".join(pronunciation)}]' if pronunciation else '')
    )

    print(data.url)

    for idx, dfn in enumerate(result.word_info.definition_info):
        lines = [dfn.definition]

        # populated if at least one translation language is specified.
        if dfn.translations:
            translation = dfn.translations[0]
            lines = [translation.word] if 'word' in translation else []
            lines.append(f'\n   {dfn.definition}')
            lines.append(f'\n   {dfn.translations[0].definition}')

        print(f'{idx + 1}. {"".join(lines)}')

        for i, example in enumerate(dfn.example_info):
            if i == 5:
                print('   • ...')
                break
            print(f'   • {example.example}')

        for i, multimedia in enumerate(dfn.multimedia_info):
            if i == 5:
                print('   ► ...')
                break

            # populated in scraped responses if the fetch_multimedia option is set to True.
            if 'content_urls' in multimedia and multimedia.content_urls:
                print(f'   ► {",".join(multimedia.content_urls)} ({multimedia.type})')
            else:
                print(f'   ► {multimedia.url} ({multimedia.type})')


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
        data = response.data
        total_results = data.total_results

        page += 1
        results += data.results
        has_next = data.per_page * data.page < total_results

        print((f'Collected {len(data.results)} results from page {page - 1}. '
            f'{"Querying next page." if has_next else "All results collected."}'))

    print(f'{len(results)} results collected. Total results: {total_results}.')

# Example 2
def search_definitions():
    """
    Performs a search for definitions containing the word 나무.
    """

    response = krdict.search(
        query='나무',
        # if you're using type checking,
        # setting the search_type parameter in a call with
        # keyword arguments will define the type of the search result.
        # when calling with an unpacked dictionary (**{...}),
        # the more specific type cannot be inferred.
        search_type=krdict.SearchType.DEFINITION,
        translation_language=krdict.TranslationLanguage.ENGLISH,
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
        search_type=krdict.SearchType.EXAMPLE,
        raise_api_errors=True
    )

    for result in response.data.results:
        print(f'• {result.example} (Word: {result.word})')

# Example 4
def search_idioms():
    """
    Performs a search for idioms and proverbs containing the word 나무.
    """

    response = krdict.search(
        query='나무',
        search_type=krdict.SearchType.IDIOM_PROVERB,
        translation_language=krdict.TranslationLanguage.ENGLISH,
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
        search_type=krdict.SearchType.WORD,
        search_target=krdict.SearchTarget.DEFINITION,
        vocabulary_level=krdict.VocabularyLevel.BEGINNER,
        multimedia_type=(
            krdict.MultimediaType.PHOTO,
            krdict.MultimediaType.ILLUSTRATION,
            krdict.MultimediaType.VIDEO,
            krdict.MultimediaType.ANIMATION,
            krdict.MultimediaType.SOUND
        ),
        # the search method must be set to 'include' for the desired behavior;
        # the default value is 'exact', which returns only exact matches.
        search_method=krdict.SearchMethod.INCLUDE,
        translation_language=krdict.TranslationLanguage.ENGLISH,
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
        search_type=krdict.SearchType.WORD,
        search_target=krdict.SearchTarget.ORIGINAL_LANGUAGE,
        search_method=krdict.SearchMethod.INCLUDE,
        translation_language=krdict.TranslationLanguage.ENGLISH,
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
        translation_language=krdict.TranslationLanguage.ENGLISH,
        raise_api_errors=True
    )

    # or, equivalently:
    # response = krdict.view(
    #     target_code=42075,
    #     translation_language=krdict.TranslationLanguage.ENGLISH,
    #     raise_api_errors=True
    # )

    _display_view_results(response)

# Example 8
def scraped_view_query():
    """
    Displays the results of a scraped view query for the word 단풍나무.
    """

    response = krdict.scraper.view(
        # scraper method can only query with target code, not query strings
        target_code=42075,
        translation_language=krdict.TranslationLanguage.ENGLISH,
        fetch_multimedia=True
    )

    _display_view_results(response)

# Example 9
def word_of_the_day():
    """
    Fetches the word of the day, then fetches extended information using the result.
    """

    wotd_response = krdict.scraper.fetch_today_word(
        translation_language=krdict.TranslationLanguage.ENGLISH
    )

    wotd_translation = ''
    if 'translation' in wotd_response.data:
        wotd_translation = f' ({wotd_response.data.translations[0].word})'

    print((f'Word of the Day: {wotd_response.data.word}{wotd_translation}'
        f'\n{wotd_response.data.definition}'
        f'\n{wotd_response.data.url}'))

    response = krdict.scraper.view(
        # with the target code from the scraped word of the day response,
        # we can use the scraper to get extended information.
        target_code=wotd_response.data.target_code,
        translation_language=krdict.TranslationLanguage.ENGLISH,
        fetch_multimedia=True
    )

    print('\nExtended Info:')
    _display_view_results(response)

# Example 10
def fetch_meaning_category():
    """
    Fetches words in the 인간 > 신체 부위 meaning category.
    """

    response = krdict.scraper.fetch_meaning_category_words(
        # equivalent: category=3,
        # equivalent: category='인간 > 신체 부위',
        # equivalent: category='human > body parts',
        category=krdict.MeaningCategory.HUMAN_BODY_PARTS,
        translation_language=krdict.TranslationLanguage.ENGLISH
    )

    _display_results(response)

# Example 11
def fetch_subject_category():
    """
    Fetches words in the 인사하기 subject category.
    """

    response = krdict.scraper.fetch_subject_category_words(
        # category also accepts an array of multiple categories,
        # or krdict.SubjectCategory.ALL to retrieve all categories' words.

        # equivalent: category=1,
        # equivalent: category='인사하기',
        # equivalent: category='greeting',
        category=krdict.SubjectCategory.ELEMENTARY_GREETING,
        translation_language=krdict.TranslationLanguage.ENGLISH
    )

    _display_results(response)

# Example 12
def hanja_info():
    """
    Displays information about hanja in a
    scraped view response.
    """

    response = krdict.scraper.view(
        target_code=14951 # target code for 가감승제
    )

    assert len(response.data.results) == 1

    # filter out non-한자
    lang_info = filter(
        lambda info: info.language_type == '한자',
        response.data.results[0].word_info.original_language_info
    )

    for idx, info in enumerate(lang_info):
        for h_info in info.hanja_info:
            print(f'Hanja {idx + 1}: {h_info.hanja}')
            print(f'Radical: {h_info.radical}')
            print(f'Stroke Count: {h_info.stroke_count}')
            print('Readings:')

            for reading in h_info.readings:
                print(f'   {reading}')

            print()


_EXAMPLE_FUNCS = [
    pagination,
    search_definitions,
    search_examples,
    search_idioms,
    search_beginner_words_with_multimedia,
    search_words_with_hanja,
    view_query,
    scraped_view_query,
    word_of_the_day,
    fetch_meaning_category,
    fetch_subject_category,
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
