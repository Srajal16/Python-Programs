'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n = int(input("Enter a Number: "))
l = list()
while n!= 0:
    r = n%2
    l.append(r)
    n = n//2
l.reverse()
for ele in l:
    print(ele, end="")
print(7%2)  #remainder
print(7//2) #kitni bar ja rha hai
