# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:17:19 2021
Good T-test
@author: matte
"""
import numpy as np
import random
import matplotlib.pyplot as plt
a= list(())#insert dataset here
mu_a=np.mean(a)
sigma_a=(np.std(a))
print("The Mean of set a is", mu_a)
print("The standard deviation for set a is", sigma_a)
N_a=len(a)#number of items in a set
print("The number of items in set a is",N_a)
SEM_a=sigma_a/(np.sqrt(N_a))
print("The standard error for set a is", SEM_a)
print("Do you want to just run a t-test and find other info with full data?")
c= list(())#insert dataset here
print("")
mode= input("Input:", )
if mode=="yes":
    mu_c=np.mean(c)#average calculation
    sigma_c=(np.std(c))#standard deviation
    N_c=len(c)#number of items in a set 
    print("")#to put space between lines
    print("The Mean of set b is", mu_c)
    print("The standard deviation for set b is", sigma_c)
    print("The number of items in set b is",N_c)
    SEM_c=sigma_c/(np.sqrt(N_c))
    print("The standard error for set b is", SEM_c)
    print("")#to put space between lines
    t=(mu_a-mu_c)/(np.sqrt((sigma_a**2)/N_a)+((sigma_c)**2)/N_c)#calculates the t stat
    print("The t-statistic between a and b is",t)
    df_1=((((sigma_a**2)/N_a)+((sigma_c**2/N_c)))**2)/((sigma_a**4/((N_a)**2*(N_a-1)+(sigma_c**4/((N_c)**2*(N_c-1))))))
    print("With", df_1, "degrees of freedom")
    graph=input("Do you want the bell curves for a and b?")
    if graph=="yes":
        x=np.linspace(np.min(a),np.max(a),1000)
        y=(1/(np.sqrt(2*3.14159))*(2.71828**-((x-mu_a)**2)/(2*sigma_a**2)))
        plt.plot(x,y)
        x=np.linspace(np.min(c),np.max(c),1000)
        y=(1/(np.sqrt(2*3.14159))*(2.71828**-((x-mu_c)**2)/(2*sigma_c**2)))
        plt.plot(x,y)
        plt.show()
    histogram=input("do you want the histogram?")
    if histogram=="yes":
        plt.hist(a)
        plt.hist(c)
if mode=="no":
    b= list(random.choice(c)
    for i in range(0, N_a))
    mu_b=np.mean(b)#average calculation
    sigma_b=(np.std(b))#standard deviation
    N_b=len(b)#number of items in a set 
    print("")#to put space between lines
    print("The Mean of set b is", mu_b)
    print("The standard deviation for set b is", sigma_b)
    print("The number of items in set b is",N_b)
    SEM_b=sigma_b/(np.sqrt(N_b))
    print("The standard error for set b is", SEM_b)
    print("")#to put space between lines
    t=(mu_a-mu_b)/(np.sqrt((sigma_a**2)/N_a)+((sigma_b)**2)/N_b)#calculates the t stat
    print("The t-statistic between a and b is",t)
    df=((((sigma_a**2)/N_a)+((sigma_b**2/N_b)))**2)/((sigma_a**4/((N_a)**2*(N_a-1)+(sigma_b**4/((N_b)**2*(N_b-1))))))
    print("With", df, "degrees of freedom")
    print("")
    
    graph=input("Do you want the bell curves for a and b?")
    if graph=="yes":
        x=np.linspace(np.min(a),np.max(a),1000)
        y=(1/(np.sqrt(2*3.14159))*(2.71828**-((x-mu_a)**2)/(2*sigma_a**2)))
        plt.plot(x,y)
        x=np.linspace(np.min(b),np.max(b),1000)
        y=(1/(np.sqrt(2*3.14159))*(2.71828**-((x-mu_b)**2)/(2*sigma_b**2)))
        plt.plot(x,y)
        plt.show()
    histogram=input("do you want the histogram?")
    if histogram=="yes":
        plt.hist(a)
        plt.hist(b)
        

