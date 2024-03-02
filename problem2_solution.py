# Sample list of strings
string_list = ["apple", "banana", "kiwi", "orange", "grape", "pear", "fig"]

# Use a lambda function to define custom sort order
custom_sort = lambda s: (len(s), s)

# Sort the list using the custom sort order
sorted_list = sorted(string_list, key=custom_sort)

# Print the sorted list
print("Sorted List:", sorted_list)