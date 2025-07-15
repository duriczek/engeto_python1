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
texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# User login.
username = input("username: ")
password = input("password: ")

# Check if the user is registered.
if users.get(username.strip()) != password.strip():
    print("Unregistered user, terminating the program...")
    exit()

# Text selection.
print("-" * 40, f"Welcome to the app, {username.title()}.", sep="\n")
print(f"We have {len(texts)} texts to be analyzed.", "-" * 40, sep="\n")
choice = input(f"Enter a number btw. From 1 to {len(texts)}: ")

# Check if the input is a valid number.
if not choice.isdigit() or int(choice) not in range(1, len(texts) + 1):
    print("Invalid selection. Exiting.", "-" * 40, sep="\n")
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
print("-" * 40)
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

# Determine how wide the graph heading should be.
if max(counts) <= 11:
    max_spaces = 1
else:
    max_spaces = max(counts) - 10

print("-" * 40, f"LEN|OCCURRENCES{" ":<{max_spaces}}|NR.", "-" * 40, sep="\n")

# Print out the final "histogram".
max_spaces += 11

for i in range(len(lengths)):
    length = lengths[i]
    count = counts[i]
    stars = "*" * count
    print(f"{length:3}|{stars:<{max_spaces}}|{count}")
print("-" * 40)
