price = float(input("Введіть ціну товару: "))
discount = float(input ("Введіть знижку (у вигляді десяткового дробу): "))

final_price = price * (1 - discount)
print(final_price)