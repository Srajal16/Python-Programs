'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
s = input("Enter String : ")

t = s.count(" ")

for i in range(t):
    s = s.replace(" ","")
    
print(s)



