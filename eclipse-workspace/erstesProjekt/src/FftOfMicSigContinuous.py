'''
Created on 03.10.2018

@author: jakob
'''

import pyaudio
import wave, struct
from numpy.fft import rfft, rfftfreq
import numpy as np
import matplotlib.pyplot as plt
from ListPlot import ListPlot
from DataAnalyse import DataAnalyse
from FftAnalyse import FftAnalyse
from LowestFreq import LowestFreq
 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 0.5
 
while True:
    audio = pyaudio.PyAudio()
 
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    print "rec..."
    frames = ''
 
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames = frames + data
    
    print "fin"
 
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    #nb_samples = 256
    chans = 1 #??
    samps = len(frames)
    sampwidth = 1 #??
    datatype = '<{}{}'.format(samps, {1:'b',2:'h',3:'i',4:'i',8:'q'}[sampwidth])
    frameList = struct.unpack(datatype, frames)

    #Analyse and Plotting
    fftAnalyse = FftAnalyse(frameList)
    lowestFreq = LowestFreq(fftAnalyse.fftAnalyse(), fftAnalyse.getXf())
    print(lowestFreq.lowestFreq())
