import markov

def main():
    ch = markov.chain("here is a paragraph of a bunch of stupid words and shit")
    print ch

if __name__ == "__main__":
    main()