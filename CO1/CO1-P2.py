from decimal import Decimal

print(type(10))
print(type(10.0))
print(type("10"))
print(type(True))
print(type([10, 8.5]))

print(7 / 2)
print(7 // 2)
print(7 % 2)

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

items = ["33.40", "0.10", "0.10", "0.10"]

total_float = 0.0
for x in items:
    total_float += float(x)

total_decimal = Decimal("0.00")
for x in items:
    total_decimal += Decimal(x)

print("Float:", total_float)
print("Decimal:", total_decimal)
