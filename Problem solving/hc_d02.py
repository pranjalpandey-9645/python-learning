'''
The provided code stub reads an integer, n, from STDIN. 
For all non-negative integers i<n, print i^2.

Input

5

then output

0
1
4
9
16
'''

if __name__ == "__main__":

    n = int(input())

    print("--------------")
    
    for i in range(n):
        print(i**2)