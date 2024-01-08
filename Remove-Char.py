'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
65 -> A  90 -> Z   97 -> a 
'''

String1 = "#Justice!For@Chutki123"
String2 = ""
for i in String1:
    if(ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        String2 = String2+i
        
print(String2)
print(chr(97))