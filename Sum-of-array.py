'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

array = []
n = int(input("Enter Size: "))
for i in range (n):
    elements = int(input("Enter number of elements: "))
    array.append(elements)
print(array)

sum = 0
for i in range(n):
    sum = sum + array[i]
print(sum)