letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def rot13(message):
    new_sen = []
    for i in list(message):
        if i.upper() in letters:
            if i.isupper() == True:
                new_sen.append(letters[(letters.index(str(i.upper())) + 13) % 26])
            else:
                new_sen.append((letters[(letters.index(str(i.upper())) + 13) % 26]).lower())
        else:
            new_sen.append(i)
    return "".join(new_sen)