#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ws_globals,sys,datetime,time
from ws_globals import *
from datetime import *
#import requests
import time
from datetime import date
import gc
import random
import os
#print time.strftime('%a, %d %b %Y %H:%M:%S GMT%z')

import urllib2

def get_time_date():

    dt={}
    dt["current_time"] = time.strftime("%H:%M:%S")
    dt["current_time"] = time.strftime("%H:%M")
    dt["current_date"] = days_of_week[int(time.strftime("%w"))]+", "+time.strftime("%d")+\
    " "+months[int(time.strftime("%m"))]
    '''
    print time.strftime("%d")
    print time.strftime("%m")
    print time.strftime("%w")
    print time.strftime("%H")
    print time.strftime("%M")
    print time.strftime("%S")
    '''
    return dt
    
#print get_time_date()
def attach_sign(value):
    value = int(round(float(value)))
    if value>0:
        return "+"+unicode(value)
    elif value<0:
        return unicode(value)
    else:
        return "0"
        
        


def get_local_data(sensors_request_string):
    ls_data={}
    try:
        if debug:
            sensors_string = '19.6;69.9;24.7;48.1;29.7;739.34;'
        else:
            sensors_request = urllib2.urlopen(sensors_request_string)
            sensors_string = sensors_request.read()  
            sensors_request.close()
        
        sd = (sensors_string).split(";")
        
        ls_data["local_temp_out"]=attach_sign(round(float(sd[0])))
        ls_data["local_temp_in"] =attach_sign(round(float(sd[2])))
        ls_data["local_hum_out"]=int(float(sd[1]))
        ls_data["local_hum_in"]=int(float(sd[3]))
        ls_data["local_pressure"]=int(float(sd[5]))
        
        #xxx=xxx/0
        #debug data
        if debug:
            lto=random.randint(-30,30)
            if lto>0: s="+"
            else: s=""
            ls_data["local_temp_out"]=s+str(lto)
    
            ls_data["local_pressure"]=random.randint(720,760)  
            ls_data["local_hum_out"]=random.randint(99,100)

    except:
        if debug: print "Error getting sensor data:", sys.exc_info()[0]
        ls_data={}
    
    return ls_data

if __name__=="__main__":
    import rpiWSi
    if os.uname()[0]=="Linux":
        rpiWSi.ws_start(90)
    else:
        rpiWSi.ws_start(0)
