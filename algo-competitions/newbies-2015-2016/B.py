t = int(input())


def is_palindrome(s):
    if s == s[::-1]:
        return 1
    return 0


if 1 <= t <= 100:
    for i in range(t):
        n = int(input())
        if 1 <= n <= 1000:
            n_dec_ans = is_palindrome(str(n))
            n_hex_ans = is_palindrome(hex(n)[2:])
            n_bi_ans = is_palindrome(bin(n)[2:])
            if n_dec_ans + n_hex_ans + n_bi_ans >= 2:
                print("Magical")
            else:
                print("I'm sorry Sherlock :(")
