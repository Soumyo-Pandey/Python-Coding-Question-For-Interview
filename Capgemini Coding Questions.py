#Capgemini Coding Questions [two dates are given find the no of mondays between them]
import datetime
import calendar

def weekday_count(start, end):
    start_date = datetime.datetime.strptime(start, '%d/%m/%Y')
    end_date = datetime.datetime.strptime(end, '%d/%m/%Y')
    week = {}
    for i in range((end_date-start_date).days):
        day = calendar.day_name[(start_date + datetime.timedelta(days = i+1)).weekday()]
        week[day] = week[day] + 1 if day in week else 1
    return week

print(weekday_count("01/01/2019","31/01/2019"))
