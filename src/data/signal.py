'''
Created on 26 maj 2015

@author: fragom
'''

class Signal(object):
    '''
    classdocs, clase base trabaja con complejos
    '''
    
    def __init__(self, _param):
        '''
        Constructor
        '''
        ''' oye, convierte las arrays en dictionarios, el key value siempre must be el tiempo, so
        self.signal = {(real, imaginary)}
        '''
        self._sampletime = []
        self._complexSignal = {}
        self._valueType= _param
        self._component= ''

    def get_component(self):
        return self.__component


    def set_component(self, value):
        self.__component = value


    def del_component(self):
        del self.__component

        
    def get_value(self):
        return self.__value


    def set_value(self, value):
        self.__valueType = value


    def del_value(self):
        del self.__valueType
        

    def get_sampletime(self):
        return self.__sampletime
    
    def set_sampletime(self, value):
        self.__sampletime = value
        
    def del_sampletime(self):
        del self.__sampletime

    def get_complexSignal(self):
        ''' dictionary of complex values '''
        return self._complexSignal
    
    def get_realSignal(self):
        return self._signal.keys()
    
    def get_imagSignal(self):
        return self._signal.values()

    def set_complexSignal(self, _signalR, _signalI):
        self._complexSignal = zip(_signalR, _signalI)
        print self._complexSignal
        
    def del_complexSignal(self):
        del self._complexSignal

    sampletime = property(get_sampletime, set_sampletime, del_sampletime, "sampletime's docstring")
    signal = property(get_complexSignal, set_complexSignal, del_complexSignal, "signal's docstring")
    value = property(get_value, set_value, del_value, "value's docstring")
    component = property(get_component, set_component, del_component, "component's docstring")

from math import sqrt
from numpy import arctan2, abs, sin, cos

class SignalPMU(Signal):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor, clase que trabaja con representacion polar'''
        ''' oye, convierte las arrays en dictionarios, el key value siempre must be el tiempo, so
        self.signal = {(magnitude, angle)}
        '''
        Signal.__init__(self, 'polar')
        self._polarSignal= {}

    def get_sampletime(self):
        return self.__sampletime
    
    def set_sampletime(self, value):
        self.__sampletime = value

    def del_sampletime(self):
        del self.__sampletime

    def set_complexSignal(self, _signalR, _signalI):
        self._complexSignal = zip(_signalR, _signalI)
        
    def set_polarSignal(self, _signalM, _signalA):
        self._polarSignal = dict(zip(_signalM, _signalA))
        
    def get_polarSignal(self):
        return self._polarSignal

    def get_magSignal(self):
        return self._polarSignal.keys()
    
    def get_angSignal(self):
        return self._polarSignal.values()

    def del_polarSignal(self):
        del self._polarSignal
        

    def complex2Polar(self):
        self.set_sampletime(self.sampletime)
        for valor in self.signal:
            magnitude= abs(sqrt(valor[0]^2+ valor[1]^2))
            angle= arctan2(valor[1], valor[0])
            self._polarSignal.append(magnitude, angle)
        return self.i_polarSignal
    
    def polar2Complex(self):
        self.set_sampletime(self.sampletime)
        for valor in self.signal:
            real= valor[0]* cos(valor[1])
            imag= valor[0]* sin(valor[1])
            self._complexSignal.append(real, imag)
        return self.i_complexSignal      
    
    signal = property(get_polarSignal, set_polarSignal, del_polarSignal, "signal's docstring")