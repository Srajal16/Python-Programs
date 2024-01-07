'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
s = input("Enter String : ")

alphabets = digits = special = vowel = consonant = 0


for i in range(len(s)):
    if(s[i].isalpha()):
        alphabets = alphabets + 1
    elif(s[i].isdigit()):
        digits = digits + 1

    else:
        special = special + 1
        
    if(s[i] in ('a','e','i','o','u')):
        vowel = vowel + 1
    
    elif(s[i]>='a' and s[i]<='z'):
        consonant = consonant + 1
        
        
        
        
print("alphabets",alphabets)
print("digits",digits)
print("special",special)
print("vowel",vowel)
print("consonant",consonant)