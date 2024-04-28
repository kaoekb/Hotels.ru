def min_experiments(n, k):
    # Таблица для сохранения результатов подзадач
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Базовые случаи
    for i in range(1, n + 1):
        dp[i][1] = i  # Если есть только один предмет, нужно проверить каждый этаж.
    
    for j in range(1, k + 1):
        dp[1][j] = 1  # Если только один этаж, нужен один тест.
    
    # Заполнение таблицы для всех этажей и всех предметов
    for j in range(2, k + 1):
        for i in range(2, n + 1):
            dp[i][j] = i  # Максимальное количество бросков в худшем случае
            for x in range(1, i):
                # Выбираем оптимальное разбиение
                worst = 1 + max(dp[x - 1][j - 1], dp[i - x][j])
                dp[i][j] = min(dp[i][j], worst)
    
    return dp[n][k]

print(min_experiments(5000, 2))


