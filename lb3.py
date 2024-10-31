#!/usr/bin/env python3
import sys
sys.stderr=open('errors.txt','a')
A=int(input("Write number: "))
A=A**0.5
print("sqrt(A)=", A)
res=open("output.txt",'w')
res.write(str(A))
res.close()
sys.stderr=open('errors.txt','w')
