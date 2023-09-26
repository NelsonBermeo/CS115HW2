'''
Created on 9/22/23
@author:   Nelson Bermeo
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''
import sys
from functools import reduce
from dict import *
# Be sure to submit as hw2.py.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo",
"spam", "spammy", "zzyzva"]


############################################################## EXERCISE ONE

def letterScore(letter, scorelist):
    '''letterScore(letter, scorelist) takes as input a single letter string
called letter and a list where each element in that list is itself a list of
the form [character, value] where character is a single letter and value
is a number associated with that letter then returns a single number, namely
the value associated with the given letter. allowed to crash if letter not
in scorelist'''
    
    if scorelist == []:
        return []
    elif letter == scorelist[0][0]:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

############################################################## EXERCISE TWO
    
def wordScore(S, scorelist):
    '''should take as input a string S and a scorelist and
should return as output the scrabble score of that string.'''
    if S == '':
        return 0  
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)


############################################################## EXERCISE THREE


def valid_generation(s, rack):
    '''This function takes in a string and a rack of letters and outputs a boolean whether the string can be created from the rack'''
    if len(s) == 1 and s[0] in rack:
        return True
    elif s[0] in rack:
        i = rack.index(s[0])
        return valid_generation(s[1:], rack[0:i]+rack[i+1:])
    else:
        return False

def valid_words_list(rack, dic = Dictionary):
    ''' This function takes a rack and has a set dictionary that the coder can replace with if nessesary. This function outputs a list of
valid words that can be made from the dictionary using the Rack.'''
    if dic == []:
        return []
    elif valid_generation(dic[0], rack) == True:
        return [dic[0]] + valid_words_list(rack, dic[1:])
    else:
        return valid_words_list(rack, dic[1:])

def nested_list(i):
    ''' This is a helper function for scoreList that takes a variable which would be valid word and outputs a list to be used in a nested list
list with the word score'''
    return [i, wordScore(i, scrabbleScores)]

def scoreList(rack):
    ''' This is the main function that ties the previous three together, this function takes in a rack and outputs a list of lists for each word
and their score'''
    list_of_valids = valid_words_list(rack)
    if list_of_valids == []:
        return ["",0]
    else:
        return list(map(nested_list, list_of_valids))

     
############################################################## EXERCISE FOUR

def biggest(x,y):
    ''' This is a helper function for the bestWord function and intakes two variables which are two valid words and returns the larger of the two'''
    if wordScore(x, scrabbleScores) > wordScore(y, scrabbleScores):
        return x
    return y
 
def bestWord(Rack):
    ''' This function takes in a rack and returns a list of the highest scored word with the word and the points'''
    valid_lists = valid_words_list(Rack)
    if valid_lists ==[]:
        return ["",0]
    else: 
        biggest_word = reduce(biggest, valid_lists)
        return nested_list(biggest_word)

##############################################################













    
