# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
import matplotlib.pyplot as plt
plt.grid(True)

N = 4700
N = 5000
all_n = [2, 5, 10, 20, 30, 50, 100, 200, 500]
#all_n = [52]
c = 0 # maximum allowed failures

all_p = range(0, 10000, 1)
all_p = [x/10000 for x in all_p]


def get_Pd(n, d, p):
    Pd = math.comb(n, d) * (p**d) * ((1-p)**(n-d))
    return Pd

def get_Pa(c, n, p):
    Pa = 0
    d = 0
    total_pd = []
    while d <= c:
        Pd = get_Pd(n, d, p)
        Pa = Pa + Pd
        d = d + 1
        total_pd.append(Pd)
    return Pa

def get_idx(a_list, num, tol=0.000001):
    while tol <= 1:
        for i, n in enumerate(a_list):
            if abs(n - num) < tol:
                return i
        tol = tol * 10

def get_AOQ(p, Pa, N, n):
    AOQ = Pa * p * (N - n) / N
    return AOQ

def get_ATI(n, N, Pa):
    ATI = n + (1 - Pa) * (N - n)
    return ATI

for n in all_n:
    all_pa = []
    all_aoq = []
    all_ati = []
    for p in all_p:
        Pa = get_Pa(c, n, p)
        AOQ = get_AOQ(p, Pa, N, n)
        ATI = get_ATI(n, N, Pa)
        all_pa.append(Pa)
        all_aoq.append(AOQ)
        all_ati.append(ATI)

    all_p_inPercentage = [p*100 for p in all_p]
    
    plot_ATI = False
    plot_AOQ = False
    plot_OC = True
    
    if plot_ATI:
        # plot for ATI
        plt.grid(True)
        plt.xticks(list([a/20 for a in range(0,2100,20)]))    
        plt.xlabel("% defective", fontsize=30)
        plt.ylabel("Average Total Inspection (ATI)", fontsize=20)
        plt.title('Lot size N=%d units\nsample size: n units\ndefect allowed: c units' % N, fontsize=20)
        plt.plot(all_p_inPercentage, all_ati, label="n: %d c: %d" % (n, c))
        plt.legend()
     
    if plot_AOQ:    
        # plot for AOQ
        plt.grid(True)
        plt.xticks(list([a/20 for a in range(0,2100,20)]))
        #plt.yticks(list([a/20 for a in range(0,21,1)]))
        plt.xlabel("% defective", fontsize=30)
        plt.ylabel("Average Outgoing Quality Curve (AOQ)", fontsize=20)
        plt.title('Lot size N=%d units\nsample size: n units\ndefect allowed: c units' % N, fontsize=20)
        plt.plot(all_p_inPercentage, all_aoq, label="n: %d c: %d" % (n, c))
        plt.legend()
    
    if plot_OC:
        # plot for OC
        plt.grid(True)
        plt.xticks(list([a/20 for a in range(0,2100,20)]))
        plt.yticks(list([a/20 for a in range(0,21,1)]))
        plt.xlabel("% defective", fontsize=30)
        plt.ylabel("probability of acceptance", fontsize=30)
        plt.plot(all_p_inPercentage, all_pa, label="n: %d c: %d" % (n, c))
        plt.legend()



for i in range(0, 13, 1):
    ii = i*100
    print("{p:0.1f}% {pa:.3f} {AOQ:.4f}".format(p=all_p_inPercentage[ii], 
                                                     pa=all_pa[ii],
                                                     AOQ=all_aoq[ii]))

