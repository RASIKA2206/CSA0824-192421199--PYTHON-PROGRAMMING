from decimal import Decimal, ROUND_HALF_UP
STANDARD_FAT = Decimal("3.50")
STANDARD_SNF = Decimal("8.50")
STEP = Decimal("0.10")
REGULAR_BASE = Decimal("30.00")
REGULAR_FAT_STEP = Decimal("0.40")
SEASONAL_BASE = Decimal("32.00")
SEASONAL_FAT_STEP = Decimal("0.45")
SNF_STEP_VALUE = Decimal("0.30")
BONUS_RATE = Decimal("0.50")
BONUS_LIMIT = Decimal("500.00")
def round_step(value):
    return (value / STEP).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP)
def rate_per_litre(fat, snf, season="regular"):
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))
    if not Decimal("2.00") <= fat <= Decimal("7.00"):
        raise ValueError("Invalid fat")
    if snf < 0:
        raise ValueError("Invalid SNF")
    fat_steps = round_step(fat - STANDARD_FAT)
    snf_steps = round_step(snf - STANDARD_SNF)
    if season == "april_june":
        base = SEASONAL_BASE
        fat_value = SEASONAL_FAT_STEP
    else:
        base = REGULAR_BASE
        fat_value = REGULAR_FAT_STEP
    rate = base + fat_steps * fat_value
    rate += snf_steps * SNF_STEP_VALUE
    return rate.quantize(Decimal("0.01"))
def payout(litres, fat, snf, season):
    litres = Decimal(str(litres))
    if litres < 0:
        raise ValueError("Invalid quantity")
    return (litres * rate_per_litre(fat, snf, season)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP)
def ten_day_total(entries, season):
    total_litres = Decimal("0.00")
    base_payment = Decimal("0.00")
    for litres, fat, snf in entries:
        total_litres += Decimal(str(litres))
        base_payment += payout(litres, fat, snf, season)
    if total_litres > BONUS_LIMIT:
        bonus = (total_litres * BONUS_RATE).quantize(Decimal("0.01"))
    else:
        bonus = Decimal("0.00")
    final_payment = base_payment + bonus
    return total_litres, base_payment, bonus, final_payment
entries = [
    ("300.00", "4.25", "8.65"),
    ("250.00", "3.55", "8.50")
]
quantity, base, bonus, final = ten_day_total(
    entries, "april_june")
print("Total litres:", quantity)
print("Base payment:", base)
print("Bonus:", bonus)
print("Final payment:", final)
