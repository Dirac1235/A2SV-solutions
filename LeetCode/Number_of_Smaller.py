first = list(map(int, input().split(" ")))

arr1 = list(map(int, input().split(" ")))
arr2 = list(map(int, input().split(" ")))

i = 0
j = 0
count = 0
c = []

while  j < len(arr2):
    if i < len(arr1) and arr1[i] < arr2[j]:
        count += 1
        i += 1
    else:
        if len(c) != 0:
            c.append(c[-1] + count)
        else:
            c.append(count)
        count = 0
        j += 1

print(*c)