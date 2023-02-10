t = int(input())
for i in range(t):
    print()
    n = int(input())
    d_list = []
    for i in range(n):
        d = int(input())
        d_list.append(d)
    # minimum surface exopsure only valid when u have put cubes from largest to lowest on top
    d_list.sort(reverse=True)
    minimum_surface = 0
    for di in range(len(d_list)):
        if di+1 == len(d_list):
            surf = (d_list[di]**2)*5
            minimum_surface += surf
        else:
            surf = (d_list[di]**2)*4 + \
                abs(d_list[di]**2 - d_list[di+1]**2)
            minimum_surface += surf
    print(minimum_surface)

# side-by-side stack problem probably
