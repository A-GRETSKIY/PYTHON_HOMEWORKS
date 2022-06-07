            # 1.Используя словарь, напишите программу, которая выведет на экран
            # название дня недели по его номеру. (1 - «Monday»)

week_day = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
for key in week_day:
    print(key, week_day[key])

            # 2.Представьте описание кота (домашнее животное) на основе словаря

cat = {
    'name': 'Begemot',
    'color': 'black',
    'age': '2',
    'breed': 'Sphynx',
}
print(cat)

            # 3.Напишите программу которая считает строку текста с клавиатуры и
            # выведет на экран статистику, сколько раз какая буква встречается в
            # этой строке. Например, для строки «Hello world» эта статистика
            # выглядит, как: «H» - 1 , «e» - 1, «l» - 3 и т. д.

s = input()
res = {}
for item in s:
    if res.get(item):
        res[item] += 1
    else:
        res[item] = 1
print(res)