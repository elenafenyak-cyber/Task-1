# Константи для переведення
FOOT_TO_CM = 30.48
INCH_TO_CM = 2.54

# Ввід даних
feet = int(input("Feet: "))
inches = int(input("Inches: "))

# Обчислення
height_cm = feet * FOOT_TO_CM + inches * INCH_TO_CM

# Вивід результату (ціле число)
print("Your height is:", int(height_cm), "cm.")