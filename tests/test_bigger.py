def bigger(a, b):
    if a > b:
        return a
    else:
        return b

def test_bigger():
    assert bigger(5, 10) == 10 

test_bigger()

def test_bigger_when_negative():
    assert bigger(-1, -5) == -1 

test_bigger_when_negative()

def test_bigger_when_equal():
    assert bigger(0, 0) == 0

test_bigger_when_equal()


print(bigger(5, 1))
