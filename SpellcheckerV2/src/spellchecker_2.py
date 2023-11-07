# Write your solution here
from difflib import *

user_input = input("write text: ")

lst = user_input.split()

wordlist = []
checked_word = []
wrong_words = []

with open("wordlist.txt") as new_file:
    for line in new_file:
        parts = line.replace("\n", "")
        wordlist.append(parts)

for i in lst:
    if i.lower() not in wordlist:
        wrong_words.append(i)
        i = f"*{i}*"
        
    checked_word.append(i)

final_word = ""

for i in checked_word:
    final_word += i
    final_word += " "

print(final_word)
print("suggestions:")
for i in wrong_words:
    print(f"{i}: {', '.join(get_close_matches(i.lower(), wordlist))}")



