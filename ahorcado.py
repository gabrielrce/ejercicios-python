import random

IMAGES = ['''


    +---+
    |   |
        |
        |
        |
        |
        ========''', '''


    +---+
    |   |
    O   |
        |
        |
        |
        ========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        ========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        ========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        ========''', '''


    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        ========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |

        ========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ========''', '''

    ''']

WORDS = ['computadora', 'conejo', 'andres', 'hola']


def selectWord():
    i = random.randint(0, len(WORDS) - 1)
    return WORDS[i]


def display(hiddenWord, tries):
    print(IMAGES[tries])
    print(' ')
    print(hiddenWord)
    print('-------------------------------------')


def run():
    word = selectWord()
    hiddenWord = ['-'] * len(word)
    tries = 0

    while True:
        display(hiddenWord, tries)
        x = str(input('Escoge una letra: '))
        letterIndex = []

        for i in range(len(word)):
            if word[i] == x:
                letterIndex.append(i)

        if len(letterIndex) == 0:
            tries += 1

            if tries == 7:
                display(hiddenWord, tries)
                print(' ')
                print('Perdiste, la palabra correcta era {}'.format(word))
                break

        else:
            for i in letterIndex:
                hiddenWord[i] = x

            letterIndex = []

        try:
            hiddenWord.index('-')
        except ValueError:
            print('Felicidades, ganaste. La palabra es: {}'.format(word))
            break


if __name__ == '__main__':

    run()
