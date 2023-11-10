# using arrays with for loops

person_lived_locations = ['tbilisi', 'batumi', 'kutaisi',
                          'telavi', 'rustavi', 'gurjaani', 'sighnaghi']


# for location in person_lived_locations:
#     print(location)

# using dictionaries with for loops

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'hobbies': ['tennis', 'football', 'swimming', 'cycling', 'running', 'dancing', 'singing'],
    'address': {
        'street': '50 Main street',
        'city': 'Boston',
        'state': 'MA'
    }
}

for key, value in person.items():
    print(key, value)
