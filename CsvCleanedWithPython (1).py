import numpy as np
import pandas as pd
df = pd.read_csv('sales_data.csv')
df.head(5)
df.info()
df['Order Year']=df['Order Date'].str.split(' ').str[0].str.split('-').str[0]
df['Order Year']=df['Order Date'].str.split(' ').str[0].str.split('-').str[0]
df['Order Month']=df['Order Date'].str.split(' ').str[0].str.split('-').str[1]
#convert float data to int for minimize our data to low 
df['Order Month'] = df['Order Month'].astype(int)
df['Order Year'] = df['Order Year'].astype(int)

df.head(5)

#Modifying the various Products
category_mapping = {
  'USB-C Charging Cable': 'Charging Cables',
  'Lightning Charging Cable': 'Charging Cables',
  'AAA Batteries (4-pack)': 'Batteries', 
  'AA Batteries (4-pack)': 'Batteries',
  'Wired Headphones': 'Headphones',
  'Apple Airpods Headphones': 'Headphones',
  'Bose SoundSport Headphones': 'Headphones',
  '27in FHD Monitor': 'Smart Tv',
  '27in 4K Gaming Monitor': 'Smart Tv',
  '34in Ultrawide Monitor': 'Smart Tv',
  'Flatscreen TV': 'Smart Tv',
  '20in Monitor': 'Smart Tv',
  'iPhone': 'Smart Phones',
  'Google Phone': 'Smart Phones',
  'Vareebadd Phone': 'Smart Phones',
  'Macbook Pro Laptop': 'Laptops',
  'ThinkPad Laptop': 'Laptops',
  'LG Washing Machine': 'Cleaning Machines',
  'LG Dryer': 'Cleaning Machines'
}

def change(x):
  return category_mapping.get(x, 'Others')

df['Product'] = df['Product'].apply(change)

df.head(3)

category_mapping = {
  'Vêtements': 'Clothes',
  'Alimentation': 'Alimentation',
  'Électronique': 'Electronic', 
  'Sports': 'Sports'
}

def change1(x):
  return category_mapping.get(x, 'Others')

df['catégorie'] = df['catégorie'].apply(change)

df.tail(3)

#renaming the Category
df.rename(columns={'catégorie':'Category'},inplace=True)

df.tail(5)

 #Using regular expression to extract city name
df['Purchase City'] = df['Purchase Address'].str.extract(r', ([A-Za-z\s]+),', expand=False)

df.tail(5)

df.head(3)

# Dictionary to map int to month name
month_map = {1:'January', 2:'February', 3:'March', 4:'April', 
             5:'May', 6:'June', 7:'July', 8:'August',  
             9:'September', 10:'October', 11:'November', 12:'December'}

# Convert integer month to month name using map  
df['Order Month'] = df['Order Month'].map(month_map)


df.tail(5)

df.to_csv('data_modified.csv', index=False)

