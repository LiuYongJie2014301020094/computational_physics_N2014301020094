# -*- coding: utf-8 -*-
"""
Created on Sun Jan 08 22:16:30 2017

@author: LYJ
"""

import numpy as np
import pylab as pl
import random
import math 

class cream():
    """
    diffusion，cream in coffee
    """
    def __init__(self,steps):
        self.steps=steps
        self.xy=[[0]*(101) for i in range(101)]
        for i in range(40,61):
            for j in range(40,61):
                self.xy[i][j]=1
                
    def simulate(self):
        for n in range(self.steps):
            temp1=random.randint(0,100)
            temp2=random.randint(0,100)
            if self.xy[temp1][temp2]!=0:
                temp3=random.uniform(0,1)
                if temp3<=0.25:
                    if temp2-1>=0 and self.xy[temp1][temp2-1]==0:
                        self.xy[temp1][temp2-1]=1
                        self.xy[temp1][temp2]=0
                elif temp3<=0.5:
                    if temp2+1<=100 and self.xy[temp1][temp2+1]==0:
                        self.xy[temp1][temp2+1]=1
                        self.xy[temp1][temp2]=0
                elif temp3<=0.75:
                    if temp1-1>=0 and self.xy[temp1-1][temp2]==0:
                        self.xy[temp1-1][temp2]=1
                        self.xy[temp1][temp2]=0
                elif temp3<=1:
                    if temp1+1<=100 and self.xy[temp1+1][temp2]==0:
                        self.xy[temp1+1][temp2]=1
                        self.xy[temp1][temp2]=0
        return self.xy
        
a=cream(100000)
b=a.simulate()
for i in range(101):
    for j in range(101):
        if b[i][j]!=0:
           pl.scatter([i],[j],9,color='red')
pl.xlim(0,100)
pl.ylim(0,100)

pl.show()