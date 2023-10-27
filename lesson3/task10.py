# yeild functions in python

def simple_generator():
    yield "1"
    yield "hello"
    yield "there"


generator = simple_generator()
print(generator)
for value in generator:
    print(value)
