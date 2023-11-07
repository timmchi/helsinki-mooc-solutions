# Write your solution here
def chessboard(x):
    for i in range(x):
        if i % 2 != 0:
            print(("01"*x)[:x])
        else:
            print(("10"*x)[:x])
# Testing the function
if __name__ == "__main__":
    chessboard(3)
