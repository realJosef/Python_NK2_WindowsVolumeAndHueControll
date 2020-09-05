import rtmidi, time
import win32api
from systray import *
from playsound import playsound
from audioController import *
from var import *
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from hue import *
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY, VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
m_volume = cast(interface, POINTER(IAudioEndpointVolume))
masterMuteButton = getMasterMuteButton()
focusMuteButton = getFocusMuteButton()
trayMenu()

def midiCallback(message, data):
    currentFocusedWindow = getFocusedWindow()
    control = message[0][1]
    value = message[0][2]
    if (control in buttons):
        def presetButton():
            if applications[int(name[-1])] != "FocusedWindow" and applications[int(name[-1])] != "Master":
                return True
        name = buttons[control]
        if name in isRemoveButton():
            if presetButton():
                writeConfig(name, str(""))
        if name in isSetButton():
            if presetButton():
                writeConfig(name, str(currentFocusedWindow))
        if name in isMuteButton():
            muteButtonNumber = int(name[-1])
        try:
            if name == masterMuteButton:
                AudioController.toggle_mute(m_volume)
            if name == focusMuteButton:
                muteCurrentFocus()
            if name == "track_left":
                Hue_Toggle(2) 
            if name == "track_right":
                Hue_Toggle(1)
            if name == "play":
                win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)    
            if name == "rwd":
                win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
            if name == "fwd":
                win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
        except Exception:
                pass
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            try:
                if session.Process.name() == currentFocusedWindow and name[0] == "m" and applications[muteButtonNumber] == "FocusedWindow":
                    AudioController.toggle_mute(volume) 
                if session.Process.name() == applications[muteButtonNumber] and name[0] == "m" and applications[muteButtonNumber] != "Master" and applications[muteButtonNumber] != "FocusedWindow":
                    AudioController.toggle_mute(volume)
            except Exception:
                pass
    else:
        try:
            idx = knobs.index(control)
            if idx == 0:
                setHueColorKnob(1, value)
            if idx == 1:
                Hue_Bri(1, value)
            if idx == 2:
                setHueColorKnob(2, value)
            if idx == 3:
                Hue_Bri(2, value)
        except ValueError:
            pass
        try:
            idx = sliders.index(control)
            if value == 25:
                playsound('../Audio/beep25.mp3')
                time.sleep(0.1)
            elif value == 50:
                playsound('../Audio/beep50.mp3')
                time.sleep(0.1)
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                try:
                    appname = session.Process.name()
                    applicationControll(applications, idx, appname, volume, value, currentFocusedWindow)
                except Exception:
                    pass
        except ValueError:
            pass

midiin = rtmidi.MidiIn()
port = midiin.open_port(0)

while True:
    applications = readConfig()
    sessions = AudioUtilities.GetAllSessions()
    port.set_callback(midiCallback)
    time.sleep(1)