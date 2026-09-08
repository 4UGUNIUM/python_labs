FIO = input('ФИО: ')
FIOsplited = FIO.split()

initials = ''.join([name[0] for name in FIOsplited]).upper()

print(f'Инициалы: {initials}.')
print(f"Длина (символов): {len(' '.join(FIOsplited))}")