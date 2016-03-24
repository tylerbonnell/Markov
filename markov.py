from random import randint

class Markov:

    def __init__(self, text):
        self.eos = '{eos}'  # end of sentence
        map = {}
        start = {}
        sentences = text.split('.')
        for sen in sentences:
            words = sen.strip().split()
            words.append(self.eos)
            if len(words) > 1:
                start[words[0]] = start.get(words[0], 0) + 1
                for i in range(0, len(words) - 1):
                    w = words[i]
                    n = words[i + 1]
                    if w not in map:
                        map[w] = {}
                    map[w][n] = map[w].get(n, 0) + 1
        self.map = map
        self.start = start

    # Generates and returns a sentence
    def sentence(self):
        start = self.nextWord(self.start)
        word = self.nextWord(self.map[start])
        while word != self.eos:
            start += ' ' + word
            word = self.nextWord(self.map[word])
        return start

    # Chooses a word from a dictionary based on the weight,
    # where dict is a dictionary mapping words to likelyhood
    def nextWord(self, dict):
        sum = 0
        for k, v in dict.items():
            sum += v
        pos = randint(1, sum)
        run = 0
        for k, v in dict.items():
            run += v
            if run >= pos:
                return k
        return "this shouldn't ever be returned"