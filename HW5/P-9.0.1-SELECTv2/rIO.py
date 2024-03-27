import os, sys

def readMatrix(ax):
    n_row = int(ax[0])
    n_col = int(ax[1])

    ret = []
    for i in range(n_row):
        ret.append( list(map(int, ax[2+i*n_col: 2+(i+1)*n_col])))
        pass

    return ret, ax[n_row*n_col+2:]

def readArray(ax):
    n = int(ax[0])
    
    ret = list(map(int, ax[1:1+n]))
    return ret, ax[1+n:]

def get_jpa_shortname():
    prefix = '-'.join(os.path.basename(os.getcwd()).split('-')[2:])
    return prefix