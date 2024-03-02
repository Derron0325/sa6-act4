def exponential_mapping(numbers, n):
    # Use a lambda function and map to raise each number to the power of n
    mapped_numbers = list(map(lambda x: x ** n, numbers))

    return mapped_numbers

# Example usage:
numbers_list = [2, 3, 4, 5]
constant_n = 3

# Map each number to the power of constant_n using the custom lambda function
mapped_result = exponential_mapping(numbers_list, constant_n)

# Print the result
print(f"Exponential Mapping with n={constant_n}:", mapped_result)