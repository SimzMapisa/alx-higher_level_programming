import random

random_num = random.randint(-10, 10)

if (random_num == 0):
    print("%d is zero" % random_num)
elif (random_num < 0):
    print("%d is negative" % random_num)
else:
    print("%d is positive" % random_num)
