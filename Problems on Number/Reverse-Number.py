'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
num = 1234
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)
