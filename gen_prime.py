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
while j <= int(maxim):
    for k in arr:
        if (j%k == 0):
            break
        if (k == arr[-1]):
            arr.append(j)
        continue
    j = j + 1
for i in range(a):
    for j in range(len(arr)):
        if (arr[j] >= limit_low[i] and arr[j] <= limit_high[i]):
            print arr[j]
    print ""
