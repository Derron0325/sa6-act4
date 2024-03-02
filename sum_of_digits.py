# Import lambda function from functools module
from functools import reduce

# Lambda function to compute the sum of digits
sum_of_digits = lambda x: reduce(lambda a, b: int(a) + int(b), str(x))

# Example usage
number = 12345
result = sum_of_digits(number)
print(f"The sum of digits in {number} is: {result}")