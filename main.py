s = input()
res = {}
for item in s:
    if res.get(item):
        res[item] += 1
    else:
        res[item] = 1
print(res)




