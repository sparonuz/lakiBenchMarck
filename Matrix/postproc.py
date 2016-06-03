#!/usr/bin/python
import sys
import os
import numpy as np
import random
import matplotlib.pyplot as plt

file_in = sys.argv[1]
fig_name=file_in[:-3]+'png'
data    = np.genfromtxt(file_in)
measure = data[:,1:]
mean    = np.mean(measure, axis=1)
measure    = mean[0]/measure
mean    = np.mean(measure, axis=1)
std     = np.std(measure, axis=1) 

x = data[:,0]
y = mean

# example error bar values that vary with x-position
error = std
plt.axis([1, 17, 0.1, 1.5])
fig = plt.errorbar(x,y, yerr=error)
plt.savefig(fig_name, format='png')
#plt.show()

