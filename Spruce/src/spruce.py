# Write your solution here
def line(integer, string):
    if string != "":
        print(string[0]*integer)
    else:
        print("*"*integer)

def spruce(size):
    n = 1 # need another variable that will handle whitespaces, going from 4 to 3 to 2 to 1
    space = size - 1
    print("a spruce!")
    for i in range(size):
        if i < size - 1:
            print(" "*space, end="")
            space -= 1
        line(i+n,"")
        n += 1
  
    print(" "*(size-1), end="")
    line(1,"")
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)