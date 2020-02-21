#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version: 1.0
# licence : gpl-3.0 or superior
# author: Gaetan Bruel
# email: gaetan.bruel@jdev.fr
# date: 20/01/2020
# description : Get SVG icons for a theme from github material.io/icons and organized by category


import os, time, shutil
from threading import Thread
import urllib.request
import json
from config import *

print('JOB START')

#### start job
error = {}
def getSvg(n, version):
    # create theme directory
    #
    themeDirectory = WORKING_PATH + '/' + THEME
    if not os.path.exists(themeDirectory):
        os.mkdir(themeDirectory)

    # Create folder and download files for each category
    #                     
    for dirpath, dirnames, files in os.walk(ORIGINAL_SVG_PATH):
        for fileName in files:
            # get category directory if not exists
            #
            category = dirpath.split('/')[-1]
            categoryDirectory = '{}/{}'.format(themeDirectory,category)
            if not os.path.exists(categoryDirectory):
                os.mkdir(categoryDirectory)

            # get icon name
            #
            iconName = fileName.replace('_24px.svg','')
            iconName = iconName.replace('24px.svg','')
            if iconName[0:3] == 'ic_':
                iconName = iconName[3:]
            
            # call icon from font api
            #
            urlIcon = URL.format(iconName, version)
            targetIcon = '{}/{}.svg'.format(categoryDirectory, iconName)
            if not os.path.exists(targetIcon):
                try:
                    urllib.request.urlretrieve(urlIcon, targetIcon)
                except:
                    if not iconName in error:
                        error[iconName] = {
                            "version":version,
                            "category": category,
                            "input": dirpath+'/'+fileName,
                            "url": urlIcon,
                            "output": targetIcon,
                            "msg": "Failed to download file. File copied and past to target."
                        }
                        if COPY:
                            shutil.copyfile(dirpath+'/'+fileName, targetIcon)
  

try:
    # Create and start thread(s)
    threadNum = 0
    while threadNum < MAX_THREAD :
        t = Thread(target=getSvg, args=(threadNum,VERSION))
        t.daemon = True
        t.start()
        t.join()
        threadNum += 1
except:
   print("Error: Error with thread")
finally:
    if len(error):
        print("JOB FINISH WITH ERRORS")
        with open(ERRORS_PATH, 'w') as outfile:
            json.dump(error, outfile)
    else : 
        print("JOB FINISH")
