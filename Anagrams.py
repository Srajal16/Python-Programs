'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
a = input("Enter String 1: ")
b = input("Enter String 2: ")


if(sorted(a) == sorted(b)):
    print("Strings are anagram")
else:
    print("They are not anagram")
