import csv

configPath = "../ConfigFile/sliders.cfg"

def readConfig():
    config = []
    with open(configPath, "r") as configfile:
        for slider in configfile:
            if len(config) < 8:
                config.append(slider.strip().split(":")[1])
    return config

def getMasterMuteButton():
    i = 0
    for x in readConfig():
        if "Master" in x:
            return "m_" + str(i)
        i += 1 

def getFocusMuteButton():
    i = 0
    for x in readConfig():
        if "FocusedWindow" in x:
            return "m_" + str(i)
        i += 1 

def writeConfig(name, appname):
    config = []
    with open(configPath, 'r') as sliderconfig:
        for line in sliderconfig:
            config.append(line.strip().split(":"))
    config[int(name[-1])][1] = appname

    with open(configPath, 'w', newline='') as sliderconfig:
        writeconfig = csv.writer(sliderconfig, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in config:
            writeconfig.writerow(line)

def isMuteButton():
    muteButtons = []
    for i in range(48, 56):
        muteButtons.append(buttons[i])
    return muteButtons

def isSetButton():
    setButtons = []
    for i in range(32, 40):
        setButtons.append(buttons[i])
    return setButtons

def isRemoveButton():
    removeButtons = []
    for i in range(65, 72):
        removeButtons.append(buttons[i])
    return removeButtons

buttons = {
    58: 'track_left',
    59: 'track_right',
    46: 'cycle',
    60: 'marker_set',
    61: 'marker_left',
    62: 'marker_right',
    43: 'rwd',
    44: 'fwd',
    42: 'stop',
    41: 'play',
    45: 'record',
    32: 's_0',
    33: 's_1',
    34: 's_2',
    35: 's_3',
    36: 's_4',
    37: 's_5',
    38: 's_6',
    39: 's_7',
    48: 'm_0',
    49: 'm_1',
    50: 'm_2',
    51: 'm_3',
    52: 'm_4',
    53: 'm_5',
    54: 'm_6',
    55: 'm_7',
    64: 'r_0',
    65: 'r_1',
    66: 'r_2',
    67: 'r_3',
    68: 'r_4',
    69: 'r_5',
    70: 'r_6',
    71: 'r_7'
}

knobs = [16, 17, 18, 19, 20, 21, 22, 23]

sliders = [0, 1, 2, 3, 4, 5, 6, 7]