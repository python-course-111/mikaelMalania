# dictionaries in python
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

# Pop item from dictionary

person.pop('age')
print(person)

# Pop last item from dictionary
person.popitem()
print(person)

# Add item to dictionary
person['phone'] = '555-555-5555'

print(person)
