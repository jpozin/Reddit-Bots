import praw

bot = praw.Reddit(user_agent="CountdownBot", client_id="secret", client_secret="secret", username="secret", password="secret")
subreddit = bot.subreddit("ClassicRock")

comments = subreddit.stream.comments()

for comment in comments:
    body = comment.body
    if "countdown" in body.lower():
        message = "[Did someone need a countdown?](http://bit.ly/1b73uns)"
        comment.reply(message)
