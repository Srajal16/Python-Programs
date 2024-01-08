'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def remove_chars(str1, str2):
    result = ""
    
    for char in str1:
        if char not in str2:
            result += char
    
    return result

# Input strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Remove characters from string1 using characters in string2
result_string = remove_chars(string1, string2)

# Display the result
print("Result:", result_string)



