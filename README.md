##Raspberry PI based desktop weather forecast station and clock with 3.2 lcd display.

###Hardware setup:

-   Raspberry PI model B https://www.raspberrypi.org/products/model-b/
-   3.2" LCD display for raspberry PI http://www.aliexpress.com/item/Free-Shipping-2014-New-Arrival-1Pcs-3-2-Inch-LCD-Touch-Screen-Display-Monitor-Module-For/1975039117.html
-   USB Wi-fi dongle http://www.tp-linkru.com/products/details/cat-11_TL-WN725N.html
-   SD card

In order to get smaller box I need to:
- unsolder two ports (audio jack and composite video port)
- solder power wires directly to a usb port

The idea of dock from http://www.thingiverse.com/thing:525241

###Software setup:

Python source code: https://github.com/krokus57/rpiWSi

You need to have:
-  some experience in linux and programing
-  working internet connection
-  install python 2.7
-  pygame framework
-  get api key from api.weatherunderground.com
-  weather icons

I use great VClouds icons from 
    http://www.deviantart.com/art/VClouds-Weather-2-179058977
#####You have to get permission from author to use them in you project!

For the first run change next lines in file globals.py:

    #==============================================================
    #interface language. uncomment one of them. you can create you own language file and use it here
    #from lang_ru import *
    from lang_en import *
    
    #weather underground api key NEED TO CHANGE
    wu_api_key = 'b12345abcd9ffda0a51f'
    
    #gps coordinates NEED TO CHANGE
    wu_gps_coordinates = '55.6890593,37.2906527'
    #weather underground api language. Must be exactly as declared in WeatherUnderground API
    #wu_language = 'RU'
    wu_language = 'EN'
    
    #do not change!
    wu_icon_set = 'k'
    
    #choose you temperature units (C/F)
    temperature_inits="celsius"
    #temperature_inits="fahrenheit"
    
    #enable demo data without internet connection
    debug=False
    #debug=True
    
    #web server port
    #After successfull setup you can get current screenshot from raspberry using browser:
    #http://raspberry_ip:8080
    web_server_port=8080
    
    #screen resolution
    screen_width,screen_height = 240,320
    #if you want to change resolution you need to completely rewrite function 
    #draw_data(screen,page,data,angle) in file ws_drawing.py
    #==============================================================


Change lang_XX.py file if you need: XX=RU or EN or yours new file:

    #==============================================================
    next arrays are the names of days and months on you language
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
    #==============================================================


All other work for drawing on the screen see in file ws_drawing.py

    function draw_data(screen,page,data,angle)

run the code from console inside rpiWSi folder with command :

    python rpiWSi.py

After successfull setup you can get current screenshot from raspberry using browser:

    http://raspberry_ip:8080

