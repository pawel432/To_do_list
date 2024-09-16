import calendar
import logging
from typing import List

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

logger = logging.getLogger(__name__)


@login_required
def mainPageRender(request, next_months: str, month: int, year: int):
    next_months = int(next_months)
    month += next_months
    if month == 13:
        month = 1
        year += 1
    if month == 0:
        month = 12
        year -= 1
    if month == 1:
        previous_month = calendar.monthcalendar(year - 1, 12)
    else:
        previous_month = calendar.monthcalendar(year, month - 1)
    if month == 12:
        next_month = calendar.monthcalendar(year + 1, 1)
    else:
        next_month = calendar.monthcalendar(year, month + 1)
    current_month = calendar.monthcalendar(year, month)
    pre_month_last_week_index = len(previous_month) - 1
    cur_month_last_week_index = len(current_month) - 1

    pre_month_last_week = previous_month[pre_month_last_week_index]
    current_month_first_week = current_month[0]
    current_month_last_week = current_month[cur_month_last_week_index]
    next_month_first_week = next_month[0]
    for i in range(0, 7):
        if current_month_first_week[i] == 0:
            current_month_first_week[i] = pre_month_last_week[i]
    current_month[0] = current_month_first_week
    for i in range(0, 7):
        if current_month_last_week[i] == 0:
            current_month_last_week[i] = next_month_first_week[i]
    current_month[cur_month_last_week_index] = current_month_last_week
    return render(request, 'mainPage.html',
                  {'date': current_month,
                   'month': month, 'year': year})


# new format:

def changeMonthFormat(monthList: List, monthNumber: int, year: int):
    for week in monthList:
        for day in range(0, len(week)):
            oldDayVar = week[day]
            week[day] = [oldDayVar, monthNumber, year]


# if month == 13:
#     month = 1
#     year += 1
# if month == 0:
#     month = 12
#     year -= 1
# if month == 1:
#     previous_month = calendar.monthcalendar(year - 1, 12)
#     changeMonthFormat(previous_month, 12, year - 1)
# else:
#     previous_month = calendar.monthcalendar(year, month - 1)
#     changeMonthFormat(previous_month, month - 1, year)
# if month == 12:
#     next_month = calendar.monthcalendar(year + 1, 1)
#     changeMonthFormat(next_month, 1, year + 1)
# else:
#     next_month = calendar.monthcalendar(year, month + 1)
#     changeMonthFormat(next_month, month + 1, year)
# current_month = calendar.monthcalendar(year, month)
# changeMonthFormat(current_month, month, year)

# pre_month_last_week_index = len(previous_month) - 1
# cur_month_last_week_index = len(current_month) - 1

# pre_month_last_week = previous_month[pre_month_last_week_index]
# current_month_first_week = current_month[0]
# current_month_last_week = current_month[cur_month_last_week_index]
# next_month_first_week = next_month[0]

# for i in range(0, 7):
#     if current_month_first_week[i][0] == 0:
#         current_month_first_week[i][0] = pre_month_last_week[i][0]
#         current_month_first_week[i][1] = pre_month_last_week[i][1]
#         current_month_first_week[i][2] = pre_month_last_week[i][2]
# current_month[0] = current_month_first_week
# for i in range(0, 7):
#     if current_month_last_week[i][0] == 0:
#         current_month_last_week[i][0] = next_month_first_week[i][0]
#         current_month_last_week[i][1] = next_month_first_week[i][1]
#         current_month_last_week[i][2] = next_month_first_week[i][2]
# current_month[cur_month_last_week_index] = current_month_last_week


@login_required
def addTaskPageRender(request, month, day, year):
    return render(request, 'addTaskPage.html', {'user': request.CustomUser, 'year': year, 'month': month, 'day': day})
