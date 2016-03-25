from markov import Markov

def main():
    f = open('sherlock.txt', 'r')
    mk = Markov(f.read())
    for i in range(0, 3):
        print mk.sentence()

if __name__ == '__main__':
    main()