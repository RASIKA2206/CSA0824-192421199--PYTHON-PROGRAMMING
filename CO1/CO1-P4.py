litres = 8.5
fat = 4.2
snf = 8.7

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)

rate = 30 + fat_steps * 0.40
rate += snf_steps * 0.30

amount = round(litres * rate, 2)

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate:", rate)
print("Amount:", amount)

print((4.2 - 3.5) / 0.1)
print(round((4.2 - 3.5) / 0.1))
