def average(score1, score2, score3):
    NUMBER_TESTS = 3
    score1 = int(input("Input score1:"))
    if (score1 < 0):
        print("Bad input, good-bye!")
    score2 = int(input("Input score2:"))
    score3 = int(input("Input score3:"))
    numavg = ((score1 + score2 + score3)/NUMBER_TESTS)
    return float(numavg)



if __name__ == '__main__':
#    first_name = get_fname()
#    # str.capitalize(input("Please enter your first name:"))
#    last_name = get_lname()
#    age = int(input("Please enter your age:"))
    numavg = str(round(average(), 2))
    print(f'{numavg}')

