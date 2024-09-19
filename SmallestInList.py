'''Write a Python Program to find the smallest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
1
'''
# Read the size of the list
size = int(input("Enter the size of the list: "))

# Initialize an empty list to store the elements
elements = []

# Read the elements of the list
for _ in range(size):
    element = int(input())
    elements.append(element)

# Find the smallest element in the list
smallest_element = min(elements)

# Print the smallest element
print(smallest_element)


