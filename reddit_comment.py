import praw, re
from markov import Markov

def valid_redditor(user):
    comments = user.get_comments(limit=1)
    try:
        for c in comments:
            return True
    except:
        return False

def main():
    r = praw.Reddit(user_agent="Markov Comment Generator by /u/officialdovahkiin")
    name = raw_input("reddit username: ")
    user = r.get_redditor(name)
    if (valid_redditor(user)):
        try:
            comment_amount = int(raw_input("number of comments to consider: "))
            sentence_amount = int(raw_input("number of sentences to generate: "))
            comments = user.get_comments(limit=(None if comment_amount <= 0 else comment_amount))
            text = ""
            for c in comments:
                text += c.body + ". "
            mk = Markov(text)
            sentences = ""
            for i in range(0, sentence_amount):
                sentences += mk.sentence() + ". "
            print sentences
        except:
            print "Please enter a valid number"
    else:
        print "No comments found for /u/" + name

if __name__ == "__main__":
    main()