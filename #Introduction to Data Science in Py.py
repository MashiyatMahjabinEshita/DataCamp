#Introduction to Data Science in Python

#Importing Python Modules 
import statsmodels as sm
import seaborn as sns
import numpy as np

#Creating numbers and strings

# Bayes' favorite toy
favorite_toy = "Mr. Squeaky"
type(favorite_toy)
## <class 'str'>

# Bayes' owner
owner = 'DataCamp'

## 'DataCamp'

# Bayes' height
height = 24
print('height  || ', height, ' || ', type(height))

## height  ||  24  ||  <class 'int'>
# Bayes' age
bayes_age = 4.0
print('bayes_age  || ', bayes_age, ' || ', type(bayes_age))

## bayes_age  ||  4.0  ||  <class 'float'>
# owner = DataCamp
# fur_color = "blonde'
#'===================================='
# 2.6 Load a DataFrame
# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
url = 'https://raw.githubusercontent.com/QuanNguyenIU/DataCamp/main/Python/Intro.%20to%20Data%20Science%20in%20Python/ransom.csv'
ransom = pd.read_csv(url)

# Display DataFrame
#ransom
#'===================================='
#3.2 Loading a DataFrame

# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
url = 'https://raw.githubusercontent.com/QuanNguyenIU/DataCamp/main/Python/Intro.%20to%20Data%20Science%20in%20Python/credit_records.csv'
credit_records = pd.read_csv(url)

# Display the first five rows of credit_records using the .head() method
credit_records.head()
#'========================================='
#3.3 Inspecting a DataFrame

credit_records.info()

## <class 'pandas.core.frame.DataFrame'>
## RangeIndex: 104 entries, 0 to 103
## Data columns (total 5 columns):
##  #   Column    Non-Null Count  Dtype  
## ---  ------    --------------  -----  
##  0   suspect   104 non-null    object 
##  1   location  104 non-null    object 
##  2   date      104 non-null    object 
##  3   item      104 non-null    object 
##  4   price     104 non-null    float64
## dtypes: float64(1), object(4)
## memory usage: 4.2+ KB
#=============================================
#3.5 Two methods for selecting columns

# Select the column item from credit_records
# Use brackets and string notation
credit_records["item"]

## 0         broccoli
## 1      fizzy drink
## 2         broccoli
## 3         broccoli
## 4            shirt
##           ...     
## 99           shirt
## 100          pants
## 101          dress
## 102         burger
## 103      cucumbers
## Name: item, Length: 104, dtype: object

# Select the column item from credit_records
# Use dot notation
items = credit_records.item
url = 'https://raw.githubusercontent.com/QuanNguyenIU/DataCamp/main/Python/Intro.%20to%20Data%20Science%20in%20Python/mpr.csv'
mpr = pd.read_csv(url)

# Use info() to inspect mpr
print(mpr.info())
# Select column "Dog Name" from mpr
name = mpr["Dog Name"]

# Select column "Status" from mpr
is_missing = mpr["Status"]

# Display the columns
print(name, is_missing)
#=========================================
#3.7 Logical testing
height_inches = 65
height_inches > 70
## False
plate1 = 'FRQ123'
plate1 == "FRQ123"
## True
fur_color = 'blonde'
fur_color != "brown"
#True
#========================================
#3.8 Selecting missing puppies

# Select the dogs where Age is greater than 2
mpr[mpr.Age > 2]
# Select the dogs whose Status is equal to Still Missing
mpr[mpr.Status == "Still Missing"]
# Select all dogs whose Dog Breed is not equal to Poodle
mpr[mpr["Dog Breed"] != "Poodle"]
#==========================================
#3.9 Narrowing the list of suspects
# Select purchases from 'Pet Paradise'
credit_records[credit_records.location == 'Pet Paradise']
#Plotting with matplotlib 
#4.2 Working hard
# From matplotlib, import pyplot under the alias plt
from matplotlib import pyplot as plt

# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked)

# Display Deshaun's plot
plt.show()
# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked)

# Plot Officer Aditya's hours_worked vs. day_of_week
plt.plot(aditya.day_of_week, aditya.hours_worked)

# Plot Officer Mengfei's hours_worked vs. day_of_week
plt.plot(mengfei.day_of_week, mengfei.hours_worked)

# Display all three line plots
plt.show()
#==========
#4.5 Adding a legend
# Officer Deshaun
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')

# Add a label to Aditya's plot
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')

# Add a label to Mengfei's plot
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a command to make the legend display
plt.legend()

# Display plot
plt.show()
#4.6 Adding labels
# Lines
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a title
plt.title('Hours Worked per Days of Week')

# Add y-axis label
plt.ylabel('Hours Worked')

# Legend
plt.legend()

# Display plot
plt.show()
#=====================
#4.7 Adding floating text
url = 'https://raw.githubusercontent.com/QuanNguyenIU/DataCamp/main/Python/Intro.%20to%20Data%20Science%20in%20Python/six_months.csv'
six_months = pd.read_csv(url)
six_months
# Create plot
plt.plot(six_months.month, six_months.hours_worked)

# Add annotation "Missing June data" at (2.5, 80)
plt.text(2.5, 80, "Missing June data")

# Display graph
plt.show()
#==============================
#4.9 Tracking crime statistics
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color="DarkCyan")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle=':')
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker='s')
plt.legend()
plt.show()
#====================================
#4.10 Playing with styles
# Change the style to fivethirtyeight
plt.style.use('fivethirtyeight')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()

# Change the style to ggplot
plt.style.use('ggplot')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()

# View all available styles
plt.style.available
#=================================
#4.11 Identifying Bayes’ kidnapper
# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label = 'Ransom', linestyle = ':', color = 'gray')
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

# Add x- and y-labels
plt.xlabel("Letter")
plt.ylabel("Frequency")

# Add a legend
plt.legend()

# Display plot
plt.show()

