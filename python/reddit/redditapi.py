import os
import praw

def RedditInstance(purpose):
    return praw.Reddit(user_agent=purpose,
                       client_id=os.environ["REDDIT_ID"],
                       client_secret=os.environ["REDDIT_KEY"])
