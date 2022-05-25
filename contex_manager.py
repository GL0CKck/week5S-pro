
with open(f'{input("Name file for write: ")}.txt', 'w') as new_f:
    with open(f'{input("Name file for read: ")}.txt', 'r') as f:
        num = f.read().split()
        for i in range(0, len(num)):
            new_f.write(f'{i+1}: ' + num[i] + '\n')


