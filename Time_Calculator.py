def add_time(start, duration, startDay=None):
    
    hourCount = 0
    dayCount = 0
    freq = 0
    day = ""
    newDay = 0
    origin = start.split()
    startTime = origin[0]
    startPeriod = origin[1]

    startTime = startTime.split(':')
    startHour = int(startTime[0])
    startMin = int(startTime[1])
    
    operand = duration.split(':')
    addHour = int(operand[0])
    addMin = int(operand[1])
    
    if startPeriod == 'PM':
        startHour = startHour + 12
    
    newHour = startHour + addHour
    newMin = startMin + addMin
    
    while newMin > 60:
        remainder = newMin - 60
        newMin = remainder
        newHour = newHour + 1
    
    period = newHour
    
    while period >= 12:
        period = period - 12
        freq = freq + 1
        
    while newHour >= 24:
        remainder = newHour - 24
        newHour = remainder
        dayCount = dayCount + 1
        hourCount = hourCount + 1
        
    if newHour == 0:
            newHour = 12

    if startPeriod == "AM" and freq % 2 != 0:
        startPeriod = "PM"
    elif startPeriod == "PM" and freq % 2 == 0:
        startPeriod = "AM"
    else:
        startPeriod = startPeriod
    
    if newHour > 12:
        newHour = newHour - 12
    
    newHour = str(newHour)
    
    if newMin < 10:
        newMin = "0" + str(newMin)
    else:
        newMin = str(newMin)
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
    
    if dayCount == 1:
        day = "(next day)"
    elif dayCount > 1:
        day = "(" + str(dayCount) + " days later)"
    
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