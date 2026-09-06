def word_count(sentence):
    sentence = sentence.split()
    counts = {}
    for word in sentence:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def test_word_count():
    assert word_count("hello world hello") == {'hello': 2, 'world': 1}

test_word_count()

print(word_count("hi asal hi"))