with open('new_file.txt', 'wb') as new_file:
    data = bytearray([1, 2, 3, 4, 5])
    new_file.write(data)
