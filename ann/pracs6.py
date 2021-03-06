# -*- coding: utf-8 -*-
"""171104056NehaShinkrepracs6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PP_SgehnfKedhRf2fGghHLeAeNV9BAng
"""

#perceptron learning rule

import numpy as np
w=np.array([1,-1,0,0.5])
x1=np.array([1,-2,0,-1])
x2=np.array([0,1.5,-0.5,-1])
x3=np.array([-1,1,0.5,-1])

def cal(x,w):
  op1=x*w
  i=0
  y=0
  while i!=len(op1):
    y=y+op1[i]
    i=i+1
  if y>=0:
    o1=1
  else:
    o1=-1
  return o1  

def perceptron(w,x,c,d):
    op=(d-cal(x,w))
    a=c*op*x      
    w=w+a
    print(w)
    return w

print("w2,w3,w4 are as follows:")
c=0.1
w2=perceptron(w,x1,c,-1)
w3=perceptron(w2,x2,c,-1)
w4=perceptron(w3,x3,c,1)