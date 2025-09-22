#Exercise 1: Cars
cars_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars_list = cars_str.split(", ")
print(f"There are {len(cars_list)} companies in the list.")
print("Companies in reverse order (Z-A):")
print(sorted(cars_list, reverse=True))
with_o = [car for car in cars_list if "o" in car.lower()]
print(f"Number of companies with 'o': {len(with_o)}")
without_i = [car for car in cars_list if "i" not in car.lower()]
print(f"Number of companies without 'i': {len(without_i)}")
cars_with_dupes = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
unique_cars = list(set(cars_with_dupes))  
print(f"Unique companies: {', '.join(unique_cars)}")
print(f"Now there are {len(unique_cars)} unique companies.")
asc_reversed = [car[::-1] for car in sorted(unique_cars)]
print("Companies in A-Z order but reversed letters:")
print(asc_reversed)

#Exercise 2: What’s your name?

def get_full_name(first_name, last_name, middle_name=""):
    if middle_name:  
        full_name = f"{first_name} {middle_name} {last_name}"
    else:  
        full_name = f"{first_name} {last_name}"
    return full_name.title()
print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))  

print(get_full_name(first_name="bruce", last_name="lee"))  

#Exercise 3: From English to Morse

MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
    " ": "/"  
}

def english_to_morse(text):
    text = text.upper()
    return " ".join(MORSE_CODE_DICT[char] for char in text if char in MORSE_CODE_DICT)
def morse_to_english(morse_code):
    reverse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    words = morse_code.split(" / ")  
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_word = "".join(reverse_dict[letter] for letter in letters)
        decoded_words.append(decoded_word)
    return " ".join(decoded_words)
print(english_to_morse("ayoub eraji"))  
print(morse_to_english(".- -.-- --- ..- -... / . .-. .- .--- .."))  



