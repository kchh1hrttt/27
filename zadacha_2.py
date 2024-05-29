while True:
    try:
        n = int(input("Введіть натуральне число (більше 0): "))
        if n > 0:
            break
        else:
            print("Помилка: Введене число не є натуральним.")
    except ValueError:
        print("Помилка: Введіть ціле число.")

for i in range(1, n + 1):
    print(i)
