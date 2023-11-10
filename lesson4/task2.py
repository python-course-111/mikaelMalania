data_file = open("./files/texts/info.txt", "r")

# print(data_file.read(5))
# print(data_file.readline())
# print(data_file.readline())

for line in data_file:
    for char in line:
        print(char)


data_file.close()