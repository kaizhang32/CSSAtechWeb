# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:36:47 2017

@author: Danni
"""

import random
def judge(guess):
 
    gue = int(guess)
 
    if (gue<0) or (gue>20):
        print('Wrong,Please input a number between 0 to 20.')
        guess = input('Please input a number between 0 to 20：')
        judge(guess)
        
    return gue
      

def istrue(n,guess):
    n=random.randint(1,21)
    print(n)
    b=str(input('Hello! What is your name?'))
    print('Well,',b,',I am thinking of a number between 1 and 20.')
    guess=int(input( 'Take a guess:'))
    guess = judge(guess)
    for a in range(1,6):
        if n!= guess:
            if guess<n:
                print('Your guess is too low.')
                guess=int(input('Take a guess:'))
                guess = judge(guess)
            
            elif guess>n:
                print('guess is high.')
                guess=int(input('Take a guess:'))
                guess = judge(guess)
               
            
            if n == guess:
                print('Good Job,',b,',You have guessed my number in',a+1,'guesses!')
                #guessed = True
                break
                 
            if a == 5:
                print('The number I was thinking of was',n)
    return;
        
istrue(n,guess)


        #break
    
             
             
#if a==6:    
   #print('The number I was thinking of was',n)
    