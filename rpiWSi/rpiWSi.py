#!/usr/bin/env python
# -*- coding: utf-8 -*-

#try this python code in your pygame program (don't have X11 running when you start it):
import os
#os.environ['SDL_VIDEODRIVER']="fbcon" # could be "directfb", try "aalib" for extra fun

import sys
import gc
from ws_globals import *
from ws_drawing import *
from ws_local_data import *
from ws_wu_data import *
from ws_thread_worker import *
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer


def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

def ws_start(angle=0):
    
    #serv = HTTPServer(("localhost",8080),HttpProcessor)

    class HttpProcessor(BaseHTTPRequestHandler):
        def do_GET(self):
            
            if self.path==("/img"):
                filename = os.path.realpath("{1}/{0}".format('page.png',app_dir))
                
                if angle<>0:
                    img_data = pygame.transform.rotate(screen, -angle)    
                else:
                    img_data=screen
                img=pygame.image.save(img_data, filename)
                self.send_response(200)
                self.send_header('Content-type',    'image/png')
                self.end_headers()
                with open(filename, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                
                self.send_response(200)
                self.send_header('content-type','text/html')
                self.end_headers()
                
                self.wfile.write('<html><head><meta charset="utf-8">')
                if debug: 
                    refresh_rate=5 
                else: 
                    refresh_rate=60
                    

                self.wfile.write('<meta http-equiv="refresh" content="'+str(refresh_rate)+'">')
                self.wfile.write('<title>Погодная станция</title>')
                data='<p align="center"><img src="/img" alt=""></p>'
                self.wfile.write(data)            
                self.wfile.write('</head></html>')

    
    if angle<>90 and angle <>-90 and angle<>0:angle=0
    
    if os.uname()[0]=="Linux":
        os.environ["SDL_FBDEV"] = "/dev/fb1"
    
    TIME_UPDATE_EVENT = USEREVENT
    WU_DATA_UPDATE_EVENT = USEREVENT+1
    LOCAL_DATA_UPDATE_EVENT = USEREVENT+2
    
    def show_sizeof(x,level=0):
        #print "\t"*level,x.__class__, sys.getsizeof(x)#, x
        child_size=0
        if hasattr(x,'__iter__'):
            if hasattr(x,'items'):
                for xx in x.items():
                    child_size=child_size+show_sizeof(xx,level+1)
            else:
                for xx in x:
                    child_size=child_size+show_sizeof(xx,level+1)
        return sys.getsizeof(x) + child_size 
    
    def save_wu_data(args):
        
        data.update(args)
        #print "WU", args
    
    #===========================================================================
    # def save_local_data(args):
    #    
    #     data.update(args)
    #     
    #===========================================================================
    try:
        print "Starting web server"
        serv = HTTPServer(('',web_server_port),HttpProcessor)
        serv.timeout=0
        print "Ok. Using tcp port: "+str(web_server_port)
    except:
        print"Error opening tcp port:" + str(web_server_port)
        print "Stopped!"
        return
        
    pygame.init()
    
    if os.uname()[0]=="Linux":
        screen = pygame.display.set_mode((screen_height,screen_width))
    else:
        #if system screen orientation landscape change width and height
        if angle<>0:
            screen = pygame.display.set_mode((screen_height,screen_width))
        else:
            screen = pygame.display.set_mode((screen_width,screen_height))
    
    
    
    pygame.display.set_caption('RPi weather station')
    pygame.display.toggle_fullscreen()
    
    #hide mouse in Linux
    if os.uname()[0]=="Linux":
        pygame.mouse.set_visible(False)
    
    screen.fill(BACK)
    #pygame.mouse.set_visible(0)
    
    #print pygame.display.Info()
    
    data={}
    
    dt_data=get_time_date()
    data.update(dt_data)
    
    page=0
    draw_data(screen,page,data,angle)
    pygame.display.flip()

    add_worker1 = ThreadWorker(get_wu_data,save_wu_data)
    add_worker1.start((wu_api_key, wu_gps_coordinates, wu_language, wu_icon_set))

    #add_worker2 = ThreadWorker(get_local_data,save_local_data)
    #add_worker2.start((sensors_request_string,))
    
    if debug:  
        pygame.time.set_timer(TIME_UPDATE_EVENT, 1000) #redraw screen
        pygame.time.set_timer(WU_DATA_UPDATE_EVENT, 1000) #get weather underground data
        #pygame.time.set_timer(LOCAL_DATA_UPDATE_EVENT, 1000) #get local sensor data
    else:
        pygame.time.set_timer(TIME_UPDATE_EVENT, 1000) #redraw screen
        pygame.time.set_timer(WU_DATA_UPDATE_EVENT, 1000*60*20) #get weather underground data
        #pygame.time.set_timer(LOCAL_DATA_UPDATE_EVENT, 1000*60*5) #get local sensor data
    
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT or event.type ==MOUSEBUTTONUP:
                gc.collect()#unused memory clean
                pygame.display.flip()#redraw screen
                pygame.quit()
                serv.server_close()
                #serv.socket.close()
                sys.exit()
                return
            elif event.type == TIME_UPDATE_EVENT: #redraw time and data
                dt_data=get_time_date()
                data.update(dt_data)
     
                draw_data(screen,page,data,angle)
                pygame.display.flip()
                
                #pygame.image.save(screen, "using_sprites.png")  
                #redraw 
                #pygame.display.update()
                #print gc.collect()
            elif event.type == WU_DATA_UPDATE_EVENT: # weather underground data
                pass    
                add_worker1 = ThreadWorker(get_wu_data,save_wu_data)
                add_worker1.start((wu_api_key, wu_gps_coordinates, wu_language, wu_icon_set))
                
            #===================================================================
            # elif event.type == LOCAL_DATA_UPDATE_EVENT:# local sensor data
            #     pass
            #     add_worker2 = ThreadWorker(get_local_data,save_local_data)
            #     add_worker2.start((sensors_request_string,))
            #===================================================================

        serv.handle_request()

        pygame.time.delay(200)
        #pygame.event.wait()

if __name__=="__main__":
    if os.uname()[0]=="Linux":
        ws_start(90)
    else:
        ws_start(0)

'''

sync -r -a -v -e "ssh -l root" /Users/rim/Dropbox/WPC/Python/rpiWS   root@192.168.99.25:/root/


'''
        
#if __name__=="__main__":
#    print format_temperature("+21.0")
#    print format_temperature('-25')
#    print format_temperature("+21")
#    print format_temperature('-25.9')
#    print format_temperature('0.0')
    