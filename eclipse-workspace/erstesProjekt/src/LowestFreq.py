'''
Created on 03.10.2018

@author: jakob 
THis class needs two arrays from an fft-analysis-result. One is the x-Axis which contains 
the frequenzies. The other is the y-Axis which contains the corresponding intensity to each 
frequenzy.
The method lowestFreq detects frequenzy peaks in the spectrum. It
detects the peak with the smallest frequenzy above 60 Hz, that holds an intensity greater than
40000 units.
It returns the frequenzy value of the detected peak in the intensity spectrum. 
'''

class LowestFreq:
    '''
    classdocs
    '''


    def __init__(self, intensityArray, frequenzyArray):
        '''
        Constructor
        '''
        #
        self.intensityArray = intensityArray.tolist()
        self.frequenzyArray = frequenzyArray.tolist()
    
    def lowestFreq(self):
        for i in range(0, len(self.intensityArray)):
           print(i)
           if ((self.intensityArray[i]>40000) and (i > 60)):
               return self.frequenzyArray[i]
            