# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(word: str):
    backwards_word = word[::-1]
    return backwards_word == word
       
def asker():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")

asker()