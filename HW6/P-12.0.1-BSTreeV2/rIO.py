# Created by Jiang Long 
# 
# DKU CS301 FALL 2021 SESSION 01
# 

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


def concat_text_block(a,b, msg):
    msg = '\n'.join([i for i in msg.splitlines() if len(i.strip())>0])
    msg_width = max(map(lambda i:len(i.rstrip()), msg.splitlines()))
    mx = '''
%s>
%s
%s>
''' % ('-'*msg_width, msg, '-'*msg_width)
    
    aheight = len( a.splitlines())
    mheight = len(mx.splitlines())
    if aheight > mheight:
        mx = ('\n'.join( [''] * ((aheight - mheight)//2))) + mx
        pass
    
    c = concat_text_block2(a,mx)
    c = concat_text_block2(c,b)
    return c

def concat_text_block2(a,b, space = 4):
    
    ax = a.splitlines()
    bx = b.splitlines()
    
    # extend match both's height
    if len(ax)< len(bx): ax.extend(['']* (len(bx) - len(ax)))
    if len(bx)< len(ax): bx.extend(['']* (len(ax) - len(bx)))
    
    # side a 's max width
    a_width = max(map(lambda i:len(i.rstrip()), a.splitlines()))
    
    fill_fn = lambda i: i.rstrip() + ' '* (a_width + space - len(i.rstrip()))
    m = [ fill_fn(i) + j for i,j in zip(ax,bx)]
    return '\n'.join(m)
        
def dash(tag, n=60):
    print ('-'*n)    
    print(tag)
    print ('-'*n)
    return 