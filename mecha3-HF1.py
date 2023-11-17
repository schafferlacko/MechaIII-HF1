# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 15:57:01 2023

@author: schaffer laszlo
"""

import numpy as np
import sympy as sp

L1=0.02
#L1=float(input("L1: "))
L2=0.18
#L2=float(input("L2: "))
L3=0.04
#L3=float(input("L3: "))
L4=0.08
#L4=float(input("L4: "))
alpha0=20
#alpha0=float(input("alpha0: "))
BC=0.06
#BC=float(input("BC: "))
omega1=np.array([0, 0, 10])
#omega1=np.array([0, 0, float(input("omega1: "))])
epsilon1=0

# ===============================
# vB=omega1*rAB
rAB=np.array([(np.cos(np.deg2rad(alpha0))*L1), (np.sin(np.deg2rad(alpha0))*L1), 0])

vB=np.cross(omega1, rAB)
print("vB vektor: "+str(vB))
print("vB vektor abszolútértéke: "+str(np.linalg.norm(vB)))

#================================
# vC=vB+omega1*rBC

rDBx=L4-rAB[0]
DB=np.sqrt((rDBx**2)+(rAB[1]**2))
#singamma1=rAB[1]/DB
radgamma1=np.arcsin(rAB[1]/DB)
gamma1=np.rad2deg(np.arcsin(rAB[1]/DB))

#BC**2=L3**2+DB**2-2*L3*DB*np.cos(gamma2)
radgamma2=np.arccos(((L3**2)+(DB**2)-BC**2)/(2*L3*DB))
gamma2=np.rad2deg(np.arccos(((L3**2)+(DB**2)-BC**2)/(2*L3*DB)))

rDC=np.array([(-1*(np.cos(radgamma1+radgamma2)))*L3, np.sin(radgamma1+radgamma2)*L3, 0])

#vC=vB+np.cross(a, b)
omega3, vC=sp.symbols('omega, vC')

#eq1=sp.Eq(vC, vB+(np.cross()))
