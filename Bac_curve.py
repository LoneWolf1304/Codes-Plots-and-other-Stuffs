import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scienceplots
plt.style.use(['notebook','grid','science'])
value=pd.read_excel("Bac_Growth.ods", engine="odf", nrows=10)
time=value["Time"]
absorb=value["Abs"]
fig, axs= plt.subplots(figsize=(8,10))
axs.scatter(time,absorb)
axs.set_title("Bacterial Growth Curve (Absorbance vs. Time)")
axs.set_xlabel("Time (min)")
axs.set_ylabel("Absorbance")
plt.show()

'''def f(L,x0,k,x):
	return L/(1+np.exp(-k*(x-x0)))
	
ptot,pcov= curve_fit(f,time,absorb)
x=np.arange(0,253,0.1)
L=ptot[0]
x0=ptot[1]
k=ptot[2]
print(L,x0,k)
curve=f(L,x0,k,x)
axs.plot(x,curve)
plt.show()'''
