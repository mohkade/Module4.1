MAX = 10
MIN = 0

if __name__ == '__main__':
    y = 5
    if y < MIN:
        print("y is below 0")
    else:
        print("y is above 0")
    x = 7
    if MIN < x < MAX:
        print("x is between 0 and 10")
    if MIN < x != MAX:
        print("x is higher than 0 but does not equal to 10")
    if MIN < x <= MAX:
        print("x is higher than 0 up to and including 10")
    else:
        print("none")
