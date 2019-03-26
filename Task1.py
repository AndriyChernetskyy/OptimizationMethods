import pandas as pd
from math import fabs

def f(x):
    return x**6 + 3*x**2 + 6*x -1
    
def dichotomy_method() :
    eps = float(input('eps = '))
    delta = float(input('float = '))
    a = int(input('a = '))
    b = int(input('b = '))
    
    y_i = list()
    z_i = list()
    f_y = list()
    f_z = list()
    a_k = list()
    b_k = list()

    while (fabs(a - b) > eps) :
        yk = (a + b - delta) / 2
        zk = (a + b + delta) / 2
        y_i.append(yk)
        z_i.append(zk)
        fyk = f(yk)
        f_y.append(fyk)
        fzk = f(zk)
        f_z.append(fzk)
        if fyk > fzk :
            a = yk
            a_k.append(a)
            b_k.append(b)
        if fyk <= fzk :
            b = zk
            a_k.append(a)
            b_k.append(b)
        
    x = (a_k[-2] - b_k[-2]) / 2 
    print('\nx = ' + str(x) + '\n')

    dict = {
        "yk":y_i[:-1],
        "zk":z_i[:-1],
        "f(y)":f_y[:-1],
        "f(z)":f_z[:-1],
        "ak":a_k[:-1],
        "bk":b_k[:-1]
    }
    brics = pd.DataFrame(dict)
    brics.index += 1
    return brics

print(dichotomy_method())