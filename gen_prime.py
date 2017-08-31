#!/usr/bin/env python
from math import sqrt

a = int(raw_input(""))
limit_low, limit_high = [], []
for i in range(a):
    limit = raw_input("")
    b, c = limit.split(" ")
    limit_low.append(int(b))
    limit_high.append(int(c))

maxim = max(limit_high)
j = 3
arr = [2]
while j <= maxim:
    for k in arr:
        if (j%k == 0):
            break
        if (k == arr[-1]):
            arr.append(j)
        continue
    j = j + 1
for i in range(a):
    index = 0
    length = len(arr)
    for j in range(length):
        if arr[j] >= limit_low[i]:
            index = j
            break
    while (index < length):
        if arr[index] >= limit_high[i]:
            break
        print arr[index]
        index = index + 1
    print ""
