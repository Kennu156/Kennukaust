import praw
import credentials

reddit = praw.Reddit(
    client_id= credentials.client_id,
    client_secret= credentials.client_secret,
    user_agent="python3:Kennu156:0.1 (by u/Kennu156)",
)


for submission in reddit.subreddit("Eesti").top(limit=10):
    print(submission.title)

import praw

reddit = praw.Reddit(
   client_id= 'tmNtAvAgBjdEatlWk2PnWw',
  client_secret= 'NGaJwqso_109dVX3tlMIE-Z1aVBSAw',
    user_agent="python3:Kennu156:0.1 (by u/Kennu156)",
)
subreddit = reddit.subreddit('Eesti')

words = []

for submission in subreddit.hot(limit = 2):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        word = ""
        for letter in top_level_comment.body:
            if(letter == " "):
                #if(word and not word[-1].isalnum()):
                 #   word = word[:-1]
                #if not word in commonWords:
                words.append(word)
                word = ''
            else:
                word += letter
        
wordCount = {}

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1
    

print(wordCount)
    
        
