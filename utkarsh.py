import numpy as np
import matplotlib.pyplot as plt

k = 50

t = np.linspace(0,0.08,1000)
x = np.cos(100*np.pi*t) + np.cos(2*np.pi*k*t)

y1 = (1/(np.sqrt(1 + (np.pi/2)**2)))*np.cos(100*np.pi*t - np.arctan(np.pi/2))


#k = 25


y2 = (1/(np.sqrt(1 + (np.pi*k/100)**2)))*np.cos(2*k*np.pi*t - np.arctan(k*np.pi/100))


y3 = (1/(np.sqrt(1 + (np.pi*k*2/100)**2)))*np.cos(2*k*2*np.pi*t - np.arctan(2*k*np.pi/100))

k = 40

y4 = (1/(np.sqrt(1 + (np.pi*k*2/100)**2)))*np.cos(2*k*2*np.pi*t - np.arctan(2*k*np.pi/100))

k=60

y5 = (1/(np.sqrt(1 + (np.pi*k*2/100)**2)))*np.cos(2*k*2*np.pi*t - np.arctan(2*k*np.pi/100))




plt.plot(t,y1 + y2)
plt.plot(t,y1 + y3)

plt.plot(t,y1 + y4)
plt.plot(t,y1 + y5)



plt.show()
