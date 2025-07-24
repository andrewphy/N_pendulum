import numpy as np
def angulares(x,L,dt):
    oa=np.arcsin(x/L)
    if np.isnan(oa).any()==True:
        oa = oa[~np.isnan(oa)]
        print('se eliminaron NAN')
    if np.isinf(oa).any()==True:
        oa = oa[~np.isinf(oa)]
        print('se eliminaron inf')
    wa = np.gradient(oa, dt)

    return oa,wa