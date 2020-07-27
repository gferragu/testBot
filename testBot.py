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