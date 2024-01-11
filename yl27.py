import praw
import credentials

reddit = praw.Reddit(
    client_id= credentials.client_id,
    client_secret= credentials.client_secret,
    user_agent="python3:Kennu156:0.1 (by u/Kennu156)",
)


for submission in reddit.subreddit("Eesti").top(limit=10):
    print(submission.title)