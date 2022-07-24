'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
arr = list(map(int, input('Введи числа: ').split()))
prod = 0
print(f'Исходный массив: {arr}')

for i in range(int(len(arr) / 2)):
    prod = arr[i] * arr[len(arr) - i - 1]
    print(prod)
if len(arr) % 2 == 1:
    print(arr[int(len(arr) / 2)]*arr[int(len(arr) / 2)])



