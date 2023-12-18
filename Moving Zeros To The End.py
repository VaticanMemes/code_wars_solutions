def move_zeros(lst):
    """
    Three step process
    1. Count all the zeros
    2. Delete all the zeros
    3. Append all the zeros
    """
    # Step 1
    count = 0
    for i in lst:
        if i == 0:
            count += 1
    # Step 2
    lst = [i for i in lst if i != 0]
    
    # Step 3
    for i in range(count):
        lst.append(0)
    
    return lst