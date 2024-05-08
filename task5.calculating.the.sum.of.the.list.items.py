#. Вычисление суммы элементов списка:
#Программа вычисляет и выводит сумму всех элементов списка, который вводит пользователь.

list1 = []

for i in range(1, 6):
    numbers = int(input('ваше число'))

    list1.append(numbers)

summa = sum(list1)

print(summa)




