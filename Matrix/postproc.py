#!/usr/bin/python
import sys
import os
import numpy as np
import random
import matplotlib.pyplot as plt

file_in1 = sys.argv[1]
file_in2 = sys.argv[2]
title    = sys.argv[3]
fig_name = sys.argv[4]
data     = np.genfromtxt(file_in1)
measure  = data[:,1:]
mean     = np.mean(measure, axis=1)
measure  = mean[0]/measure
mean     = np.mean(measure, axis=1)
std      = np.std(measure, axis=1) 

x = data[:,0]
y = mean

# example error bar values that vary with x-position
error = std
plt.axis([1, 17, 0.1, 1.5])
plt.ylabel('Scaling Efficiency')
plt.xlabel('# Cores')
plt.title(title)
plt.errorbar(x,y, yerr=error, label='Laki')

data     = np.genfromtxt(file_in2)
measure  = data[:,1:]
mean     = np.mean(measure, axis=1)
measure  = mean[0]/measure
mean     = np.mean(measure, axis=1)
std      = np.std(measure, axis=1)

y = mean
error = std
plt.errorbar(x,y, yerr=error, label='Ulisse')
plt.legend()



plt.title(title)
plt.savefig(fig_name, format='png')
#plt.show()

