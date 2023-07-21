from sys import stdin
input = stdin.readline

tmp_king, tmp_stone, n = input().split()

pos_king = (int(8 - int(tmp_king[1])), ord(tmp_king[0]) - ord('A'))
pos_stone = (int(8 - int(tmp_stone[1])), ord(tmp_stone[0]) - ord('A'))
n = int(n)

for _ in range(n):
    inst = input().strip()
    y, x = pos_king
    ny, nx = 0, 0
    if inst == 'B':
        ny = y + 1
        nx = x
    elif inst == 'T':
        ny = y - 1
        nx = x
    elif inst == 'R':
        ny = y
        nx = x + 1
    elif inst == 'L':
        ny = y
        nx = x - 1
    elif inst == 'RT':
        ny = y - 1
        nx = x + 1
    elif inst == 'LT':
        ny = y - 1
        nx = x - 1
    elif inst == 'RB':
        ny = y + 1
        nx = x + 1
    elif inst == 'LB':
        ny = y + 1
        nx = x - 1

    if ny < 0 or ny >= 8 or nx < 0 or nx >= 8:
        continue

    if (ny, nx) == pos_stone:
        r, c = pos_stone
        nr = r + ny - y
        nc = c + nx - x
        if nr < 0 or nr >= 8 or nc < 0 or nc >= 8:
            continue
        pos_stone = (nr, nc)
    pos_king = (ny, nx)

print(''.join([chr(pos_king[1] + ord('A')), str(8 - pos_king[0])]))
print(''.join([chr(pos_stone[1] + ord('A')), str(8 - pos_stone[0])]))