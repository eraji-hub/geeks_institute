3 <= 3 < 9
3 == 3 == 3
bool(0)
bool(5 == "5")
bool(4 == 4) == bool("4" == "4")
bool(bool(None))

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


# --- IGNORE ---

longest_sentence = ""

print("Try to enter the longest sentence you can WITHOUT the letter 'A'.")
print("Type 'quit' to exit.\n")

while True:
    user_input = input("Enter your sentence: ")
    
    if user_input.lower() == "quit":
        print("\nThanks for playing!")
        break

    if "a" in user_input.lower():
        print("Oops! Your sentence contains the letter 'A'. Try again.\n")
        continue

    if len(user_input) > len(longest_sentence):
        longest_sentence = user_input
        print("🎉 Congratulations! This is the new longest sentence without 'A'.\n")
    else:
        print("Your sentence is valid but not longer than the current longest. Try again.\n")

if longest_sentence:
    print("The longest sentence you entered without 'A' is:")
    print(longest_sentence)
