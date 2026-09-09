def reverse_string(word):
    reverse_str = ""
    for char in word:
        reverse_str = char + reverse_str
    return reverse_str


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


test_reverse_string()

print(reverse_string("salam"))
