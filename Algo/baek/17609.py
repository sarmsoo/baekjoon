from sys import stdin
input = stdin.readline

def is_palindrome(str_):
    left, right = 0, len(str_) - 1

    while left < right:
        if str_[left] == str_[right]:
            left += 1
            right -= 1
        else:
            if left < right - 1:
                tmp = str_[:right] + str_[right + 1:]
                if tmp[:] == tmp[::-1]:
                    return 1

            if left + 1 < right:
                tmp = str_[:left] + str_[left + 1:]
                if tmp[:] == tmp[::-1]:
                    return 1
            return 2
    return 0

for _ in range(int(input())):
    print(is_palindrome(input().strip()))