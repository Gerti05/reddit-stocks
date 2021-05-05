import praw
from praw.models import MoreComments
import time
import json

reddit = praw.Reddit(client_id='o7XLb9pm64Cuyw', client_secret='NlW8pLbG3rogvU1PkAq3ySXe0L3vAg', user_agent='Stock Comment Extraction')

subreddit = reddit.subreddit('wallstreetbets')

hot_wallstreetbets = subreddit.hot(limit=100)

with open('data.json', 'w', encoding='utf-8') as f:

    data_list = []

    for submission in hot_wallstreetbets:
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            data = [{'Comment': comment.body, 'id': comment.id}]
            data_list.append(data)


    json.dump(data_list, f, ensure_ascii=False, indent=4)