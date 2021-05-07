import praw
from praw.models import MoreComments
import time
import json

reddit = praw.Reddit(client_id='o7XLb9pm64Cuyw',
                     client_secret='NlW8pLbG3rogvU1PkAq3ySXe0L3vAg', user_agent='Stock Comment Extraction')

submission = reddit.submission(id="n77hgs")


with open('redditData.json', 'w', encoding='utf-8') as f:

    data_list = []

    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        data = [{'Comment': comment.body, 'id': comment.id}]
        data_list.append(data)

    json.dump(data_list, f, ensure_ascii=False, indent=4)
