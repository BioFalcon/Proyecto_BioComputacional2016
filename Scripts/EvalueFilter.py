import csv
import os

with open('Trinity_Diff.blastx','r') as f:
 reader=csv.reader(f,delimiter='\t')
 Blast = list(reader)

i=0
while i < len(Blast):
 if float(Blast[i][10]) > 1E-9:
  del Blast[i]
 else:
  i=i+1

os.system('> Trinity_DiffEval.blastx')
f=open('Trinity_DiffEval.blastx','w')
for i in range(0,len(Blast)):
 f.write(Blast[i][0]+'\t'+Blast[i][1]+'\t'+Blast[i][2]+'\t'+Blast[i][3]+'\t'+Blast[i][4]+'\t'+Blast[i][5]+'\t'+Blast[i][6]+'\t'+Blast[i][7]+'\t'+Blast[i][8]+'\t'+Blast[i][9]+'\t'+Blast[i][10]+'\t'+Blast[i][11]+'\n')

f.close()
