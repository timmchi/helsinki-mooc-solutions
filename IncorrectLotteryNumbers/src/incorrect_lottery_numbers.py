# Write your solution here
def file_reader():
    first_filter = []
    with open("lottery_numbers.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            if len(parts[0]) <= 7:
                first_filter.append(parts)

    return first_filter

def filter_incorrect():
    lst = file_reader()

    for week in lst:
        week_number = week[0].split()
        try:
            integ = int(week_number[1])
        except:
            lst.remove(week)

    for week in lst:
        week_values = week[1].split(",")
        try:
            for value in week_values:
                value = int(value)
        except:
            lst.remove(week)

    for week in lst:
        week_values = week[1].split(",")
        for value in week_values:
            if 1 <= int(value) <= 39:
                continue
            else:
                lst.remove(week)

    for week in lst:
        week_values = week[1].split(",")
        if len(week_values) != 7:
            lst.remove(week)
        elif len(week_values) != len(set(week_values)):
            lst.remove(week)

    with open("correct_numbers.csv", "w") as new_file:
        for i in lst:
            line = f"{i[0]};{i[1]}"
            new_file.write(line+"\n")

# filter_incorrect()