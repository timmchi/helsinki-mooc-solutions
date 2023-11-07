# Write your solution here
from random import *
from string import *

def generate_strong_password(length: int, number: bool, special: bool):
    words = ascii_lowercase
    specials = "!?=+-()#"
    numbers = "0123456789"

    index_pool = list(range(1, 26))
    pw_draw = sample(index_pool, length)

    pw = ""
    pw_list = []

    
    if not number and not special:
        for i in pw_draw:
            pw += words[i]

    elif number and not special:
        for i in pw_draw:
            if len(pw) < length:
                pw += numbers[randint(0, 9)]
                pw += words[i]
                cond = randint(0, 1)
                if cond == 0:
                    pw += words[i]
                elif cond == 1:
                    pw += numbers[randint(0, 9)]

    elif not number and special:
        for i in pw_draw:
            if len(pw) < length:
                pw += words[i]
                pw += specials[randint(0, 7)]
                cond = randint(0, 1)
                if cond == 0:
                    pw += words[i]
                elif cond == 1:
                    pw += specials[randint(0, 7)]
                    
    elif number and special:
        for i in pw_draw:
            if len(pw) < length:
                pw += numbers[randint(0, 9)]
                pw += words[i]
                pw += specials[randint(0, 7)]
                cond = randint(0, 2)
                if len(pw) < length and cond == 0:
                    pw += words[i]
                elif len(pw) < length and cond == 1:
                    pw += numbers[randint(0, 9)]
                elif len(pw) < length and cond == 3:
                    pw += specials[randint(0, 7)]


    for i in pw:
        pw_list.append(i)

    length_diff = len(pw_list) - length

    if length_diff == 0:
        shuffle(pw_list)
        return "".join(pw_list)
    else:
        for i in range(length_diff):
            pw_list.remove(pw_list[i])
        return "".join(pw_list)