def test_sum(): #using list
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 5, "Should be 6"


if __name__ == "__main__":
    test_sum()
    print("Everything passed")
    test_sum_tuple()
    print("Everything passed")
