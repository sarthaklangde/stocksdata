import sys
import csv
import numpy
import matplotlib.pyplot as plt

thisfile,filename=sys.argv


#Create a list of rows of daily stock prices
exFile=open(filename)

reader=csv.reader(exFile)
exData=list(reader)

lsize=len(exData)
print 'Number of years :',lsize

exd=numpy.array(exData)
x=numpy.array(exd[:,0]).astype(numpy.float)
y=numpy.array(exd[:,1]).astype(numpy.float)
plt.xticks(x)
plt.plot(x,y)
'''#plt.xlim((0,numpy.maximum(x))
#plt.ylim((0,numpy.maximum(x))

xy=[]
xx=[]
for n in range(lsize):
    xy.append(x[n]*y[n])
    xx.append(x[n]*x[n])

print xy
print xx
 
sumx=numpy.sum(x)
sumy=numpy.sum(y)
sumxy=numpy.sum(xy)
sumxx=numpy.sum(xx)

slopem=((lsize*(sumxy))-(sumx*sumy))/((lsize*sumxx)-(sumx*sumx)).astype(numpy.float)
print 'm =',slopem


interc=((sumy-slopem*sumx)/lsize).astype(numpy.float)
print 'c =',interc

print 'Equation of Regression Line is : y = ',slopem,'x +',interc
equation=slopem*x+interc

plt.plot(x,equation)'''
plt.rcParams['xtick.major.pad'] = 8
plt.savefig('abc.png',dpi=100)


