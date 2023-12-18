def descending_order(num):
    new_num = list(str(num))
    new_num.sort(reverse=True)
    return int("".join(new_num))