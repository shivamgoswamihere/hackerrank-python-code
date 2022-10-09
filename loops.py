"""
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i^2.
"""

#Solution

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i*i,end='\n')
        