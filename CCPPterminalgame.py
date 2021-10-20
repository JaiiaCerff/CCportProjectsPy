#terminal game.
import random


words = ['the', 'and', 'ye']
ll = 9
win = random.randint(0,2)

def hello():
    print('Hello! Let\'s play a game. I am thinking of a word, you must guess it. You can ask me if the word contains any Letter, if it does, I\'ll tell you, if it does not you lose a life. Do you want to play?')
    print('y/n')
    if input() == 'y':
        print('Okay I\'m thinking of a word. You have nine lives!')
    else:
        print("""okay :'( i'll find someone else to play with...""")
hello()

def letterinword(l,word):
    global ll
    if l == word:
        print('great job you guessed it!')
    elif l in word:
        print('Yep! That letter is in my word')
    else:
        if ll > 1:
            ll -= 1
            print('Oh no that letter is not in my word. You lose a life... you now have {x} lives left'.format(x=ll))
        else:
            print('sorry you lose...')
        
def longest(l):
    longest = 0
    for word in l:
        if len(word) >= longest:
            longest = len(word)
    return longest


for l in range(1,(longest(words)+9)):  
    letterinword(input(),words[win])



