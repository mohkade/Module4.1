age = 15
registered = False

if age >= 18:
    if registered:
        print("Be sure to vote")
else:
    print('In {0:2d} years you can vote'.format(18-age))