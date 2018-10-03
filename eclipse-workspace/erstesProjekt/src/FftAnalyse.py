'''
Created on 03.10.2018

@author: jakob
'''
import pyaudio
import wave, struct
from numpy.fft import rfft
import numpy as np
import matplotlib.pyplot as plt

class FftAnalyse:
    '''
    classdocs
    '''


    def __init__(self, audioArray):
        '''
        Constructor
        '''
        self.audioArray = audioArray
        # Number of samplepoints
        self.N = len(self.audioArray)/2
        # sample spacing
        self.T = 2.0 /44100
        self.xf = np.linspace(0.0, 1.0/(2.0*self.T), self.N/2)
    
    def fftAnalyse(self):
        self.yf = rfft(self.audioArray)
        self.yfAbs =  np.abs(self.yf[:self.N//2])
        return self.yfAbs
    
    def getXf(self):
        return self.xf
    
    def getSamplePointNumber(self):
        return self.N