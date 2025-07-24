import numpy as np
import matplotlib.pyplot as plt

def matrices_MC(n, m=1.0, g=9.81, L=1.0):
    """
    Construye las matrices M y C para un N-péndulo de longitud total L y n masas.
    Se asume: todas las masas m_i = m y espaciadas uniformemente.
    """
    a = L / n  # distancia entre masas

    # Matriz de masa (simétrica)
    M = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            M[i, j] = m * a**2 * (n - max(i, j))

    # Matriz de rigidez (simétrica diagonal)
    C = np.zeros((n, n))
    for i in range(n):
        C[i, i] = m * g * a * (n - i)

    return M, C

def frecuencias_naturales(n, m=1.0, g=9.81, L=1.0):
    """
    Resuelve el problema de autovalores (C - ω²M) = 0 y devuelve las frecuencias ω.
    """
    M, C = matrices_MC(n, m, g, L)
    # Resolver (C - ω² M) v = 0 → generalized eigenvalue problem
    eigvals, eigvecs = np.linalg.eig(np.linalg.inv(M) @ C)
    
    # Filtrar solo valores reales y positivos
    omega2 = np.real(eigvals)
    omega2 = omega2[omega2 > 0]
    omegas = np.sqrt(np.sort(omega2))

    return omegas

# --- Ejemplo: calcular y graficar frecuencias para N=2 a 16 ---
L_total = 1
n_list = [2,3,4,5,6,8,10,13]
frecuencias_modo0 = []
for n in n_list:
    omegas = frecuencias_naturales(n, L=L_total)
    frecuencia_fundamental = omegas[0] / (2*np.pi)  # convertir a Hz
    frecuencias_modo0.append(frecuencia_fundamental)
periodos0=np.divide(np.ones(np.size(frecuencias_modo0)),frecuencias_modo0)
print(periodos0)