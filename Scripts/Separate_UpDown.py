import csv
import os

with open('Differential0_05.csv','r') as f:
 reader=csv.reader(f,delimiter='\t')
 DESeq = list(reader)


i=1
Up=[]
Down=[]
while i < len(DESeq):
 if float(DESeq[i][2]) > 0: 
  Up.append(DESeq[i])
 else:
  Down.append(DESeq[i])
 i=i+1

os.system('> Up0_05.tab')
os.system('> Down0_05.tab')
f=open('Up0_05.tab','w')
g=open('Down0_05.tab','w')
f.write('ID'+'\t'+DESeq[0][0]+'\t'+DESeq[0][1]+'\t'+DESeq[0][2]+'\t'+DESeq[0][3]+'\t'+DESeq[0][4]+'\t'+DESeq[0][5]+'\n')
g.write('ID'+'\t'+DESeq[0][0]+'\t'+DESeq[0][1]+'\t'+DESeq[0][2]+'\t'+DESeq[0][3]+'\t'+DESeq[0][4]+'\t'+DESeq[0][5]+'\n')
for i in range(0,len(Up)):
 f.write(Up[i][0]+'\t'+Up[i][1]+'\t'+Up[i][2]+'\t'+Up[i][3]+'\t'+Up[i][4]+'\t'+Up[i][5]+'\t'+Up[i][6]+'\n')

for i in range(0,len(Down)):
 g.write(Down[i][0]+'\t'+Down[i][1]+'\t'+Down[i][2]+'\t'+Down[i][3]+'\t'+Down[i][4]+'\t'+Down[i][5]+'\t'+Down[i][6]+'\n')

f.close()
g.close()
