import RAKE
import redditapi

minscore = 1.5


reddit = redditapi.RedditInstance('Get top comments from top posts.')
topposts = reddit.subreddit('all').hot(limit=5)
posttext = []
for post in topposts:
    text = [post.title]
    post.comments.replace_more(limit=0)
    for comment in post.comments.list():
        text.append(comment.body)
    posttext.append(text)
keywordAnalyzer = RAKE.Rake('python/reddit/stopwords.txt')
keywordCount = {}
for post in posttext:
    keywords = keywordAnalyzer.run('\n'.join(post))
    for keyword in keywords:
        if keyword[1] <= minscore:
            break
        if keyword[0] in keywordCount:
            keywordCount[keyword[0]] += 1
        else:
            keywordCount[keyword[0]] = 1
for keyword in keywordCount:
    if keywordCount[keyword] > 3:
        print keyword
