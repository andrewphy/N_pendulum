import numpy as np

def periodo_modo_n(L, n,t, g=9.81,i=False):
    j01 = 2.4048  # Primer cero de J0
    j0k = j01     # Usamos el mismo valor para j_0,k

    # Términos intermedios
    coef = 4 * np.pi / j01
    factor_raiz = np.sqrt(L / (n * g) * (n + 0.5))
    correccion = 1 + (j0k**2 - 2) / (12 * (2 * n + 1)**2)
    
    # Período
    T = coef * factor_raiz * correccion**(-0.5)
    print(f"Período Teorico: {T:.4f} s")
    #ERROR
    E=abs(T-t)/T*100
    if i==True:
        print(f"Error Teorico: {E:.4f} %")
    return T
