# * Imports
from pydub.playback import play # to play an audio file
from scipy.io import wavfile
from tkinter import *
from random import randint, shuffle
import subprocess, threading, time
import librosa # audio file management
import os
from math import sqrt


# * CLICKS PER SECOND METER
time_frames = []
def estimateClicks():
    global time_frames
    time_frames.append(time.time())
    length_list = len(time_frames)
    N = 6
    if length_list > 1:
        # If two times are considerably far from eachother, we throw away the former times, only leaving the last one, i.e., resetting timer

        if time_frames[-1] - time_frames[-2] > 2:
            time_frames = time_frames[-1:]
            tempo = 0
            return tempo

        else:
            if length_list < N:
                interval = (time_frames[-1] - time_frames[0]) / (length_list - 1)
            else:
                interval = (time_frames[-1] - time_frames[-N]) / (N - 1)
            tempo = int(60/interval)

            return tempo
    else:
        # Continue to click until more than 1 entry
        tempo = 0
        return tempo

# * RGB VALUE
def rgbString(r, g, b):
    # Don't worry about the :02x part, but for the curious,
    # it says to use hex (base 16) with two digits.
    return f'#{r:02x}{g:02x}{b:02x}'


# * onTrackDistance
def onTrackDistance(app):
    '''
    Calculate the distance if player was on track:
    '''
    app.timeRunning = app.timeSeconds - app.timeCounter.value
    app.percentageTimeOfTotal = ( app.timeRunning / app.timeSeconds )
    on_track_distance = app.percentageTimeOfTotal * app.distanceMeters
    return on_track_distance


# * RESET APP VALUES
def resetAll(app):
    app.distanceTextBox.text = "Distance goal (meters) : "
    app.timeTextBox.text = "Time goal (minutes) : "
    app.heightTextBox.text = "Height (meters):  "
    app.timerDelay = 20


# * SETUP INSTRUCTIONS
def setupInstructions(app):
    app.instructions = '''

    Rhythm is an application devoted to aiding runners in
    maintaining a desired pace through the music they listen to.

    Instructions:
    Press 'Space' to simulate each step of your run
    Use the 'Left' and 'Right' arrows to move your avatar

    Click on 'Set Goal' for Rhythm to help you achieve a
    specific running goal in terms of distance and time

    Click on 'Adaptive' to run at your own pace, and Rhythm will
    play songs in your playlist to match your running tempo
    '''    


# * CHECK RUNNER STATUS
def checkRunnerFinished(app):
    # Congrats! made the objective
    if float(app.distanceCounter.value) >= app.distanceMeters:        
        app.mode = 'congratulationsMode'
        resetAll(app)

    # print(app.distanceCounter.value)
    # print(app.timeCounter.value, f'{app.distanceCounter.value} < {app.distanceMeters}' )
    # Runner did not make the objective
    if (app.timeCounter.value <= 0 and
        int(float(app.distanceCounter.value)) < int(app.distanceMeters)):
        app.mode = 'improvementMode'


# * INITIALIZE PLAYLIST
def getOriginalSongs():
    dir_path = r'/Users/gonzalodehermenegildo/Desktop/Projects/Rhythm/songs/originals'
    file_names = os.listdir(dir_path) # list file and directories

    # try to remove .DS_Store default mac file if there
    try: file_names.remove('.DS_Store') # remove mac os file
    except Exception: pass

    playlist = [ ]
    for song in file_names:
        # only get name of song, remove '.wav' ending
        name = song[:-4]
        name = Song('songs/originals/'+ song)
        playlist.append(name)
    return playlist


def getAlteredSongs():
    dir_path = r'/Users/gonzalodehermenegildo/Desktop/Projects/Rhythm/songs/altered'
    file_names = os.listdir(dir_path) # list file and directories
    # try to remove .DS_Store default mac file if there
    try: file_names.remove('.DS_Store') # remove mac os file
    except Exception: pass

    playlist = [ ]
    for song in file_names:
        # only get name of song, remove '.wav' ending
        name = song[:-4]
        name = Song('songs/altered/'+ song)
        playlist.append(name)
    return playlist

# * PACE CALCULATOR
def setRequiredParameters(app):
    '''
    Stride length calculation source: https://www.livestrong.com/article/438560-the-average-stride-length-in-running/
    '''
    app.distanceMeters = float(app.distanceTextBox.text[25:]) # In meters!!
    app.timeMinutes = float(app.timeTextBox.text[21: ]) # In minutes!!
    app.timeSeconds = app.timeMinutes*60
    app.heightMeters = float(app.heightTextBox.text[18: ])  # In meters!!

    app.timeCounter.value = app.timeSeconds
    app.strideMeters = app.heightMeters * 1.17

    numberSteps = int(app.distanceMeters/app.strideMeters)

    app.stepsPerMinute = int(numberSteps / app.timeMinutes)

    # rightFootStepsPerMinute = int(stepsPerMinute/2)
    app.paceCounter.value = app.stepsPerMinute

# * Reduce Decimals
def reduceDecimals(val):
    string = str(val)
    dotIndex = string.index('.')
    string = string[ : dotIndex+3]

    # add decimal 0 to end of number if only one decimal point
    newDotIndex = string.index('.')

    if len(string[newDotIndex:]) < 3: string += '0'

    return string

# * GIF LOADER
def loadAnimatedGif(path):
    # load first sprite outside of try/except to raise file-related exceptions
    spritePhotoImages = [ PhotoImage(file=path, format='gif -index 0') ]
    i = 1
    while True:
        try:
            spritePhotoImages.append(PhotoImage(file=path,
                                                format=f'gif -index {i}'))
            i += 1
        except Exception as e: return spritePhotoImages
