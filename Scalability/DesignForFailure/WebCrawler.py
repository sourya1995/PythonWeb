import celery
import requests
import tenacity

app = celery.Celery('WebCrawler', broker='redis://localhost',
                    backend='redis://localhost')


def do_something(url_to_crawl):
    dic = {}
    r = requests.get(url=url_to_crawl)
    if r.status_code != 200:
        raise RuntimeError
    text = r.text
    dic['data'] = text
    dic['status_code'] = r.status_code
    return dic

@app.task()
def getURL(url_to_crawl):
    @tenacity.retry(wait=tenacity.wait_fixed(5), stop=tenacity.stop_after_attempt(3))
    def do_something_and_retry(url_to_crawl):
        return do_something(url_to_crawl)
    return do_something_and_retry(url_to_crawl)
        

if __name__ == '__main__':
    urls = ["http://example.io", "http://example.org/", "http://example.com"]

    results = []
    for url in urls:
        results.append(getURL.delay(url))

    for result in results:
        print("Task state: %s" % result.state)
        print("Result: %s" % result.get())
        print("Task state: %s" % result.state)
