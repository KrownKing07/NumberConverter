# %%
# constants 
import re


ROMAN = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
        }

# %%
for decimal, roman in ROMAN.items():
    print(f"dezimal: {decimal} <> römisch {roman}")

# %%

# user_number = 4566
user_number = int(input("Gib bitte eine Zahl ein:"))

number = user_number
result = ""

for decimal, roman in ROMAN.items():
    while (number - decimal) >= 0:
        number = number - decimal
        result += roman
        print(number, decimal)
    continue
# das Gleiche:
# result += "test"
# result = result + "test"

print(f"dezimal: {user_number} <> römisch {result}")

# %%
