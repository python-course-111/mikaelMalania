# yeild functions in python

def simple_easy_generator():
    yield "1"
    yield "hello"
    yield "there"


generator = simple_easy_generator()
print(generator)
for value in generator:
    print(value)
