import quippers
assert quippers.concat("hello ", "world!") == "hello world!"
assert quippers.add_in_rust(1, 2) == 3
assert quippers.sub_in_rust(5, 2) == 3