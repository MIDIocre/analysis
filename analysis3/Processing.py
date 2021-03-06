#!/usr/bin/python

import sys
import numpy as np

def distance(s):	# function to calculate distances within bin
	ss=list(s)
	ss.sort()
	#print ss 
	dists=[0 for i in xrange(12)]
	for i in xrange(len(ss)-1):
		for j in xrange(i+1,len(ss)):
			#print ss[i],ss[j],abs(ss[i]-ss[j])%12
			dists[abs(ss[i]-ss[j])%12]+=1
	return dists

def distanceb(s1,s2):		# function to calculate distances between adjacent bin
	ss1=list(s1)
	ss2=list(s2)
	ss1.sort()
	ss2.sort()
	#print ss 
	dists=[0 for i in xrange(12)]
	for i in xrange(len(ss1)):
		for j in xrange(len(ss2)):
			#print ss[i],ss[j],abs(ss[i]-ss[j])%12
			dists[abs(ss1[i]-ss2[j])%12]+=1
	return dists


f=sys.stdin
dic={'Note_off_c':0, 'Note_on_c':1}
status=[0 for i in xrange(128)]
#fulldata=[]
s=set([])
durations=[]
sumdists, sumdists_w=np.zeros(12),np.zeros(12)
sumdistsb, sumdistsb_w=np.zeros(12), np.zeros(12)
sumnotes, sumnotes_w=np.zeros(128),np.zeros(128)
mark_firstbin=1
time_pre=-1
allnotes=[]
for l in f:
	#fulldata.append(status)
	ls=l.split()
	time=int(ls[1])
	note=int(ls[4])
	volecity=int(ls[5])
	spre=set(s)
	todo=dic[ls[2]]*volecity
	if todo==0:
		s.discard(note) # set of playing notes
		status[note]=0 # list of playing notes
	elif todo>0:
		s.add(note) # set of playing notes
		allnotes.append(note)
		#status[note]=volecity # volecity taken into account 
		status[note]=1 #volecity not taken into acount 
	if time!=time_pre: #only when time actually changed - change bin, do calculation
		duration=time-time_pre # duration of bin
		durations.append(duration)
		dists=np.array(distance(s))	#for sum calculations
		sumdists+=dists	#for sum calculations
		sumdists_w+=dists*duration	#for sum calculations weighted by duration
		if mark_firstbin==1:
			mark_firstbin=0
			distsb=np.zeros(12)
		else:
			distsb=np.array(distanceb(spre,s))
			sumdistsb+=distsb
			sumdistsb_w+=distsb*duration
		sumnotes+=np.array(status)
		sumnotes_w+=np.array(status)*duration
		#print str(duration)+'\t'+'\t'.join(map(str,dists))+'\t'+'\t'.join(map(str,distsb))+'\t'+'\t'.join(map(str,status))+'\t'+'\t'.join(map(str,duration*dists))+'\t'+'\t'.join(map(str,duration*distsb))+'\t'+'\t'.join(map(str,duration*status))       # print bin based statistics
		time_pre=time

modulated_notes=np.zeros(12) # 
for i in range(128):
	modulated_notes[i%12]+=sumnotes[i]


# result of the whole piece of music 
#print 'full\t'+'\t'.join(map(str,sumdists/sumdists.max()))+'\t'+'\t'.join(map(str,sumdistsb/sumdistsb.max()))+'\t'+'\t'.join(map(str,sumnotes/sumnotes.max()))+'\t'+'\t'.join(map(str,sumdists_w/sumdists_w.max()))+'\t'+'\t'.join(map(str,sumdistsb_w/sumdistsb_w.max()))+'\t'+'\t'.join(map(str,sumnotes_w/sumnotes_w.max()))


print 'full\t'+'\t'.join(map(str,(sumdists-sumdists.mean())/sumdists.std()))+ \
'\t'+'\t'.join(map(str,(sumdistsb-sumdistsb.mean())/sumdistsb.std()))+ \
'\t'+'\t'.join(map(str,(modulated_notes-modulated_notes.mean())/modulated_notes.std()))+ \
'\t'+'\t'.join(map(str,(sumnotes-sumnotes.mean())/sumnotes.std()))+ \
'\t'+'\t'.join(map(str,([np.median(durations),np.std(durations)])))+ \
'\t'+'\t'.join(map(str,([np.median(allnotes),np.std(allnotes)])))









