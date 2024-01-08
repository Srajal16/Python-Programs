def change_to_next_lexicographic(input_string):
    result = ""

    for char in input_string:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        else:
            result += char

    return result

# Input string from the user
user_input = input("Enter a string: ")

# Change every letter to the next lexicographic alphabet
result_string = change_to_next_lexicographic(user_input)

# Display the result
print("Result:", result_string)
