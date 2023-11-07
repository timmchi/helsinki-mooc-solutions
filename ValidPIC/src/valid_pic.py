# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):

    date = pic[:6]
    marker = pic[6]
    pid = pic[7:10]
    control = pic[10]

    chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    if len(pic) > 11:
        return False
    
    year_last_two = date[4:]
    if marker == "+":
        year_first_two = 18
    elif marker == "-":
        year_first_two = 19
    elif marker == "A":
        year_first_two = 20
    
    yer = int(f"{year_first_two}{year_last_two}")

    try:
        datetime((yer), (int(date[2:4])), (int(date[:2])))

    except ValueError:
        return False

    if marker not in "+-A":
        return False

    numbah = date + pid

    index = int(numbah) % 31

    if chars[index] != control:
        return False

    return True

    # print(datetime((int(date[4:])), (int(date[2:4])), (int(date[:2]))))

# print(is_it_valid("290200A1239"))
# 290200-1239
# 290200A1239
# returns False even tho it is valid

    # numbah = date + pid
    # index = int(numbah) % 31

    # if len(pic) > 11 or marker not in "+-A" or chars[index] != control:
    #     return False