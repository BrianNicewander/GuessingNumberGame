# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:41:44 2020

@author: Brian
"""
import random

def ranNumber():
    guess ='wrong'
    numberOfGuesses = 0
    randomNumber = random.randint(1,100)
    while guess == 'wrong':
         number = int(input("Please enter a number between 1 and 100 "))
         if number > randomNumber:
            print("The number you picked is to high try a lower number ")
            numberOfGuesses += 1
            guess = 'wrong'
         elif number < randomNumber:
            print("The number you picked is to low try a higher number")
            numberOfGuesses += 1
            guess = 'wrong'
         elif number == randomNumber:
            print("Congratulation you guessed the right number the number was ", randomNumber)
            numberOfGuesses += 1
            print("It took you", numberOfGuesses, 'times to guess the right number')
            guess = 'right'
            
        
ranNumber()