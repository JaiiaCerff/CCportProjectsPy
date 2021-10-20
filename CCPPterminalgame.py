#terminal game.
import random
import sys
import os



words = ['the', 'and', 'yes', 'bing', 'bong', 'boom','big']
ll = 9
win = random.randint(0,len(words))

#welcome

#length/template

def word_len():
    global win
    global words
    wordemp = []
    for l in range(0,len(words[win])):
        wordemp += ['_']
    return wordemp

temp = word_len()

def wordfin(t):
    for i in t:
        if '_' in t:
            return False
        else:
            return True

            
      


def letterinword(l,word):
    global ll
    newwordemp = temp
    if l == word:
        print('great job you guessed it!')
        fin('great job you guessed it!')
    elif l in word:
        print('Yep! That letter is in my word')
        i = -1 
        for le in word:
            i += 1
            if le==l:
                newwordemp[i]=le
        print(newwordemp)
    else:
        if ll > 1:
            ll -= 1
            print('Oh no that letter is not in my word. You lose a life... you now have {x} lives left'.format(x=ll))
            print(temp)
        else:
            print('sorry you lose...')
            fin('sorry you lose...')
    
    if wordfin(newwordemp) == True:
        print('great job you guessed it!')
        fin('great job you guessed it!')
        



def longest(l):
    longest = 0
    for word in l:
        if len(word) >= longest:
            longest = len(word)
    return longest


def fin(wl):
    if wl == 'great job you guessed it!':
        print('Congratulations, you won!')
    elif wl == 'sorry you lose...':
        print('GAME OVER')
    else:
        sys.exit()
    print('Would you like to play again?')
    print('y/n')
    if input() == 'y':
        os.execl(sys.executable, 'python', 'CCPPterminalgame.py', *sys.argv[1:])
    else:
        sys.exit()

def hello():
    
    print('Hello! Let\'s play a game. I am thinking of a word, you must guess it. You can ask me if the word contains any Letter, if it does, I\'ll tell you, if it does not you lose a life. Do you want to play?')
    print('y/n')
    if input() == 'y':
        print('Okay I\'m thinking of a word. You have nine lives!')
        print(temp)
    else:
        print("""okay :'( i'll find someone else to play with...""")
        fin('')

    tempres = word_len()
    for l in range(1,100):  
        letterinword(input(),words[win])
    


hello()



    




