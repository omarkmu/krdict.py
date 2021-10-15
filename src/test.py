# type: ignore
"""
Handles testing the krdict module.
"""

import os
import unittest
import dotenv
import krdict

BASE_LINK_URL = 'https://krdict.korean.go.kr/dicSearch/SearchView'

dotenv.load_dotenv()
krdict.set_key(os.getenv('KRDICT_KEY'))

class TestKRDict(unittest.TestCase):
    """Contains KRDict test cases."""
    def test_basic_search(self):
        """Basic search query returns proper results"""
        response = krdict.search_words(query='나무', raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(len(data['results']), 10)
        self.assertEqual(data['num_results'], 10)
        self.assertEqual(data['total_results'], 53)
        self.assertEqual(data['start_index'], 1)

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
            link = f'{BASE_LINK_URL}?ParaWordNo={target_code}'

            self.assertEqual(result['word'], word)
            self.assertEqual(result['part_of_speech'], pos)
            self.assertEqual(result['homograph_num'], homograph_num)
            self.assertEqual(result['target_code'], target_code)
            self.assertEqual(result['link'], link)
            self.assertEqual(len(result['definitions']), meaning_len)

            for index in range(meaning_len):
                def_info = result['definitions'][index]

                self.assertIn('definition', def_info)
                self.assertIn('order', def_info)
                self.assertEqual(def_info['order'], index + 1)

    def test_start_index(self):
        """Setting start_index parameter returns proper start_index"""
        response = krdict.search_words(query='나무', start_index=20, raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['start_index'], 20)

    def test_num_results(self):
        """Setting num_results parameter returns correct number of results"""
        response = krdict.search_words(query='나무', num_results=15, raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['num_results'], 15)
        self.assertEqual(len(data['results']), 15)

    def test_sort(self):
        """Setting sort parameter to popular returns sorted results"""
        response = krdict.search_words(query='나무', sort='popular', raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['results'][0]['target_code'], 32750)
        self.assertEqual(data['results'][1]['target_code'], 38842)
        self.assertEqual(data['results'][2]['target_code'], 38847)

    def test_translation(self):
        """Setting translation_language parameter returns results with translations"""
        response = krdict.search_words(
            query='나무',
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

    def test_definition_search(self):
        """Definition search query returns proper results"""
        response = krdict.search_definitions(query='나무', raise_api_errors=True)

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
        response = krdict.search_examples(query='나무', raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['total_results'], 2281)

        for result in data['results']:
            self.assertIn('example', result)

    def test_idiom_proverb_search(self):
        """Idiom/Proverb search query returns proper results"""
        response = krdict.search_idioms_proverbs(query='나무', raise_api_errors=True)

        self.assertIn('data', response)
        data = response['data']

        self.assertEqual(data['total_results'], 13)

        for result in data['results']:
            self.assertIn('word', result)

    def test_search_method(self):
        """Advanced search method with various search methods returns proper results"""
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

    def test_api_error(self):
        """Invalid query string results in an API error"""
        response = krdict.search(query='')
        self.assertIn('error', response)
        self.assertIn('request_params', response)
        self.assertEqual(response['error']['error_code'], 100)
        self.assertEqual(response['error']['message'], 'Incorrect query request')

    def test_raise_api_errors(self):
        """Invalid query string with raise_api_errors=True raises"""
        with self.assertRaises(krdict.KRDictException) as ctx:
            krdict.search(query='', raise_api_errors=True)
        self.assertIsInstance(ctx.exception.request_params, dict)
        self.assertEqual(ctx.exception.error_code, 100)
        self.assertEqual(ctx.exception.message, 'Incorrect query request')


if __name__ == '__main__':
    unittest.main(verbosity=2)
