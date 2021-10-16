A summary of expected parameter types for various [functions](functions.md).

---

## Classification

The classification of a dictionary entry.
```bash
'all' | 'word' | 'phrase' | 'expression'
```

## MultimediaType

A type of multimedia file.
```bash
'all' | 'photo' | 'illustration' | 'video' | 'animation' | 'sound' | 'none'
```

## OptionsDict

Additional options to apply to a query. All of the keys are not required.
```python
{
    'fetch_multimedia': bool, # default: False
    'fetch_page_data': bool, # default: True
    'raise_scraper_errors': bool, # default: False
    'use_scraper': bool # default: False
}
```

- `'fetch_multimedia'`: Controls whether multimedia is scraped during view queries. No effect unless the `'use_scraper'` option is `True`.
- `'fetch_page_data'`: Controls whether pronunciation URLS and extended language information are scraped. No effect unless the `'use_scraper'` option is `True`.
- `'raise_scraper_errors'`: Controls whether errors that occur during scraping are raised. No effect unless the `'use_scraper'` option is `True`.
- `'use_scraper'`: Controls whether the scraper should be used to fetch more information.

See also: [`set_default`](functions.md#set_default).

## OriginType

The classification of a dictionary entry's origin.
```bash
'all' | 'native' | 'hanja' | 'loanword' | 'hybrid'
```

## PartOfSpeech

A Korean part of speech.
```bash
| 'all'
| 'noun'
| 'pronoun'
| 'numeral'
| 'particle'
| 'verb'
| 'adjective'
| 'determiner'
| 'adverb'
| 'interjection'
| 'affix'
| 'bound noun'
| 'auxiliary verb'
| 'auxiliary adjective'
| 'ending'
| 'none'
```

## ScraperTranslationLanguage

A language to include translations for during a scraper fetch.
```bash
| 'chinese'
| 'english'
| 'japanese'
| 'french'
| 'spanish'
| 'arabic'
| 'mongolian'
| 'vietnamese'
| 'thai'
| 'indonesian'
| 'russian'
```

## SearchMethod

The method to use when searching.

- `'exact'`: Returns entries that are an exact match of the query.
- `'include'`: Returns entries that include the query.
- `'start'`: Returns entries that start with the query.
- `'end'`: Returns entries that end with the query.

```bash
'exact' | 'include' | 'start' | 'end'
```

## SearchTarget

The target of the search query; what to search by.
```bash
| 'headword'
| 'definition'
| 'example'
| 'original_language'
| 'pronunciation'
| 'application'
| 'application_shorthand'
| 'idiom'
| 'proverb'
| 'reference_info'
```

## SearchType

The type of search to perform.
```bash
'word' | 'idiom_proverb' | 'definition' | 'example'
```

## SortMethod

A sorting method to use for search results.
```bash
'alphabetical' | 'popular'
```

## TargetLanguage

A target original language to search by.
```bash
| 'all'
| 'native_word'
| 'sino-korean'
| 'unknown'
| 'english'
| 'greek'
| 'dutch'
| 'norwegian'
| 'german'
| 'latin'
| 'russian'
| 'romanian'
| 'maori'
| 'malay'
| 'mongolian'
| 'basque'
| 'burmese'
| 'vietnamese'
| 'bulgarian'
| 'sanskrit'
| 'serbo-croatian'
| 'swahili'
| 'swedish'
| 'arabic'
| 'irish'
| 'spanish'
| 'uzbek'
| 'ukrainian'
| 'italian'
| 'indonesian'
| 'japanese'
| 'chinese'
| 'czech'
| 'cambodian'
| 'quechua'
| 'tagalog'
| 'thai'
| 'turkish'
| 'tibetan'
| 'persian'
| 'portuguese'
| 'polish'
| 'french'
| 'provencal'
| 'finnish'
| 'hungarian'
| 'hebrew'
| 'hindi'
| 'other'
| 'danish'
```

## TranslationLanguage

A language to include translations for.
```bash
| 'all'
| 'english'
| 'japanese'
| 'french'
| 'spanish'
| 'arabic'
| 'mongolian'
| 'vietnamese'
| 'thai'
| 'indonesian'
| 'russian'
```

## VocabularyGrade

The vocabulary level of a dictionary entry.
```bash
'all' | 'beginner' | 'intermediate' | 'advanced'
```

## MeaningCategory

A meaning category which a dictionary entry may belong to.
```bash
| '전체'
| '인간 > 전체'
| '인간 > 사람의 종류'
| '인간 > 신체 부위'
| '인간 > 체력 상태'
| '인간 > 생리 현상'
| '인간 > 감각'
| '인간 > 감정'
| '인간 > 성격'
| '인간 > 태도'
| '인간 > 용모'
| '인간 > 능력'
| '인간 > 신체 변화'
| '인간 > 신체 행위'
| '인간 > 신체에 가하는 행위'
| '인간 > 인지 행위'
| '인간 > 소리'
| '인간 > 신체 내부 구성'
| '삶 > 전체'
| '삶 > 삶의 상태'
| '삶 > 삶의 행위'
| '삶 > 일상 행위'
| '삶 > 친족 관계'
| '삶 > 가족 행사'
| '삶 > 여가 도구'
| '삶 > 여가 시설'
| '삶 > 여가 활동'
| '삶 > 병과 증상'
| '삶 > 치료 행위'
| '삶 > 치료 시설'
| '삶 > 약품류'
| '식생활 > 전체'
| '식생활 > 음식'
| '식생활 > 채소'
| '식생활 > 곡류'
| '식생활 > 과일'
| '식생활 > 음료'
| '식생활 > 식재료'
| '식생활 > 조리 도구'
| '식생활 > 식생활 관련 장소'
| '식생활 > 맛'
| '식생활 > 식사 및 조리 행위'
| '의생활 > 전체'
| '의생활 > 옷 종류'
| '의생활 > 옷감'
| '의생활 > 옷의 부분'
| '의생활 > 모자, 신발, 장신구'
| '의생활 > 의생활 관련 장소'
| '의생활 > 의복 착용 상태'
| '의생활 > 의복 착용 행위'
| '의생활 > 미용 행위'
| '주생활 > 전체'
| '주생활 > 건물 종류'
| '주생활 > 주거 형태'
| '주생활 > 주거 지역'
| '주생활 > 생활 용품'
| '주생활 > 주택 구성'
| '주생활 > 주거 상태'
| '주생활 > 주거 행위'
| '주생활 > 가사 행위'
| '사회 생활 > 전체'
| '사회 생활 > 인간관계'
| '사회 생활 > 소통 수단'
| '사회 생활 > 교통 수단'
| '사회 생활 > 교통 이용 장소'
| '사회 생활 > 매체'
| '사회 생활 > 직장'
| '사회 생활 > 직위'
| '사회 생활 > 직업'
| '사회 생활 > 사회 행사'
| '사회 생활 > 사회 생활 상태'
| '사회 생활 > 사회 활동'
| '사회 생활 > 교통 이용 행위'
| '사회 생활 > 직장 생활'
| '사회 생활 > 언어 행위'
| '사회 생활 > 통신 행위'
| '사회 생활 > 말'
| '경제 생활 > 전체'
| '경제 생활 > 경제 행위 주체'
| '경제 생활 > 경제 행위 장소'
| '경제 생활 > 경제 수단'
| '경제 생활 > 경제 산물'
| '경제 생활 > 경제 상태'
| '경제 생활 > 경제 행위'
| '교육 > 전체'
| '교육 > 교수 학습 주체'
| '교육 > 전공과 교과목'
| '교육 > 교육 기관'
| '교육 > 학교 시설'
| '교육 > 학습 관련 사물'
| '교육 > 학문 용어'
| '교육 > 교수 학습 행위'
| '교육 > 학문 행위'
| '종교 > 전체'
| '종교 > 종교 유형'
| '종교 > 종교 활동 장소'
| '종교 > 종교인'
| '종교 > 종교어'
| '종교 > 신앙 대상'
| '종교 > 종교 활동 도구'
| '종교 > 종교 행위'
| '문화 > 전체'
| '문화 > 문화 활동 주체'
| '문화 > 음악'
| '문화 > 미술'
| '문화 > 문학'
| '문화 > 예술'
| '문화 > 대중 문화'
| '문화 > 전통 문화'
| '문화 > 문화 생활 장소'
| '문화 > 문화 활동'
| '정치와 행정 > 전체'
| '정치와 행정 > 공공 기관'
| '정치와 행정 > 사법 및 치안 주체'
| '정치와 행정 > 무기'
| '정치와 행정 > 정치 및 치안 상태'
| '정치와 행정 > 정치 및 행정 행위'
| '정치와 행정 > 사법 및 치안 행위'
| '정치와 행정 > 정치 및 행정 주체'
| '자연 > 전체'
| '자연 > 지형'
| '자연 > 지표면 사물'
| '자연 > 천체'
| '자연 > 자원'
| '자연 > 재해'
| '자연 > 기상 및 기후'
| '동식물 > 전체'
| '동식물 > 동물류'
| '동식물 > 곤충류'
| '동식물 > 식물류'
| '동식물 > 동물의 부분'
| '동식물 > 식물의 부분'
| '동식물 > 동식물 행위'
| '동식물 > 동물 소리'
| '개념 > 전체'
| '개념 > 모양'
| '개념 > 성질'
| '개념 > 속도'
| '개념 > 밝기'
| '개념 > 온도'
| '개념 > 색깔'
| '개념 > 수'
| '개념 > 세는 말'
| '개념 > 양'
| '개념 > 정도'
| '개념 > 순서'
| '개념 > 빈도'
| '개념 > 시간'
| '개념 > 위치 및 방향'
| '개념 > 지역'
| '개념 > 지시'
| '개념 > 접속'
| '개념 > 의문'
| '개념 > 인칭'
```

## SubjectCategory

A subject category (themes and situations) which a dictionary entry may belong to.
```bash
| '전체'
| '인사하기'
| '소개하기 (자기소개)'
| '소개하기 (가족소개)'
| '개인 정보 교환하기 (초급)'
| '위치 표현하기'
| '길찾기'
| '교통 이용하기 (초금)'
| '물건 사기 (초금)'
| '음식 주문하기'
| '요리 설명하기 (초금)'
| '시간 표현하기'
| '날짜 표현하기'
| '요일 표현하기'
| '날씨와 계절 (초금)'
| '하루 생활'
| '학교생활 (초금)'
| '한국 생활 (초금)'
| '약속하기'
| '전화하기'
| '감사하기'
| '사과하기'
| '여행 (초금)'
| '주말 및 휴가 (초금)'
| '취미 (초금)'
| '가족 행사 (초금)'
| '건강 (초금)'
| '병원 이용하기'
| '약국 이용하기 (초금)'
| '공공 기관 이용하기 (도서관)'
| '공공 기관 이용하기 (우체국)'
| '공공 기관 이용하기 (출입국 관리 사무소)'
| '초대와 방문 (초금)'
| '집 구하기 (초금)'
| '집안일 (초금)'
| '감정, 기분 표현하기 (초금)'
| '성격 표현하기 (초금)'
| '복장 표현하기 (초금)'
| '외모 표현하기 (초금)'
| '영화 보기'
| '개인 정보 교환하기 (중급)'
| '교통 이용하기 (중급)'
| '지리 정보 (중급)'
| '물건 사기 (중급)'
| '음식 설명하기'
| '요리 설명하기 (중급)'
| '날씨와 계절 (중급)'
| '학교생활 (중급)'
| '한국 생활 (중급)'
| '직업과 진로 (중급)'
| '직장 생활 (중급)'
| '여행 (중급)'
| '주말 및 휴가 (중급)'
| '취미 (중급)'
| '가족 행사 (중급)'
| '가족 행사 (명절)'
| '건강 (중급)'
| '공공기관 이용하기'
| '초대와 방문 (중급)'
| '집 구하기 (중급)'
| '집안일 (중급)'
| '감정, 기분 표현하기 (중급)'
| '성격 표현하기 (중급)'
| '복장 표현하기 (중급)'
| '외모 표현하기 (중급)'
| '공연과 감상'
| '대중 매체'
| '컴퓨터와 인터넷 (중급)'
| '사건, 사고, 재해 기술하기'
| '환경 문제 (중급)'
| '문화 비교하기'
| '인간관계 (중급)'
| '한국의 문학'
| '문제 해결하기 (분실 및 고장)'
| '실수담 말하기'
| '연애와 결혼'
| '언어 (중급)'
| '지리 정보 (고급)'
| '경제∙경영'
| '경제-경영'
| '식문화'
| '기후'
| '교육'
| '직업과 진로 (고급)'
| '직장 생활 (고급)'
| '여가 생활'
| '보건과 의료'
| '주거 생활'
| '심리'
| '외양'
| '대중문화'
| '컴퓨터와 인터넷 (고급)'
| '사회 문제'
| '환경 문제 (고급)'
| '사회 제도'
| '문화 차이'
| '인간관계 (고급)'
| '예술'
| '건축'
| '과학과 기술'
| '법'
| '스포츠'
| '언론'
| '언어 (고급)'
| '역사'
| '정치'
| '종교'
| '철학∙윤리'
| '철학-윤리'

```
