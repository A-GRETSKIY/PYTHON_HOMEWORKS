a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(a[0], a[1], a[2], a[3], sep='\n')
s = []
for i in a:
    s.extend(i)
print(sum(s))
