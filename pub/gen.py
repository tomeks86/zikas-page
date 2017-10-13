#!/usr/bin/python

import sys

fin=open(sys.argv[1]).readlines()

N=1
for i in range(len(fin)):
	if fin[i]=='\n':
		N+=1

lout=""
li="\t\t<li>\n"
fli="\t\t</li>\n"
it="<i>"
fit="</i>"
br="<br />"
nl='\n'

I=0
for i in range(N-1):
	#print I
	lout+=li
	lout+="\t\t\t"+it
	lout+=fin[I].strip()
	lout+=fit+br+nl
	while (fin[I]!='\n'):
		I+=1
		lout+="\t\t\t"+fin[I].strip()+br+nl
	lout=lout.strip()+nl+fli
	I+=1

print lout
