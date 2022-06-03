name = input('Name: ')
res = 'Correct' if name.istitle() and name.isalpha() else 'Incorrect'
print(res)