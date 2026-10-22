entries = [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3)
]

total = 0

for litres, fat, snf in entries:
    if litres < 0 or fat < 2 or fat > 7 or snf < 0:
        print("Invalid entry")
        continue

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = 30 + fat_steps * 0.40
    rate += snf_steps * 0.30

    payment = round(litres * rate, 2)
    total += payment

    print("Payment:", payment)

print("Ten-day total:", round(total, 2))
