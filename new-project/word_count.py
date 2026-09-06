def word_count(sentence):
    sentence = sentence.split()
    counts = {}
    for word in sentence:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count("hi asal hi"))