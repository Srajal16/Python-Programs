'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
65 -> A  90 -> Z   97 -> a 
'''

def maximum_occurring_character(input_string):
    max_char = ""
    max_count = 0

    for i in range(len(input_string)):
        count = 0
        for j in range(len(input_string)):
            if input_string[i] == input_string[j]:
                count += 1

        if count > max_count:
            max_count = count
            max_char = input_string[i]

    return max_char

# Example usage:
input_string = "programming"
result = maximum_occurring_character(input_string)
print(f"The maximum occurring character in '{input_string}' is: {result}")
