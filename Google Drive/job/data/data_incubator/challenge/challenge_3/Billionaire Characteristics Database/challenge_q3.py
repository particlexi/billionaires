#analyze billionaires from 1996-2014 data

import pandas as pd
import numpy as np

billfile = pd.read_stata("Billionaires1996-2014.dta")

cn_bill = billfile[(billfile.countrycode=="CHN")]
us_bill = billfile[(billfile.countrycode=="USA")]

##########################################################################################
us_networth_year = us_bill.groupby("year")["networthusbillion"].sum()
us_gdp = us_bill.groupby("year")["gdpcurrentus"].mean()
us_ratio = us_networth_year/us_gdp
us_ratio.fillna(0,inplace=True)
us_ratio = us_ratio[us_ratio!=0]
us_ratio_max = us_ratio.max()
us_ratio = us_ratio/us_ratio_max
us_gdp.fillna(0,inplace=True)
us_gdp = us_gdp[us_gdp!=0]

cn_networth_year = cn_bill.groupby("year")["networthusbillion"].sum()
cn_gdp = cn_bill.groupby("year")["gdpcurrentus"].mean()
cn_ratio = cn_networth_year/cn_gdp
cn_ratio.fillna(0,inplace=True)
cn_ratio = cn_ratio[cn_ratio!=0]
cn_ratio = cn_ratio/us_ratio_max
cn_gdp.fillna(0,inplace=True)
cn_gdp = cn_gdp[cn_gdp!=0]

##########################################################################################
us_networth_av = us_bill.groupby("year")["networthusbillion"].mean()
us_networth_av.fillna(0,inplace=True)
us_networth_av = us_networth_av[us_networth_av!=0]
us_networth_av = us_networth_av.drop([2015])
us_networth_av = us_networth_av.drop(["September 2015"])
us_num = us_bill.groupby("year")["name"].count()
us_num.fillna(0,inplace=True)
us_num = us_num[us_num!=0]
us_num = us_num.drop([2015])
us_num = us_num.drop(["September 2015"])

cn_networth_av = cn_bill.groupby("year")["networthusbillion"].mean()
cn_networth_av.fillna(0,inplace=True)
cn_networth_av = cn_networth_av[cn_networth_av!=0]
cn_networth_av = cn_networth_av.drop([2015])
cn_networth_av = cn_networth_av.drop(["September 2015"])
cn_num = cn_bill.groupby("year")["name"].count()
cn_num.fillna(0,inplace=True)
cn_num = cn_num[cn_num!=0]
cn_num = cn_num.drop([2015])
cn_num = cn_num.drop(["September 2015"])
##########################################################################################

import matplotlib.pyplot as plt

fig1 = plt.figure()

plt.subplot(2,1,1)
plt.scatter(us_ratio.index,us_ratio,color='red',s=50,label='USA')
plt.scatter(cn_ratio.index,cn_ratio,color='blue',s=50,label='CHN')
plt.ylim((0 ,1.1))
#plt.ylim((0 ,15*10**(-11)))
#plt.xlabel('Year',fontsize=20)
plt.ylabel('Total Billionaire Wealth/GDP\n[a.u.]',fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend()

plt.subplot(2,1,2)
plt.scatter(us_gdp.index,us_gdp,color='red',s=50)
plt.scatter(cn_gdp.index,cn_gdp,color='blue',s=50)
#plt.ylim((0 ,1.1))
plt.ylim((0 ,2*10**(13)))
plt.xlabel('Year',fontsize=20)
plt.ylabel('GDP (Dollar)',fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)


##########################################################################################

fig2 = plt.figure()

plt.subplot(2,1,1)
plt.scatter(us_networth_av.index,us_networth_av,color='red',s=50,label='USA')
plt.scatter(cn_networth_av.index,cn_networth_av,color='blue',s=50,label='CHN')
plt.ylim((0 ,10))
#plt.ylim((0 ,15*10**(-11)))
#plt.xlabel('Year',fontsize=10)
plt.ylabel('Average Billionaire Wealth\n(Billion Dollar)',fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend()

plt.subplot(2,1,2)
plt.scatter(us_num.index,us_num,color='red',s=50)
plt.scatter(cn_num.index,cn_num,color='blue',s=50)
plt.ylim((0 ,600))
#plt.ylim((0 ,2*10**(13)))
plt.xlabel('Year',fontsize=20)
plt.ylabel('Number of Billionaires',fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.show()