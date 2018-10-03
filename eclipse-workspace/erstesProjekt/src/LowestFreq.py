'''
Created on 03.10.2018

@author: jakob
'''

class LowestFreq:
    '''
    classdocs
    '''


    def __init__(self, yfAbs, xf):
        '''
        Constructor
        '''
        self.yfAbs = yfAbs.tolist()
        self.xf = xf.tolist()
    
    def lowestFreq(self):
        for i in range(0, len(self.yfAbs)):
           print(i)
           if ((self.yfAbs[i]>40000) and (i > 60)):
               return self.xf[i]
            