""" 
Practice with defining funcions
lab1.py
George Harvey
1/31/2018
"""

### Excersise #3
def alarm_clock():
	"""
	Calculates abd outputs the time when the alarm goes off based on 
	time current time (in hours) and number of hours to wait for the alarm.
	"""
	print('done')
	## question 3 solution ##

	current_time_string = input("What is the current time (in hours)? ")
	waiting_time_string = input("How many hours do you have to wait? ")

	current_time_int = int(current_time_string)
	waiting_time_int = int(waiting_time_string)

	hours = current_time_int + waiting_time_int

	timeofday = hours % 24

	print(timeofday)


### Excersise #5
def word_variables():
	

	word1 = "All"
	word2 = "work"
	word3 = "and"
	word4 = "no"
	word5 = "play"
	word6 = "makes"
	word7 = "Jack"
	word8 = "a"
	word9 = "dull"
	word10 = "boy."

	print(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)


### Exercise #7
def interest_formula():

	P = 10000
	n = 12
	r = 0.08

	t = int(input("Compound for how many years?"))

	final = P * ( ( (1+(r/n)) ** (n*t)))

	print('The final amount after ', t, ' years is ', final)
