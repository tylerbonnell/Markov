class Markov:

    def __init__(self, text):
        map = {}
        start = {}
        sentences = text.split(".")
        for sen in sentences:
            words = sen.strip().split()
            for i in range(0, len(words) - 1):
                w = words[i]
                n = words[i + 1]
                if w not in map:
                    map[w] = {}
                map[w][n] = map[w].get(n, 0) + 1
        self.map = map

    # Generates and returns a sentence
    def sentence(self):
        print self.map

    # Chooses a word from a dictionary based on the weight,
    # where dict is a dictionary mapping words to likelyhood
    def nextWord(self, dict):

