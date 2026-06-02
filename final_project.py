import pandas as pd
import numpy as np
"""data={
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["Ram Sharma", "Sita Thapa", "Hari Karki", "Gita Rai", "Rohan Shah"],
    "Age": [24, 28, 32, 26, 30],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [45000, 40000, 55000, 48000, 52000],
    "Experience": [2, 4, 7, 3, 5],
    "City": ["Kathmandu", "Pokhara", "Lalitpur", "Bhaktapur", "Kathmandu"]
}
df=pd.DataFrame(data)
df.to_csv("employee_data.csv", index=False)
print("csv file created successfully")"""

df=pd.read_csv("/Users/stutipangeni/Downloads/numpy_python/employee_data.csv")
""""print(df.head())
print(df.tail())
print(df[['Name','Salary']])"""
"""result=df['Salary']>50000
print(df[result])"""

"""result=df['City']=='Kathmandu'
print(df[result])"""

"""result=np.mean(df['Salary'])
print("Average Salary:", result)"""

"""result=np.min(df['Salary'])
print(f"minimum salary : {result}")"""

"""count=np.sum(df['EmployeeID'].isin(df['Department']))
print(f"Total number of employees in each department:\n{count}")"""
"""
sorting=df.sort_values(by='Salary',ascending=False)
print(sorting)"""

"""grouping=df.groupby('Department')[('EmployeeID')].count()
print(grouping)
"""
"""grouping=df.groupby('Department')['Experience'].mean()
print(grouping)"""