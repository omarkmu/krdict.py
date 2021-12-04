"""
Handles testing request logic.
"""

import unittest
import unittest.mock
import krdict


def _mock_request_get(*args, **kwargs): # pylint: disable=unused-argument
    return unittest.mock.Mock(('raise_for_status',))


class KRDictRequestTest(unittest.TestCase):
    """Contains test cases for request logic."""

    def setUp(self):
        krdict.set_key('TEST_KEY')
        self.addCleanup(krdict.set_key, None)

        request_patcher = unittest.mock.patch('requests.get', side_effect=_mock_request_get)
        self.addCleanup(request_patcher.stop)

        request_patcher.start()

    def test_key(self):
        """Provided API key is added to requests"""

        # an explicit provided key is used
        _, params, _ = krdict.request.send_request({'key': 'PROVIDED_KEY'})

        self.assertIn('key', params)
        self.assertEqual(params['key'], 'PROVIDED_KEY')

        # the key set with set_key is used
        _, params, _ = krdict.request.send_request({})

        self.assertIn('key', params)
        self.assertEqual(params['key'], 'TEST_KEY')

        # no key is supplied if the key is unset
        krdict.set_key(None)
        _, params, _ = krdict.request.send_request({})

        self.assertNotIn('key', params)

    def test_max_syllables(self):
        """Setting max_syllables parameter sets default min_syllables"""

        _, params, _ = krdict.request.send_request({'max_syllables': 5})

        self.assertIn('letter_e', params)
        self.assertIn('letter_s', params)

        self.assertEqual(params['letter_e'], '5')
        self.assertEqual(params['letter_s'], '1')

    def test_min_syllables(self):
        """Setting min_syllables parameter sets default max_syllables"""

        _, params, _ = krdict.request.send_request({'min_syllables': 10})

        self.assertIn('letter_s', params)
        self.assertIn('letter_e', params)

        self.assertEqual(params['letter_s'], '10')
        self.assertEqual(params['letter_e'], '0')

    def test_multiple_parameters(self):
        """Lists of parameters are properly transformed"""

        _, params, _ = krdict.request.send_request({
            'part_of_speech': (krdict.PartOfSpeech.NOUN, krdict.PartOfSpeech.VERB),
            'translation_language': (
                krdict.TranslationLanguage.ENGLISH,
                krdict.TranslationLanguage.SPANISH,
                krdict.TranslationLanguage.JAPANESE
            ),
            'vocabulary_grade': (
                krdict.VocabularyLevel.BEGINNER,
                krdict.VocabularyLevel.INTERMEDIATE
            )
        })

        self.assertIn('pos', params)
        self.assertIn('trans_lang', params)
        self.assertIn('level', params)

        self.assertEqual(params['pos'], '1,5')
        self.assertEqual(params['trans_lang'], '1,4,2')
        self.assertEqual(params['level'], 'level1,level2')

    def test_parameter_transformation(self):
        """Parameters to requests are properly transformed"""

        _, params, _ = krdict.request.send_request({
            'query': '나무',
            'page': 2,
            'per_page': 25,
            'sort': krdict.SortMethod.POPULAR,
            'search_type': krdict.SearchType.DEFINITION,
            'search_target': krdict.SearchTarget.DEFINITION,
            'target_language': krdict.TargetLanguage.GERMAN,
            'search_method': krdict.SearchMethod.INCLUDE,
            'classification': krdict.Classification.WORD,
            'origin_type': krdict.OriginType.LOANWORD,
            'vocabulary_grade': krdict.VocabularyLevel.ADVANCED,
            'part_of_speech': krdict.PartOfSpeech.NOUN,
            'multimedia_info': krdict.MultimediaType.VIDEO,
            'meaning_category': krdict.MeaningCategory.ANIMALS_AND_PLANTS_ALL,
            'subject_category': krdict.SubjectCategory.ADVANCED_ART
        })

        self.assertIn('q', params)
        self.assertIn('start', params)
        self.assertIn('num', params)
        self.assertIn('sort', params)
        self.assertIn('part', params)
        self.assertIn('target', params)
        self.assertIn('lang', params)
        self.assertIn('method', params)
        self.assertIn('type1', params)
        self.assertIn('type2', params)
        self.assertIn('level', params)
        self.assertIn('pos', params)
        self.assertIn('multimedia', params)
        self.assertIn('sense_cat', params)
        self.assertIn('subject_cat', params)

        self.assertEqual(params['q'], '나무')
        self.assertEqual(params['start'], '2')
        self.assertEqual(params['num'], '25')
        self.assertEqual(params['sort'], 'popular')
        self.assertEqual(params['part'], 'dfn')
        self.assertEqual(params['target'], '2')
        self.assertEqual(params['lang'], '8')
        self.assertEqual(params['method'], 'include')
        self.assertEqual(params['type1'], 'word')
        self.assertEqual(params['type2'], 'loanword')
        self.assertEqual(params['level'], 'level3')
        self.assertEqual(params['pos'], '1')
        self.assertEqual(params['multimedia'], '3')
        self.assertEqual(params['sense_cat'], '126')
        self.assertEqual(params['subject_cat'], '96')

    def test_translated_flag(self):
        """Setting a translation language sets the translated flag"""

        _, params, _ = krdict.request.send_request({
            'translation_language': krdict.TranslationLanguage.SPANISH
        })

        self.assertIn('trans_lang', params)
        self.assertIn('translated', params)

        self.assertEqual(params['trans_lang'], '4')
        self.assertEqual(params['translated'], 'y')

    def test_view(self):
        """Parameters for view endpoint are properly transformed"""

        # target code query
        _, params, search_type = krdict.request.send_request({'target_code': 32750}, False, 'view')

        self.assertEqual(search_type, 'view')

        self.assertIn('q', params)
        self.assertIn('method', params)

        self.assertEqual(params['q'], '32750')
        self.assertEqual(params['method'], 'target_code')

        # default homograph number
        _, params, search_type = krdict.request.send_request({'query': '나무'}, False, 'view')

        self.assertEqual(search_type, 'view')

        self.assertIn('q', params)
        self.assertEqual(params['q'], '나무0')

        # provided homograph number
        _, params, search_type = krdict.request.send_request({
            'query': '나무',
            'homograph_num': 1
        }, False, 'view')

        self.assertEqual(search_type, 'view')

        self.assertIn('q', params)
        self.assertEqual(params['q'], '나무1')


if __name__ == "__main__":
    unittest.main()
