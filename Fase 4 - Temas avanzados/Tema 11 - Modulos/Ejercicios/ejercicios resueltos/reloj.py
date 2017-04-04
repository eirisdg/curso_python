#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: eirisdg
"""
from time import sleep
import datetime

for i in range(0,60,1):
    dt = datetime.datetime.now()
    print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
    sleep(1)