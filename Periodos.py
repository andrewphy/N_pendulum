import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from CALCULADOR_PERIODOS import Fourier
from Periodos_teoricos import periodo_modo_n
from calculo_angulares import angulares
from Graficadora import Graficadora
#cst
L=1
L2=L/2
L3=0.33
L4=L/4
dt=0.034

#EXTRAER DATOS
t,xa,xb=np.loadtxt("DATOS\datos_2masas_1metroMODIFY.txt", unpack=True, delimiter=' ',skiprows=3)
at,x1,x2,x3=np.loadtxt("DATOS\datos_3masas_1metroMODIFY.txt", unpack=True, delimiter=' ',skiprows=13)
bt,y1,y2,y3,y4=np.loadtxt("DATOS\datos_4masas_1metroMODIFY.txt", unpack=True, delimiter=' ',skiprows=3)
#calculos thetas
oa,wa=angulares(xa,L2,dt)
ob,wb=angulares(xb,L2,dt)
o1,w1=angulares(x1,L3,dt)
o2,w2=angulares(x2,L3,dt)
o3,w3=angulares(x3,L3,dt)
o4,w4=angulares(y1,L4,dt)
o5,w5=angulares(y2,L4,dt)
o6,w6=angulares(y3,L4,dt)
o7,w7=angulares(y4,L4,dt)
Graficadora(at,x3,N=3,n=3)

#CALCULO DE PERIODOS.
TA=Fourier(dt,oa)
TB=Fourier(dt,ob)
T=periodo_modo_n(L,2,TA,i=True)

#_________________________
T1=Fourier(dt,o1)
T2=Fourier(dt,o2)
T3=Fourier(dt,o3)
T_3=periodo_modo_n(L,3,T2,i=True)
