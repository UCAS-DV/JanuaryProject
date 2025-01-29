# Music Festival Management System

currentTimes = ()
currentTimeframes = []
schedule = []

days = int(input("How many days are you going to have the festival be? :"))
dayCount = 0

def updateCurrentTimes(timeframes, startTime, endTime):
    timeframeCount = timeframes
    timeNow = startTime
    timeNowHour = startTime

    currentTimes = currentTimes + timeNow
    currentTimes = currentTimes + timeNowHour

    while timeNow <= endTime:
        remainder = timeframeCount % 2
        if remainder == 1:
            timeNowHour = timeNowHour + 1
        elif remainder == 0:
            timeNow = timeNow + .30

if days >= dayCount:
    start = float(input("What time does the performance start? (Minutes are after a decimal point, ex. 10.30)"))
    end = float(input("What time does the performance end? (Minutes are after a decimal point, ex 12.30)"))
    timeframes = end - start
    timeframes = timeframes / 2
    currentTimeframes = currentTimeframes + timeframes
    updateCurrentTimes()

def performancesInDay():
    performInDay = int(input("How many performances are in this day?"))
    if performInDay > 0:
        