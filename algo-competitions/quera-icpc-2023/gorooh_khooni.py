t = int(input())


def O_remover(s):
    b = list(s)
    for i in range(len(b)):
        if b[i] == "O":
            del b[i]
    c = "".join(b)
    return c


def get_g(s):
    return s[:-1]


def get_r(s):
    return s[-1]


for i in range(t):
    group_input = input().split(" ")
    d, m, c = group_input[0], group_input[1], group_input[2]
    d_g, d_r = get_g(d), get_r(d)
    m_g, m_r = get_g(m), get_r(m)
    c_g, c_r = get_g(c), get_r(c)
    d_g = O_remover(d_g)
    m_g = O_remover(m_g)
    c_g = O_remover(c_g)
    flag_g = True
    flag_r = True
    # group
    if len(c_g) == 1:
        if (c_g not in m_g) and (c_g not in d_g):
            flag_g = False
    elif len(c_g) == 2:
        if (d_g, m_g) not in {('AB', 'A'), ('A', 'AB'), ('B', 'A'), ('AB', 'AB'), ('B', 'AB'), ('A', 'B'), ('AB', 'B')}:
            flag_g = False
    # r
    if m_r == "-" and d_r == "-" and c_r == "+":
        flag_r = False
    if flag_g and flag_r:
        print("valid")
    else:
        print("invalid")
