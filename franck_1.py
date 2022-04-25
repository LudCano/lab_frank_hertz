# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:13:41 2022

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("lab1.tsv", sep = "\t")
df = df.apply(lambda x: x.str.replace(',','.'))

df['V'] = df['V'].astype(float)
df['A'] = df['A'].astype(float)


"""
plt.scatter(df["V"], df["A"])
plt.grid()
"""

V = df["V"]
A = df["A"]

plt.figure(1)
plt.scatter(V, A, s = 6)

col = [0]
for i in range(len(V)-1):
    val = V[i]
    
    #determinar subida
    if V[i+1]>val:
        col.append(0)
    else:
        col.append(1)

#df["color"] = col
#plt.scatter(df["V"], df["A"], c = df["color"])


# Reconocer parábolas usando los límites de subidas y bajadas
par_num = 0
parabol = [0]
lst_color = [par_num]
conta = 0
for i in range(len(col)-1):
    if col[i] != col[i+1]:
        conta =  conta + 1
        if conta == 2:
            par_num = par_num + 1
            conta = 0
            lst_color.append(par_num)
    parabol.append(par_num)


df["parab"] = parabol

#plt.scatter(df["V"], df["A"], c = df["parab"])


# Trabajar parábola por parábola
#no tomamos en cuenta la primera y última parábola (por gráfico)
lst_color = lst_color[1:-1]





def my_poli(df, num, if_plot = 0):
    
    dat = df[df["parab"] == num]
    X = dat["V"].to_list()
    
    Y = dat["A"].to_list()
    
    # Train Algorithm (Polynomial)
    
    degree = 2
    mod = np.polyfit(X,Y, degree)
    poly_fit = np.poly1d(mod)
    #print(poly_fit)
    # Plot data if required (1)
    if if_plot == 1:
        xx = np.linspace(min(X), max(X), 100)
        plt.plot(xx, poly_fit(xx), c='r',linestyle='-')
        plt.title('Polynomial')
        plt.xlabel('X')
        plt.ylabel('Y')
        
        plt.grid(True)
        plt.scatter(X, Y)
        plt.show()
    return mod

def find_peak(coefs):
    a = coefs[0]; b = coefs[1]
    loc_max = -b/(2*a)
    return loc_max


def plot_maxs(df, mod, num, maximo = 0):
    dat = df[df["parab"] == num]
    X = dat["V"].to_list()
    Y = dat["A"].to_list()
    poly_fit = np.poly1d(mod)
    xx = np.linspace(min(X), max(X), 100)
    plt.plot(xx, poly_fit(xx), linestyle='--')
    plt.title('Polynomial')
    plt.xlabel('X')
    plt.ylabel('Y')
    recta_y = [min(df[df["parab"] == num]["A"]), max(df[df["parab"] == num]["A"])]
    print(recta_y)
    recta_x = [maximo, maximo]
    #plt.grid(True)
    plt.scatter(X, Y, s = 3)
    plt.plot(recta_x, recta_y)
    plt.show()


plt.figure(2)
picos = []
for i in lst_color:
    coef = my_poli(df, i)
    pico_local = find_peak(coef)
    picos.append(pico_local)
    plot_maxs(df ,coef, i, pico_local)



# VALORES DE RESTA
diferencias = []
for i in range(len(picos) -1):
    i = i + 1
    dif = picos[i] - picos[i-1]
    diferencias.append(dif)
    
print(np.mean(diferencias), np.var(diferencias))