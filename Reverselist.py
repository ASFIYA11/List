'''Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10
'''
# Input: List elements
elements = input().split()

# Convert elements to integers
elements = [int(i) for i in elements]

# Print the list in reverse order
for element in elements[::-1]:
    print(element, end=" ")
