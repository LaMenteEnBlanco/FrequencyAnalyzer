'''
Created on 02.10.2018

@author: jakob
This class is meant as a filter. It needs the input array that contains values below and aboe 40.000.
It iterates through the array searches for values greater than 40.000. It puts those values in a dictionary 
with the corresponding index as key. 
The resulting dictionary is printed out to the command window.
'''

import numpy as np

class DataAnalyse:
    '''
    classdocs
    '''


    def __init__(self, yfAbs):
        '''
        Constructor
        '''
        self.yfAbs = yfAbs.tolist()
        self.resultDic = {}
    
    def formants(self):    
        for i in range(0, len(self.yfAbs)):
            if i == 0:
                self.yfAbs[i]= 0
                
            if self.yfAbs[i]>40000:
                self.resultDic[i] = self.yfAbs[i]
            
        print(self.resultDic)    
            
            