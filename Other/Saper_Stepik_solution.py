n, m = [int(x) for x in input().split()]
stars = [(i, j) for i in range(n) for j, c in enumerate(input()) if c == '*']

for i in range(n):
    for j in range(m):
        if (i, j) in stars:
            print('*', end='')
        else:
            print (sum(1 for x in (i-1, i, i+1) for y in (j-1, j, j+1) if (x, y) in stars), end='')
    print()