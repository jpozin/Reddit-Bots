from random import randrange
import praw

bot = praw.Reddit(user_agent="HereHaveARandomNumber", client_id="secret", client_secret="secret", username="secret", password="secret")
subreddit = praw.subreddit("probability")

comments = subreddit.stream.comments()

for comment in comments:
    body = comment.body
    if "random number" in body.lower():
        commentlength = len(body)
        unifnum = randrange(1, 1 + commentlength)
        message = "Did someone need a random number? I generated a uniform random number between 1 and the number of characters in your comment, {}. The number I generated is {}".format(commentlength, unifnum)
        comment.reply(message)
