cash = int(input())
sum = 0
for i in [100, 20, 10, 5, 1]:
    sum += cash // i
    cash = cash % i
print(sum)