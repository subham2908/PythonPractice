# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.

set1 = {1, 2, 3, 4, 5, 5}
print(set1)  # Output: {1, 2, 3, 4, 5}

# Creating a set with mixed data types
set2 = {1, "hello", 3.14, (1, 2)}
print(set2)  # Output: {1, 'hello', 3.14, (1, 2)}

# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()

set1 = {1, 2, 3}
set1.add(4)
print(set1)  # Output: {1, 2, 3, 4}


set1 = {1, 2, 3, 4}

# Remove an element, raises KeyError if the element is not found
set1.remove(3)
print(set1)  # Output: {1, 2, 4}

# Discard an element, does not raise an error if the element is not found
set1.discard(5)  # No error
print(set1)  # Output: {1, 2, 4}

# Remove an arbitrary element and return it
removed_element = set1.pop()
print(removed_element)  # Output: 1 (or another element, since sets are unordered)
print(set1)  # Output: {2, 4}

# Clear all elements from the set
set1.clear()
print(set1)  # Output: set()


# doing union on a set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}


# doing intersection on a set
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection_set = set1 & set2  # or set1.intersection(set2)
print(intersection_set)  # Output: {2, 3}

#Difference on a set
set1 = {1, 2, 3}
set2 = {2, 3, 4}
difference_set = set1 - set2  # or set1.difference(set2)
print(difference_set)  # Output: {1}

#Symmeteric Difference on a set
set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 5}
symmetric_difference_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 4}

# Checking Subset and Superset

set1 = {1, 2, 3}
set2 = {1, 2}
set3 = {1, 2, 3, 4}

print(set2.issubset(set1))  # Output: True
print(set1.issuperset(set2))  # Output: True
print(set1.issubset(set3))  # Output: True
print(set3.issuperset(set1))  # Output: True
print(set2.issuperset(set3)) #Output: False



# Disjoint Sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}

print(set1.isdisjoint(set2))  # Output: True
print(set1.isdisjoint(set3))  # Output: False


# Removing Duplicates from a List


list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(list_with_duplicates))
print(unique_list)  # Output: [1, 2, 3, 4, 5]


# Set Comprehensions

# Create a set of squares for numbers from 0 to 9
squares_set = {x**2 for x in range(10)}
print(type(squares_set))
print(squares_set)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}  can give output in any sequence


# Use of Set data types
'''
When dealing with large datasets where you need to ensure uniqueness and perform frequent membership tests, 
sets are more efficient than lists or tuples.

Summary

    Eliminating duplicates: Automatically handles duplicate elements.
    Membership testing: Efficient O(1) average time complexity.
    Mathematical set operations: Clean and efficient union, intersection, difference, etc.
    Large data collections: More efficient than lists for uniqueness and membership testing.
    Graph algorithms: Useful for tracking visited nodes and other operations.
    Data aggregation: Ensures unique items from multiple sources.
    Counting distinct elements: Easy way to count unique items.
    Immutable collections: Use frozenset for immutable sets.
    
'''

# Removing duplicates from a list
data = [1, 2, 2, 3, 4, 4, 5]
unique_data = list(set(data))
print(unique_data)  # Output: [1, 2, 3, 4, 5]



# Efficient membership testing
my_set = {'apple', 'banana', 'cherry'}
print('banana' in my_set)  # Output: True
print('grape' in my_set)   # Output: False



# Counting distinct elements
data = [1, 2, 2, 3, 4, 4, 5]
distinct_count = len(set(data))
print(distinct_count)  # Output: 5


# Sorting

# Define a set of integers
my_set = {5, 3, 1, 4, 2}

# Convert the set to a list and sort it
sorted_list = sorted(my_set)
print(sorted_list)  # Output: [1, 2, 3, 4, 5]

#===================================================================================

# Define a set of strings
my_set = {"banana", "apple", "cherry", "date"}

# Convert the set to a list and sort it
sorted_list = sorted(my_set)
print(sorted_list)  # Output: ['apple', 'banana', 'cherry', 'date']

#====================================================================================
#sorting based on custom key

# Define a set of strings
my_set = {"banana", "apple", "cherry", "date"}

# Convert the set to a list and sort it by the length of each string
sorted_list = sorted(my_set, key=len)
print(sorted_list)  # Output: ['date', 'apple', 'banana', 'cherry']

#====================================================================================
#Sorting set of tuple


# Define a set of tuples
my_set = {(1, 'apple'), (3, 'banana'), (2, 'cherry')}

# Convert the set to a list and sort it by the first element of each tuple
sorted_list = sorted(my_set, key=lambda x: x[0])
print(sorted_list)  # Output: [(1, 'apple'), (2, 'cherry'), (3, 'banana')]

# Sort it by the second element of each tuple
sorted_list_by_second = sorted(my_set, key=lambda x: x[1])
print(sorted_list_by_second)  # Output: [(1, 'apple'), (3, 'banana'), (2, 'cherry')]


#====================================================================================
# Define a set of integers
my_set = {5, 3, 1, 4, 2}

# Convert the set to a list, sort it, and convert it back to a set
sorted_list = sorted(my_set)
sorted_set = set(sorted_list)
print(sorted_set)  # Output: {1, 2, 3, 4, 5} (order is not guaranteed)

#==============================================================================
# Sorting in descending order

# Define a set of integers
my_set = {5, 3, 1, 4, 2}

# Convert the set to a list and sort it in descending order
sorted_list_desc = sorted(my_set, reverse=True)
print(sorted_list_desc)  # Output: [5, 4, 3, 2, 1]