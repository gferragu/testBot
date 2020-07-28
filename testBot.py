# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import praw
# from praw.helpers import comment_stream #This is deprecated

client_id = "1iSYC_8rmmp7bw"
client_secret = "Ja9duo1jFVZFyDgZlhs3nY7tMsQ"
user_agent = "mac:testBot:v1.0.0 (b u/testBot-1)"
# %% Read Only "Reddit" Instance
# reddit = praw.Reddit(client_id=client_id,
#                      client_secret=client_secret,
#                      user_agent=user_agent)

# print(reddit.read_only)

# for submission in reddit.subreddit("learnpython").hot(limit=10):
#     print(submission.title)

# %% Authorized Reddit Instance (read and comment)

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username="testBot-1",
                     password="hummushummus69")

print(reddit.read_only)  # Output: False

# Switch back to read only
# reddit.read_only = True

# %% Getting instances of "subreddit" and "submission"

# for submission in reddit.subreddit("learnpython").hot(limit=10):
#     print(submission.title)

# assume you have a Reddit instance bound to variable `reddit`
subreddit = reddit.subreddit("redditdev")

print(subreddit.display_name)  # Output: redditdev
print(subreddit.title)         # Output: reddit Development
print(subreddit.description)   # Output: A subreddit for discussion of ...

# %%

# assume you have a Subreddit instance bound to variable `subreddit`
for submission in subreddit.hot(limit=10):
    print(submission.title)     # Output: the submission's title
    print(submission.score)     # Output: the submission's score
    print(submission.id)        # Output: the submission's ID
    print(submission.url)       # Output: the URL the submission points to
                                # or the submission's URL if it's a self post

# assume you have a Reddit instance bound to variable `reddit`
"""
But how do you generate the submission id?
"""
submission = reddit.submission(id="39zje0")
print(submission.title)  # Output: reddit will soon only be available ...

# or
submission = reddit.submission(url='https://www.reddit.com/...')