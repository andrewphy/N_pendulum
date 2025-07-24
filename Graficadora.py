import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from CALCULADOR_PERIODOS import Fourier
from Periodos_teoricos import periodo_modo_n
from calculo_angulares import angulares

def Graficadora(x,y,N,K):
    plt.figure(figsize=(8, 5))
    plt.plot(x,y, 'r-')
    plt.title(f'Posicion vs tiempo masa {N},N={N}')
    plt.xlabel('Posicion (m)')
    plt.ylabel('Tiempo (s)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'GRAFICAS\\posicion\\{K}L\\angulo_vs_tiempo_masa{N}_N={N}.pdf')
    plt.show()
    return