import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from CALCULADOR_PERIODOS import Fourier
from Periodos_teoricos import periodo_modo_n
from calculo_angulares import angulares
from DatosG import Datos
from Graficadora import Graficadora
import math as mt
#cst

L=1
k=1
T1=[]
T2=[]
T3=[]
TA=[]
#EXTRAER DATOS
for i in [2,3,4,5,6,8,10,12,15]:
    print(f"Masas={i}")
    name=f"DATOS\\datos_{i}masas_{k}metroMODIFY"
    l=L/i
    dt=0.033
    t,z,x,y=Datos(name,34,i)
    o1,w1=angulares(x,l,dt)
    o2,w2=angulares(y,l,dt)
    o3,w3=angulares(z,l,dt)
    Graficadora(t,z,i,k)
    print('masa1')
    T1.append(Fourier(dt,o1,1,i,k))
    print(f"Periodo exp: {Fourier(dt,o1,1,i,k):.4f}")
    print('masa mitad')
    if i%2==0:
        T2.append(Fourier(dt,o2,i/2+1,i,k))
        print(f"Periodo exp: {Fourier(dt,o2,i/2+1,i,k):.4f}")
    else:
        T2.append(Fourier(dt,o2,mt.ceil(i/2),i,k))
        print(f"Periodo exp: {Fourier(dt,o2,mt.ceil(i/2),i,k):.4f}")
    print('masa extremal')
    T3.append(Fourier(dt,o3,i,i,k))
    print(f"Periodo exp: {Fourier(dt,o3,i,i,k):.4f}")
    TA.append(periodo_modo_n(L,i,T3))
#print(TA)
