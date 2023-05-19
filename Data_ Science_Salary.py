#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv('ds_salaries.csv')
df.head()


# In[3]:


df.shape


# In[4]:


df.isna().sum()


# In[5]:


# Count the number of duplicate entries
print("Number of duplicate entries: ", df.duplicated().sum())


# In[6]:


# Drop the duplicate entries
df = df.drop_duplicates()


# In[7]:


# Count the number of duplicate entries after dropping
print("Number of duplicate entries after dropping: ", df.duplicated().sum())


# In[8]:


df.columns


# In[9]:


df['work_year'].value_counts()


# In[10]:


df['experience_level'].value_counts()


# In[11]:


df['employment_type'].value_counts()


# In[12]:


df['job_title'].value_counts()


# In[13]:


df['salary_currency'].value_counts()


# In[14]:


df['employee_residence'].value_counts()


# In[15]:


df['company_location'].value_counts()


# In[16]:


df['remote_ratio'].value_counts()


# In[17]:


df['company_size'].value_counts()


# In[18]:


plt.figure(figsize=(30,20))
# Select the top 10 job titles based on salary
top_jobs = df.groupby('job_title')['salary_in_usd'].mean().nlargest(10)

# Create a bar plot
plt.bar(top_jobs.index, top_jobs.values)

# Add labels and title
plt.xlabel('Job Title')
plt.ylabel('Average Salary (in USD)')
plt.title('Top 10 Job Titles by Salary')

# Display the plot
plt.show()


# In[19]:


#plt.figure(figsize=(30,20))
# Select the top 10 job titles based on salary
top_location = df.groupby('company_location')['salary_in_usd'].mean().nlargest(10)

# Create a bar plot
plt.bar(top_location.index, top_location.values)

# Add labels and title
plt.xlabel('Company Location')
plt.ylabel('Average Salary (in USD)')
plt.title('Top 10 salary by Company Location')

# Display the plot
plt.show()


# In[20]:


# Group by work year and calculate the mean salary
year_salaries = df.groupby('work_year')['salary_in_usd'].mean()

# Create a line plot
plt.figure(figsize=(10,6))
plt.plot(year_salaries.index, year_salaries.values)
plt.xlabel('Work Year')
plt.ylabel('Average Salary in USD')
plt.title('Average Salary by Work Year')
plt.show()


# In[21]:


df_ft = df[df['employment_type'] == 'FT']
title_salaries = df_ft.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)[:10]

plt.figure(figsize=(10,6))
title_salaries.plot(kind='bar')
plt.xlabel('Job Title')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salaries for Top 10 Job Titles in FT Employment Type')
plt.show()


# In[22]:


df_ft = df[df['employee_residence'] == 'IN']
title_salaries = df_ft.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)[:10]

plt.figure(figsize=(10,6))
title_salaries.plot(kind='bar')
plt.xlabel('Job Title')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salaries in India for Job titles')
plt.show()


# In[23]:


df_ft = df[df['employee_residence'] == 'US']
title_salaries = df_ft.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)[:10]

plt.figure(figsize=(10,6))
title_salaries.plot(kind='bar')
plt.xlabel('Job Title')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salaries in USA for Job titles')
plt.show()


# In[24]:


# Filter the dataset to include only Principal Data Scientists
df_pds = df[df['job_title'] == 'Principal Data Scientist']

# Group the dataset by work year and calculate the mean salary
yearly_salary = df_pds.groupby('work_year')['salary_in_usd'].mean()

# Create a line plot
plt.figure(figsize=(10,6))
yearly_salary.plot(kind='line')
plt.xlabel('Work Year')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salary of Principal Data Scientists by Work Year')
plt.show()


# In[25]:


df_ds = df[df['job_title'] == 'Data Scientist']

# Group the dataset by work year and calculate the mean salary
yearly_salary = df_ds.groupby('work_year')['salary_in_usd'].mean()

# Create a line plot
plt.figure(figsize=(10,6))
yearly_salary.plot(kind='line')
plt.xlabel('Work Year')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salary of Data Scientist by Work Year')
plt.show()


# In[26]:


# Filter the dataset to include only Principal Data Scientists
df_da = df[df['job_title'] == 'Data Analyst']

# Group the dataset by work year and calculate the mean salary
yearly_salary = df_da.groupby('work_year')['salary_in_usd'].mean()

# Create a line plot
plt.figure(figsize=(10,6))
yearly_salary.plot(kind='line')
plt.xlabel('Work Year')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salary of Data Analyst by Work Year')
plt.show()


# In[27]:


df_dds = df[df['job_title'] == 'Director of Data Science']

# Group the dataset by work year and calculate the mean salary
yearly_salary = df_dds.groupby('work_year')['salary_in_usd'].mean()

# Create a line plot
plt.figure(figsize=(10,6))
yearly_salary.plot(kind='line')
plt.xlabel('Work Year')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salary of Director of Data Science by Work Year')
plt.show()


# In[28]:


df_dst = df[df['job_title'] == 'Applied Data Scientist']

# Group the dataset by work year and calculate the mean salary
yearly_salary = df_dst.groupby('work_year')['salary_in_usd'].mean()

# Create a line plot
plt.figure(figsize=(10,6))
yearly_salary.plot(kind='line')
plt.xlabel('Work Year')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salary of Applied Data Scientist by Work Year')
plt.show()


# In[29]:


df_dst = df[df['job_title'] == 'Head of Data Science']

# Group the dataset by work year and calculate the mean salary
yearly_salary = df_dst.groupby('work_year')['salary_in_usd'].mean()

# Create a line plot
plt.figure(figsize=(10,6))
yearly_salary.plot(kind='line')
plt.xlabel('Work Year')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salary of Head of Data Science by Work Year')
plt.show()


# In[30]:


df_hd = df[df['job_title'] == 'Head of Data']

# Group the dataset by work year and calculate the mean salary
yearly_salary = df_hd.groupby('work_year')['salary_in_usd'].mean()

# Create a line plot
plt.figure(figsize=(10,6))
yearly_salary.plot(kind='line')
plt.xlabel('Work Year')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salary of Head of Data by Work Year')
plt.show()


# In[31]:


df_ft_ds = df[(df['employment_type'] == 'FT') & (df['job_title'] == 'Data Scientist')]

# Group the dataset by work year and calculate the mean salary
yearly_salary = df_ft_ds.groupby('work_year')['salary_in_usd'].mean()

# Create a line plot
plt.figure(figsize=(10,6))
yearly_salary.plot(kind='line')
plt.xlabel('Work Year')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salary of Data Scientists (Employed Full Time) by Work Year')
plt.show()


# In[32]:


df_pt_ds = df[(df['employment_type'] == 'PT') & (df['job_title'] == 'Data Scientist')]

# Group the dataset by work year and calculate the mean salary
yearly_salary = df_pt_ds.groupby('work_year')['salary_in_usd'].mean()

# Create a line plot
plt.figure(figsize=(10,6))
yearly_salary.plot(kind='line')
plt.xlabel('Work Year')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salary of Data Scientists (Employed Part Time) by Work Year')
plt.show()


# In[33]:


df_ft_ads = df[(df['employment_type'] == 'FT') & (df['job_title'] == 'Applied Data Scientist')]

# Group the dataset by work year and calculate the mean salary
yearly_salary = df_ft_ads.groupby('work_year')['salary_in_usd'].mean()

# Create a line plot
plt.figure(figsize=(10,6))
yearly_salary.plot(kind='line')
plt.xlabel('Work Year')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salary of Data Scientists (Employed Full Time) by Work Year')
plt.show()


# In[35]:


df_filtered = df[(df['company_location'] == 'IN') & (df['work_year'] == 2023)]
plt.figure(figsize=(10, 6))
plt.hist(df_filtered['salary_in_usd'], bins=20)
plt.xlabel('Salary in USD')
plt.ylabel('Frequency')
plt.title('Salary Distribution for Company Location India (Year 2023)')
plt.show()


# In[37]:


df_filtered = df[(df['company_location'] == 'IN') & (df['work_year'] == 2023)]

title_salaries = df_filtered.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)

plt.figure(figsize=(15, 10))
title_salaries.plot(kind='line')
plt.xlabel('Job Title')
plt.ylabel('Mean Salary in USD')
plt.title('Mean Salary for Company Location India (Year 2023) by Job Title')
plt.show()


# In[ ]:




