def pig_latin(word):
    if word[0] in {'a', 'e', 'i', 'o', 'u'}:
        return word + 'hay'
    else:
        return word[1:] + word[0] + 'ay'

print(pig_latin("ello"))
