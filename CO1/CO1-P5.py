litres_text = input("Enter litres: ")
fat_text = input("Enter fat: ")
snf_text = input("Enter SNF: ")

try:
    litres = float(litres_text)
    fat = float(fat_text)
    snf = float(snf_text)

    if litres < 0:
        print("Invalid quantity")
    elif fat < 2.0 or fat > 7.0:
        print("Invalid fat")
    elif snf < 0:
        print("Invalid SNF")
    else:
        fat_steps = round((fat - 3.5) / 0.1)
        snf_steps = round((snf - 8.5) / 0.1)

        rate = 30 + fat_steps * 0.40
        rate += snf_steps * 0.30

        amount = litres * rate

        print(f"Rate: Rs. {rate:.2f}")
        print(f"Amount: Rs. {amount:.2f}")

except ValueError:
    print("Invalid numeric input")
