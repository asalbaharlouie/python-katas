def is_palindrome(word):
    reverse_str = ""
    for char in word:
        reverse_str = char + reverse_str
    if word == reverse_str:
        return True
    else:
        return False


def test_is_palindrome_when_true():
    assert is_palindrome("level")


test_is_palindrome_when_true()


def test_is_palindrome_when_false():
    assert is_palindrome("hello")


test_is_palindrome_when_false()


def test_is_palindrome_when_empty():
    assert is_palindrome("")


test_is_palindrome_when_empty()


def test_is_palindrome_when_has_only_one_char():
    assert is_palindrome("h")


print(is_palindrome("bahar"))
