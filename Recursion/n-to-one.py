'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def printName(f,n):
    if(f>n):
      return
    printName(f+1,n)
    print(f)
   

printName(1,3)