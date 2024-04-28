# Находим НОД двух чисел с помощью алгоритма Евклида.
def find_nod(x, y):
    while y:
        x, y = y, x % y
    return x

def find_common_divisors(numbers):
    if not numbers:
        return []

    # Начинаем с НОД первого элемента
    common_nod = numbers[0]
    
    # Вычисляем НОД для всего списка чисел
    for num in numbers[1:]:
        common_nod = find_nod(common_nod, num)
        if common_nod == 1:  # Если НОД становится 1, дальше проверять не имеет смысла
            return [1]

    # Теперь находим все делители найденного НОД
    divisors = []
    for i in range(1, int(common_nod**0.5) + 1):
        if common_nod % i == 0:
            divisors.append(i)
            if i != common_nod // i:
                divisors.append(common_nod // i)
    return sorted(divisors)


user_input = input("Введите массив чисел через пробел: ")
numbers = list(map(int, user_input.split()))
print(find_common_divisors(numbers))
