import praw
import re

bot = praw.Reddit(user_agent="CheerUpBot", client_id="secret", client_secret="secret", username="secret", password="secret")
subreddit = bot.subreddit("all")

comments = subreddit.stream.comments()

for comment in comments:
    body = comment.body
    if re.findall("i am sad") or re.findall("i'm sad"):
        message = "Are you sad? Cheer up! [Here](http://bit.ly/2sxbLUB) is a picture of a happy kitten"
        comment.reply(message)
