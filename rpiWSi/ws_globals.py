#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

#weather underground api key NEED TO CHANGE
wu_api_key = 'b12345abcd9ffda0a51f'
wu_api_key = 'b5abcd9ffda0a51f'

#gps coordinates NEED TO CHANGE
wu_gps_coordinates = '55.6890593,37.2906527'
#weather underground api language
wu_language = 'RU'

#do not change!
wu_icon_set = 'k'

#choose you temperature units (C/F)
temperature_inits="celsius"
#temperature_inits="fahrenheit"


#debug=False
debug=True
show_rect = False
#show_rect = True

web_server_port=8080

#sensors_request_string = u"http://192.168.99.13/sensors"
#sensors_request_string = "test"

screen_width,screen_height = 240,320

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
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0,0,0)
BACK = (64,67,73)

app_dir = os.path.dirname(__file__) 

if __name__=="__main__":
    import rpiWSi,os
    if os.uname()[0]=="Linux":
        rpiWSi.ws_start(90)
    else:
        rpiWSi.ws_start(0)
