const enumTypes = new Set([
    'Classification',
    'MultimediaType',
    'OriginType',
    'PartOfSpeech',
    'ResponseType',
    'SearchMethod',
    'SearchTarget',
    'SearchType',
    'SortMethod',
    'TargetLanguage',
    'TranslationLanguage',
    'VocabularyLevel',
    'SemanticCategory',
    'SubjectCategory',
    'ScrapedResponseType',
    'ScraperSearchTarget',
    'ScraperTargetLanguage',
    'ScraperTranslationLanguage',
    'ScraperVocabularyLevel',
]);
const responseTypes = new Set([
    'DefinitionResponse',
    'ErrorResponse',
    'ExampleResponse',
    'IdiomProverbResponse',
    'ViewResponse',
    'WordResponse',
    'ScrapedDefinitionResponse',
    'ScrapedExampleResponse',
    'ScrapedIdiomProverbResponse',
    'ScrapedViewResponse',
    'ScrapedWordResponse',
    'WordOfTheDayResponse',
]);
const otherTypes = new Set([
    'KRDictException',
    'SearchCondition',
]);
const mainFunctions = new Set([
    'krdict.advanced_search',
    'krdict.search',
    'krdict.set_key',
    'krdict.view',
]);
const scraperFunctions = new Set([
    'krdict.scraper.advanced_search',
    'krdict.scraper.fetch_semantic_category_words',
    'krdict.scraper.fetch_subject_category_words',
    'krdict.scraper.fetch_word_of_the_day',
    'krdict.scraper.search',
    'krdict.scraper.view',
]);
const splitRegex = /[^A-Za-z\._]+/;


function linkify() {
    const codeBlocks = document.getElementsByTagName('pre');

    if (!codeBlocks || codeBlocks.length === 0) {
        return;
    }

    for (const block of codeBlocks) {
        if (block.children.length !== 1) {
            continue;
        }

        const code = block.children[0];
        if (!code.classList.contains('language-python')) {
            // only care about python blocks
            continue;
        }

        const stack = [code];
        do {
            const node = stack.pop();
            if (node.childNodes.length > 0) {
                if (node.classList.contains('hljs-comment')) {
                    continue;
                }

                for (const child of node.childNodes) {
                    stack.push(child);
                }

                continue;
            }

            if (node.nodeType !== Node.TEXT_NODE) {
                // process only text nodes directly
                continue;
            }

            const tokens = node.textContent.split(splitRegex).filter(s => {
                if (mainFunctions.has(s) || scraperFunctions.has(s)) {
                    return true;
                }

                return s.split('.').some(s => {
                    return enumTypes.has(s) || responseTypes.has(s) || otherTypes.has(s);
                });
            });

            for (let token of tokens) {
                let page = '';
                if (mainFunctions.has(token)) {
                    page = 'main';
                } else if (scraperFunctions.has(token)) {
                    page = 'scraper';
                }

                let idx = node.textContent.indexOf(token);
                if (idx === -1) {
                    continue;
                }

                if (token.indexOf('.') !== -1) {
                    if (token.startsWith('krdict.')) {
                        token = token.slice(7);
                        idx += 7;
                    }

                    if (token.startsWith('scraper.')) {
                        token = token.slice(8);
                        idx += 8;
                    }

                    // prevent the function definitions from becoming too busy
                    // but still link to enums from the example code
                    if (document.location.pathname.indexOf('examples') !== -1) {
                        const end = token.indexOf('.');
                        if (end !== -1) {
                            token = token.slice(0, end);
                        }
                    }
                }

                if (enumTypes.has(token)) {
                    page = 'enums';
                } else if (responseTypes.has(token)) {
                    page = 'return_types';
                } else if (otherTypes.has(token)) {
                    page = 'other';
                }

                if (page === '') {
                    continue;
                }

                const leftSplit = node.textContent.slice(0, idx);
                const rightSplit = node.textContent.slice(idx + token.length);

                const anchor = document.createElement('a');
                anchor.textContent = token;
                anchor.classList.add('code-anchor');
                anchor.href = `../${page}/#${token.toLowerCase()}`;

                const leftNode = document.createTextNode(leftSplit);

                node.parentElement.insertBefore(leftNode, node);
                node.parentElement.insertBefore(anchor, node);
                node.textContent = rightSplit;
            }
        } while (stack.length > 0);
    }
}

window.addEventListener('DOMContentLoaded', linkify, false);
