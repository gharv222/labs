"""
lab6start.py
George Harvey
March 7, 2018
"""

def opposite_nums(num_list):
    """
    Maps numbers in the num_list to numbers of same value, but opposite sign
    num_list: list of numbers
    Returns: list of original numbers, but with opposite sign
    >>> opposite_nums([1,2,3,4])
    [-1, -2, -3, -4]
    >>> opposite_nums([-1,-2,-3,-4])
    [1, 2, 3, 4]
    >>> opposite_nums([2,3,4,5])
    [-2, -3, -4, -5]
    """

    result = []
    for num in num_list:
        result.append(num * -1)
        
    

    return result

def keep_words(word_list):
    """
    Filters out strings that have digits
    word_list: list of strings
    Returns: list of strings that have only letters in them
    >>> keep_words(['hello', 'h3llo', 'G00D', 'Good'])
    ['hello', 'Good']
    >>> keep_words(['abc', 'a1b2', 'cde'])
    ['abc', 'cde']
    >>> keep_words(['hi', 'by3', 'car', 'r2n'])
    ['hi', 'car']
    """
    result = [ ]
    for word in word_list:
        if word.isalpha():
            result.append(word)

    return result

def sum_of(num_list):
    """
    Sums up the numbers in num_list
    num_list: list of numbers
    Returns: the sum of the numbers in the num_list
    >>> sum_of([1,2,3])
    6
    >>> sum_of([])
    
    >>> sum_of([-5, 10, 7])
    12
    """
    result = 0

    if not num_list:
        return None

    for num in num_list:
        result = result + num

    

    return result

def average(num_list):
    """
    Average numbers in num_list
    num_list: list of numbers
    Returns: the average of the numbers in num_list. 
    If num_list is empty, return None
    >>> average([1,2,3,4,5,6,7])
    4.0
    >>> average([2,4,6,8,10])
    6.0
    >>> average([-5,-8, 10, 3])
    0.0
    """
    if not num_list:
        return None
    result = 0

    for num in num_list:
        result = result + num

    result = result/len(num_list)

    return result

def capitalize(sentence):
    """
    Capitalize all the words in sentence. 
    Implementation requirements:
      Use str.split( ) to convert sentence into a list of words.
      Use list.join( ) to convert a list of words into a string
    sentence: string of words separated by white spaces
    Return: string with the same words that sentence has, but capitalized.
    >>> capitalize('hello this is a test')
    'Hello This Is A Test'
    >>> capitalize('Hello, this is a test to see what happens')
    'Hello, This Is A Test To See What Happens'
    >>> capitalize('Python is taught in data structures')
    'Python Is Taught In Data Structures'
    """
    new_word_list = [ ]

    
    for word in sentence.split():
        new_word_list.append(word.capitalize())

    new_sentence = ' '.join(new_word_list)
    return new_sentence

if __name__ == '__main__':
    import doctest
    doctest.testmod( )