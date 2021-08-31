#!/usr/bin/env python3
#Author:WMO
#version:V0.03(a basic version,need a bug update,unkown)
#the text just used in TECHNOLOGY
import random
r=random.choice
b=('-','+')
n=0
while n<6:
    x=r(b)
    y=r(b)
    z=r(b)
    n+=1
    if x==y==z=='-':
        m='+'
        print(x,y,z,'\033[0;31m--->\033[0m',m,m,m)
    elif x==y==z=='+':
        k='-'
        print(x,y,z,'\033[0;31m--->\033[0m',k,k,k)
    else:
        print(x,y,z,'\033[0;32m--->\033[0m',x,y,z)
