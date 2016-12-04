# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 20:41:24 2016

@author: LYJ
"""

import matplotlib.pyplot as plt
import numpy as np
import math
class hyperion:
    def __init__(self,GM=4*math.pi**2,dt=0.0001,time=10):
        self.GM=GM
        self.x=[1]
        self.y=[0]
        self.vx=[0]
        self.vy=[2*math.pi]
        self.dt=dt
        self.time=time
        self.r=[math.sqrt(self.x[0]**2+self.y[0]**2)]
        self.t=[0]
        self.w=[0]
        self.theta=[0]
    def calculate(self):
        for i in range(int(self.time//self.dt)):
            self.vx.append(self.vx[i]-self.GM*self.x[i]*self.dt/self.r[i]**3)
            self.vy.append(self.vy[i]-self.GM*self.y[i]*self.dt/self.r[i]**3)
            self.x.append(self.x[i]+self.vx[i+1]*self.dt)
            self.y.append(self.y[i]+self.vy[i+1]*self.dt)
            self.r.append(math.sqrt(self.x[i+1]**2+self.y[i+1]**2))
            self.w.append(self.w[i]-3*self.GM/self.r[i]**5*(self.x[i]*math.sin(self.theta[i])-self.y[i]*math.cos(self.theta[i]))*(self.x[i]*math.cos(self.theta[i])+self.y[i]*math.sin(self.theta[i]))*self.dt)
            self.theta.append(self.theta[i]+self.w[i+1]*self.dt)
            self.t.append(self.t[i]+self.dt)
            if self.theta[i+1]<-math.pi:
                self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
                self.theta[i+1]=self.theta[i+1]-2*math.pi
    def show_results(self,color):
        ax1=plt.subplot(121)
        ax2=plt.subplot(122)
        plt.sca(ax1)
        plt.plot(self.t,self.theta,'g',label=r'Circular orbit')
        plt.title(r'Hyperion  $\Theta$ versus time',fontsize=14)
        plt.xlabel(u'time(yr)',fontsize=14)
        plt.ylabel(u'$\Theta$(radians)',fontsize=14)
        plt.sca(ax2)
        plt.plot(self.t,self.w,'g',label=r'Circular orbit')
        plt.title(r'Hyperion  $\omega$ versus time',fontsize=14)
        plt.xlabel(u'time(yr)',fontsize=14)
        plt.ylabel(u'$\omega$(radians/yr)',fontsize=14)
        #plt.xlim(-1,1)
        #plt.ylim(-1,1)
        plt.legend(fontsize=14,loc='best')
a=hyperion()
a.calculate()
a.show_results('g')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
import math
class hyperion:
    def __init__(self,GM=4*math.pi**2,dt=0.0001,time=10):
        self.GM=GM
        self.x=[1]
        self.y=[0]
        self.vx=[0]
        self.vy=[5]
        self.dt=dt
        self.time=time
        self.r=[math.sqrt(self.x[0]**2+self.y[0]**2)]
        self.t=[0]
        self.w=[0]
        self.theta=[0]
    def calculate(self):
        for i in range(int(self.time//self.dt)):
            self.vx.append(self.vx[i]-self.GM*self.x[i]*self.dt/self.r[i]**3)
            self.vy.append(self.vy[i]-self.GM*self.y[i]*self.dt/self.r[i]**3)
            self.x.append(self.x[i]+self.vx[i+1]*self.dt)
            self.y.append(self.y[i]+self.vy[i+1]*self.dt)
            self.r.append(math.sqrt(self.x[i+1]**2+self.y[i+1]**2))
            self.w.append(self.w[i]-3*self.GM/self.r[i]**5*(self.x[i]*math.sin(self.theta[i])-self.y[i]*math.cos(self.theta[i]))*(self.x[i]*math.cos(self.theta[i])+self.y[i]*math.sin(self.theta[i]))*self.dt)
            self.theta.append(self.theta[i]+self.w[i+1]*self.dt)
            self.t.append(self.t[i]+self.dt)
            if self.theta[i+1]<-math.pi:
                self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
                self.theta[i+1]=self.theta[i+1]-2*math.pi
    def show_results(self,color):
        ax1=plt.subplot(121)
        ax2=plt.subplot(122)
        plt.sca(ax1)
        plt.plot(self.t,self.theta,'m',label=r'Elliptical orbit')
        plt.title(r'Hyperion  $\Theta$ versus time',fontsize=14)
        plt.xlabel(u'time(yr)',fontsize=14)
        plt.ylabel(u'$\Theta$(radians)',fontsize=14)
        plt.sca(ax2)
        plt.plot(self.t,self.w,'m',label=r'Elliptical orbit')
        plt.title(r'Hyperion  $\omega$ versus time',fontsize=14)
        plt.xlabel(u'time(yr)',fontsize=14)
        plt.ylabel(u'$\omega$(radians/yr)',fontsize=14)
        #plt.xlim(-1,1)
        #plt.ylim(-1,1)
        plt.legend(fontsize=14,loc='best')
a=hyperion()
a.calculate()
a.show_results('m')
plt.show()