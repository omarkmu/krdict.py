"""
Handles testing the krdict module.
"""

import os
import unittest
import krdict

_BASE_VIEW_URL = 'https://krdict.korean.go.kr/dicSearch/SearchView?ParaWordNo={}'

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

krdict.set_key(os.getenv('KRDICT_KEY'))

class TestKRDict(unittest.TestCase):
    """Contains test cases for the main module."""
    def test_api_error(self):
        """Invalid query string results in an API error"""
        response = krdict.search(query='')
        self.assertIn('error', response)
        self.assertIn('request_params', response)
        self.assertEqual(response['response_type'], 'error')
        self.assertNotIn('data', response)

        if response['response_type'] == 'error':
            self.assertEqual(response['error']['error_code'], 100)
            self.assertEqual(response['error']['message'], 'Incorrect query request')

    def test_basic_search(self):
        """Basic search query returns proper results"""
        response = krdict.search(query='나무', search_type='word', raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(len(data['results']), 10)
        self.assertEqual(data['per_page'], 10)
        self.assertEqual(data['total_results'], 53)
        self.assertEqual(data['page'], 1)

        expected_values = [
            (0, 32750, 3, '나무','명사'),
            (0, 38842, 2, '나무라다', '동사'),
            (0, 38841, 1, '나무꾼', '명사'),
            (0, 38844, 1, '나무람', '명사'),
            (0, 17918, 1, '나무배', '명사'),
            (0, 17919, 1, '나무뿌리', '명사'),
            (0, 17920, 1, '나무숲', '명사'),
            (1, 38845, 2, '나무아미타불', '명사'),
            (2, 38846, 1, '나무아미타불', '감탄사'),
            (0, 17921, 1, '나무저', '명사')
        ]

        for idx, values in enumerate(expected_values):
            [homograph_num, target_code, meaning_len, word, pos] = values
            result = data['results'][idx]

            self.assertEqual(result['word'], word)
            self.assertEqual(result['part_of_speech'], pos)
            self.assertEqual(result['homograph_num'], homograph_num)
            self.assertEqual(result['target_code'], target_code)
            self.assertEqual(result['url'], _BASE_VIEW_URL.format(target_code))
            self.assertEqual(len(result['definitions']), meaning_len)

            for index in range(meaning_len):
                def_info = result['definitions'][index]

                self.assertIn('definition', def_info)
                self.assertIn('order', def_info)
                self.assertEqual(def_info['order'], index + 1)

    def test_definition_search(self):
        """Definition search query returns proper results"""
        response = krdict.search(query='나무', search_type='definition', raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['total_results'], 493)

        for result in data['results']:
            self.assertIn('word', result)
            self.assertIn('definitions', result)

            for def_info in result['definitions']:
                self.assertIn('definition', def_info)

    def test_example_search(self):
        """Example search query returns proper results"""
        response = krdict.search(query='나무', search_type='example', raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['total_results'], 2281)

        for result in data['results']:
            self.assertIn('example', result)

    def test_idiom_proverb_search(self):
        """Idiom/Proverb search query returns proper results"""
        response = krdict.search(query='나무', search_type='idiom_proverb', raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['total_results'], 13)

        for result in data['results']:
            self.assertIn('word', result)

    def test_page(self):
        """Setting page parameter returns proper page"""
        response = krdict.search(
            query='나무',
            search_type='word',
            page=2,
            raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['page'], 2)

    def test_per_page(self):
        """Setting per_page parameter returns correct number of results"""
        response = krdict.search(
            query='나무',
            search_type='word',
            per_page=15,
            raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['per_page'], 15)
        self.assertEqual(len(data['results']), 15)

    def test_raise_api_errors(self):
        """Invalid query string with raise_api_errors=True raises"""
        with self.assertRaises(krdict.KRDictException) as ctx:
            krdict.search(query='', raise_api_errors=True)
        self.assertIsInstance(ctx.exception.request_params, dict)
        self.assertEqual(ctx.exception.error_code, 100)
        self.assertEqual(ctx.exception.message, 'Incorrect query request')

    def test_search_method(self):
        """Advanced search with various search methods returns proper results"""
        response = krdict.advanced_search(query='나무', raise_api_errors=True)
        self.assertIn('data', response)
        self.assertEqual(response['data']['total_results'], 1)
        self.assertEqual(response['data']['results'][0]['target_code'], 32750)

        response = krdict.advanced_search(query='나무', search_method='start', raise_api_errors=True)
        self.assertIn('data', response)
        self.assertEqual(response['data']['total_results'], 17)

        response = krdict.advanced_search(query='나무', search_method='end', raise_api_errors=True)
        self.assertIn('data', response)
        self.assertEqual(response['data']['total_results'], 33)

    def test_sort(self):
        """Setting sort parameter to popular returns sorted results"""
        response = krdict.search(
            query='나무',
            search_type='word',
            sort='popular',
            raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['results'][0]['target_code'], 32750)
        self.assertEqual(data['results'][1]['target_code'], 38842)
        self.assertEqual(data['results'][2]['target_code'], 38847)

    def test_translation(self):
        """Setting translation_language parameter returns results with translations"""
        response = krdict.search(
            query='나무',
            search_type='word',
            guarantee_keys=True,
            raise_api_errors=True,
            translation_language=['english', 'japanese'])

        self.assertIn('data', response)
        data = response['data']

        for result in data['results']:
            self.assertIn('definitions', result)
            self.assertIsInstance(result['definitions'], list)

            for def_info in result['definitions']:
                self.assertIn('translations', def_info)
                self.assertIsInstance(def_info['translations'], list)
                self.assertEqual(len(def_info['translations']), 2)

                eng_translation = def_info['translations'][0]
                jpn_translation = def_info['translations'][1]

                self.assertIsInstance(eng_translation, dict)
                self.assertIn('word', eng_translation)
                self.assertIn('definition', eng_translation)
                self.assertIn('language', eng_translation)
                self.assertEqual(eng_translation['language'], '영어')

                self.assertIsInstance(jpn_translation, dict)
                self.assertIn('word', jpn_translation)
                self.assertIn('definition', jpn_translation)
                self.assertIn('language', jpn_translation)
                self.assertEqual(jpn_translation['language'], '일본어')

    def test_view(self):
        """Basic view query returns proper results"""
        response = krdict.view(target_code=32750, raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['total_results'], 1)

        word_info = data['results'][0]['word_info']

        self.assertIn('word', word_info)
        self.assertIn('word_unit', word_info)
        self.assertIn('word_type', word_info)
        self.assertIn('part_of_speech', word_info)
        self.assertIn('homograph_num', word_info)
        self.assertIn('vocabulary_grade', word_info)
        self.assertIn('definition_info', word_info)
        self.assertEqual(len(word_info['definition_info']), 3)

    def test_view_word_info(self):
        """Basic view query with word info returns proper results"""
        response = krdict.view(query='나무', raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['total_results'], 1)
        self.assertEqual(data['results'][0]['target_code'], 32750)

class TestKRDictScraper(unittest.TestCase):
    """Contains test cases for the scraper module."""
    def test_scraper_advanced(self):
        """Advanced search query with scraper returns proper results"""
        response = krdict.advanced_search(query='나무',
            raise_api_errors=True,
            guarantee_keys=True,
            search_type='word',
            search_method='include',
            sort='popular',
            options={'use_scraper': True})

        self.assertIn('data', response)
        data = response['data']

        self.assertIn('search_url', data)
        self.assertEqual(len(data['results']), 10)

        for result in data['results']:
            self.assertIn('pronunciation_urls', result)
            self.assertEqual(len(result['pronunciation_urls']), 1)

    def test_scraper_category(self):
        """Advanced search query using categories with scraper returns proper results"""
        response = krdict.advanced_search(query='가',
            raise_api_errors=True,
            guarantee_keys=True,
            search_method='include',
            subject_category='위치 표현하기',
            search_type='word',
            options={
                'use_scraper': True
            })
        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(len(data['results']), 2)

        self.assertEqual(data['results'][0]['word'], '가리키다')
        self.assertIn('pronunciation_urls', data['results'][0])
        self.assertEqual(data['results'][0]['pronunciation_urls'][0],
            ('https://dicmedia.korean.go.kr/multimedia/multimedia_files/'
            'convert/20170223/442961/SND000021293.mp3'))

        self.assertEqual(data['results'][1]['word'], '가운데')
        self.assertIn('pronunciation_urls', data['results'][1])
        self.assertEqual(data['results'][1]['pronunciation_urls'][0],
            ('https://dicmedia.korean.go.kr/multimedia/multimedia_files/'
            'convert/20160913/20000/17000/307982/SND000317336.mp3'))

    def test_scraper_fetch_today_word(self):
        """Fetching word of the day with scraper returns proper results"""
        response = krdict.scraper.fetch_today_word()

        self.assertIn('data', response)
        data = response['data']

        self.assertIn('target_code', data)
        self.assertIn('word', data)
        self.assertIn('definition', data)
        self.assertIn('url', data)
        self.assertIn('homograph_num', data)

    def test_scraper_fetch_today_word_translation(self):
        """Fetching word of the day with translation with scraper returns proper results"""
        response = krdict.scraper.fetch_today_word(translation_language='english')

        self.assertIn('data', response)
        data = response['data']

        self.assertIn('target_code', data)
        self.assertIn('word', data)
        self.assertIn('definition', data)
        self.assertIn('url', data)
        self.assertIn('homograph_num', data)

        self.assertIn('translation', data)
        self.assertIn('definition', data['translation'])
        self.assertIn('language', data['translation'])

    def test_scraper_fetch_meaning_category_words(self):
        """Fetching meaning category words with scraper returns proper results"""
        response = krdict.scraper.fetch_meaning_category_words(category=3, per_page=15)

        self.assertIn('data', response)
        data = response['data']

        self.assertIn('search_url', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)
        self.assertIn('total_results', data)
        self.assertIn('results', data)

        self.assertEqual(data['search_url'],
            ('https://krdict.korean.go.kr/dicSearchDetail/'
            'searchDetailSenseCategoryResult?searchFlag=Y&currentPage=1&blockCount=15&sort=W'
            '&lgCategoryCode=1&miCategoryCode=1003'))
        self.assertEqual(data['page'], 1)
        self.assertEqual(data['per_page'], 15)
        self.assertEqual(len(data['results']), 15)
        self.assertEqual(data['total_results'], 113)

    def test_scraper_fetch_meaning_category_words_translation(self):
        """Fetching meaning category words with translation with scraper returns proper results"""
        response = krdict.scraper.fetch_meaning_category_words(
            guarantee_keys=True,
            category=3,
            per_page=15,
            translation_language='english')

        self.assertIn('data', response)
        data = response['data']

        self.assertIn('search_url', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)
        self.assertIn('total_results', data)
        self.assertIn('results', data)

        self.assertEqual(data['search_url'],
            ('https://krdict.korean.go.kr/eng/dicSearchDetail/'
            'searchDetailSenseCategoryResult?searchFlag=Y&nation=eng&nationCode=6'
            '&currentPage=1&blockCount=15&sort=W&lgCategoryCode=1&miCategoryCode=1003'))
        self.assertEqual(data['page'], 1)
        self.assertEqual(data['per_page'], 15)
        self.assertEqual(len(data['results']), 15)
        self.assertEqual(data['total_results'], 113)

        for result in data['results']:
            self.assertIn('definitions', result)
            for dfn in result['definitions']:
                self.assertIn('definition', dfn)
                self.assertIn('order', dfn)
                self.assertIn('translation', dfn)

                if dfn['translation']:
                    self.assertIn('definition', dfn['translation'])
                    self.assertIn('word', dfn['translation'])
                    self.assertIn('language', dfn['translation'])
                    self.assertEqual(dfn['translation']['language'], '영어')

    def test_scraper_fetch_subject_category_words(self):
        """Fetching meaning category words with scraper returns proper results"""
        response = krdict.scraper.fetch_subject_category_words(category=1, per_page=15)

        self.assertIn('data', response)
        data = response['data']

        self.assertIn('search_url', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)
        self.assertIn('total_results', data)
        self.assertIn('results', data)

        self.assertEqual(data['search_url'],
            ('https://krdict.korean.go.kr/dicSearchDetail/searchDetailActCategoryResult?'
            'searchFlag=Y&currentPage=1&blockCount=15&sort=W&actCategory=20001'))
        self.assertEqual(data['page'], 1)
        self.assertEqual(data['per_page'], 15)
        self.assertEqual(len(data['results']), 15)
        self.assertEqual(data['total_results'], 17)

    def test_scraper_fetch_subject_category_words_translation(self):
        """Fetching meaning category words with translation with scraper returns proper results"""
        response = krdict.scraper.fetch_subject_category_words(
            guarantee_keys=True,
            category=1,
            per_page=15,
            translation_language='english')

        self.assertIn('data', response)
        data = response['data']

        self.assertIn('search_url', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)
        self.assertIn('total_results', data)
        self.assertIn('results', data)

        self.assertEqual(data['search_url'],
            ('https://krdict.korean.go.kr/eng/dicSearchDetail/searchDetailActCategoryResult?'
            'searchFlag=Y&nation=eng&nationCode=6'
            '&currentPage=1&blockCount=15&sort=W&actCategory=20001'))
        self.assertEqual(data['page'], 1)
        self.assertEqual(data['per_page'], 15)
        self.assertEqual(len(data['results']), 15)
        self.assertEqual(data['total_results'], 17)

        for result in data['results']:
            self.assertIn('definitions', result)
            for dfn in result['definitions']:
                self.assertIn('definition', dfn)
                self.assertIn('order', dfn)
                self.assertIn('translation', dfn)

                if dfn['translation']:
                    self.assertIn('definition', dfn['translation'])
                    self.assertIn('word', dfn['translation'])
                    self.assertIn('language', dfn['translation'])
                    self.assertEqual(dfn['translation']['language'], '영어')

    def test_scraper_view(self):
        """Basic view query with scraper returns proper results"""
        response = krdict.view(target_code=55874,
            guarantee_keys=True,
            raise_api_errors=True,
            options={'use_scraper': True})

        self.assertIn('data', response)
        self.assertEqual(len(response['data']['results']), 1)
        result = response['data']['results'][0]

        self.assertIn('word_info', result)
        self.assertIn('pronunciation_info', result['word_info'])
        self.assertIn('original_language_info', result['word_info'])

        self.assertEqual(len(result['word_info']['pronunciation_info']), 1)
        self.assertIn('url', result['word_info']['pronunciation_info'][0])

        self.assertEqual(len(result['word_info']['original_language_info']), 1)
        orig_info = result['word_info']['original_language_info'][0]

        self.assertIn('pronunciation_info', result['word_info'])
        self.assertEqual(len(result['word_info']['pronunciation_info']), 1)
        self.assertIn('url', result['word_info']['pronunciation_info'][0])

        self.assertEqual(orig_info['original_language'], '木曜日')
        self.assertEqual(orig_info['language_type'], '한자')

        self.assertIn('hanja_info', orig_info)
        self.assertEqual(len(orig_info['hanja_info']), 3)

        hanja_1 = orig_info['hanja_info'][0]
        self.assertEqual(hanja_1['hanja'], '木')
        self.assertEqual(hanja_1['radical'], '木')
        self.assertEqual(hanja_1['stroke_count'], 4)
        self.assertEqual(len(hanja_1['readings']), 2)

        self.assertEqual(hanja_1['readings'][0], '나무 목')
        self.assertEqual(hanja_1['readings'][1], '모과 모')

        hanja_2 = orig_info['hanja_info'][1]
        self.assertEqual(hanja_2['hanja'], '曜')
        self.assertEqual(hanja_2['radical'], '日')
        self.assertEqual(hanja_2['stroke_count'], 18)
        self.assertEqual(len(hanja_2['readings']), 1)

        self.assertEqual(hanja_2['readings'][0], '빛날 요')

        hanja_3 = orig_info['hanja_info'][2]
        self.assertEqual(hanja_3['hanja'], '日')
        self.assertEqual(hanja_3['radical'], '日')
        self.assertEqual(hanja_3['stroke_count'], 4)
        self.assertEqual(len(hanja_3['readings']), 1)

        self.assertEqual(hanja_3['readings'][0], '날 일')

    def test_scraper_view_multimedia(self):
        """Basic view query with multimedia scraper returns proper results"""
        response = krdict.view(
            target_code=14997,
            raise_api_errors=True,
            guarantee_keys=True,
            options={
                'use_scraper': True,
                'fetch_page_data': False,
                'fetch_multimedia': True
            })

        self.assertIn('data', response)
        self.assertEqual(len(response['data']['results']), 1)
        result = response['data']['results'][0]

        self.assertIn('word_info', result)
        self.assertIn('definition_info', result['word_info'])
        self.assertIn('multimedia_info', result['word_info']['definition_info'][0])
        media_info = result['word_info']['definition_info'][0]['multimedia_info']

        for info in media_info:
            self.assertIn('media_urls', info)
            self.assertEqual(len(info['media_urls']), 1)

    def test_scraper_word(self):
        """Basic search query with scraper returns proper results"""
        response = krdict.search(
            query='나무',
            guarantee_keys=True,
            raise_api_errors=True,
            search_type='word',
            options={'use_scraper': True})

        self.assertIn('data', response)
        data = response['data']

        self.assertIn('search_url', data)
        self.assertEqual(len(data['results']), 10)

        for result in data['results']:
            self.assertIn('pronunciation_urls', result)
            self.assertEqual(len(result['pronunciation_urls']), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
