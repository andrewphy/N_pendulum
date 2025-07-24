import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
def Fourier(dt, oa,i,N,K):
    n = len(oa)
    frecuencias = np.fft.fftfreq(n, dt)
    fft_oa = np.fft.fft(oa)
    espectro = np.abs(fft_oa) / n

    mascara = frecuencias > 0
    frecuencias = frecuencias[mascara]
    espectro = espectro[mascara]

    peaks, _ = find_peaks(espectro)

    if len(peaks) == 0:
        print("⚠️ No se encontraron picos en el espectro. Señal posiblemente ruidosa o muy amortiguada.")
        return None

    frecs_dominantes = frecuencias[peaks]
    amps_dominantes = espectro[peaks]

    indice_max = np.argmax(amps_dominantes)
    f_principal = frecs_dominantes[indice_max]
    T_principal = 1 / f_principal

    plt.figure(figsize=(8,5))
    plt.plot(frecuencias, espectro)
    plt.xlabel("Frecuencia (Hz)")
    plt.xlim(0,3)
    plt.ylabel("Amplitud")
    plt.title(f"Transformada de Fourier masa {i:.0f} para {N} masas ")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'GRAFICAS\\FRECUENCIAS\\{K}L\\Transformada de Fourier masa {i} para {N} masas.pdf')
    plt.show()
    #print(f"Frecuencia dominante: {f_principal:.4f} Hz")
    #print(f"Período Experimental: {T_principal:.4f} s")
    return T_principal