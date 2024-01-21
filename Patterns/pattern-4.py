'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

for i in range(1,5):
    for j in range(1,5):
        if(j<=5-i):
            print("*",end='')
        else:
            print(" ",end='')
    print()