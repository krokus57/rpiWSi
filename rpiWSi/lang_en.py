#!/usr/bin/env python
# -*- coding: utf-8 -*-


days_of_week={1:u"Mon",
              2:u"Tue",
              3:u"Wed",
              4:u"Thur",
              5:u"Fri",
              6:u"Sat",
              0:u"Sun"
          }

months={
        1 :u"January",
        2 :u"February",
        3 :u"March",
        4 :u"April",
        5 :u"May",
        6 :u"June",
        7 :u"July",
        8 :u"August",
        9 :u"September",
        10:u"October",
        11:u"November",
        12:u"December",
        }


short_months={
        1 :u"JAN",
        2 :u"FEB",
        3 :u"MAR",
        4 :u"APR",
        5 :u"MAY",
        6 :u"JUN",
        7 :u"JUL",
        8 :u"AUG",
        9 :u"SEP",
        10:u"OCT",
        11:u"NOV",
        12:u"DEC",
        }



#other localizing strings:
str_tomorrow=u"Tomorrow"
str_pressure=u"Pressure"
str_humidity=u"Humidity"
str_wind=u"Wind"
str_pressure_units_line_1=u"mm"
str_pressure_units_line_2=u""
str_pressure_units_line_3=u"Hg"
str_wind_speed=u"m/s"






#do not change anything below

if __name__=="__main__":
    import rpiWSi,os
    if os.uname()[0]=="Linux":
        rpiWSi.ws_start(90)
    else:
        rpiWSi.ws_start(0)


