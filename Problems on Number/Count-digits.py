'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Iterative Python program to count 
# number of digits in a number 


def countDigit(n): 
	count = 0
	while n != 0: 
		n //= 10
		count += 1
	return count 


# Driver Code 
n = 345289467
print("Number of digits : % d" % (countDigit(n))) 


