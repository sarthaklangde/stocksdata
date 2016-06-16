import sys
import time
import csv
import numpy
import math
import calendar
from datetime import datetime
import matplotlib.pyplot as plt
thisname, filename=sys.argv
#Create a list of rows of daily stock prices

exFile1=open(filename)
reader1=csv.reader(exFile1)
exData1=list(reader1)



lsize1=len(exData1)
print 'Size of data :',lsize1


name='output_'+filename





date_format = "%d/%m/%Y"
x=[]
y=[]
years=[]
indexst=[]
n=1
datecom = datetime.strptime(exData1[n][0],date_format)
while(datecom.year==2016):
    del exData1[n]
    datecom = datetime.strptime(exData1[n][0],date_format)






lsize1=len(exData1)
print lsize1
for n in range (1,lsize1):
    datecom = datetime.strptime(exData1[n][0],date_format)
    if(datecom.year not in years):
        years.append(datecom.year)
        indexst.append(n-1)
indexst.append(lsize1)
print len(years)
print indexst






lsize3=len(years)
n=1
k=0


w,h=367,lsize3
avg=[[0 for a in range(w)] for b in range(h)]

with open('mahindra_monthly_avg.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)

    #spamwriter.writerow(['Year','Price'])
w,h=12,lsize3
monthly=[[[] for a in range(w)] for b in range(h)]

#print len(monthly)


while(n<lsize1):
    with open('mahindra_monthly_avg.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL) 
        spamwriter.writerow([years[k]])           
        spamwriter.writerow(['Month','Price'])
            


    while(n<indexst[k+1]):
        datecom = datetime.strptime(exData1[n][0], date_format)
        if(exData1[n][2]!=''):

            x.append(datecom.timetuple().tm_yday)
            y.append(exData1[n][2])
            #print k,datecom.month
            monthly[k][datecom.month-1].append(exData1[n][2])
            #print datecom.month
        n=n+1
     
    print 'For year',years[k],':'
    for mon in range (0,12):
        monlen=len(monthly[k][mon])
        res=map(float,monthly[k][mon])
        monthlyavg=sum(res)/len(res)    
        print calendar.month_name[mon+1],':', round(monthlyavg,2)
        
        with open('mahindra_monthly_avg.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)            
            spamwriter.writerow([calendar.month_name[mon+1],round(monthlyavg,2)])
    
    del x[:]
    del y[:]
    k=k+1
    



