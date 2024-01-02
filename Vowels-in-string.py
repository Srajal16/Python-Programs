'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it. '''

String = input("Enter a String: ")
count = 0
String = String.lower()
for m in String:
    if m == 'a' or m == 'e' or m == 'i' or m == 'o' or m == 'u':
       count = count + 1 
       
if count == 0 :
    print("No vowles found")
else :
    print("vowles found", count)