def add(a, b):
    return a + b

def test_add():
    assert add(2, 4) == 6

def test_add2():
    assert add(-1, -1) == -2

def test_add3():
    assert add(0, 1 ) == 1
 
test_add()
test_add2()

