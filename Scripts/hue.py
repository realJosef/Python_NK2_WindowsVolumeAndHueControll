from phue import Bridge
import random

b = Bridge('192.168.178.115')

def Hue_Color(color, light):
    if color == "red":
        command = {'on' : True, 'bri' : 254, 'xy' : [0.6827, 0.3047]}
        b.set_light(light, command)
    if color == "blue":
        command = {'on' : True, 'bri' : 254, 'xy' : [0.1356, 0.0475]}
        b.set_light(light, command)
    if color == "white":
        command = {'on' : True, 'bri' : 254, 'ct' : 500}
        b.set_light(light, command)
    if color == "orange":
        command = {'on' : True, 'bri' : 254, 'xy' : [0.6117, 0.3682]}
        b.set_light(light, command)
    pass

def Hue_Switch(light, switch):
    b.set_light(light, 'on', switch)
    pass
    
def Hue_Bri(light, value):
    b.set_light(light, 'bri', value * 2)
    pass

def Hue_Toggle(light):
    if b.get_light(light, 'on') == True:
        Hue_Switch(light, False) 
    elif b.get_light(light, 'on') == False:
        Hue_Switch(light, True)

def setHueColorKnob(light, value):
    if value in range(0, 11):
        Hue_Switch(light, False)
    if value in range(20, 40):
        Hue_Color("orange", light)
    if value in range(40, 60):
         Hue_Color("white", light)
    if value in range(60, 80):
        Hue_Color("blue", light)
    if value in range(80, 101):
        Hue_Color("red", light)