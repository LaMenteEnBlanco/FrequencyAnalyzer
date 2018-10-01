'''
Created on 05.09.2018

@author: jakob
The included method, listPlot() prints out a diagramm of the input array. 

'''

import pyaudio
import wave, struct
from numpy.fft import rfft
import numpy as np
import matplotlib.pyplot as plt

class ListPlot:  
    def __init__(self, array):
        self.array = array
        # Number of samplepoints
        self.N = len(self.array)/2
        # sample spacing
        self.T = 2.0 /44100
        self.xf = np.linspace(0.0, 1.0/(2.0*self.T), self.N/2)
    def listPlot(self):
    
        yf = rfft(self.array)
        #xf = rfftfreq(44100)

        fig, ax = plt.subplots()
        ax.plot(self.xf, 2.0/self.N * np.abs(yf[:self.N//2]))
        #ax.plot(range(len(2.0/self.N * np.abs(yf[:self.N//2]))),2.0/self.N * np.abs(yf[:self.N//2]))
        plt.show() 
        k=0
        return
    def getScaledArray(self):
        return self.yf
    
    def getSamplePointNumber(self):
        return self.N