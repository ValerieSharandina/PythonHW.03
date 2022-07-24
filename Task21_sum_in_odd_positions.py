'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт
сумму элементов списка, стоящих на нечётной позиции.

*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

array = list(map(int, input('Введи необходимое количество чисел: ').split()))


def sum_in_odd_position(numbers_list:list) -> int:
    sum = 0
    for i in range(len(numbers_list)):
        if i %2 ==1:
            sum += numbers_list[i]
    return sum
print(array)
print(f'сумма элементов на нечетной позиции равна {sum_in_odd_position(array)}')