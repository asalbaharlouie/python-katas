def reverse_string(word):
    reverse_str = ""
    for char in word:
        reverse_str = char + reverse_str

    return reverse_str


print(reverse_string("salam"))
