BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

entries = [
    ("F001", 10, 3.5, 8.5, "Morning"),
    ("F002", 8.5, 4.2, 8.7, "Evening")
]

for farmer_id, litres, fat, snf, shift in entries:
    print(farmer_id, litres, fat, snf, shift)
