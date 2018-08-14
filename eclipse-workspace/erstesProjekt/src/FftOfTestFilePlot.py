'''
Created on 08.08.2018

@author: jakob
'''

#TestFile Name: test100_300_500_700_44100.wav
#channels: mono
#length: 8s
#frameRate: 44100 fps

#Code-Quelle: https://stackoverflow.com/questions/6951046/pyaudio-help-play-a-file
#Plot ist aus:
#https://stackoverflow.com/questions/25735153/plotting-a-fast-fourier-transform-in-python



import pyaudio
import wave, struct
from numpy.fft import rfft
import numpy as np
import matplotlib.pyplot as plt




 
#FORMAT = pyaudio.paInt16
#CHANNELS = 1
#RATE = 44100
CHUNK = 1024
#RECORD_SECONDS = 5
WAVE_INPUT_FILENAME = "test100_300_500_700_44100.wav"

#Opening the audio-file and saving it into the stream with the name wf
wf = wave.open(WAVE_INPUT_FILENAME, 'rb')
audio = pyaudio.PyAudio()
 
# 
stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()), 
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(), 
                    output=True
            )


#Playing
'''
data = wf.readframes(CHUNK)
print(data)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)
    print(data)
print( "Data-String:"+ data +"\n done" )

stream.write(data)
data = wf.readframes(CHUNK)

print(data)

'''


#Quelle: https://stackoverflow.com/questions/41871445/python-wave-readframe-to-numpy-areay-for-fft
#Quelle2: https://stackoverflow.com/questions/19709018/convert-3-byte-stereo-wav-file-to-numpy-array
nb_samples = 256
chans = wf.getnchannels()
samps = wf.getnframes()
sampwidth = wf.getsampwidth()
datatype = '<{}{}'.format(samps*chans, {1:'b',2:'h',3:'i',4:'i',8:'q'}[sampwidth])


waveData = wf.readframes(samps)

#print(len(waveData))


frame = struct.unpack(datatype, waveData)
fft = abs(rfft(frame))**2
print(fft)
#Stopping
stream.close()
audio.terminate()

wf.close()
#N und T wurden durch ausprobieren ermittelt
# Number of samplepoints
N = 44100*0.5
# sample spacing
T = 1.0 / 2700

xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
yf = rfft(frame)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show() 
