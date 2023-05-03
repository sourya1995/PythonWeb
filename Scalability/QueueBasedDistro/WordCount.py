import celery

app = celery.Celery('celery-test',
                    broker='redis://localhost',
                    backend='redis://localhost')

@app.task
def getWordCount(text):
    wordlist = text.split(' ')
    dict = {}
    for word in wordlist:
        if word not in dict.keys():
            dict[word] = 1
        else:
            dict[word] += 1
    return dict

if __name__ == '__main__':
    texts = ["He's a fantastic manager who has won so many trophies. He always wants to win more and. I have to say that I'm proud to play for him. Sometimes it is not easy, he's never happy and always wants to win more and wants you to improve every day, but I like that."]
    results = []
    for text in texts:
        results.append(getWordCount.delay(text))

    for result in results:
        print("Task state: %s" % result.state)
        print("Result: %s" % result.get())
        print("Task state: %s" % result.state)
