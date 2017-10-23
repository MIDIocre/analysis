#!/usr/bin/python

import sys
import numpy as np

def distance(s):
	ss=list(s)
	ss.sort()
	#print ss 
	dists=[0 for i in xrange(12)]
	for i in xrange(len(ss)-1):
		for j in xrange(i+1,len(ss)):
			#print ss[i],ss[j],abs(ss[i]-ss[j])%12
			dists[abs(ss[i]-ss[j])%12]+=1
	return dists



f=sys.stdin
dic={'Note_off_c':0, 'Note_on_c':1}
status=[0 for i in xrange(128)]
#fulldata=[]
s=set([])
sumdists=np.zeros(12)
sumnotes=np.zeros(128)
for l in f:
	#fulldata.append(status)
	ls=l.split()
	time=int(ls[1])
	note=int(ls[4])
	volecity=int(ls[5])
	todo=dic[ls[2]]*volecity
	if todo==0:
		s.discard(note) # set of playing notes
		status[note]=0 # list of playing notes
	elif todo>0:
		s.add(note) # set of playing notes
		#status[note]=volecity # volecity into account 
		status[note]=1 #volecity not into acount 
	dists=np.array(distance(s))
	sumnotes+=np.array(status)
	sumdists+=dists	#for sum calculations
	#print time,status
	#print time,s
	print str(time)+'\t'+'\t'.join(map(str,dists))+'\t'+'\t'.join(map(str,status))

print 'full\t'+'\t'.join(map(str,sumdists/sumdists.max()))+'\t'+'\t'.join(map(str,sumnotes/sumnotes.max()))

#fulldata.append(status)







