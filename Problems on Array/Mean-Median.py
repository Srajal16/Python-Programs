'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''




a = []
n = int(input("Enter Size: "))
for i in range (n):
    elements = int(input("Enter number of elements: "))
    a.append(elements)


sum = 0
for i in range(n):
    sum = sum + a[i]
mean = sum/n
if n%2 == 0:
    print(int(a[n/2]+a[(n/2)+1])/2)
else:
    print(a[(n/2)+1])
print("Mean: ",mean)