'''
Created on 7 apr 2015

@author: fragom
'''
from classes import PhasorMeasH5

def abc2phasor():
    #Get the signal (a, b, c)
    '''input of the function:
    result file, .mat, either from DY or OMC 
    type of signal'''
    ''' TODO: Unify inputs files of MAE and outputs of MEE, should be the same and easy to access '''
    h5pmu= PhasorMeasH5.PhasorMeasH5('C:/Users/fragom/PhD_CIM/Modelica/Models/Results/Dymola/SMIB1L_Group1_Nordic44.mat')
    #calculate phasor from signal
    h5pmu.set_signal("pwLine4.n.vr","pwLine4.n.vi")
    h5pmu.set_source('voltage')
    h5pmu.calc_phasorSignal()
    print h5pmu.get_phasor().get_magnitude()
    print h5pmu.get_phasor().get_angle()
    print h5pmu.get_phasor().get_time()
    #save meas to h5 file    
    h5pmu.save_h5('C:/Users/fragom/PhD_CIM/Modelica/Models/Results/Dymola')
    
if __name__ == '__main__':
    abc2phasor()