#part 1
import pandas as pd
df = pd.read_csv('data/survey_results_public.csv')
df.tail(10)
df.shape
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# part 2
df['email']
df.email
df[['last', 'email']]
df.iloc[[0, 1], 2]
df.loc[[0, 1], ['email', 'last']]


df.columns
df['Hobbyist']
df.loc[0:2, 'Hobbyist':'Employment']

#part 3
df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column'
schema_df.sort_index(inplace=True)

df.reset_index(inplace=True)

#part 4
filt = (df['last'] == 'Schafer') | (df['first'] == 'John')
df.loc[~filt, 'email']

filt = df['LanguageWorkedWith'].str.contains('Python', na=False)
df.loc[filt]

#part 5
df.columns
df.columns = ['first_name', 'last_name', 'email'] #to reaname name of all columns
df.columns = [x.lower() for x in df.columns] #to convert all columns using list comprehension
df.rename(columns={'first_name': 'first', 'last_name': 'last'}, inplace=True) #to rename specific rows

df.loc[2] = ['John', 'Smith', 'JohnSmith@email.com'] #to rename all columns in a row
df.loc[2, ['last', 'email']] = ['Doe', 'JohnDoe@email.com'] #to rename specific columns of a row
df.loc[2, 'last'] = 'Smith'
df.at[2, 'last'] = 'Doe' # we can make use of 'at' method to change value of single column in a row

filt = (df['email'] == 'JohnDoe@email.com') # if we want to change rows based on filter
df.loc[filt, 'last'] = 'Smith'

df['email'] = df['email'].str.lower()

df['email'].apply(len) #using apply on a series

def update_email(email):
    return email.upper()
df['email'].apply(update_email)#using function to apply on a series
df['email'] = df['email'].apply(update_email)

df['email'] = df['email'].apply(lambda x: x.lower()) #performing same using lambda function

df.apply(len, axis='columns') #using apply on dataframe
df.apply(pd.Series.min)
df.apply(lambda x: x.min())

df.applymap(len) #apply len on all elements in the data frame
df.applymap(str.lower) #this will work only if all values are strings

df['first'].map({'Corey': 'Chris', 'Jane': 'Mary'})#using map to replace values in a row
df['first'] = df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'})

df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)#using rename to convert the values
df['Hobbyist'].map({'Yes': True, 'No': False})
df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No': False})

#part 6
df['first'] + ' ' + df['last']
df['full_name'] = df['first'] + ' ' + df['last']
df.drop(columns=['first', 'last'], inplace=True)
df['full_name'].str.split(' ', expand=True)
df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)
df.append({'first': 'Tony'}, ignore_index=True)
df.append(df2, ignore_index=True, sort=False)
df = df.append(df2, ignore_index=True, sort=False)

df.drop(index=4)
filt = (df['last'] == 'Doe')
df.drop(index=df[filt].index)
