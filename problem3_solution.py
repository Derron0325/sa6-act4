def find_maximum(numbers, comparison_lambda):
    maximum = numbers[0]

    for num in numbers:
        maximum = comparison_lambda(maximum, num)

    return maximum

# Example usage:
numbers_list = [4, 8, 2, 10, 5, 7]

# Define a lambda function to compare two numbers and return the greater one
compare_lambda = lambda x, y: x if x > y else y

max_number = find_maximum(numbers_list, compare_lambda)

print("Maximum Number:", max_number)