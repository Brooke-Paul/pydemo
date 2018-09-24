def test(n, m):
    try:
        avg = n / m
        print(avg)
    except Exception as e:
        if e.__class__ == ZeroDivisionError:
            print("this is zero exception")


if __name__ == "__main__":
    # test(10, 0)    try catch resolve exception
    test(10, 2)

