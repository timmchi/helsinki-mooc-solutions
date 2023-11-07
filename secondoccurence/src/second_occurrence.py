# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")

index = word.find(char)

if index == -1:
    print("The substring does not occur twice in the string.")
else:
    new_index = word.find(char, index + len(char))

    if new_index == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {new_index}.")
