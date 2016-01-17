#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from settings import *

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0,0,0)
BACK = (64,67,73)

app_dir = os.path.dirname(__file__) 

show_rect = False
#show_rect = True


if __name__=="__main__":
    import rpiWSi,os
    if os.uname()[0]=="Linux":
        rpiWSi.ws_start(90)
    else:
        rpiWSi.ws_start(0)
