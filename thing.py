"""
SimpleNews
Get interesting things from Reddit
By Dylan Hamer
"""

import praw

client = "<CLIENT>"
secret = "<SECRET>"
agent = "SimpleNews (by /u/dylanhamer13)"

reddit = praw.Reddit(client_id=client,
                     client_secret=secret,
                     user_agent=agent)

def getStuff(post=4):
    limit = post+2
    jokes = reddit.subreddit("jokes").hot(limit=limit)
    showerthoughts = reddit.subreddit("showerthoughts").hot(limit=limit)
    news = reddit.subreddit("news").hot(limit=limit)
    
    joke = list(jokes)[post]
    jokeTitle = joke.title
        jokeBody = joke.body

    showerthought = list(showerthoughts)[post].title
    newsHeadline = list(news)[post].title
    
    return jokeBody, jokeTitle, showerthought, newsHeadline
    
def main():
    jokeBody, jokeTitle, showerthought, newsHeadline = getStuff()
    print("Hello, Dylan!")
    print("Joke Of The Day: {} \n {}".format(jokeTitle, jokeBody))
    print("Showerthought Of The Day: {}".format(showerthought))
    print("News Of The Day: {}".format(newsHeadline))
    
main()
