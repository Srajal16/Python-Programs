'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''




# Define a function to find the smallest and second-smallest elements in an array
def find_smallest_and_second_smallest(arr):
    # Check if the array has at least two elements
    if len(arr) < 2:
        return "Array should have at least two elements."

    # Initialize variables to hold the smallest and second-smallest values
    smallest = float('inf')  # 'inf' represents infinity, initially set to a large value
    second_smallest = float('inf')

    # Iterate through each number in the array
    for num in arr:
        # Check if the current number is smaller than the current smallest
        if num < smallest:
            # If true, update the second_smallest and smallest values
            second_smallest = smallest
            smallest = num
        # Check if the current number is smaller than the current second_smallest
        elif num < second_smallest and num != smallest:
            # If true, update the second_smallest value
            second_smallest = num

    # Return the smallest and second-smallest values
    return smallest, second_smallest

# Example usage
# Create an array of numbers
my_array = [4, 2, 7, 1, 3, 9, 5, 8]
# Call the function to find the smallest and second-smallest values
smallest_value, second_smallest_value = find_smallest_and_second_smallest(my_array)

# Print the results
print(f"Smallest: {smallest_value}")
print(f"Second Smallest: {second_smallest_value}")
