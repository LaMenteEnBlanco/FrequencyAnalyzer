'''
Created on 02.10.2018

@author: jakob
'''

import numpy as np

class DataAnalyse:
    '''
    classdocs
    '''


    def __init__(self, yfAbs, xf):
        '''
        Constructor
        '''
        self.yfAbs = yfAbs.tolist()
        self.xf = xf.tolist()
        self.resultDic = {}
    
    def formants(self):    
        for i in range(0, len(self.yfAbs)):
            if i == 0:
                self.yfAbs[i]= 0
                
            if self.yfAbs[i]>10000:
                self.resultDic[i] = self.yfAbs[i]
            
        print(self.resultDic)    
            
            