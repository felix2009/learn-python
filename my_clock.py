#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def clock_display(hour, minute, second):
    hour_output = str(hour)
    minute_output = str(minute)
    second_output = str(second)

    if hour < 10:
        hour_output ='0' + hour_output
    if minute < 10:
        minute_output = '0' + minute_output
    if second < 10:
        second_output = '0' + second_output

    time_output = hour_output + ':' + minute_output + ':' + second_output
    print(time_output, end='\r')
    return


def my_clock(start_hour, start_minute, start_second):
    hour = start_hour
    minute = start_minute
    second = start_second

    while True:
        #计算时，分和秒
        second = second + 1
        if second == 60:
            second = 0
            minute = minute + 1

        if minute == 60:
            minute = 0
            hour = hour + 1

        #过完一天
        if hour == 24:
            hour = 0

        #显示分和秒
        clock_display(hour, minute, second)
        time.sleep(1)

    return

my_clock(23, 59, 24)
