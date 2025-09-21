# Зчитування чисел, поки є вхідні дані
import sys

for line in sys.stdin:
    a = float(line)
    # Округлення за правилами: додаємо 0.5 і відкидаємо дробову частину
    print(int(a + 0.5))