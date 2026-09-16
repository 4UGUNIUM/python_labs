N = int(input('in_1: '))

count = 0
count2 = 0

for n in range(N):
    person = input(f'in_{n+2}: ').split()

    surname = person[0].upper()
    name = person[1].upper()
    age = int(person[2])
    part = person[3] == 'True'

    if part == True:
        count += 1
    if part == False:
        count2 += 1

print(f'out: {count}, {count2}')
