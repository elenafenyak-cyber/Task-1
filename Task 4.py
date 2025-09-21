# Ввід даних
n = int(input())
k = int(input())

# Відрізаємо k останніх цифр (ділення націло)
result = n // (10 ** k)

# Вивід результату
print(result)