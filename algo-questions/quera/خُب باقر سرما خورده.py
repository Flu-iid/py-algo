l = [input() for i in range(5)]
result = ""
for i in range(5):
    if "MOLANA" in l[i] or "HAFEZ" in l[i]:
        result += f"{i+1} "
print(result if result else "NOT FOUND!")
