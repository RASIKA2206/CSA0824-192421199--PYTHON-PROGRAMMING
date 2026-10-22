def rate_per_litre(fat, snf):
    if not 2.0 <= fat <= 7.0:
        raise ValueError("Invalid fat")
    if snf < 0:
        raise ValueError("Invalid SNF")

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = 30 + fat_steps * 0.40
    rate += snf_steps * 0.30

    return round(rate, 2)

def payout(litres, fat, snf):
    if litres < 0:
        raise ValueError("Invalid quantity")
    return round(litres * rate_per_litre(fat, snf), 2)

assert payout(10, 3.5, 8.5) == 300.00
assert payout(8.5, 4.2, 8.7) == 283.90

assert rate_per_litre(2.0, 8.5) == 24.00
assert rate_per_litre(7.0, 8.5) == 44.00

try:
    payout(-5, 3.5, 8.5)
except ValueError:
    print("Negative quantity: PASS")

try:
    payout(10, 8.0, 8.5)
except ValueError:
    print("Fat range: PASS")

print("All tests passed")
