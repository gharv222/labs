"""
George Harvey]
COMP 525
Lab 9
"""

def count_words(file_in):
	"""
	Counts how many times each word in a text files appears
	file_in: txt file
	returns: a dictionary that keys are each word in the 
	txt file and their value is how many times it appears
	"""

	fin = open(file_in, 'r')
	word_dict = {}
	for line in fin:
		tmp_list = line.split()
		for word in tmp_list:
			if word in word_dict:
				word_dict[word] += 1
			else: 
				word_dict[word] = 1
	return word_dict