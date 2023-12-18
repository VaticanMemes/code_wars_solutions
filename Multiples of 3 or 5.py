def solution(number):
    multiples = []
    for i in range(number):
        if i % 3 == 0 and i % 5 == 0:
            multiples.append(i)
        elif i % 3 == 0:
            multiples.append(i)
        elif i % 5 == 0:
            multiples.append(i)
    return sum(multiples)