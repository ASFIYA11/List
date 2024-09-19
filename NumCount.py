'''Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3
'''
# Input: List elements
elements = input().split()

# Convert elements to integers
elements = [int(i) for i in elements]

# Input: Value to count
value = int(input())

# Initialize count
count = 0

# Loop through list and count occurrences of value
for element in elements:
    if element == value:
        count += 1

# Output the count
print(count)
