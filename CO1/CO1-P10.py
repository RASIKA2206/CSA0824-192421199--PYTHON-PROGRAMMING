from decimal import Decimal
from time import perf_counter

def float_total(payments):
    total = 0.0
    for amount in payments:
        total += amount
    return total

def decimal_total(payments):
    total = Decimal("0.00")
    for amount in payments:
        total += Decimal(str(amount))
    return total

for n in [30, 6000, 15000]:
    payments = [33.40] * n

    start = perf_counter()
    f_total = float_total(payments)
    f_time = perf_counter() - start

    start = perf_counter()
    d_total = decimal_total(payments)
    d_time = perf_counter() - start

    print("Payments:", n)
    print("Float total:", f_total)
    print("Decimal total:", d_total)
    print("Float time:", f_time)
    print("Decimal time:", d_time)
    print()
