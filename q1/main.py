def comp(n):
    last = n % 10
    last_two = n % 100

    if last == 1 and last_two != 11:
        return f"{n} компьютер"
    elif last in (2, 3, 4) and last_two not in (12, 13, 14):
        return f"{n} компьютера"
    else:
        return f"{n} компьютеров"


user_input = input("Сколько компьютеров? ")
number = int(user_input)
print(comp(number))
