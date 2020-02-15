#def average(score1, score2, score3):
def average():
    NUMBER_TESTS = 3

#def score1():
    score1 = int(input("Input score1:"))
    if (score1 < 0):
        print("Bad input, please add a positive number!")
    elif(score1>0):
        print("Enter score 2")
    score2 = int(input("Input score2:"))
    if (score2 < 0):
        print("Bad input, please add a positive number!")
    elif(score2>0):
        print("Enter score 3")
    score3 = int(input("Input score3:"))
    if (score3 < 0):
        print("Bad input, please add a positive number!")
    elif(score3>0):
        print("Average of score 1, score 2 and score 3 is ")
    numavg = float((score1 + score2 + score3)/NUMBER_TESTS)
    return numavg

if __name__ == '__main__':
#    first_name = get_fname()
#    # str.capitalize(input("Please enter your first name:"))
#    last_name = get_lname()
#    age = int(input("Please enter your age:"))
    numavg = str(round(average(), 2))
    print(f'{numavg}')

