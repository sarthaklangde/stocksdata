import sys
import time
import csv
import numpy
import math

thisname, filename=sys.argv
#Create a list of rows of daily stock prices

exFile1=open('SENSEX.csv')
reader1=csv.reader(exFile1)
exData1=list(reader1)

exFile2=open(filename)
reader2=csv.reader(exFile2)
exData2=list(reader2)


lsize1=len(exData1)
print 'Size of data :',lsize1

lsize2=len(exData2)
print 'Size of data :',lsize2

x=[]
y=[]
i=1;
j=1;
while((i<lsize1) and (j<lsize2)):
	datesen = time.strptime(exData1[i][0], "%d/%m/%Y")
	datecom = time.strptime(exData2[j][0], "%d/%m/%Y")
	if(datesen==datecom):
		if(exData1[i][2]!='' and exData2[j][2]!=''):
			x.append(exData1[i][2])
			y.append(exData2[j][2])
		i=i+1
		j=j+1	
		#print 'Hello'
					
	else:
		if(datesen>datecom):
			i=i+1
			#print 'LO!'
		else:
			j=j+1	
			#print 'LO@'


'''for n in range (1,lsize1):
	datesen = time.strptime(exData1[n][0], "%d/%m/%Y")
	datecom = time.strptime(exData2[n][0], "%d/%m/%Y")
	if(datesen==datecom):
		if(exData1[n][2]!=''&&exData2[n][2]!=''):
			x.append(exData1[n][2])
			y.append(exData2[n][2])
				
	
		

exd=numpy.array(exData)

#x is first columns and y is second'''

lsize=len(x)

x=numpy.array(x).astype(numpy.float)
y=numpy.array(y).astype(numpy.float)
with open('output.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter='"',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for n in range(lsize):
		spamwriter.writerow([x[n],y[n]])



yy=[]
xx=[]
xy=[]
for n in range(lsize):
    xy.append(x[n]*y[n])
    xx.append(x[n]*x[n])
    yy.append(y[n]*y[n])


 
sumx=numpy.sum(x).astype(numpy.float)
sumxx=numpy.sum(xx).astype(numpy.float)
sumy=numpy.sum(y).astype(numpy.float)
sumyy=numpy.sum(yy).astype(numpy.float)
sumxy=numpy.sum(xy).astype(numpy.float)

'''print sumx
print sumy
print sumxx
print sumxy
print sumyy'''
sxx=sumxx-((sumx*sumx)/lsize)
syy=sumyy-((sumy*sumy)/lsize)
sxy=sumxy-((sumx*sumy)/lsize)


sigma=sxy/math.sqrt(sxx*syy)

print 'Correlation : ',sigma




