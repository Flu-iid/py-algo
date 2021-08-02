# Rename Pro
# Change specific charecter('s) in files name

names = ["Android", "Android.manage", "Androidopedia", "My android", "heyandroid"]
output = []
for name in names:
    name = name.lower()
    name = name.replace("android", "droid")
    output += name,
print(output)