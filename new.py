from random import randint
ones, twos, threes, fours, fives, sixes = 0,0,0,0,0,0
for trial in range(10000):
    x = randint(1,6)
    if x == 1:
        ones += 1
    elif x == 2:
        twos += 2
    elif x == 3:
        threes += 3
    elif x == 4:
        fours += 4
    elif x == 5:
        fives += 5
    else:
        sixes += 6

res = (ones + twos + threes + fours + fives + sixes) / 10000
print("Average value over 10000 trials is", res)
