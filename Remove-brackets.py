'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
65 -> A  90 -> Z   97 -> a 
'''

Exp = "(a-b)+[c*d]+{e/f}"

Exp2 = ""


for i in Exp:
    if ord(i) == 41 or ord(i) == 40 or ord(i) == 91 or ord(i) == 93 or ord(i) == 123 or ord(i) == 125:
        # TODO: write code...
        pass
    else:
        Exp2 = Exp2 + i
print(Exp2)