def spin_words(sentence):
    new_sentence = []
    for single_word in sentence.split():
        if len(single_word) >= 5:
            new_sentence.append("".join(reversed(list(single_word))))
        else:
            new_sentence.append(single_word)
    return (" ".join(new_sentence))