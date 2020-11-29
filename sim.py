# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:08:32 2020

@author: koval
"""

from scipy import sparse as sp
import numpy as np

#initialisation des variables
a0 = 38.10#meVnm^2
dz = 0.01#nm
Lb = 70#nm
Lp = 10#nm
L=Lp+2*Lb
N=int(L/dz+1)
_y1=[16.20,13.37,21.44]
_y2=[5.82,4.23,8.43]
_K=[1.89,3.41,1.12]
_V=[50,0,45]
print(L/dz)

#Création du maillage
z=np.linspace(0,L,N)

#Création des matrices des opérateurs
temp=[_y1[0]*sp.identity((Lb/L*N)+1),_y1[1]*sp.identity(Lp/L*N),_y1[2]*sp.identity(Lb/L*N)]
y1=sp.block_diag(temp).toarray()
temp=[_y2[0]*sp.identity((Lb/L*N)+1),_y2[1]*sp.identity(Lp/L*N),_y2[2]*sp.identity(Lb/L*N)]
y2=sp.block_diag(temp).toarray()
temp=[_K[0]*sp.identity((Lb/L*N)+1),_K[1]*sp.identity(Lp/L*N),_K[2]*sp.identity(Lb/L*N)]
K=sp.block_diag(temp).toarray()
temp=[_V[0]*sp.identity((Lb/L*N)+1),_V[1]*sp.identity(Lp/L*N),_V[2]*sp.identity(Lb/L*N)]
V=sp.block_diag(temp).toarray()
