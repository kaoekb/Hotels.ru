def print_multiplication_table():    
    # Выводим заголовки для столбцов
    print("   ", end="")
    for i in range(1, n + 1):
        print(f"{i:4}", end="")
    print()  # Переход на новую строку после заголовков

    # Выводим строки таблицы умножения
    for i in range(1, n + 1):
        # Вывод номера строки
        print(f"{i:2}", end="")
        for j in range(1, n + 1):
            # Вывод произведения чисел
            print(f"{i * j:4}", end="")
        print()  # Переход на новую строку после каждой строки таблицы


n = int(input("Введите максимальное число для таблицы умножения: "))
print_multiplication_table()
