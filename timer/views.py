# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from dateutil import tz
from django.shortcuts import render

def findTimes(locations):
    times=[]
    for location in locations:
        location_tz = tz.gettz(location)
        times.append(datetime.datetime.now(tz=location_tz).strftime("%H:%M:%S"))
    return times

def isExtendedHours(day, hour, minute):
    if(day == "Sat" or day == "Sun"):
        return True

    if(hour < 7):
        if(hour == 6):
            if(minute < 30):
                return True
        return True
    if(hour > 4):
        return True
    return False


def index(request):
    date = datetime.datetime.now()
    day = date.strftime("%a")

    timezones = ["America/Los_Angeles", "America/New_York"]
    times = findTimes(timezones)
    temp = times[0]
    day = date.strftime("%a")
    hour = int(date.strftime("%H"))
    minute = int(date.strftime("%M"))
    return render(request, "html/index.html", {
        "times": times,
        "day": day,
        "extendedHours": isExtendedHours(day, hour, minute)
    })

