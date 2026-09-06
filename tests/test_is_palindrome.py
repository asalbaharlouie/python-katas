def is_palindrome(word):
    reverse_str = ""
    for char in word:
        reverse_str = char + reverse_str
    if word == reverse_str:
        return True
    else: 
        return False 
    #اینجا همچین چیزی هم میتونیم بنویسیم return word == reverse_str

def test_is_palindrome_when_true():
    assert is_palindrome("level") == True

test_is_palindrome_when_true()

def test_is_palindrome_when_false():
    assert is_palindrome("hello") == False

test_is_palindrome_when_false()

def test_is_palindrome_when_empty():
    assert is_palindrome("") == True

test_is_palindrome_when_empty()

def test_is_palindrome_when_has_only_one_char():
    assert is_palindrome("h") == True

print(is_palindrome("bahar"))