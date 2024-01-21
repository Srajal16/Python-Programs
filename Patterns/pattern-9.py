'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

for i in range(1,6):
    k=6-i
    for j in range(1,6):
        if(j<=6-i):
            print(k,end='')
            k=k-1
        else:
            print(" ",end='')
    print()        