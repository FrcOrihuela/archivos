#py -3 -m venv .venv
#.venv\scripts\activate usar para crear entorno propio
from matplotlib import axes
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


data=np.loadtxt('ajustesinfiltro.txt')
x=data[:,0]
y=data[:,1]
errorx=data[:,2]
errory=data[:,3]

fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_ylabel("Potencial de Frenado (V)", fontsize=14, fontname="Times New Roman")
ax.set_xlabel("Frecuencia (Hz)", fontsize=14, fontname="Times New Roman")
ax.grid(True)
ax.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=True)   


def fit_func(x, a, b):
    return a*x+b

params,_=optimize.curve_fit(fit_func, x, y)

print(params)

ax.plot(x, fit_func(x, params[0], params[1]), color='r',
label='Ajuste')

ax.errorbar(x, y, xerr=errorx, yerr=errory, linestyle='', capsize = 3, ecolor='g',
marker='o', markersize=4, label='Data')

fig.savefig('filename.png', dpi=300)

plt.show()
