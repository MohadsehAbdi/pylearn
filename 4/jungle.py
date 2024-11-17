animals = ['🦁','🐻','🦊','🐯','🐲','🐱','🐭','🐸','🐄','🦥','🦓', '🐔' , '🐰']

print(animals[5])
print(animals[-2])

print(animals[0:6])
print(animals[6:10])

for i in range(len(animals)):
    if i % 2 == 0:
        print(i,animals[i])