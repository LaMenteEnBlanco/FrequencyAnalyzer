'''
Created on 03.10.2018

@author: jakob
This program captures the present microphone signal. It analyses the signal using fft-analyse and then 
detects the lowest formant in the spectrum above 60 Hz. The resulting frequenzy is printed out every half second.
Quelle: https://gist.github.com/mabdrabo/8678538#file-sound_recorder-py-L24 (how to record sound from mic)
Quelle 2: https://stackoverflow.com/questions/25735153/plotting-a-fast-fourier-transform-in-python (How to plot an fft
especially for me: how to treat the fft results)
Quelle 3: https://stackoverflow.com/questions/6951046/pyaudio-help-play-a-file (How to play a file with pyAudio. Helpful for me:
it is similar to import an audio file, which I needed to test the fft)
Quelle 4: https://stackoverflow.com/questions/19709018/convert-3-byte-stereo-wav-file-to-numpy-array
(Converting Wavfile into numpy array)

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
 
# Record Parameters 
format = pyaudio.paInt16
channels = 1
frameRate = 44100
chunkSize = 1024
recSeconds = 0.5
 
while True:
    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=format, channels=channels,
                rate=frameRate, input=True,
                frames_per_buffer=chunkSize)
    print "rec..."
    
    # recFrames will include the recorded audio frames
    recFrames = ''
    
    # adding the single chunks of frame to the recFrames string
    for i in range(0, int(frameRate / chunkSize * recSeconds)):
        data = stream.read(chunkSize)
        recFrames = recFrames + data
    
    print "fin"
 
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    #converting the recFrames-string into a list
    samps = len(recFrames)
    sampwidth = 1 #??
    datatype = '<{}{}'.format(samps, {1:'b',2:'h',3:'i',4:'i',8:'q'}[sampwidth])
    frameList = struct.unpack(datatype, recFrames)

    #Analyse and Printing
    fftAnalyse = FftAnalyse(frameList)
    lowestFreq = LowestFreq(fftAnalyse.fftAnalyse(), fftAnalyse.getXf())
    print(lowestFreq.lowestFreq())
