# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:04:10 2022

@author: HP
"""

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


def plot_maxs(df, mod, num, maximo = 0, plot_0 = True):
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
    #print(recta_y)
    recta_x = [maximo, maximo]
    #plt.grid(True)
    plt.scatter(X, Y, s = 3)
    plt.plot(recta_x, recta_y)
    if plot_0:
        plot_else(df, 0)
    plt.show()


def plot_else(df, num):
    dat = df[df["parab"] == num]
    X = dat["V"].to_list()
    Y = dat["A"].to_list()
    plt.scatter(X, Y, s = 3, c = "k")
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




df = pd.read_excel("lab4_06.xlsx")

V = df["V"]; A = df["A"]



parabs = [[12,27],[45,70],[96,109]]
df["parab"] = 0

conta = 1
lst_color = [conta]
for i in parabs:
    inf = i[0]; sup = i[1]
    for j in np.arange(inf, sup, 1):
        df["parab"][j] = conta
    conta = conta +1
    lst_color.append(conta)

#plt.scatter(V, A, c = df["parab"])

# Trabajar parábola por parábola
#no tomamos en cuenta la primera y última parábola (por gráfico)
lst_color = [1,2,3]
picos = []
for i in lst_color:
    coef = my_poli(df, i)
    pico_local = find_peak(coef)
    picos.append(pico_local)
    plot_maxs(df, coef, i, pico_local)
#plot_else(df, 0)


# VALORES DE RESTA
diferencias = []
for i in range(len(picos) -1):
    i = i + 1
    dif = picos[i] - picos[i-1]
    diferencias.append(dif)
    
print(np.mean(diferencias), np.var(diferencias))