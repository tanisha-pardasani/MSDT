"""
Intro to python exercises shell code
"""

def is_odd(x):
    if (x % 2 == 1) :
        print ('true')
    
    else:
        print ('false')
    """
    returns True if x is odd and False otherwise
    """


def is_palindrome(word):
    j = ""
    for i in word: 
            j = i + j;
    if ( word == j) : 
        print('true')
    else:
        print('false')
    """
    returns whether `word` is spelled the same forwards and backwards
    """


def only_odds(numlist):
    list = []
    for i in range (0, len(numlist)):
        if numlist[i] % 2 == 1 : 
            list.append(numlist[i])
    print(list) 
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """


def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    countwords = {}
    words = text.split()
    for i in words:
        if i in countwords:
            countwords[i] += 1
        else:
            countwords[i] = 1
    return countwords