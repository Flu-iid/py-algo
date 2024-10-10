def main(w:int):
    if w%2==0 and w>2:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    w = int(input())
    ans = main(w)
    print(ans)
