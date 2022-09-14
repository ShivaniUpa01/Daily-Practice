def censor(text, word):
    texts = text.split()
    letter = []
    for i in texts:
        if i == word:
            letter.append("*" * len(word))
        else:
            letter.append(i)
    return " ".join(letter)
