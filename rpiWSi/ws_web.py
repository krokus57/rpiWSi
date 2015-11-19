#!/usr/bin/env python
# -*- coding: utf-8 -*-


from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        self.end_headers()
        IMAGEFILE = 'image.png'
        with open(IMAGEFILE, 'rb') as imgfile:
            self.wfile.write(imgfile.read())
'''
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write("hello !")
 '''       


serv = HTTPServer(("localhost",8080),HttpProcessor)
serv.serve_forever()


'''
if __name__=="__main__":
    import rpiWSi,os
    if os.uname()[0]=="Linux":
        rpiWSi.ws_start(90)
    else:
        rpiWSi.ws_start(0)
'''