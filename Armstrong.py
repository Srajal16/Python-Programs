'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
low, high = 10, 10000

for n in range(low, high + 1):

    # order of number
    order = len(str(n))

    # initialize sum
    sum = 0

    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if n == sum:
        print(n, end=", ")
