'''
Created on 08.08.2018

@author: jakob
Quelle: https://gist.github.com/mabdrabo/8678538#file-sound_recorder-py-L24
'''

import pyaudio
import wave, struct
from numpy.fft import rfft
import numpy as np
import matplotlib.pyplot as plt

 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file3.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print "recording..."
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print "finished recording"
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

#N und T wurden durch ausprobieren ermittelt
# Number of samplepoints
N = 44100*0.5
# sample spacing
T = 1.0 / 2700

xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
yf = rfft(frames)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show() 
