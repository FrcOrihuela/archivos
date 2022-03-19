#py -3 -m venv .venv
#.venv\scripts\activate usar para crear entorno propio
import matplotlib.pyplot as plt
import numpy as np

data=np.loadtxt('dataset.txt')

x=data[:,0]
y=data[:,1]
z=data[:,2]

fig=plt.figure()
ax1=fig.add_subplot(221)
ax1.grid(True)
ax1.set_ylabel("y(x)", fontsize=14, fontname="Times New Roman")
ax1.set_xlabel("x", fontsize=14, fontname="Times New Roman")
ax1.plot(x,y, linestyle='dashed', linewidth=0.75, color='green')
ax2=fig.add_subplot(223)
ax2.set_xlim(-20,0)
ax2.set_ylim(0,50)
ax2.set_ylabel("z(x)", fontsize=14, fontname="Times New Roman")
ax2.set_xlabel("x", fontsize=14, fontname="Times New Roman")
ax2.plot(x,z,linestyle='dotted', linewidth=1.5, color='red' )
ax3=fig.add_subplot(122, projection='3d')
ax3.plot(x,y,z)

fig.savefig('filename.png',dpi=300)
plt.show()