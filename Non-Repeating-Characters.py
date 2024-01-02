'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it. '''

String = input("Enter a String: ")

for i in String:
    count = 0
    for j in String:
        if i == j:
            count = count +1 
        if count > 1:
            break
 
    if count ==1:
       print(i, end="")
            # TODO: write code...