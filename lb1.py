#!/usr/bin/env python3
import random
import sys
sys.stderr=open('errors.txt','a')
A=random.randint(-10,10)
print(A)
sys.stderr=open('errors.txt','w')
