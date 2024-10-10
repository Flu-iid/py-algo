database=dict()

def main(name:str):
    if name not in database:
        database[name] = database.get(name, 0)
        return "OK"
    
    else:
        database[name] += 1
        return f"{name}{database[name]}"


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        name = input()
        ans = main(name)
        print(ans)