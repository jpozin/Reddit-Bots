from random import randrange
import praw

bot = praw.Reddit(user_agent="CoinFlipBot", client_id="secret", client_secret="secret", username="secret", password="secret")
subreddit = bot.subreddit("askmath")

comments = subreddit.stream.comments()

outcomes = ["heads", "tails"]
headscount = 0
tailscount = 0

for comment in comments:
    body = comment.body
    if "coin flip" in body.lower():
        outcome = outcomes[randrange(2)]
        if outcome == "heads":
            headscount += 1
        else:
            tailscount += 1
        message = """Did someone need a coin flip? I just flipped a coin and it came up {}.
        During this session of activity, I have flipped {} heads and {} tails.
        """.format(ouctome, headscount, tailscount)
        comment.reply(message)
