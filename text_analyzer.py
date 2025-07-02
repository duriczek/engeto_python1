"""

text_analyzer.py: first project in Engeto Online Python Akademy

author: Vojtěch Duraj

email: engeto.0i4o5@passinbox.com

discord: vojtech_duraj

"""

import string

# Dictionary of the registered users and passwords.
users = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"
}

# List of texts to be analyzed.
texts = [
    "There are 7 days in a week, 24 hours in a day, and 365 days in a year. Make them count.",
    
    "End? No, the journey doesn't end here. Death is just another path, one that we all must take. "
    "The grey rain curtain of this world rolls back, and all turns to silver glass, and then you see it. "
    "White shores, and beyond, a far green country under a swift sunrise.",
    
    "Remember, remember, the 5th of November, the Gunpowder Treason and plot; I know of no reason why the Gunpowder Treason should ever be forgot."
]

# User login.
username = input("username:")
password = input("password:")

# Check if the user is registered.
if users.get(username) != password:
    print("Unregistered user, terminating the program...")
    exit()

# Welcome heading.
print("-" * 40)
print(f"Welcome to the app, {username.title()}.")
print(f"We have {len(texts)} texts to be analyzed.")
print("-" * 40)

# Text selection.
choice = int(input(f"Enter a number btw. From 1 to {len(texts)}: "))
print("-" * 40)

# Check if the input is a valid number.
if not choice in range(1, len(texts) + 1):
    print("Invalid selection. Exiting.")
    exit()

# Split the text into a list of words.
chosen_text = texts[int(choice) - 1]
words = chosen_text.split()
stripped_words = [word.strip(string.punctuation) for word in words]

# Count up the different words in the text.
word_count = len(stripped_words)
titlecase_count = sum(1 for word in stripped_words if word.istitle())
uppercase_count = sum(1 for word in stripped_words if word.isupper())
lowercase_count = sum(1 for word in stripped_words if word.islower())
numeric_count = sum(1 for word in stripped_words if word.isnumeric())
numeric_sum = sum(int(word) for word in stripped_words if word.isnumeric())

# Print out the results.
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers is {numeric_sum}.")

# Create a dictionary of word lenghts and occurences.
word_lengths = {}
for word in stripped_words:
    length = len(word)
    word_lengths[length] = word_lengths.get(length, 0) + 1

# Split the dictionary into two lists.
word_lengths = dict(sorted(word_lengths.items()))
lengths = list(word_lengths.keys())
counts = list(word_lengths.values())

# Print out the final "histogram".
# 1st: Let's determine how wide the graph heading should be.
if max(counts) <= 10:
    max_spaces = 1
else:
    max_spaces = max(counts) - 9

print("-" * 40)
print(f"LEN|OCCURENCES{" ":<{max_spaces}}|NR.")
print("-" * 40)

# 2nd: Print out the rest of the graph.
max_spaces += 10

for i in range(len(lengths)):
    length = lengths[i]
    count = counts[i]
    stars = "*" * count
    print(f"{length:3}|{stars:<{max_spaces}}|{count}")
