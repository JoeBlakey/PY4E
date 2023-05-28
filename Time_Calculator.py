def add_time(start, duration, startDay=None):
    #Declaring Variables
    hourCount = 0
    dayCount = 0
    freq = 0
    day = ""
    newDay = 0
    #Splitting time into individual parts
    origin = start.split()
    startTime = origin[0]
    startPeriod = origin[1]

    startTime = startTime.split(':')
    startHour = int(startTime[0])
    startMin = int(startTime[1])
    
    operand = duration.split(':')
    addHour = int(operand[0])
    addMin = int(operand[1])
    #Converting from 12-hour to 24-hour time
    if startPeriod == 'PM':
        startHour = startHour + 12
    #Calculating new time
    newHour = startHour + addHour
    newMin = startMin + addMin
    #Adding an hour if sum of old min + new min > 60
    while newMin > 60:
        remainder = newMin - 60
        newMin = remainder
        newHour = newHour + 1
    #Determining how many AM/PM cycles are completed
    period = newHour
    while period >= 12:
        period = period - 12
        freq = freq + 1
    #Adding a day if > 24 hours    
    while newHour >= 24:
        remainder = newHour - 24
        newHour = remainder
        dayCount = dayCount + 1
        hourCount = hourCount + 1
    #Converting 00:00 AM/PM to 12:00 AM/PM
    if newHour == 0:
            newHour = 12
    #Determining new AM/PM
    if startPeriod == "AM" and freq % 2 != 0:
        startPeriod = "PM"
    elif startPeriod == "PM" and freq % 2 == 0:
        startPeriod = "AM"
    else:
        startPeriod = startPeriod
    #Converting from 24-hour to 12-hour time
    if newHour > 12:
        newHour = newHour - 12
    #Converting new time from int to string to allow for formatting
    newHour = str(newHour)    
    if newMin < 10:
        newMin = "0" + str(newMin)
    else:
        newMin = str(newMin)
    #Calculating new day of week based on starting day
    if startDay is not None:
        startDay = startDay.title()
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        index = week.index(startDay)
        newdayCount = dayCount
        while newdayCount > 7:
            newdayCount = newdayCount - 7  
        newDay = index + newdayCount
        if newDay == 7:
            newDay = 0
        newDay = week[newDay]
    #Formatting for number of days in future
    if dayCount == 1:
        day = "(next day)"
    elif dayCount > 1:
        day = "(" + str(dayCount) + " days later)"
    #Fomatting for final output
    if startDay is not None:
        if dayCount > 0:
            new_time = newHour + ":" + newMin + " " + startPeriod + ", " + newDay + " " + day
        else:
            new_time = newHour + ":" + newMin + " " + startPeriod + ", " + newDay
    else:
        if dayCount > 0:
            new_time = newHour + ":" + newMin + " " + startPeriod + " " + day
        else:
            new_time = newHour + ":" + newMin + " " + startPeriod
    
    #print(new_time)
    return new_time

print(add_time("11:59 PM", "24:05"))