string = input()

length = [1] * len(string)

for i in range(1, len(string)):
    for j in range(0, i):
        if ord(string[i]) > ord(string[j]) and length[i] < length[j] + 1:
            print(string[j])
            length[i] = length[j] + 1
    print(length)
print(26 - max(length))
