# Write your solution here
year = int(input("Please type in a year: "))
loop = True
counter = 0

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            year += 1
            counter +=1
        else:
            loop = True
    else:
        year += 1
        counter +=1
else:
    # print("That year is not a leap year.")
    loop = True

while loop:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"The next leap year after {year - counter} is {year}")
                break
            else:
                year += 1
                counter += 1
        else:
            print(f"The next leap year after {year - counter} is {year}")
            break
    else:
        year += 1
        counter += 1
    