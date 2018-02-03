'''
Created on 2018年1月11日

@author: gaoxing
'''
import random
from numbergen import UniformRandomInt
for i in range(1,16):
    a = random.randint(100,999)
    b = random.randint(10,99)
    print("%d题： %dx%d= \t%d题： %d/%d= " %(i,a,b,i,random.randint(100,999),random.randint(10,99)))

