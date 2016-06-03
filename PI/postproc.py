#!/usr/bin/python
import sys
import os
import numpy as np
import random
import matplotlib.pyplot as plt

file_in = sys.argv[1]
data    = np.genfromtxt(file_in)
x = data[:,0]
measure = np.zeros((5, 100))
measure = data[:,1:]
std     = np.zeros(5)
mean    = np.zeros(5)
mean    = np.mean(measure, axis=1)
for i in range(5):
	measure[i,:] *= x[i]

measure = mean[0]/measure
mean    = np.mean(measure, axis=1)
std     = np.std(measure, axis=1) 
y = mean

# example error bar values that vary with x-position
plt.errorbar(x,y, yerr=std)
#plt.show()
file_in = sys.argv[2]

data    = np.genfromtxt(file_in)
x = data[:,0]
measure = np.zeros((5, 100))
measure = data[:,1:]
std     = np.zeros(5)
mean    = np.zeros(5)
mean    = np.mean(measure, axis=1)
measure = mean[0]/measure
mean    = np.mean(measure, axis=1)
std     = np.std(measure, axis=1)

y = mean

## example error bar values that vary with x-position
error = std
plt.errorbar(x,y, yerr=error)
plt.show()

