import quippers

if __name__ == "__main__":
    assert quippers.concat_in_rust("hello ", "world!") == "hello world!"
    assert quippers.add_in_rust(1, 2) == 3
    assert quippers.subtract_in_rust(5, 2) == 3
    print("Success!")