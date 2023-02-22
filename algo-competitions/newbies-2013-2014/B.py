import sys
inputlist = sys.stdin.readlines()
for n in inputlist:
    print(f"{int(n)**2}"[::-1])
