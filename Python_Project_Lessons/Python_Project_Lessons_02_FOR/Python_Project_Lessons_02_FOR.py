i = 0
while i < 10:
    print(i)
    i += 1

for x in "Hello World":
    print(x * 2, end = "")

# в проверки if - continue то что true пропускает. И идет дальше.

print("\n2 Вариант:\n")

for x in 'Hello World':
    if x == 'o':
        continue
    print(x * 2, end = "")

print("\n3 Вариант:\n")

# в проверки if - break печатает до true потом остановка цикла.

for x in 'Hello World':
    if x == 'W':
        break
    print(x * 2, end = "")
