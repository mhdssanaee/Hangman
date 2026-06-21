def getName():
    name=str(input('Enter your name:'))
    print('Hi',name,'.Welcome to Hangman Game:)')
    return startORend()


def startORend():
    SE=str(input('DO you wanna play? If yes,please enter \'s\' to start:')).lower()
    if SE=='s':
        return randomCountry()
        
import random
import os
from playsound import playsound
def randomCountry():
    factor=0
    choosefactor=str(input('''Choose difficulty:
enter \'h\' for Hard
enter \'m\' for Medium
enter \'e\' for Easy
which one? ''')).lower()
    if choosefactor=='h':
        factor=1.75
    elif choosefactor=='m':
        factor=2
    elif choosefactor=='e':
        factor=2.5

    readfile=open('CountryNames.txt','r')
    countryList=readfile.read().split('\n')
    randomcountry=random.choice(countryList).lower().replace(' ','')
    lenn=len(randomcountry)
    slash='_ '*lenn
    health=round(factor*lenn)
    print(slash)
    print('you have ',health,' chances')
    correctguesses=0
    allguesses=[]
    guesstrue=''
    dir = os.getcwd()
    correctsound = dir + '\correct1.mp3'
    wrongsound = dir + '\wronganswer.mp3'
 
    letter=str(input('Guess a country or a letter: ')).lower()
    while True:
        if letter in allguesses:
            letter=str(input('You have already guessed this letter.Guess again: ')).lower()
        elif letter not in allguesses:
            if letter==randomcountry:
                playsound(correctsound)
                answer=str(input('You won! DO you want play again? Enter \'y\' for Yes:')).lower()
                if answer=='y':
                    return randomCountry()
                
            elif letter not in randomcountry:
                playsound(wrongsound)
                health=health-1
                if health!=0: 
                        print('not true:( Your health is:',health)
                        allguesses.append(letter)
                        letter=str(input('Guess again: ')).lower()
                elif health==0:
                    print('You lose:( The country was:',randomcountry)
                    return startORend()    
                    
            elif letter in randomcountry:
                
                playsound(correctsound)
                for i in randomcountry:
                    if i==letter:
                        correctguesses+=1
                allguesses.append(letter)
                guesstrue+=letter
                for i in randomcountry:
                    if i in guesstrue:
                        print (i,end=' ')
                    else:
                        print ('_',end=' ')
                
                if correctguesses<lenn:
                    letter=str(input('\nGuess again: ')).lower()
                    
                elif correctguesses==lenn:
                    answer2=str(input('\nYou won! DO you want play again? Enter \'y\' for Yes:')).lower()
                    if answer2=='y':
                        return randomCountry()
        
getName()
    
    
            
        
            
    
    




