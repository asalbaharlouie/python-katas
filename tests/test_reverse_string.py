def reverse_string(word):
    reverse_str = "" #رشته جدید این تو ریخته میشه
    for char in word:
        reverse_str = char + reverse_str  #هر حرف جدید میره اول صف، پس کلمه عکس میشه

    return reverse_str

def test_reverse_string():
    assert reverse_string("hello") == 'olleh'

test_reverse_string()

print(reverse_string("salam"))