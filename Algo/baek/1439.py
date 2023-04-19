from sys import stdin
input = stdin.readline

zero = 0
one = 0
prev = ''
for str in input():
    if prev == str:
        continue
    else:
        if str == '0':
            zero += 1
        elif str == '1':
            one += 1
    prev = str

print(min(zero, one))