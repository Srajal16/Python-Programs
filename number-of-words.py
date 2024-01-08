'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

s = input("Enter a String: ")

n = len(s)
count = 0
for i in range(n):
    
    if s[i] == " ":
       count = count + 1

print(count+1)