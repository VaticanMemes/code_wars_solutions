def solution(s):
    new_list = []
    if not s:
        return []
    for i in range(0, len(list(s)), 2):
        new_list.append("".join((list(s)[i:i+2])))
    if len(new_list[-1]) == 1:
        new_list[-1] = new_list[-1] + "_"
    return(new_list)