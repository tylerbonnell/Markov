from markov import Markov

def main():
    mk = Markov("here is a paragraph of a bunch of stupid words and shit and shit and shit")
    print mk.sentence()

if __name__ == "__main__":
    main()