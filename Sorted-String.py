'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
a = input("Enter String : ")
b = a.lower()
lst = list(b)
print("Sorted String: ")
lst.sort()
for i in lst:
    print(i, end="")



