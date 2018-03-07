"""
lab5.py
George Harvey
Updated March 7, 2018
Practice with sequence traversal and string processing
Use doctest to run test cases
"""

def spell_w(word):
	"""
	Prints out characters in word seperated by '-' using a while loop
	word: string
	Returns: None
	>>> spell_w('hi')
	h-i-
	>>> spell_w('hello')
	h-e-l-l-o-
	"""
	idx = 0
	while(idx < len(word)):
		letter = word[idx]
		print(letter, end='-')
		idx = idx + 1

def spell_f(word):
	"""
	Prints out characters in word seperated by '-' using a for loop
	word: string
	Returns: None
	>>> spell_f('hi')
	h-i-
	>>> spell_f('hello')
	h-e-l-l-o-
	"""
	for letter in word:
		print(letter, end='-')

def my_len(word):
	"""
	Returns the length word using string traversal and accumulator pattern
	word: string
	Returns: Integer value corresponding to length of word
	>>> my_len('test')
	4
	>>> my_len('testtwo')
	7
	"""
	word_len = 0 
	# loop over string word with loop variable ch of type string
	for ch in word:
		# accumulate 1 into word_len to count the characters
		word_len = word_len + 1
	return word_len

def my_find(word, letter):
    """
    Tests if letter is in word
    word: string
    letter: one-character string
    Returns: True if letter is in word, False otherwise
    >>> my_find('apple', 'l')
    True
    >>> my_find('orange','w')
    False
    """
    found = False
    # loop over string word using the loop variable ch of type string
    # Note: loop variable name MUST be different than parameter letter!
    for ch in word:
        if ch == letter:
            found = True
    return found

def parse_season(season_list):
    """
    Print out names of seasons in season_list
    season_list: list of season names
    >>> parse_season(['fall','winter','spring','summer'])
    fall
    winter
    spring
    summer
    >>> parse_season(['spring','summer','fall','winter'])
    spring
    summer
    fall
    winter
    """
    for a_season in season_list:
        print(a_season)

def double_number(num_list):
    """
    Return copy of number_list with all its numbers doubled
    number_list: list of numbers
    Return: list of numbers
    >>> double_number([1,2,3])
    [2, 4, 6]
    >>> double_number([2,4,6])
    [4, 8, 12]
    """
    double_number_list = [ ]
    for num in num_list:
        double_num = num * 2
        double_number_list.append(double_num)
    return double_number_list

if __name__ == '__main__':
	import doctest
	doctest.testmod( )