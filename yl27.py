import praw
import matplotlib.pyplot as plt
from collections import Counter


reddit = praw.Reddit(
    client_id='tmNtAvAgBjdEatlWk2PnWw',
    client_secret='NGaJwqso_109dVX3tlMIE-Z1aVBSAw',
    user_agent="python3:Kennu156:0.1 (by u/Kennu156)"
)

subreddit_name = 'eesti'

# leiab subredditist 10 kõige populaarsemat postitust
subreddit = reddit.subreddit(subreddit_name)
hot_posts = subreddit.hot(limit=10)

# salvestab sõnade sagedust
word_counter = Counter()

# arv sõnu kõigis kommentaarides
total_words = 0

# loop läbi postituste pealkirjade ja kommentaaride
for post in hot_posts:
    # Töötle pealkirja
    title_words = post.title.lower().split()
    word_counter.update(title_words)
    total_words += len(title_words)

    # Töötle kommentaare
    post.comments.replace_more(limit=None)
    for comment in post.comments.list():
        comment_words = comment.body.lower().split()
        word_counter.update(comment_words)
        total_words += len(comment_words)


common_words = word_counter.most_common(10)

# Leiab ja prindib sõnade protsendid

print("10 enim kasutatud sõnad subredditis r/eesti:")
for word, count in common_words:
    percentage = (count / total_words) * 100
    print("{}: {:.1f}%".format(word, percentage))

plt.bar([word[0] for word in common_words], [(word[1] / total_words) * 100 for word in common_words])
plt.xlabel('Words')
plt.ylabel('Percentage')
plt.title(subreddit_name)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()

