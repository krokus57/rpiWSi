#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame, sys
from pygame.locals import *
import pygame.gfxdraw
import os
import ws_globals
from ws_globals import *
import time
from datetime import date
from datetime import *

def draw_data(screen,page,data,angle):
    
    def draw_text(screen,text,font,size,left,top,width,align="center",text_color=WHITE,back_color=BACK):
        global app_dir
        
        font = os.path.realpath("{1}/{0}".format(font,app_dir))
                
        font = pygame.font.Font(font, size)
        
        surface = font.render(text, True, text_color, back_color)
        rect=surface.get_rect()
        height=rect.height
        if align=="center":
            rect.center = (width/2+left,rect.height/2+top)
        if align=="left":
            rect.center = (rect.width/2+left,rect.height/2+top)
        if align=="right":
            rect.center = (left+width-rect.width/2,rect.height/2+top)
    
    
    
        #surface = pygame.transform.smoothscale(surface, (rect.width, rect.height))    
        unrotated_rect=rect
        if angle==90:
            rotatedSurf = pygame.transform.rotate(surface, 90)    
            rect2 = rotatedSurf.get_rect()
            rect2.left=rect.top
            rect2.top=screen_width-rect.left-rect.width
            rect=rect2
            surface=rotatedSurf    
            fill_rect=Rect(top,screen_width-left-width,height,width)
        elif angle==-90:
            rotatedSurf = pygame.transform.rotate(surface, -90)    
            rect2 = rotatedSurf.get_rect()
            rect2.left=screen_height-rect.top-rect.height
            rect2.top=rect.left
            
            rect=rect2
            surface=rotatedSurf
            fill_rect=Rect(screen_height-top-height,left,height,width)
        else:
            fill_rect=Rect(left,top,width,rect.height)
            
        screen.fill(BACK, fill_rect)
        screen.blit(surface, rect)
        if show_rect: pygame.gfxdraw.rectangle(screen, rect, WHITE)
        return unrotated_rect
    
    def draw_image(screen,file_name, screen_rect,back_color=BACK):
        global app_dir
        file_name = os.path.realpath("{1}/{0}".format(file_name,app_dir))
        
        surface = pygame.image.load(file_name)
        rect = surface.get_rect()
    
        if screen_rect.width ==0: screen_rect.width =rect.width
        if screen_rect.height==0: screen_rect.height=rect.height
        
        #rect=rect.fit(screen_rect)
        rect=rect.fit(Rect(0,0,screen_rect.width,screen_rect.height))
        if rect.width<screen_rect.width:
            rect.left=screen_rect.left+(screen_rect.width-rect.width)/2
        else:
            rect.left = screen_rect.left
        rect.top=screen_rect.top
        surface = pygame.transform.smoothscale(surface, (rect.width, rect.height))    
    
        if angle==90:
            rotatedSurf = pygame.transform.rotate(surface, 90)    
            rect2 = rotatedSurf.get_rect()
            rect2.left=rect.top
            rect2.top=screen_width-rect.left-rect.width
            rect=rect2
            surface=rotatedSurf
            screen.fill(back_color, rect)
            screen.blit(rotatedSurf, rect)
        elif angle==-90:
            rotatedSurf = pygame.transform.rotate(surface, -90)    
            rect2 = rotatedSurf.get_rect()
            rect2.left=screen_height-rect.top-rect.height
            rect2.top=rect.left
            rect=rect2
            surface=rotatedSurf
            screen.fill(back_color, rect)
            screen.blit(rotatedSurf, rect)
        
        screen.fill(back_color, rect)
        screen.blit(surface, rect)
    
        if show_rect: pygame.gfxdraw.rectangle(screen, rect, WHITE)  
        return rect 
    
    #date and time
    text=data.get("current_time")
    draw_text(screen,text,'fonts/calibrib.ttf',81, 0,  0, screen_width,"center",WHITE,BACK)
    #draw_text(screen,text,'fonts/calibrib.ttf',61, 0,  0, screen_width,"center",WHITE,BACK)
    text=data.get("current_date")
    draw_text(screen,text,'fonts/calibrib.ttf',18, 0, 65, screen_width,"center",WHITE,BACK)
    
    #temp today
    yy=87
    text=format_temperature(data.get("local_temp_out"))
    if text<>None: text=text+u"°"
    draw_text(screen,text,'fonts/calibri.ttf' ,60, screen_width/2, yy, screen_width/2,"center",WHITE,BACK)

    #image forecast today
    if data.get("image_0")<>None:
        draw_image(screen,'images/'+unicode(data.get("image_0")), Rect(0,yy-4,screen_width/2,76),BACK)
           
   #forecast today
    yy=yy+50
    text=format_temperature(data.get("temp_fore_0_min"))+u"° / "+format_temperature(data.get("temp_fore_0_max"))+u"°"
    draw_text(screen,text,'fonts/calibrib.ttf',18, screen_width/2, yy, screen_width/2,"center",WHITE,BACK)

    
    text=data.get("conditions_0")
    if debug:
        text= u"Переменная облачность"
    yy=160
    draw_text(screen,text,'fonts/calibrib.ttf',18, 0, yy, screen_width,"center",WHITE)
 
 
     #Давление влажность ветер (заголовки)
    yy=186
    text=str_pressure
    draw_text(screen,text,'fonts/calibri.ttf',16, 0               , yy, screen_width/3,"center",WHITE,BACK)
    text=str_wind
    draw_text(screen,text,'fonts/calibri.ttf',16, screen_width/3  , yy, screen_width/3,"center",WHITE,BACK)
    text=str_humidity
    draw_text(screen,text,'fonts/calibri.ttf',16, screen_width/3*2, yy, screen_width/3,"center",WHITE,BACK)

    #Давление влажность ветер(данные)
    yy=yy+14
    fs=34
    ww=8
    text=correct_data(data.get("local_pressure"))
    #text=text+u"мм"
    pressure_rect=draw_text(screen,text,'fonts/calibri.ttf',fs, 0-ww               , yy, screen_width/3,"center",WHITE,BACK)
    text=correct_data(data.get("wind_kph"))
    #text=text+u"м/с"
    wind_rect=draw_text(screen,text,'fonts/calibri.ttf',fs, screen_width/3-ww  , yy, screen_width/3,"center",WHITE,BACK)
    text=correct_data(data.get("local_hum_out"))
    #text=text+u"%"
    humidity_rect=draw_text(screen,text,'fonts/calibri.ttf',fs, screen_width/3*2-ww, yy, screen_width/3,"center",WHITE,BACK)
 

    #Давление влажность ветер (единицы измерения)
    yy=pressure_rect.top+2
    xx=pressure_rect.left+pressure_rect.width+4
    ww=ww
    text=str_pressure_units_line_1
    p_ei=draw_text(screen,text,'fonts/calibri.ttf',10, xx , yy, ww,"center",WHITE,BACK)
    text=str_pressure_units_line_2
    yy=pressure_rect.top+pressure_rect.height/3
    p_ei=draw_text(screen,text,'fonts/calibri.ttf',10, xx , yy, ww,"center",WHITE,BACK)
    yy=pressure_rect.top+pressure_rect.height/3*2-2
    text=str_pressure_units_line_3
    p_ei=draw_text(screen,text,'fonts/calibri.ttf',10, xx , yy, ww,"center",WHITE,BACK)
    
    yy=wind_rect.top+humidity_rect.height/3
    xx=wind_rect.left+wind_rect.width+6
    text=str_wind_speed
    p_ei=draw_text(screen,text,'fonts/calibri.ttf',10, xx , yy, ww,"center",WHITE,BACK)
    
    yy=humidity_rect.top+humidity_rect.height/3
    xx=humidity_rect.left+humidity_rect.width+3
    text=u"%"
    p_ei=draw_text(screen,text,'fonts/calibri.ttf',10, xx , yy, ww,"center",WHITE,BACK)
    
     #dates for forecast
    yy=240
    text=str_tomorrow
    rr=draw_text(screen,text,'fonts/calibri.ttf',13, 0               , yy, screen_width/3,"center",WHITE,BACK)
    
    
    next_day=date.today()+timedelta(days=2)
    wd=(next_day).isoweekday()
    if wd==7: wd=0
    text=days_of_week[wd]+", "+unicode(next_day.day)+u" "+short_months[next_day.month]
    draw_text(screen,text,'fonts/calibri.ttf',13, screen_width/3  , yy, screen_width/3,"center",WHITE,BACK)

    next_day=date.today()+timedelta(days=3)
    wd=(next_day).isoweekday()
    if wd==7: wd=0
    text=days_of_week[wd]+", "+unicode(next_day.day)+u" "+short_months[next_day.month]
    draw_text(screen,text,'fonts/calibri.ttf',13, screen_width/3*2, yy, screen_width/3,"center",WHITE,BACK)
    
    #images forecast free days
    #yy=214
    yy=yy+rr.height-1
    hh=50
    try:
        if data.get("image_1")<>None:            draw_image(screen,'images/'+data.get("image_1"), Rect(0             ,  yy,screen_width/3,hh),BACK)
    except:
        draw_image(screen,'images/na.png', Rect(0             ,  yy,screen_width/3,hh),BACK)
        
    try:
        if data.get("image_2")<>None:
            draw_image(screen,'images/'+data.get("image_2"), Rect(screen_width/3,  yy,screen_width/3,hh),BACK)
    except:
        draw_image(screen,'images/na.png', Rect(screen_width/3,  yy,screen_width/3,hh),BACK)
        
    try:
        if data.get("image_3")<>None:
            draw_image(screen,'images/'+data.get("image_3"), Rect(screen_width/3*2,yy,screen_width/3,hh),BACK)
    except:
        draw_image(screen,'images/na.png', Rect(screen_width/3*2,yy,screen_width/3,hh),BACK)
        
    #draw_image(screen,'images/'+data.get("image_2"), Rect(screen_width/3,  yy,screen_width/3,0),BACK)
    #draw_image(screen,'images/'+data.get("image_3"),+ Rect(screen_width/3*2,yy,screen_width/3,0),BACK)
    
    #temp forecast free days
    yy=yy+hh-2
    text=format_temperature(data.get("temp_fore_1_min"))+u"°,"+format_temperature(data.get("temp_fore_1_max"))+u"°"
    draw_text(screen,text,'fonts/calibrib.ttf',17, 0               , yy, screen_width/3,"center",WHITE,BACK)
    text=format_temperature(data.get("temp_fore_2_min"))+u"°,"+format_temperature(data.get("temp_fore_2_max"))+u"°"
    draw_text(screen,text,'fonts/calibrib.ttf',17, screen_width/3  , yy, screen_width/3,"center",WHITE,BACK)
    text=format_temperature(data.get("temp_fore_3_min"))+u"°,"+format_temperature(data.get("temp_fore_3_max"))+u"°"
    draw_text(screen,text,'fonts/calibrib.ttf',17, screen_width/3*2, yy, screen_width/3,"center",WHITE,BACK)
    
    #pygame.draw.line(screen, WHITE, (0, 300), (240, 300), 2)
    #text="www.imarh.ru"
    #draw_text(screen,text,'fonts/calibri.ttf',18, 0, 302, screen_width,"center",WHITE,BACK)





def correct_data(val):
    if val==None:
        return u"н.д."
    else:
        return unicode(val)
    
def format_temperature(temp):
    try:
        f=int(round(float(temp)))
        if f>0:
            return u"+"+unicode(f)
        if f<0:
            return unicode(f)
        if f==0:
            return unicode(f)
    except:
        return correct_data(temp)  
    return correct_data(temp)  

def wu2int_value(val):
    try:
        val=int(round(float(val)))
        return val
    except:
        return None 
    return None


if __name__=="__main__":
    import rpiWSi
    if os.uname()[0]=="Linux":
        rpiWSi.ws_start(90)
    else:
        rpiWSi.ws_start(0)
        


