"""
lab4.py
George Harvey
Updated Feb 28, 2018
Practice with sequence traversal and string processing
"""

def spell_w(word):
	"""
	Prints out characters in word seperated by *** using a while loop
	word: string
	Returns: None
	"""
	# define loop variable idx and initialize with 0
	idx = 0

	# write while header
	while(idx < (len(word))):
		letter = word[idx]
		print(letter, '***')
		idx = idx +1	
	# termination condition tests that idx is smaller than no. chars in word
		# define local variable letter to store character in word at idx

		# print out character in letter and end printing with ***

		# advance idx to next position

	print( ) # print new empty line


def spell_f(word):
	"""
	Prints out characters in word seperated by *** using a for loop
	
	word: string
	Returns: None

	"""
	for letter in word:
		print(letter, '***')
	# write for header, in which we
	# create loop variable letter to iterate through characters in word

		# print out characdter in letter and end printing with ***


	print( ) # print new empty line

def my_len(word):
	"""
	Returns the length word using string traversal and accumulator pattern
	
	word: string
	Returns: Integer value corresponding to length of word
	"""

	word_len = 0 # initialize variable word_len to track length

	# loop over the word letter by letter
	for each_letter in word:
		word_len = word_len +1

		# accumulate 1 into word_len to count the letters

	# return word_len
	return word_len

def my_find(word, letter):
	"""
	Tests if letter is in word
	word: string
	letter: one-character string
	Returns: True if letter is in word, False otherwise
	"""
	# initialize variable found to False
	found = False
	# loop over word using a loop variable different than letter!!!
	for char in word:
		if char == letter:
			found = True


		# tests if loop variable is the same as letter

			# update found to True

	# return found
	return found