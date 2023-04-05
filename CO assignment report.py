# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 03:05:54 2023

@author: hp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_file(file_name):
    """
    This function takes name of the file and reads it from local directory and loads it into a dataframe.
    Then transposes the dataframe and returns both the first and transposed dataframes. It also sets
    the header for the transposed dataframe
    Parameters
    ----------
    file_name : string
        Name of the file tobe read into the datarame.
    Returns
    -------
    
    A dataframe loaded from the file and it's transpose.
    """

    name = file_name
    df = pd.read_excel(name)
    df_transpose = pd.DataFrame.transpose(df)
    #Header setting
    header = df_transpose.iloc[0].values.tolist()
    df_transpose.columns = header
    return(df, df_transpose)
def clean_df(df):
    """
    
    Parameters
    ----------
    df : dataframe
        Dataframe that needs to be cleaned and index converted.
    Returns
    -------
    df : dataframe
        dataframe with required columns and index as int.
    """

    #Cleaning the dataframe
    df = df.iloc[1:]
    df = df.iloc[11:55]
    
    #Converting index ot int
    df.index = df.index.astype(int)
    df = df[df.index>1989]

    #cleaning empty cells
    df = df.dropna(axis = 'columns')
    return df
df_energy_total,df_energy_countries = read_file("C:/Users/hp/Downloads/Electric_power_consumption 2.xls")
#mean and median
print(df_energy_total,df_energy_countries.describe())

country =['Albania', 'Algeria','Angola','Bahrain','Bangladesh','Brazil','China','Colombia','Denmark','Ethiopia','Germany']
country_name =['AL', 'DZ', 'AO','BHR','BD', 'BR', 'CN', 'COL', 'DK', 'ET', 'GE']
years= [1990, 1994, 1998, 2002, 2006, 2010, 2014]
#Cleaning the dataframe
df_energy_countries = clean_df(df_energy_countries)

#selecting only required data
df_energy_time = pd.DataFrame.transpose(df_energy_countries)
df_energy_subset_time = df_energy_time[years].copy()
df_energy_subset_time = df_energy_subset_time.loc[df_energy_subset_time.index.isin(country)]

#plotting the data
n= len(country)
r=np.arange(n)
width= 0.1
plt.bar(r-0.3, df_energy_subset_time[1990], color = 'grey',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_energy_subset_time[1994], color = 'green',width = width, edgecolor = 'black',label='1994')
plt.bar(r-0.1, df_energy_subset_time[1998], color = 'orange',width = width, edgecolor = 'black',label='1998')
plt.bar(r, df_energy_subset_time[2002], color = 'red',width = width, edgecolor = 'black',label='2002')
plt.bar(r+0.1, df_energy_subset_time[2006], color = 'steelblue',width = width, edgecolor = 'black',label='2006')
plt.bar(r+0.2, df_energy_subset_time[2010], color = 'greenyellow',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.3, df_energy_subset_time[2014], color = 'khaki',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("Electricity use")
plt.xticks(width+r, country_name)
plt.legend()
plt.title("Electric power consumption (kWh per capita)")
plt.savefig("Electric_power.png", dpi=300, bbox_inches='tight')
plt.show()
df_methane_total,df_methane_countries = read_file("C:/Users/hp/Downloads/methnae co2 emissions.xls")

country =['Albania', 'Algeria','Angola','Bahrain','Bangladesh','Brazil','China','Colombia','Denmark','Ethiopia','Germany']
country_name =['AL', 'DZ', 'AO','BHR','BD', 'BR', 'CN', 'COL', 'DK', 'ET', 'GE']
years= [1990, 1994, 1998, 2002, 2006, 2010, 2014]

df_methane_countries = clean_df(df_methane_countries)

#selecting the data
df_methane_time = pd.DataFrame.transpose(df_methane_countries)
df_methane_subset_time = df_methane_time[years].copy()
df_methane_subset_time = df_methane_subset_time.loc[df_methane_subset_time.index.isin(country)]

#plotting the data
n= len(country)
r=np.arange(n)
width= 0.1
plt.bar(r-0.3, df_methane_subset_time[1990], color = 'steelblue',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_methane_subset_time[1994], color = 'greenyellow',width = width, edgecolor = 'black',label='1995')
plt.bar(r-0.1, df_methane_subset_time[1998], color = 'steelblue',width = width, edgecolor = 'black',label='2000')
plt.bar(r, df_methane_subset_time[2002], color = 'violet',width = width, edgecolor = 'black',label='2005')
plt.bar(r+0.1, df_methane_subset_time[2006], color = 'darkgrey',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.2, df_methane_subset_time[2010], color = 'navy',width = width, edgecolor = 'black',label='2014')
plt.bar(r+0.3, df_methane_subset_time[2014], color = 'purple',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Country")
plt.ylabel(" Methane emission")
plt.xticks(width+r, country_name)
plt.legend()
plt.title("methane emissions (kt)")
plt.savefig("methane.png", dpi=300, bbox_inches='tight')
plt.show()
#GDP
df_gdp_total, df_gdp_countries= read_file("C:/Users/hp/Downloads/GDP 2.xls")

#Cleaning the dataframe

df_gdp_countries= df_gdp_countries.iloc[1:]
df_gdp_countries = df_gdp_countries.iloc[11:55]

df_gdp_countries.index = df_gdp_countries.index.astype(int)
df_gdp_countries = df_gdp_countries[df_gdp_countries.index>1989]





#GDP LINE PLOT
plt.figure()
plt.plot(df_gdp_countries.index, df_gdp_countries["Bangladesh"])
plt.plot(df_gdp_countries.index, df_gdp_countries["China"] )
plt.plot(df_gdp_countries.index, df_gdp_countries["Germany"])
plt.plot(df_gdp_countries.index, df_gdp_countries["France"])
plt.plot(df_gdp_countries.index, df_gdp_countries["United Kingdom"])
plt.plot(df_gdp_countries.index, df_gdp_countries["India"])
plt.plot(df_gdp_countries.index, df_gdp_countries["Kenya"])
plt.plot(df_gdp_countries.index, df_gdp_countries["Saudi Arabia"])
plt.plot(df_gdp_countries.index, df_gdp_countries["United States"])

plt.xlim(1991,2014)
plt.xlabel("Year")
plt.ylabel("GDP")
plt.legend(['BD', 'CN', 'DE',  'FR', 'UK', 'IN', 'KE', 'KSA', 'US', 'IL'], prop = {'size': 8})
plt.title("GDP per captia")
plt.savefig("GDP_Per_Capita.png", dpi = 300, bbox_inches='tight')
plt.show()
#population data
df_pop_total,df_pop_countries = read_file("C:/Users/hp/Documents/ASSIGNMENT 2/population growth11.xlsx")
df_pop_countries = df_pop_countries.iloc[1:]
df_pop_countries = df_pop_countries.iloc[11:55]

df_pop_countries.index = df_pop_countries.index.astype(int)
df_pop_countries = df_pop_countries[df_pop_countries.index>1989]





#plotting the population data
n= len(country)
r=np.arange(n)
width= 0.1
plt.figure()
plt.plot(df_pop_countries.index, df_pop_countries["Bangladesh"])
plt.plot(df_pop_countries.index, df_pop_countries["China"] )
plt.plot(df_pop_countries.index, df_pop_countries["Germany"])
plt.plot(df_pop_countries.index, df_pop_countries["France"])
plt.plot(df_pop_countries.index, df_pop_countries["United Kingdom"])
plt.plot(df_pop_countries.index, df_pop_countries["India"])
plt.plot(df_pop_countries.index, df_pop_countries["Kenya"])
plt.plot(df_pop_countries.index, df_pop_countries["Saudi Arabia"])
plt.plot(df_pop_countries.index, df_pop_countries["United States"])
plt.xlim(1991,2014)
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend(['BD', 'CN', 'DE',  'FR', 'UK', 'IN', 'KE', 'KSA', 'US', 'IL'], prop = {'size': 8})
plt.title("Population growth")
plt.savefig("Population.png", dpi = 300, bbox_inches='tight')
plt.show()


