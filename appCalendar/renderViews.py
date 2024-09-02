import calendar
import datetime
import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def mainPageRender(request):
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    kalendarz = calendar.monthcalendar(year, month)
    # quantityOfDays = calendar.monthrange(year, month)[1]
    # logger.info(quantityOfDays)
    # iterationsNum = 0
    # for week in kalendarz:
    #     iterationsNum += 1
    #     if iterationsNum == 1:
    #         zeroDaysIndexes = []
    #         noweDni = []
    #         for day in range(0, len(week)):
    #             if week[day] == 0:
    #                 zeroDaysIndexes.append(day)
    #         for i in range(0, len(zeroDaysIndexes)):
    #             noweDni.append(quantityOfDays - i)
    #         noweDni.reverse()
    #         for day in range(0, len(week)):
    #             if week[day] == 0:
    #                 pass
    #                 week[day] = noweDni[day]
    #     if iterationsNum == 5:
    #         zeroDaysIndexes = []
    #         noweDni = []
    #         for day in range(0, len(week)):
    #             if week[day] == 0:
    #                 zeroDaysIndexes.append(day)
    #         for i in range(0, len(zeroDaysIndexes)):
    #             noweDni.append(1 + i)
    #         iterator = 0
    #         for day in range(0, len(week)):
    #             if week[day] == 0:
    #                 week[day] = noweDni[iterator]
    #                 iterator += 1
    # logger.info(kalendarz)
    return render(request, 'mainPage.html',
                  {'date': kalendarz,
                   'month': month, 'year': year})


def addTaskPageRender(request, month, day, year):
    return render(request, 'addTaskPage.html', {'user': request.CustomUser, 'year': year, 'month': month, 'day': day})
