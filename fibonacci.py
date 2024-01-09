'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def fibonacciSeries(i):
    if i<=1:
        return i
    else:
        return (fibonacciSeries(i-1)+fibonacciSeries(i-2))

n = int(input("Please enter a number: "))
if n<=0:
    print("Enter a positive number: ")
else:
    print("Series: ")
    for i in range(n):
        print(fibonacciSeries(i), end=" ")
