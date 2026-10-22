from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.50")
STANDARD_SNF = Decimal("8.50")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

def rate_per_litre(fat, snf):
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    if not Decimal("2.00") <= fat <= Decimal("7.00"):
        raise ValueError("Invalid fat")
    if snf < 0:
        raise ValueError("Invalid SNF")

    fat_steps = ((fat - STANDARD_FAT) / Decimal("0.10")).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - STANDARD_SNF) / Decimal("0.10")).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE
    rate += snf_steps * SNF_STEP_VALUE
    return rate.quantize(Decimal("0.01"))

def payout(litres, fat, snf):
    litres = Decimal(str(litres))
    if litres < 0:
        raise ValueError("Invalid quantity")

    amount = litres * rate_per_litre(fat, snf)
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print("Rate:", rate_per_litre("4.2", "8.7"))
print("Payment:", payout("8.5", "4.2", "8.7"))
