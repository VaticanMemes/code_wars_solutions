def sum_two_smallest_numbers(numbers):
    lowest = second_lowest = 10000000000000000000000000000
    a = 0
    for i in numbers:
        if i <= lowest:
            lowest = int(i)
    for i in numbers:
        if i <= second_lowest and i > lowest:
            second_lowest = int(i)
        elif i <= lowest and a == 0:
            a = 1
        elif i <= lowest and a == 1:
            second_lowest = int(i)
    return lowest + second_lowest
    """
    ^
    |
    |
    
    What the actual fuck was that.
    For future employers:
    I made this when I was just starting out.
    🙏🙏🙏 plz don't cancel me for this.
    """