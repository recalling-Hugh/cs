import sys
Haab={'pop':0,'no':1,'zip':2,'zotz':3,'tzec':4,'xul':5,'yoxkin':6,'mol':7,'chen':8,'yax':9,'zac':10,'ceh':11,'mac':12,'kankin':13,'muan':14,'pax':15,'koyab':16,'cumhu':17,'uayet':18}
Tzolkin=['imix','ik','akbal','kan','chicchan','cimi','manik','lamat','muluk','ok','chuen','eb','ben','ix','mem','cib','caban','eznab','canac','ahau']
n=int(sys.stdin.readline())
print(n)
for i in range(n):
    day=sys.stdin.readline().split()
    day[0]=int(day[0].replace('.',''))
    day[2]=int(day[2])
    num=day[0]+Haab[day[1]]*20+day[2]*365+1
    date1=num%13
    if date1==0:
        date1=13
    date2=num%20
    if date2==0:
        date2=20
    date2=Tzolkin[date2-1]
    year=(num-1)//260
    print(date1,date2,year)