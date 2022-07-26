import praw
red = praw.Reddit(client_id='CV0uXmTV_HBqzhy-hPMkvA',
client_secret='6N6OHwiu_Ilqx10M64lfJu4ImeoOCQ',
user_agent='pyred')

for i in red.front.hot():
    print(i)
