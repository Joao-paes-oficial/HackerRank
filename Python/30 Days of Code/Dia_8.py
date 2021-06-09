amount = int(input())
phoneBook = dict()

for _ in range(amount):
    line = input()
    line = line.split()
    phoneBook[line[0]] = phoneBook.get(line[0], line[1])

while 1:
    try:
        a = input()
        if a in phoneBook:
            print(str(a) + "=" + str(phoneBook[a]))
        else:
            print('Not found')
    except:
        break