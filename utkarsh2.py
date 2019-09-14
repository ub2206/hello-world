import numpy as np
import matplotlib.pyplot as plt

#k = 50

t = np.linspace(0,0.08,1000)
x = 16*np.sin(100*np.pi*t) 

y1 = 16*(1/(np.sqrt(1 + (np.pi/2)**2)))*np.sin(100*np.pi*t - np.arctan(np.pi/2))



plt.plot(t,x)
plt.plot(t,y1)


plt.show()
