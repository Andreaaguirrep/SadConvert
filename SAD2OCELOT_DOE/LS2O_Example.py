__author__ = 'D. Oumbarek Espinos'
"""
Function to read SAD files and organize to feed into OCELOT
Version - 03/04/2025
"""

import numpy as np
import matplotlib as plt
import ocelot
from ocelot import *
from ocelot.cpbd.beam import *
from ocelot.gui.accelerator import *
from ocelot.optics.elements import *
from ocelot.optics import * 
import re
import LoadSAD2OCELOTLine as LS2O

FilePath = r'C:\XXXXXX' #Put here the file path

Monits, CAVS, Sexts, Quads, Bends, Drifts, Line_order = LS2O.LoadSAD2OCELOTLine(FilePath) #This reads and and clasifies the elements in a .SAD file


#Creation of the elements in OCELOT
for NKey, Nval in Drifts.items():
    exec(NKey + " = Drift(l = Nval)")
    

if len(Monits)>0: 
    for NKey, Nval in Monits.items():
        exec(NKey + " = Monitor( )") 
    
    

if len(Bends)>0: 
    for NKey, Nval in Bends.items():
        #key: (L,ANGLE,Rotate,E1,E2,F1,Fringe)
        exec(NKey + " = SBend(l = Nval[0],  angle = Nval[1])") 
          
        
        for ij in range(2,len(Nval)):
            if np.isnan(Nval[ij])==False:
                if ij==2:
                    exec(NKey + ".tilt = Nval[ij]") 
                elif ij==3:
                    exec(NKey + ".e1 = Nval[1]*Nval[ij]")               
                elif ij==4:
                    exec(NKey + ".e2 = Nval[1]*Nval[ij]")   
                elif ij==5:
                    exec(NKey + ".fint = Nval[ij]")   
                               
if len(Quads)>0: 
    for NKey, Nval in Quads.items():
        #key: (L,K1,F1,FRINGE)
        if Nval[1]==0:
            exec(NKey + " = Quadrupole(l = Nval[0],  k1 = Nval[1])") 
        else:
            exec(NKey + " = Quadrupole(l = Nval[0],  k1 = Nval[1]/Nval[0])") 
          
        
        for ij in range(2,len(Nval)):
            if np.isnan(Nval[ij])==False:
                if ij==2:
                    exec(NKey + ".fint = Nval[ij]") 
                
                
if len(Sexts)>0: 
    for NKey, Nval in Sexts.items():
        #key: (L,K2,Rotate) 
        if Nval[1]==0:
            exec(NKey + " = Sextupole(l = Nval[0],  k2 = Nval[1]") 
        else:
            exec(NKey + " = Sextupole(l = Nval[0],  k2 = Nval[1]/Nval[0])") 
          
        
        for ij in range(2,len(Nval)):
            if np.isnan(Nval[ij])==False:
                if ij==2:
                    exec(NKey + ".tilt = Nval[ij]")  
                
if len(CAVS)>0:
    for NKey, Nval in CAVS.items():
        #key: (L,VOLT,PHI,FREQ)
        exec(NKey + " = Cavity(l = Nval[0],  v = Nval[1])") 
          
        
        for ij in range(2,len(Nval)):
            if np.isnan(Nval[ij])==False:
                if ij==2:
                    exec(NKey + ".phi = Nval[ij]") 
                elif ij==3:
                    exec(NKey + ".freq = Nval[ij]")
                    
                    
              

try:
    del cell
except: 
    print('meh')

endLine = len(Line_order)-1 #until the end of the line
for Nelem in Line_order[:endLine+1]:
#    print(Nelem)
    Nelem = Nelem.replace(' ', '')
#    print(Nelem)
    if 'cell' in globals():
        exec( "cell = cell +(" + Nelem + ",)")
    else:
        exec( "cell = (" + Nelem + ",)")
        
    exec( "totino = " + Nelem + ".l")
#    print(Nelem)
    
    if np.isnan(totino):
        print('**************************')
        print(Nelem)
        break
    
    
print('[][]][][][][[][]][][][][][][][]')
print('[]Line until the element ' + Line_order[endLine])
print('[][]][][][][[][]][][][][][][][]')
    
 
#Definition of a random beam for the example
E        = 3841286237.7791615*1e-9 
E_spread = 0.001 
Divx     = 2e-5 
Divy     = 2e-5 
Sizex    = 1e-4 
Sizey    = 1e-4 
Sizez    = 1e-5
Qtotal   = -2e-9 
N        = int(100000) 
    


EbeamInitial = generate_parray(sigma_x=Sizex, sigma_px=Divx, sigma_y=Sizey, sigma_py=Divy,
                    sigma_tau=Sizez, sigma_p=E_spread, chirp=0.0, charge=Qtotal, nparticles=N, energy=E,
                    tau_trunc=None)
print(EbeamInitial)

fig = 1
show_e_beam(EbeamInitial,nfig=fig,figsize=(8,6),tau_units="um")


#Tracking

method = MethodTM()
lat = MagneticLattice(cell, method=method)
print("length of the cell: ", round(lat.totalLen,6), "m")  
navi = Navigator(lat)


toto_array = deepcopy(EbeamInitial)
tws_track, toto_array = track(lat, toto_array, navi, print_progress=True) 

fig = 2
show_e_beam(toto_array,nfig=fig,figsize=(8,6),tau_units="um")




