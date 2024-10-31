#!/usr/bin/env python3
import random
import sys
sys.stderr=open('errors.txt','a')
A=int(input("Write A: "))
B=random.randint(-10,10)
print("B=",B)
if B==0:
    print("Error, B=0")
else:
    print("A/B=",A/B)
sys.stderr=open('errors.txt','w')
