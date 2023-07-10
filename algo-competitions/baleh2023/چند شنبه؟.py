Farvardin = 31
Ordibehesht = Farvardin
Khordad = Farvardin
Tir = Farvardin
Mordad = Farvardin
Shahrivar = Farvardin
Mehr = 30
Aban = Mehr
Azar = Mehr
Dey = Mehr
Bahman = Mehr
Esfand = 29

year = [
    "Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar", "Dey", "Bahman", "Esfand"]


week = ["shanbe", "1shanbe", "2shanbe",
        "3shanbe", "4shanbe", "5shanbe", "jome"]


for _ in range(int(input())):
    user_day, user_month, user_week_day = input().split()
    user_day_2, user_month_2 = input().split()
    current_week = week.index(user_week_day)
    interval = 0
    a = year.index(user_month)
    b = year.index(user_month_2)
    if a <= b:
        start_month = eval(user_month)
        end_month = eval(user_month_2)
        start_day = int(user_day)
        end_day = int(user_day_2)
        interval = start_month - start_day
        for i in range(a+1, b):
            interval += eval(year[i])
        interval += end_day
        week_interval = interval % 7
        print(week[(week_interval+current_week) % 7])
    else:
        start_month = eval(user_month_2)
        end_month = eval(user_month)
        start_day = int(user_day_2)
        end_day = int(user_day)
        interval = start_day
        for i in range(b-1, a, -1):
            interval += eval(year[i])
        interval += end_month - end_day
        week_interval = -interval % 7
        print(week[(current_week+week_interval) % 7])
