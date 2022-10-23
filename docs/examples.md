Below are some examples of potential uses of the library.  
All examples assume the `KRDICT_KEY` environment variable is set and
the following setup code has run:

```python
import os
import json
import krdict

krdict.set_key(os.getenv('KRDICT_KEY'))

# displays a limited amount of information
# returned from search and view responses.
def _display_results(response): ...
```

The definition of `_display_results` is omitted for brevity; for the full example file, see the
[source](https://github.com/omarkmu/krdict.py/blob/main/src/examples.py).

---

## 1. Pagination

Collects results from multiple queries for the word 나무
using the [`search`](main.md#search) function.

!!! note
    The maximum value for `per_page` is 100, so the below results
    can also be retrieved without pagination by setting
    `per_page` to 53 or higher.

```python
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
```
```md
Collected 20 results from page 1. Querying next page.
Collected 20 results from page 2. Querying next page.
Collected 13 results from page 3. All results collected.
53 results collected. Total results: 53.
```
---
## 2. Search By Definition

Performs a search for definitions containing the word 나무
using the [`search`](main.md#search) function.

```python
response = krdict.search(
    query='나무',
    # if you're using type checking,
    # setting the search_type parameter in a call with
    # keyword arguments will narrow the type of the search result.
    # when calling with an unpacked dictionary (**{...}),
    # the more specific type cannot be inferred.
    search_type=krdict.SearchType.DEFINITION,
    translation_language=krdict.TranslationLanguage.ENGLISH,
    raise_api_errors=True
)

_display_results(response)
```
```md
Total Results: 493
1. 가랑잎: 나무에서 떨어진 마른 잎.
   fallen leaf; dead leaf: A dry leaf fallen from a tree.
2. 가로수: 길을 따라 줄지어 심은 나무.
   roadside trees; street trees: Trees planted alongside the streets.
3. 가면: 얼굴을 감추거나 다르게 꾸미기 위하여 종이, 나무, 흙 등으로 만들어 얼굴에 쓰는 물건.
   mask: A thing that one wears over one's face, made with paper, wood, clay, etc., to conceal or adorn oneself.
4. 가시: 살에 박힌 나무의 가늘고 뾰족한 부분.
   thorn; prickle: The thin, pointed end, usually of the stem of a plant such as a rose, that is stuck in one's skin.
5. 가시덤불: 어수선하게 엉클어진 가시로 이루어진 나무나 풀.
   thornbush; bramble: A tree or bushes entwined with thorns.
6. 가지: 나무나 풀의 큰 줄기에서 갈라져 나간 작은 줄기.
   branch; sprig; bough; twig: A small twig broken off from a branch of a tree or blade of grass.
7. 갈잎: 떡갈나무의 잎.
   oak leaves: Leaves of an oak tree.
8. 갈잎: 잎이 넓은 나무의 마른 잎.
   dead leaves: Dry leaves of a broad-leaved tree.
9. 갈퀴: 철사나 대나무 조각을 엮어서 만든, 낙엽이나 곡물 등을 긁어모으는 데 사용하는 부챗살 모양의 기구.
   rake: An implement, looking like the ribs of a fan, which is made by assembling iron wires or bamboo strips and used to collect fallen leaves or grains in a garden or farmland.
10. 감나무: 감이 열리는 나무.
   persimmon tree: A tree bearing persimmons.
```
---
## 3. Search By Examples

Performs a search for examples containing the word 나무
using the [`search`](main.md#search) function.

```python
response = krdict.search(
    query='나무',
    search_type=krdict.SearchType.EXAMPLE,
    raise_api_errors=True
)

for result in response.data.results:
    print(f'• {result.example} (Word: {result.word})')
```
```md
• 나무가 지나치게 단단하면 변형이 어려워 가공성이 떨어진다. (Word: 가공성)
• 집 앞 공장에서는 나무를 가공하여 여러 가지 가구를 만든다. (Word: 가공하다)
• 책장이 나무로 되어 있네요? (Word: 가구재)
• 나무를 가꾸다. (Word: 가꾸다)
• 나무 표면이 아직도 거치니까 가는 사포로 좀 더 문질러야 되겠어. (Word: 가늘다)
• 버드나무는 수많은 푸른 실을 늘여 놓은 것 같이 가닥가닥이 푸르렀다. (Word: 가닥가닥)
• 나무에 가려지다. (Word: 가려지다)
• 나는 개울을 건너기 위해서 통나무를 가로놓았다. (Word: 가로놓다)
• 나무가 가로놓이다. (Word: 가로놓이다)
• 뒷마당에 설치된 높은 가로대에 밧줄과 나무판을 묶어서 그네를 만들었다. (Word: 가로대)
```
---
## 4. Search By Idioms/Proverbs

Performs a search for idioms and proverbs containing the word 나무
using the [`search`](main.md#search) function.

```python
response = krdict.search(
    query='나무',
    search_type=krdict.SearchType.IDIOM_PROVERB,
    translation_language=krdict.TranslationLanguage.ENGLISH,
    raise_api_errors=True
)

_display_results(response)
```
```md
Total Results: 13
1. 겨 묻은 개가 똥 묻은 개를 나무란다[흉본다]: 결점이 있기는 마찬가지인데 조금 덜한 사람이 더한 사람을 흉보는 경우를 비꼬아 이르는 말.
   A dog with husks of grain rebukes[speaks ill of] a dog with dung: A sarcastic expression about a person who has small faults and speaks ill of someone with greater faults while both have faults.
2. 열 번 찍어 아니 넘어가는 나무 없다: 아무리 굳은 마음을 가지고 있어도 여러 번 뜻을 바꾸도록 말하면 마음이 변한다.
   No tree will stand firm if chopped at ten times; Little strokes fell great oaks: People can change their mind however determined they may be if they are told to change it several times.
3. 열 번 찍어 안 넘어가는 나무 없다: 어떤 일이든 꾸준히 노력하면 이루지 못할 것이 없다.
   no tree will stand firm if chopped at ten times; little strokes fell great oaks: People can achieve anything if they keep making efforts.
4. 잘 자랄 나무는 떡잎부터 안다[알아본다]: 잘될 사람은 어렸을 때부터 그런 가능성이 보인다.
   A tree that will grow well can be known[recognized] even as a seed leaf; Sandalwood is fragrant even in seed leaf form; As the twig is bent, so grows the tree: A promising person stands out as a young child.
5. 가지 많은 나무에 바람 잘 날이 없다: 자식이 많은 부모에게는 걱정이 항상 많다.
   Trees with a lot of branches are more likely to be shaken by wind; A mother with a large brood never has a peaceful day: Parents with a lot of children tend to be worry-ridden.
6. 나무만 보고 숲을 보지 못한다: 어떤 일의 부분만 보고 전체를 보지 못한다.
   see only the trees and be unable to see the forest; not see the wood for the trees: To look at a part of something, not the whole of it.
7. 될 성부른 나무는 떡잎부터 알아본다: 크게 될 사람은 어릴 때부터 남다르다.
   a healthy and large tree can be recognized even as a seed leaf; Sandalwood is fragrant even in seed leaf; As the twig is bent, so grows the tree: A promising person stands out as a young child.
8. 똥 묻은 개가 겨 묻은 개 나무란다: 자기는 더 큰 잘못이나 결점이 있으면서 도리어 남의 작은 잘못을 흉본다.
   A dog with dung rebukes a dog with husks of grain: For one with greater faults or defects to speak ill of someone with smaller faults.
9. 못 오를 나무는 쳐다보지도 마라: 불가능한 일은 빨리 단념하라.
   Don’t even look at the tree that one cannot climb: It is advisable to give up something impossible.
10. 숯이 검정 나무란다: 자기 잘못은 생각하지 않고 남의 잘못이나 실수만 집어낸다.
   Charcoal rebukes blackness; The pot calls the kettle black: To criticize others' faults or mistakes without considering one's own.
```
---
## 5. Search Beginner Words With Multimedia

Retrieves and displays information about the first ten results
which are beginner grade words and contain any kind of multimedia
using the [`advanced_search`](main.md#advanced_search) function.

```python
response = krdict.advanced_search(
    # the API lacks a supported way to search without a query,
    # but because most definitions contain a period, it's possible to
    # achieve near-perfect results using the query '.' and the 'definition'
    # search target. in this example, all matches are returned.
    # to perform an advanced search with no query in a more precise way, use the scraper.
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
```
```md
Total Results: 295
1. 가위: 종이나 천, 머리카락 등을 자르는 도구.
   scissors: A tool for cutting paper, fabric, hair, etc.
2. 간장 (간醬): 음식의 간을 맞추는 데 쓰는, 짠맛이 나는 검은색 액체.
   soy sauce: Salty, black liquid used to flavor food.
3. 간호사 (看護師): 병원에서 의사를 도와 환자를 돌보는 것이 직업인 사람.
   nurse: A person whose job it is to assist doctors in taking care of patients at hospitals.
4. 갈비: 음식의 재료로 쓰이는 소, 돼지, 닭 등의 가슴뼈와 거기에 붙은 살. 또는 그것으로 만든 음식.
   ribs: Breastbones of cows, pigs, chickens, etc., and the flesh attached to these bones, used as an ingredient for food; or food made from these bones and their flesh.
5. 갈비탕 (갈비湯): 소의 갈비를 잘라 넣고 오랫동안 끓인 국.
   galbitang; short rib soup: Beef rib soup, made by boiling short beef ribs for long hours.
6. 감: 둥글거나 둥글넓적하며 익기 전에는 떫지만 익으면 단맛이 나는 주황색 과일.
   persimmon: An orange-colored, round or roundish flat fruit, which is astringent when unripe but sweet when ripe.
7. 감자: 껍질은 연한 갈색이며 속은 연한 노란색인, 땅속에서 자라는 둥근 덩이 모양의 줄기.
   potato: A ball-shaped stem growing underground with pale yellow flesh and light brown skin.
8. 개: 냄새를 잘 맡고 귀가 매우 밝으며 영리하고 사람을 잘 따라 사냥이나 애완 등의 목적으로 기르는 동물.
   dog: An animal raised as a pet or hunting companion, because it has a good sense of hearing and smell, is intelligent, and makes a good companion to humans.
9. 거실 (居室): 서양식 집에서, 가족이 모여서 생활하거나 손님을 맞는 중심 공간.
   living room: The central room in a western house, where family members spend time together or talk with visitors.
10. 거울: 물체의 모양을 비추어 보는 얇고 평평한 물건.
   mirror: A thin, flat object reflecting the appearance of an object or person.
```
---
## 6. Search Words Containing Hanja (한자)

Retrieves and displays information about the first ten results which contain the hanja 機 (기)
using the [`advanced_search`](main.md#advanced_search) function.

```python
response = krdict.advanced_search(
    query='機',
    search_type=krdict.SearchType.WORD,
    search_target=krdict.SearchTarget.ORIGINAL_LANGUAGE,
    search_method=krdict.SearchMethod.INCLUDE,
    translation_language=krdict.TranslationLanguage.ENGLISH,
    raise_api_errors=True
)

_display_results(response)
```
```md
Total Results: 170
1. 건조기 (乾燥機/乾燥器): 열을 가하거나 뜨거운 바람을 보내거나 물기를 흡수하는 약을 써서 물체에 있는 물기를 말리는 기계.
   drier; drying machine: A machine which dries something by using heat, hot wind, dehydrating agents, etc.
2. 검사기 (檢査機): 검사를 하는 데 쓰이는 기계.
   testing machine: Machinery used to conduct testing.
3. 게임기 (game機): 게임을 할 수 있도록 만든 전자 기계.
   game console; portable video game: An electronic machine made to play video games on.
4. 경비행기 (輕飛行機): 두 명에서 여덟 명 정도의 사람이 탈 수 있는 작은 비행기.
   light aircraft; light airplane: A small airplane which accommodates two to eight passengers.
5. 경운기 (耕耘機): 논이나 밭의 흙을 파서 뒤집어 엎는 기계.
   cultivator: The machine that is used to dig and turn over the soil of fields or paddies.
6. 계기 (契機): 어떤 일이 일어나거나 결정되도록 하는 원인이나 기회.
   opportunity; chance: A cause or opportunity for something to happen or be decided.
7. 계산기 (計算器/計算機): 계산을 빠르고 정확하게 하는 데 쓰는 기계.
   calculator: A machine used to calculate quickly and accurately.
8. 공공 기관 (公共機關): 법무부, 경찰청 등 공적인 행정 업무를 맡아 보는 기관.
   public institution: An institution that is in charge of public administrative work such as the Ministry of Justice, the National Police Agency, etc.
9. 공중 전화기 (公衆電話機): 여러 사람들이 돈을 내고 통화를 할 수 있도록 길거리나 일정한 장소에 설치한 전화 기계.
   payphone: A telephone installed on a street or in a certain place for many people to pay and make a phone call.
10. 교육 기관 (敎育機關): 교육에 관한 일을 하는 조직.
   educational institution: An organization that is related to education.
```
---
## 7. Perform a View Query

Displays the results of a view query for the word 단풍나무
using the [`view`](main.md#view) function.

!!! warning
    As shown in the result below, the API has a bug which duplicates
    한자 (hanja) with multiple 음훈 (readings). This means that, instead of
    the correct 丹楓나무, the original language is returned as 丹丹楓나무.
    This is corrected in view responses returned by
    the scraper.

```python
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

_display_results(response)
```
```text
단풍나무 「명사」 (丹丹楓나무) [단풍나무]
https://krdict.korean.go.kr/dicSearch/SearchView?ParaWordNo=42075
1. maple tree
   손바닥 모양의 잎이 가을에 빨갛게 물드는 나무.
   The tree whose palm-shaped leaves turn red in the fall.
   • 가을이 되자 교정의 단풍나무들이 빨갛게 물들었다.
   • 우리 고장에는 가을이 되면 단풍나무가 아름답게 물드는 산들이 많다.
   • 어머, 저것 좀 봐. 벌써 가을이 성큼 다가왔네.
   • 그러게. 단풍나무가 붉게 물들었구나.
   • 붉게 물든 단풍나무.
   • ...
   ► http://dicmedia.korean.go.kr:8899/front/search/searchResultView.do?file_no=97378 (사진)
```
---
## 8. Perform a Scraped View Query

Displays the results of a view query obtained by scraping for the word 단풍나무
using the scraper's [`view`](scraper.md#view) function.

The scraper returns results that contain pronunciation URLs,
multimedia URLs, and extended information about 한자 such as readings, stroke count, and radicals.

```python
response = krdict.scraper.view(
    # scraper method can only query with target code, not query strings
    target_code=42075,
    translation_language=krdict.TranslationLanguage.ENGLISH,
    fetch_multimedia=True
)

_display_results(response)
```
```text
단풍나무 「명사」 (丹楓나무) [단풍나무 (https://dicmedia.korean.go.kr/multimedia/multimedia_files/convert/20120209/23784/SND000012487.mp3)]
https://krdict.korean.go.kr/dicSearch/SearchView?ParaWordNo=42075
1. maple tree
   손바닥 모양의 잎이 가을에 빨갛게 물드는 나무.
   The tree whose palm-shaped leaves turn red in the fall.
   • 가을이 되자 교정의 단풍나무들이 빨갛게 물들었다.
   • 우리 고장에는 가을이 되면 단풍나무가 아름답게 물드는 산들이 많다.
   • 어머, 저것 좀 봐. 벌써 가을이 성큼 다가왔네.
   • 그러게. 단풍나무가 붉게 물들었구나.
   • 붉게 물든 단풍나무.
   • ...
   ► https://dicmedia.korean.go.kr/multimedia/multimedia_files/convert/20120106/3530//IMG000097378_700X466.jpg (사진)
```
---
## 9. Word of the Day

Fetches the word of the day with the
[`fetch_word_of_the_day`](scraper.md#fetch_word_of_the_day) function,
then fetches extended information about the word of the day
using the scraper's [`view`](scraper.md#view) function.

```python
wotd_response = krdict.scraper.fetch_word_of_the_day(
    translation_language=krdict.TranslationLanguage.ENGLISH
)

wotd_translation = ''
if wotd_response.data.translations:
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
_display_results(response)
```
```text
Word of the Day: 걱정거리 (cause of worry)
걱정이 되는 일.
https://krdict.korean.go.kr/eng/dicSearch/SearchView?ParaWordNo=21608&nation=eng&nationCode=6

Extended Info:
걱정거리 「명사」 [걱쩡꺼리 (https://dicmedia.korean.go.kr/multimedia/multimedia_files/convert/20120224/32989/SND000021692.mp3)]
https://krdict.korean.go.kr/dicSearch/SearchView?ParaWordNo=21608
1. cause of worry
   걱정이 되는 일.
   Something that causes concern.
   • 그는 걱정거리가 많아서 얼굴 표정이 좋지 않았다.
   • 민준이는 걱정거리를 해결하기 위해 친구들에게 조언을 구했다.
   • 올해는 비가 안 와서 가뭄이 들었다면서요.
   • 네. 그것이 요즘 농부들의 가장 큰 걱정거리라고 해요.
   • 걱정거리가 많다.
   • ...
```
---
## 10. Fetch Words in Semantic Category

Fetches words in the 인간 > 신체 부위 semantic category using the
[`fetch_semantic_category_words`](scraper.md#fetch_semantic_category_words) function.

```python
response = krdict.scraper.fetch_semantic_category_words(
    # equivalent: category=3,
    # equivalent: category='인간 > 신체 부위',
    # equivalent: category='human > body parts',
    category=krdict.SemanticCategory.HUMAN_BODY_PARTS,
    translation_language=krdict.TranslationLanguage.ENGLISH
)

_display_results(response)
```
```md
Total Results: 113
1. 가슴: 인간이나 동물의 목과 배 사이에 있는 몸의 앞 부분.
   chest: The front part of a human or animal's body, between the neck and the abdomen.
2. 고개: 목을 포함한 머리 부분.
   head: A word referring to one's head, including the neck.
3. 귀: 사람이나 동물의 머리 양옆에 있어 소리를 듣는 몸의 한 부분.
   ear: The part of a human or animal's body that hears sounds, located on both sides of the head.
4. 눈: 사람이나 동물의 얼굴에 있으며 빛의 자극을 받아 물체를 볼 수 있는 감각 기관.
   eye: The sensory organ on the face of a person or animal that can see an object when stimulated by the light.
5. 다리: 사람이나 동물의 몸통 아래에 붙어, 서고 걷고 뛰는 일을 하는 신체 부위.
   leg: A body part attached to the bottom of the torso of a person or animal that is used to walk or run.
6. 등: 사람이나 동물의 몸에서 가슴과 배의 반대쪽 부분.
   back: The part that is opposite the chest and belly on the body of a human or animal.
7. 머리: 사람이나 동물의 몸에서 얼굴과 머리털이 있는 부분을 모두 포함한 목 위의 부분.
   head: A part of the human or animal body above the neck that includes the face and hair.
8. 머리카락: 머리털 하나하나.
   hair: Each and every hair.
9. 목: 사람이나 동물의 머리와 몸통을 잇는 잘록한 부분.
   neck: The narrow part of the human or animal body that connects the head and the torso.
10. 몸: 사람이나 동물의 모습을 이루는 머리부터 발까지의 전체. 또는 그것의 상태.
   body: The entire length of the human or animal body from the head to the feet, or its state.
```
---
## 11. Fetch Words in Subject Category

Fetches words in the 인사하기 subject category
using the [`fetch_subject_category_words`](scraper.md#fetch_subject_category_words) function.

```python
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
```
```md
Total Results: 17
1. 반갑다: 보고 싶던 사람을 만나거나 원하는 일이 이루어져서 마음이 즐겁고 기쁘다.
   glad; joyful: Joyful and happy as one meets a person that one missed.
2. 성함 (姓銜): (높임말로) 사람의 이름.
   name: (honorific) One's name.
3. 씨 (氏): 그 사람을 높여 부르거나 이르는 말.
   Mr.; Ms.; Mrs.: A bound noun used to address or call out to a certain person deferentially.
4. 안녕 (安寧): 친구 또는 아랫사람과 서로 만나거나 헤어질 때 하는 인사말.
   hello; hi; good-bye; bye: A salutation uttered when the speaker meets or parts from his/her friend or junior.
5. 안녕히 (安寧히): 아무 문제나 걱정이 없이 편안하게.
   in peace: Comfortably without any problems or worries.
6. 어떠하다: 생각, 느낌, 상태, 형편 등이 어찌 되어 있다.
   such: Being such in one's thoughts, feelings, state, situation, etc.
7. 어떻다: 생각, 느낌, 상태, 형편 등이 어찌 되어 있다.
   such: Being such in one's thoughts, feelings, state, situation, etc.
8. 어서: 일이나 행동을 빨리 하도록 재촉하는 말.
   quickly; without hesitation; without delay: A word used to hurry someone to work or do something quickly.
9. 오래간만: 어떤 일이 있은 때로부터 긴 시간이 지난 뒤.
   being after a long time: A state in which a long time has passed since something happened.
10. 오래되다: 무엇이 시작되거나 생긴 후 지나간 시간이 길다.
   old; ancient: Marked by a long duration of time since the start or formation of something.
```
---
## 12. Get Hanja Information

Displays information about the hanja characters in a
scraped [`view`](main.md#view) response.

```python
response = krdict.scraper.view(
    target_code=14951 # target code for 가감승제
)

# the length of the results array for a view query is always 0 or 1
assert len(response.data.results) == 1

# filter out non-한자
lang_info = filter(
    lambda info: info.language_type == '한자',
    response.data.results[0].word_info.original_language_info
)

for info in lang_info:
    for idx, h_info in enumerate(info.hanja_info):
        print(f'Hanja {idx + 1}: {h_info.hanja}')
        print(f'Radical: {h_info.radical}')
        print(f'Stroke Count: {h_info.stroke_count}')
        print('Readings:')

        for reading in h_info.readings:
            print(f'   {reading}')

        print()
```
```md
Hanja 1: 加
Radical: 力
Stroke Count: 5
Readings:
   더할 가

Hanja 2: 減
Radical: 水
Stroke Count: 12
Readings:
   덜 감

Hanja 3: 乘
Radical: 丿
Stroke Count: 10
Readings:
   탈 승

Hanja 4: 除
Radical: 阜
Stroke Count: 10
Readings:
   덜 제
   사월 여
```
