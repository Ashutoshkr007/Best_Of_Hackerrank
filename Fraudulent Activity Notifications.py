def activityNotifications(expenditure, d):
    counting = 0
    b = [0]*201
    mid = None
    left = None
    median = d//2
    if d%2 == 0:
        mid = median-1
    for i in range(0, d):
        b[expenditure[i]] += 1
    k = 0

    for i in range(len(expenditure)-d):
        if d%2 == 0:
            left = 0
        count = 0
        value = 0
        slid = d+k
        while count <= median:
            if d%2 == 0:
                if count <= mid:
                    left += 1
            count += b[value]
            value += 1
        if d%2 == 0:
            if expenditure[slid] >= (value + left -2):
                counting += 1
        else:
            if expenditure[slid] >= 2*(value-1):
                counting += 1
        b[expenditure[i]] -= 1
        b[expenditure[slid]] += 1
        k += 1
    return counting


nd = input().split()

n = int(nd[0])

d = int(nd[1])

expenditure = list(map(int, input().rstrip().split()))

result = activityNotifications(expenditure, d)
print(result)
