#!/usr/bin/env python
# -*- coding: utf-8 -*-

#interface language
#from lang_ru import *
from lang_en import *

#weather underground api key NEED TO CHANGE
wu_api_key = 'b12345abcd9ffda0a51f'

#gps coordinates NEED TO CHANGE
wu_gps_coordinates = '55.6890593,37.2906527'
#weather underground api language
#wu_language = 'RU'
wu_language = 'EN'

#do not change!
wu_icon_set = 'k'

#choose you temperature units (C/F)
temperature_inits="celsius"
#temperature_inits="fahrenheit"

debug=False
#debug=True

#web server port
web_server_port=8080

#screen resolution
screen_width,screen_height = 240,320


#do not change anything below

if __name__=="__main__":
    import rpiWSi,os
    if os.uname()[0]=="Linux":
        rpiWSi.ws_start(90)
    else:
        rpiWSi.ws_start(0)
