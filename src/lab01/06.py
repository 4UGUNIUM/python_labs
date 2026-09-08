N = int(input())

count = 0
count2 = 0

for n in range(N):
    person = input().split()

    surname = person[0].upper()
    name = person[1].upper()
    age = int(person[2])
    part = person[3] == 'True'

    if part == True:
        count += 1
    if part == False:
        count2 += 1

print(f'Очно: {count}, Заочное: {count2}')