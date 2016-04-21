import csv
import os

with open('Counts_All.txt','r') as f:
 reader=csv.reader(f,delimiter='\t')
 Counts = list(reader)

i=0
while i < len(Counts):
 j=i+1
 while j < len(Counts):
  if Counts[i][7] == Counts[j][7]:
   Counts[i][1]= int(Counts[i][1])+int(Counts[j][1])
   Counts[i][2]= int(Counts[i][2])+int(Counts[j][2])
   Counts[i][3]= int(Counts[i][3])+int(Counts[j][3])
   Counts[i][4]= int(Counts[i][4])+int(Counts[j][4])
   Counts[i][5]= int(Counts[i][5])+int(Counts[j][5])
   Counts[i][6]= int(Counts[i][6])+int(Counts[j][6])
   print Counts[j][0]
   del Counts[j]
  else:
   break
 i=i+1

os.system('> Counts_Collapsed.txt')
f= open('Counts_Collapsed.txt','w')
for i in range(0,len(Counts)):
 f.write(Counts[i][0]+'\t'+str(Counts[i][1])+'\t'+str(Counts[i][2])+'\t'+str(Counts[i][3])+'\t'+str(Counts[i][4])+'\t'+str(Counts[i][5])+'\t'+str(Counts[i][6])+'\n')

f.close()
