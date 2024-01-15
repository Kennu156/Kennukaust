import praw
import matplotlib.pyplot as plt
from collections import Counter
import credentials


reddit = praw.Reddit(
    client_id='tmNtAvAgBjdEatlWk2PnWw',
    client_secret='NGaJwqso_109dVX3tlMIE-Z1aVBSAw',
    user_agent="python3:Kennu156:0.1 (by u/Kennu156)"
)

subreddit_name = 'eesti'

subreddit = reddit.subreddit(subreddit_name)
hot_posts = subreddit.hot(limit=10)

word_counter = Counter()

total_words = 0

for post in hot_posts:
    title_words = post.title.lower().split()
    word_counter.update(title_words)
    total_words += len(title_words)

    post.comments.replace_more(limit=None)
    for comment in post.comments.list():
        comment_words = comment.body.lower().split()
        word_counter.update(comment_words)
        total_words += len(comment_words)


common_words = word_counter.most_common(10)

for word, count in common_words:
    percentage = (count / total_words) * 100
    

labels = [word[0] for word in common_words]
sizes = [(word[1] / total_words) * 100 for word in common_words]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('r/' + subreddit_name)


plt.savefig('diagramm.png')
