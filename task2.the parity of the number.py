number = int(input("Введите число, чтобы я определил ваше число четное или нет: "))

if number == 0:
    print("Ваше число нулевое!")
elif number % 2 == 0:
    print("Ваше число четное")
else:
    print("Ваше число не четное")
