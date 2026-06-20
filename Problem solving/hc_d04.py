'''
Let's learn about list comprehensions! You are given three integers x, y and z
representing the dimensions of a cuboid along with an integer n. Print a list of all possible
coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n.
Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. Please use list comprehensions rather than
multiple loops, as a learning exercise.

Input Format
Four integers x, y, z and n, each on a separate line.

Constraints
Print the list in lexicographic increasing order.

Sample Input 0
1
1
1
2

Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Sample Input 1
2
2
2
2

Sample Output 1
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
''' 

'''
   This solution uses a nested for-loop with a conditional if-statement to solve the puzzle. 
   While this approach works and is highly readable, 
   the problem requires using a list comprehension to achieve a more concise syntax and 
   a faster, optimized execution at the C-level.
'''
if __name__ == '__main__':
    
    a = []
    
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    a.append([i, j, k])
    print(a)
    
'''
List Comprehension solution
'''
if __name__ == '__main__':
    
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    a = [
        [i, j, k]
        for i in range(x+1)
        for j in range(y+1)
        for k in range(z+1)
        if i+j+k != n
    ]
    
    print(a)