'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n = int(input())
a = [0] * n
j = 0

for i in range(n):
    temp = int(input())
    if temp != 0:
        a[j], a[i] = temp, a[j]
        j += 1

for i in range(n):
    print(a[i], end=" ")

