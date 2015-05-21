def digit_sum(x):
    temp = str(x)
    sum = 0
    for i in temp:
        sum += int(i)
    return sum