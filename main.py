x = int(input('Year: '))
if not x % 4 or x % 100 and not x % 400:
    print('Год высокостный')
else:
    print('Год не высокостный')
