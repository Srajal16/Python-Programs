'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it. '''

String = input("Enter a String: ")

String3 = String.lower()
vowels = ('a', 'e', 'i', 'o', 'u')
for i in String3:
    for x in vowels:
        if i == x:
            String3 = String3.replace(x,"")
            # TODO: write code...
print(String3)