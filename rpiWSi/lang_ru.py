#!/usr/bin/env python
# -*- coding: utf-8 -*-

days_of_week={1:u"пн",
              2:u"вт",
              3:u"ср",
              4:u"чт",
              5:u"пт",
              6:u"сб",
              0:u"вс"}

months={
        1 :u"января",
        2 :u"февраля",
        3 :u"марта",
        4 :u"апреля",
        5 :u"мая",
        6 :u"июня",
        7 :u"июля",
        8 :u"августа",
        9 :u"сентября",
        10:u"октября",
        11:u"ноября",
        12:u"декабря",
        }


short_months={
        1 :u"янв",
        2 :u"фев",
        3 :u"мар",
        4 :u"апр",
        5 :u"мая",
        6 :u"июн",
        7 :u"июл",
        8 :u"авг",
        9 :u"сен",
        10:u"окт",
        11:u"ноя",
        12:u"дек",
        }

#other localizing strings:
str_tomorrow=u"Завтра"
str_pressure=u"Давление"
str_humidity=u"Влажность"
str_wind=u"Ветер"
str_pressure_units_line_1=u"мм"
str_pressure_units_line_2=u"рт"
str_pressure_units_line_3=u"ст"
str_wind_speed=u"м/с"






#do not change anything below

if __name__=="__main__":
    import rpiWSi,os
    if os.uname()[0]=="Linux":
        rpiWSi.ws_start(90)
    else:
        rpiWSi.ws_start(0)


