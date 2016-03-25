# Looks at a certain number of comments from a user's reddit account
# (up to 1000) and generates sentences based off of what it finds

import praw, re
from markov import Markov

# Checks whether or not the user has any comments
# I don't think there's a better way to do this...
def valid_redditor(user):
    comments = user.get_comments(limit=1)
    try:
        for c in comments:
            return True
    except:
        return False

# Removes links or other weird stuff from the comment
def format_comment(c):
    return re.sub("(\[.+\]\(.*\)|https?:\/\/([^\s]+))", " ", c)

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
                text += format_comment(c.body) + ". "
            mk = Markov(text)
            sentences = ""
            for i in range(0, sentence_amount):
                sentences += mk.sentence() + ". "
            print sentences
        except:
            print "Please enter a valid number"
    else:
        print "No comments found for /u/" + name

if __name__ == '__main__':
    main()

