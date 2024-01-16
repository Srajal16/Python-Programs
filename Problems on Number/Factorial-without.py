'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Python3 program for the above approach

# Function to calculate factorial of the number
# without using multiplication operator


def factorialWithoutMul(N):

	# Variable to store the final factorial
	ans = N

	# Outer loop
	i = N - 1

	while (i > 0):
		sum = 0

		# Inner loop
		for j in range(i):
			sum += ans

		ans = sum
		i -= 1

	return ans


# Driver code
if __name__ == '__main__':

	# Input
	N = 3

	# Function calling
	print(factorialWithoutMul(N))

# This code is contributed by SURENDRA_GANGWAR


