def double_string(string):
    sentence = list(string)
    complete = []
    for letter in sentence:
        complete.append(letter + letter)

    return "".join(complete)
