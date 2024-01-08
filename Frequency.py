'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
65 -> A  90 -> Z   97 -> a 
'''

s = input("Enter String: ")
 
for i in s:
    frequency = s.count(i)
    print(str(i)+ ": "+str(frequency),end=", ")