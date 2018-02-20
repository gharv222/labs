"""
Practice with functions that do computations with values from paramters.
Some functions also return a value.
Docstrings MUST document parameters and return values.

lab3.py
George Harvey
2/20/2018
"""

def check_fermat(a, b, c, n):
	"""
	Checks validity of Fermat's Last Theorem and returns True
	if Fermat was right, or False otherwise.
	
	Fermat Last Theorem: there are no integers a,b,c, such that 
	a^n + b^n = c^n for any values of n greater 2.	
	a, b, c - integers
	n - integer greater than 2
	Returns: True if the theorem holds, or False otherwise
	"""
	# check if n is greater than 2
	if n <= 2:
		pass
	else: 
		# check if a^n + b^n = c^n
		first = pow(a, n) # set a equal to a^n
		second = pow(b, n) # set b equal to b^n
		result = pow(c, n) # set c equal to c^n
		# conditional to do the checking
		if ((first + second) == result):
			return False
		else:
			return True


		
def is_triangle(a, b, c):
	"""
	Checks if the given values form a triangle.
	
	Triangle theorem: if any of the three lengths is greater
	than the sum of the other two, a triangle cannot be formed.
	Uses 2-branch conditional with OR for violating the theorem
	a, b, c - trhee positive numbers
	Returns: True if the theorem holds, False otherwise
	"""

# conditional to do the checking
	if ((a+b < c) | (c+b < a) | (a+c < b)):
		return False
	else:
		return True