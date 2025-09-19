from demo1 import add

def test_add():
    assert demo1.add(2, 3) == 5
    assert demo1.add(0, 0) == 0
