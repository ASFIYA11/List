'''Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
'''
# Input: List elements
elements = input().split()

# Convert elements to integers
elements = [int(i) for i in elements]

# Sort the list
elements.sort()

# Print the sorted list
for element in elements:
    print(element, end=" ")
