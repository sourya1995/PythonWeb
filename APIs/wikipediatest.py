import wikipedia

def print_wikipedia_results(word):
    results = wikipedia.search(word)

    for result in results:
        try:
            page = wikipedia.page(result)
        except wikipedia.exceptions.DisambiguationError:
            print('Disambiguation Error')
            continue
        except wikipedia.exceptions.PageError:
            print('PageError for result: ' + result)
            continue

        print(page.summary.encode('utf-8'))

if __name__ == '__main__':
    print_wikipedia_results('ebooks')

