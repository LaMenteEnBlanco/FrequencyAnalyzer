'''
Created on 08.08.2018

@author: jakob
Quelle: https://gist.github.com/mabdrabo/8678538#file-sound_recorder-py-L24
'''

import pyaudio
import wave, struct
from numpy.fft import rfft, rfftfreq
import numpy as np
import matplotlib.pyplot as plt
from ListPlot import ListPlot

 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
#WAVE_OUTPUT_FILENAME = "file3.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print "recording..."
frames = ''
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames = frames + data
print "finished recording"
 

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
#waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#waveFile.setnchannels(CHANNELS)
#waveFile.setsampwidth(audio.get_sample_size(FORMAT))
#waveFile.setframerate(RATE)
#waveFile.writeframes(b''.join(frames))
#waveFile.close()

#
#nb_samples = 256
chans = 1 #??
samps = len(frames)
sampwidth = 1 #??
datatype = '<{}{}'.format(samps, {1:'b',2:'h',3:'i',4:'i',8:'q'}[sampwidth])

#
frameList = struct.unpack(datatype, frames)

listPlot = ListPlot(frameList)

listPlot.listPlot()

k=0
#for i in listPlot.getScaledArray():
#    print("Formante mit Wert {} bei Index {}".format(2.0/listPlot.getSamplePointNumber() * np.abs(i), k))  

    #if (2.0/N * np.abs(yf[i])) > 40:
#    k = k + 1
