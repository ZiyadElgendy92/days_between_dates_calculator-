#days between dates counter

daysinmonths=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def last_day_in_month(y1, m1):
    if m1 == 2:
        if ((y1 %400 ==0 or y1 %100!=0)and y1%4==0):
            daysinmonths[1] = 29
    return daysinmonths[m1-1]

def days_between_dates(d1, m1, y1, d2, m2, y2):
    age_in_days=0

    while y1 <= y2:
        while m1 <=12:
            while d1 <= last_day_in_month(y1, m1):

                if y1 == y2 and d1 == d2 and m1 == m2:
                    return age_in_days
                else:
                    d1 +=1
                    age_in_days +=1
            d1 =1
            m1 +=1
        m1 =1
        y1 +=1


