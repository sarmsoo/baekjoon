from sys import stdin
input = stdin.readline

def is_pseudo(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def is_palindrome(word, left, right):
    if word == word[::-1]:
        return 0
    else:
        while left < right:
            if word[left] != word[right]:
                check_left = is_pseudo(word, left + 1, right)
                check_right = is_pseudo(word, left, right - 1)

                if check_left or check_right:
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1

t = int(int(input()))

for _ in range(t):
    word = input().strip()
    left, right = 0, len(word)-1
    answer = is_palindrome(word, left, right)
    print(answer)