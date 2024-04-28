# Проверка числа на простоту
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Возвращает список простых чисел в заданном диапазоне
def prime_numbers_in_range(min_num, max_num):
    primes = []
    for num in range(min_num, max_num + 1):
        if is_prime(num):
            primes.append(num)
    return primes


min_val = int(input("Введите минимальное число диапазона: "))
max_val = int(input("Введите максимальное число диапазона: "))

if min_val > max_val:
    print("Минимальное значение должно быть меньше или равно максимальному.")
else:
    # Вывод простых чисел в заданном диапазоне
    prime_numbers = prime_numbers_in_range(min_val, max_val)
    print(f"Простые числа в диапазоне от {min_val} до {max_val}: {prime_numbers}")
