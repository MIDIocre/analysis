#!/usr/bin/python

import sys
f=sys.stdin
c,pcs=[],[]
for l in f:
	ls=l.split()
	c.append(int(ls[0]))
	pcs.append(map(float,ls[1:]))

pcs=list(zip(*pcs))

import matplotlib.pyplot as plt
#for i in xrange(len(pcs[0]))
plt.scatter(pcs[0],pcs[1],c=c,lw=0,s=10,alpha=0.5,edgecolor='')

plt.savefig(sys.argv[1])

