'''Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
Sample Input: 
5
2
4
1
3
1
Sample Output:
11
'''
# Read the size of the array
size = int(input("Enter the size of the array: "))

# Initialize an empty list to store the elements
elements = []

# Read the elements of the array
for _ in range(size):
    element = int(input())
    elements.append(element)

# Calculate the sum of the elements
total_sum = sum(elements)

# Print the sum of the elements
print(total_sum)
