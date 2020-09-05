from infi.systray import SysTrayIcon
from var import readConfig, writeConfig
import sys
import time 
import csv
import os
import signal

def getApplicationPerSlider():
    config = readConfig()
    slider = []
    i = 1
    for sliders in config:
        if sliders == "":
            slider.append("Slider-" + str(i) + " --Empty--")
            i += 1
            continue
        slider.append("Slider-" + str(i) + " " + sliders)
        i += 1
    return slider

def submenu(sysTrayIcon):
        print("Klicked on Submenu")

def killAll(sysTrayIcon):
    pid = os.getpid()
    os.kill(pid, signal.SIGTERM)
    print("Didnt Kill PID: " + str(pid))

def removeFromConfig(i):
       print(str(i))

def trayMenu():
    slider = getApplicationPerSlider()

    hover_text = "PyNK2"
    sub_menu = [
        (slider[0], None, submenu),
        (slider[1], None, submenu),
        (slider[2], None, submenu),
        (slider[3], None, submenu),
        (slider[4], None, submenu),
        (slider[5], None, submenu),
        (slider[6], None, submenu),
        (slider[7], None, submenu)
    ]

    menu_options = (
        (slider[0], None, submenu),
        (slider[1], None, submenu),
        (slider[2], None, submenu),
        (slider[3], None, submenu),
        (slider[4], None, submenu),
        (slider[5], None, submenu),
        (slider[6], None, submenu),
        (slider[7], None, submenu),
        ('RemoveFromSlider', "../slider.ico", sub_menu),
    )

    sysTrayIcon = SysTrayIcon("../slider.ico", hover_text, menu_options, on_quit=killAll, default_menu_index=1)
    sysTrayIcon.start()