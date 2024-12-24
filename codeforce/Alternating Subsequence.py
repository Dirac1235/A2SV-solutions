tc = int(input())
for _ in range(tc):
  arrlen = int(input())
  arr = list(map(int, input().split()))
  res = []
  for i in arr:
    if res:
      if res[-1] > 0 and i > 0 and res[-1] < i:
        res[-1] = i
      elif res[-1] < 0 and i < 0 and res[-1] < i:
       res[-1] = i
      elif res[-1] > 0 and i < 0 or res[-1] < 0 and i > 0:
       res.append(i)
    else:
      res.append(i)
  print(sum(res))
