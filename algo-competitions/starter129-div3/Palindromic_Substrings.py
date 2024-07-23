t = int(input())


def remove_palindrome(s: str, n: int):
    cyclic_s = s + s
    max_p_length = 0
    p_word = ""
    for i in range(n):
        for j in range(i + 1, n + i):
            word = cyclic_s[i : j + 1]
            if word == word[::-1]:
                word_length = len(word)
                if word_length > max_p_length and word_length > 1:
                    p_word = word
                    max_p_length = word_length

    if p_word:
        return True, p_word[max_p_length // 2 + 1]
    else:
        return False, ""


for _ in range(t):
    n = int(input())
    s = input()

    turns = 0  # if even bob wins if odd alice wins
    while len(s) > 1:
        state, to_remove = remove_palindrome(s, n)
        if state:
            s = s.replace(to_remove, "")
            turns += 1
        else:
            break

    print("Alice" if turns % 2 else "Bob")

#  read to improve palindrome
# https://blog.finxter.com/how-to-find-all-palindromes-in-a-python-string/
