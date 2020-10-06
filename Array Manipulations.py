def arrayManipulation(n, q):
    a = [0 for i in range(n)]
    for i in range(len(q)):
        minl = q[i][0]-1
        maxl = q[i][1]
        if maxl < n:
            a[maxl] -= q[i][2]
        a[minl] += q[i][2]
    sum1 = 0
    max1 = -1024
    for i in a:
        sum1 += i
        if sum1 > max1:
            max1 = sum1
    return max1

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)