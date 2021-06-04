# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
import matplotlib.pyplot as plt
plt.grid(True)

n = 52
c = 3 # maximum allowed failures
all_p = range(0, 10000, 1)
all_p = [x/10000 for x in all_p]
all_pa = []


for p in all_p:
    x = 0
    Pa = 0
    while x <= c:
        Pa = Pa + (math.comb(n, x)) * (p**x) * ((1-p)**(n-x))
        x = x + 1
    all_pa.append(Pa)

all_p = [p*100 for p in all_p]
    
plt.grid(True)
plt.xticks(list([a/20 for a in range(0,2100,20)]))
plt.yticks(list([a/20 for a in range(0,21,1)]))
plt.xlabel("% defective", fontsize=30)
plt.ylabel("probability of acceptance", fontsize=30)
plt.plot(all_p, all_pa, label="n: %d c: %d" % (n, c))
plt.legend()


round((1-all_pa[all_p.index(round(100-95.0, 2))])*100, 3)


