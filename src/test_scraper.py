"""
Handles testing the krdict package.
"""

import unittest
import krdict

class KRDictScraperTest(unittest.TestCase):
    """Contains test cases for the scraper module."""

    def test_scraper_advanced(self):
        """Advanced search query with scraper returns proper results"""
        response = krdict.scraper.advanced_search(
            query='나무',
            search_method=krdict.SearchMethod.INCLUDE,
            sort=krdict.SortMethod.POPULAR
        )

        self.assertIn('data', response)
        data = response.data

        self.assertIn('url', data)
        self.assertEqual(len(data.results), 10)

        for result in data.results:
            self.assertIn('pronunciation_urls', result)
            self.assertEqual(len(result.pronunciation_urls), 1)

    def test_scraper_category(self):
        """Advanced search query using categories with scraper returns proper results"""
        response = krdict.scraper.advanced_search(
            query='가',
            search_method=krdict.SearchMethod.INCLUDE,
            subject_category=krdict.SubjectCategory.ELEMENTARY_DESCRIBING_LOCATION
        )

        self.assertIn('data', response)
        data = response.data

        self.assertEqual(len(data.results), 2)

        self.assertEqual(data.results[0].word, '가리키다')
        self.assertIn('pronunciation_urls', data.results[0])
        self.assertEqual(data.results[0].pronunciation_urls[0],
            ('https://dicmedia.korean.go.kr/multimedia/multimedia_files/'
            'convert/20170223/442961/SND000021293.mp3'))

        self.assertEqual(data.results[1].word, '가운데')
        self.assertIn('pronunciation_urls', data.results[1])
        self.assertEqual(data.results[1].pronunciation_urls[0],
            ('https://dicmedia.korean.go.kr/multimedia/multimedia_files/'
            'convert/20160913/20000/17000/307982/SND000317336.mp3'))

    def test_scraper_fetch_meaning_category_words(self):
        """Fetching meaning category words with scraper returns proper results"""
        response = krdict.scraper.fetch_meaning_category_words(category=3, per_page=15)

        self.assertIn('data', response)
        data = response.data

        self.assertIn('url', data)
        self.assertIn('translation_urls', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)
        self.assertIn('total_results', data)
        self.assertIn('results', data)

        self.assertEqual(data.url,
            ('https://krdict.korean.go.kr/dicSearchDetail/'
            'searchDetailSenseCategoryResult?searchFlag=Y&currentPage=1&blockCount=15&sort=W'
            '&lgCategoryCode=1&miCategoryCode=1003'))
        self.assertEqual(len(data.translation_urls), 0)
        self.assertEqual(data.page, 1)
        self.assertEqual(data.per_page, 15)
        self.assertEqual(len(data.results), 15)
        self.assertEqual(data.total_results, 113)

    def test_scraper_fetch_meaning_category_words_translation(self):
        """Fetching meaning category words with translation with scraper returns proper results"""
        response = krdict.scraper.fetch_meaning_category_words(
            category=3,
            per_page=15,
            translation_language=krdict.scraper.ScraperTranslationLanguage.ENGLISH
        )

        self.assertIn('data', response)
        data = response.data

        self.assertIn('url', data)
        self.assertIn('translation_urls', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)
        self.assertIn('total_results', data)
        self.assertIn('results', data)

        self.assertEqual(data.url,
            ('https://krdict.korean.go.kr/dicSearchDetail/'
            'searchDetailSenseCategoryResult?searchFlag=Y&currentPage=1&blockCount=15&sort=W'
            '&lgCategoryCode=1&miCategoryCode=1003'))
        self.assertEqual(data.translation_urls[0].url,
            ('https://krdict.korean.go.kr/eng/dicSearchDetail/'
            'searchDetailSenseCategoryResult?nation=eng&nationCode=6&searchFlag=Y'
            '&currentPage=1&blockCount=15&sort=W&lgCategoryCode=1&miCategoryCode=1003'))
        self.assertEqual(data.page, 1)
        self.assertEqual(data.per_page, 15)
        self.assertEqual(len(data.results), 15)
        self.assertEqual(data.total_results, 113)

        for result in data.results:
            self.assertIn('definitions', result)
            for dfn in result.definitions:
                self.assertIn('definition', dfn)
                self.assertIn('order', dfn)
                self.assertIn('translations', dfn)

                translation = dfn.translations[0]
                self.assertIn('definition', translation)
                self.assertIn('word', translation)
                self.assertIn('language', translation)
                self.assertEqual(translation.language, '영어')

    def test_scraper_fetch_subject_category_words(self):
        """Fetching meaning category words with scraper returns proper results"""
        response = krdict.scraper.fetch_subject_category_words(category=1, per_page=15)

        self.assertIn('data', response)
        data = response.data

        self.assertIn('url', data)
        self.assertIn('translation_urls', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)
        self.assertIn('total_results', data)
        self.assertIn('results', data)

        self.assertEqual(data.url,
            ('https://krdict.korean.go.kr/dicSearchDetail/searchDetailActCategoryResult?'
            'searchFlag=Y&currentPage=1&blockCount=15&sort=W&actCategory=20001'))
        self.assertEqual(len(data.translation_urls), 0)
        self.assertEqual(data.page, 1)
        self.assertEqual(data.per_page, 15)
        self.assertEqual(len(data.results), 15)
        self.assertEqual(data.total_results, 17)

    def test_scraper_fetch_subject_category_words_translation(self):
        """Fetching meaning category words with translation with scraper returns proper results"""
        response = krdict.scraper.fetch_subject_category_words(
            category=1,
            per_page=15,
            translation_language=krdict.scraper.ScraperTranslationLanguage.ENGLISH
        )

        self.assertIn('data', response)
        data = response.data

        self.assertIn('url', data)
        self.assertIn('translation_urls', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)
        self.assertIn('total_results', data)
        self.assertIn('results', data)

        self.assertEqual(data.url,
            ('https://krdict.korean.go.kr/dicSearchDetail/searchDetailActCategoryResult?'
            'searchFlag=Y&currentPage=1&blockCount=15&sort=W&actCategory=20001'))
        self.assertEqual(data.translation_urls[0].url,
            ('https://krdict.korean.go.kr/eng/dicSearchDetail/searchDetailActCategoryResult?'
            'nation=eng&nationCode=6&searchFlag=Y'
            '&currentPage=1&blockCount=15&sort=W&actCategory=20001'))
        self.assertEqual(data.page, 1)
        self.assertEqual(data.per_page, 15)
        self.assertEqual(len(data.results), 15)
        self.assertEqual(data.total_results, 17)

        for result in data.results:
            self.assertIn('definitions', result)
            for dfn in result.definitions:
                self.assertIn('definition', dfn)
                self.assertIn('order', dfn)
                self.assertIn('translations', dfn)

                translation = dfn.translations[0]
                self.assertIn('definition', translation)
                self.assertIn('word', translation)
                self.assertIn('language', translation)
                self.assertEqual(translation.language, '영어')

    def test_scraper_fetch_word_of_the_day(self):
        """Fetching word of the day with scraper returns proper results"""
        response = krdict.scraper.fetch_word_of_the_day()

        self.assertIn('data', response)
        data = response.data

        self.assertIn('target_code', data)
        self.assertIn('word', data)
        self.assertIn('definition', data)
        self.assertIn('url', data)
        self.assertIn('homograph_num', data)

    def test_scraper_fetch_word_of_the_day_translation(self):
        """Fetching word of the day with translation with scraper returns proper results"""
        response = krdict.scraper.fetch_word_of_the_day(
            translation_language=krdict.scraper.ScraperTranslationLanguage.ENGLISH
        )

        self.assertIn('data', response)
        data = response.data

        self.assertIn('target_code', data)
        self.assertIn('word', data)
        self.assertIn('definition', data)
        self.assertIn('url', data)
        self.assertIn('homograph_num', data)

        self.assertIn('translations', data)
        self.assertEqual(len(data.translations), 1)
        self.assertIn('definition', data.translations[0])
        self.assertIn('language', data.translations[0])

        self.assertEqual(data.translations[0].language, '영어')

    def test_scraper_view(self):
        """Basic view query with scraper returns proper results"""
        response = krdict.scraper.view(target_code=55874)

        self.assertIn('data', response)
        self.assertEqual(len(response.data.results), 1)
        result = response.data.results[0]

        self.assertIn('word_info', result)
        self.assertIn('pronunciation_info', result.word_info)
        self.assertIn('original_language_info', result.word_info)

        self.assertEqual(len(result.word_info.pronunciation_info), 1)
        self.assertIn('url', result.word_info.pronunciation_info[0])

        self.assertEqual(len(result.word_info.original_language_info), 1)
        orig_info = result.word_info.original_language_info[0]

        self.assertIn('pronunciation_info', result.word_info)
        self.assertEqual(len(result.word_info.pronunciation_info), 1)
        self.assertIn('url', result.word_info.pronunciation_info[0])

        self.assertEqual(orig_info.original_language, '木曜日')
        self.assertEqual(orig_info.language_type, '한자')

        self.assertIn('hanja_info', orig_info)
        self.assertEqual(len(orig_info.hanja_info), 3)

        hanja_1 = orig_info.hanja_info[0]
        self.assertEqual(hanja_1.hanja, '木')
        self.assertEqual(hanja_1.radical, '木')
        self.assertEqual(hanja_1.stroke_count, 4)
        self.assertEqual(len(hanja_1.readings), 2)

        self.assertEqual(hanja_1.readings[0], '나무 목')
        self.assertEqual(hanja_1.readings[1], '모과 모')

        hanja_2 = orig_info.hanja_info[1]
        self.assertEqual(hanja_2.hanja, '曜')
        self.assertEqual(hanja_2.radical, '日')
        self.assertEqual(hanja_2.stroke_count, 18)
        self.assertEqual(len(hanja_2.readings), 1)

        self.assertEqual(hanja_2.readings[0], '빛날 요')

        hanja_3 = orig_info.hanja_info[2]
        self.assertEqual(hanja_3.hanja, '日')
        self.assertEqual(hanja_3.radical, '日')
        self.assertEqual(hanja_3.stroke_count, 4)
        self.assertEqual(len(hanja_3.readings), 1)

        self.assertEqual(hanja_3.readings[0], '날 일')

    def test_scraper_view_multimedia(self):
        """Basic view query with multimedia scraper returns proper results"""
        response = krdict.scraper.view(target_code=14997, fetch_multimedia=True)

        self.assertIn('data', response)
        self.assertEqual(len(response.data.results), 1)
        result = response.data.results[0]

        self.assertIn('word_info', result)
        self.assertIn('definition_info', result.word_info)
        self.assertIn('multimedia_info', result.word_info.definition_info[0])
        media_info = result.word_info.definition_info[0].multimedia_info

        for info in media_info:
            self.assertIn('content_urls', info)
            self.assertEqual(len(info.content_urls), 1)

    def test_scraper_word(self):
        """Basic search query with scraper returns proper results"""
        response = krdict.scraper.search(
            query='나무',
            search_type='word'
        )

        self.assertIn('data', response)
        data = response.data

        self.assertIn('url', data)
        self.assertEqual(data.url,
            ('https://krdict.korean.go.kr/dicSearch/search?'
            'mainSearchWord=나무&currentPage=1&blockCount=10&sort=W&searchType=W'))
        self.assertEqual(len(data.results), 10)

        for result in data.results:
            self.assertIn('pronunciation_urls', result)
            self.assertEqual(len(result.pronunciation_urls), 1)


if __name__ == "__main__":
    unittest.main()
