# Задаем длину списка, наполненного рэндомными числами от 1 до 100.
# Вводим искомое число
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число Х,
# которое мы водим с клавиатуры, либо ввыводит на экран максимально близкое ему по значению

import random

my_list = []
for _ in range(int(input('Введите длину списка: '))):
    my_list.append(random.randint(1, 101))

print(my_list)
number = int(input('Введите искомое число: '))
count = my_list.count(number)
if count < 1:
    nearest_value = my_list[0]
    for i in my_list:
        if abs(i - number) < abs(nearest_value - number):
            nearest_value = i
    print(f'Искомого числа в списке нет. Ближайшее к нему число {nearest_value}')

else:
    print(f'Число {number} встречается {count} раз')
