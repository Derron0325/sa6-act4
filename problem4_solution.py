def find_intersection(list1, list2):
    # Use a lambda function and filter to find the intersection
    intersection = list(filter(lambda x: x in list2, list1))

    return intersection

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Find the intersection using the custom lambda function
intersection_result = find_intersection(list1, list2)

print("Intersection of Lists:", intersection_result)