from datetime import datetime

birth_date = input("Enter your birthdate (DD/MM/YYYY): ")

day, month, year = map(int, birth_date.split("/"))

current_year = datetime.now().year
age = current_year - year

candles = age % 10

def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def print_cake(candle_count):
    candles_str = "i" * candle_count
    print(f"      --{candles_str}--")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("    -----------------\n")

if is_leap_year(year):
    print("It's a leap year! 🎉 Two cakes for you!\n")
    print_cake(candles)
    print_cake(candles)
else:
    print_cake(candles)
