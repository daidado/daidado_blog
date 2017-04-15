import redditapi
import textblob

def usercomments(username):
    reddit = redditapi.RedditInstance('User Comments')
    comments = []
    most = ""
    least = ""
    mostpos = -1
    leastpos = 1
    text = []
    plot = []
    for comment in reddit.redditor(username).comments.hot(limit=None):
        text.append(comment.body)
        blob = textblob.TextBlob(comment.body)
        plot.append((comment.created, comment.body, blob.sentiment.polarity)) 
        if blob.sentiment.polarity > mostpos:
            mostpos = blob.sentiment.polarity
            most = comment.body
        if blob.sentiment.polarity < leastpos:
            leastpos = blob.sentiment.polarity
            least = comment.body
    return (textblob.TextBlob("\n".join(text)).sentiment.polarity,
            most, least, plot)

print usercomments('sct202')
print usercomments('O0O0RION')
