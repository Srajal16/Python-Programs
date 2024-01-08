'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
65 -> A  90 -> Z   97 -> a 
'''

s = input("Enter String: ")
print(s)

s = s.title() #initial ko upper case
s = s.split()
string = ""
for i  in s:
    string +=   i[:-1] + i[-1].upper()+" "
print(string)