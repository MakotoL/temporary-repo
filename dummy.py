# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:05:25 2020

@author: ML
"""

from datetime import datetime
import math
import random


#This is a dummy file
print("This program prints hello world a random number of times")
d= datetime.now()
random.seed(d.second * (d.minute + 1))
n = (random.random() * 100) % 20
k = int(n)

for i in range(k):
	if (d.second % 2 == 1):
		print("hello world?")
	print("Hello world!")
	
	


