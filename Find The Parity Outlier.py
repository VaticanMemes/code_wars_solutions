def find_outlier(integers):
    if (int(integers[0]) % 2) == 0:
        a = 1
    else:
        a = 0
    if (int(integers[1]) % 2) == 0:
        b = 1
    else:
        b = 0
    if (int(integers[2]) % 2) == 0:
        c = 1
    else:
        c = 0
    if (a + b + c) == 3:
        numbers = "even"
    elif (a + b + c) == 2:
        numbers = "even"
    elif (a + b + c) == 1:
        numbers = "odd"
    elif (a + b + c) == 0:
        numbers = "odd"
    if numbers == "even":
        for i in integers:
            if (i % 2) != 0:
                break
    elif numbers == "odd":
        for i in integers:
            if (i % 2) == 0:
                break
    return i