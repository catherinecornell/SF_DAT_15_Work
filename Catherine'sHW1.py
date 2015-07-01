'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 7/1/2015
'''
import sys    
reload(sys)  
sys.setdefaultencoding('utf8')

import pandas as pd
# pd.set_option('max_colwidth', 50)
# set this if you need to

killings = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_15/master/hw/data/police-killings.csv')
killings.head()
killings.describe()

# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race

killings.rename(columns={'lawenforcementagency':'agency', 'raceethnicity':'race'}, inplace=True)

    

# 2. Show the count of missing values in each column
killings.isnull().sum() 

# 3. replace each null value in the dataframe with the string "Unknown"
killings.fillna(value= "Unknown")
# 4. How many killings were there so far in 2015?
killings[killings.year==2015]  #         467
# 5. Of all killings, how many were male and how many female?
killings[killings.gender=="Female"] # 22 Female
killings[killings.gender=="Male"] # 445 Male 
# 6. How many killings were of unarmed people?
killings[killings.armed=="No"]

# 7. What percentage of all killings were unarmed?
killings[killings.armed=="No"].value_counts() / killings.shape[0] 


# 8. What are the 5 states with the most killings?
killings.state.value_counts()
#CA    74
#TX    46
#FL    29
#AZ    25
#OK    22

# 9. Show a value counts of deaths for each race
killings.race.value_counts()

#White                     236 
#Black                     135
#Hispanic/Latino            67
#Unknown                    15
#Asian/Pacific Islander     10
#Native American             4



# 10. Display a histogram of ages of all killings
killings.age.sort_index().plot(kind='hist')


# 11. Show 6 histograms of ages by race
killings.age.hist(by=killings.race, sharex=True, sharey=True)


# 12. What is the average age of death by race?
killings.groupby('race').age.mean()

# 13. Show a bar chart with counts of deaths every month
killings.month.value_counts().plot(kind='bar')



###################
### Less Morbid ###
###################

majors = pd.read_csv('/Users/ccornell/Documents/GA/SF_DAT_15/hw/data/college-majors.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)
del majors['Major_code']
del majors["Employed_full_time_year_round"]
majors

# 2. Show the cout of missing values in each column
majors.isnull().sum() 

# 3. What are the top 10 highest paying majors?
majors[['Major', 'Median']].sort_index(by='Median', ascending = False).head(10)

###     Major  Median
#59                               PETROLEUM ENGINEERING  125000
#154  PHARMACY PHARMACEUTICAL SCIENCES AND ADMINISTR...  106000
#57           NAVAL ARCHITECTURE AND MARINE ENGINEERING   97000
#55                           METALLURGICAL ENGINEERING   96000
#58                                 NUCLEAR ENGINEERING   95000
#56                      MINING AND MINERAL ENGINEERING   92000
#97                    MATHEMATICS AND COMPUTER SCIENCE   92000
#48                              ELECTRICAL ENGINEERING   88000
#45                                CHEMICAL ENGINEERING   86000
#51              GEOLOGICAL AND GEOPHYSICAL ENGINEERING   85000
###


# 4. Plot the data from the last question in a bar chart, include proper title, and labels!
majors[['Major', 'Median']].sort_index(by='Median', ascending = False).head(10).plot(x='Major', y='Median', title='Top Ten Median Salaries by Major', kind='bar')

# 5. What is the average median salary for each major category?
 majors.groupby('Major_category', as_index=False).Median.mean().sort_index(by='Median')



# 6. Show only the top 5 paying major categories
 majors.groupby('Major_category', as_index=False).Median.mean().sort_index(by='Median', ascending = False).head(5)
 
 
            #Major_category     Median
#7               Engineering  77758.621
#5   Computers & Mathematics  66272.727
#13        Physical Sciences  62400.000
#3                  Business  60615.385
#8                    Health  56458.333
 
 
# 7. Plot a histogram of the distribution of median salaries
 majors.Median.plot(kind='hist')
 

# 8. Create a bar chart showing average median salaries for each major_category
 majors.groupby('Major_category', as_index=False).Median.mean().sort_index(by='Median').plot(x='Major_category', y='Median', kind='bar')

# 9. What are the top 10 most UNemployed majors?
majors[['Major', 'Unemployed']].sort_index(by='Unemployed', ascending = False).head(10)

 #Major  Unemployed
#161  BUSINESS MANAGEMENT AND ADMINISTRATION      147261
#158                        GENERAL BUSINESS       85626
#114                              PSYCHOLOGY       79066
#159                              ACCOUNTING       75379
#13                           COMMUNICATIONS       54390
#73          ENGLISH LANGUAGE AND LITERATURE       52248
#164        MARKETING AND MARKETING RESEARCH       51839
#132        POLITICAL SCIENCE AND GOVERNMENT       40376
#25                        GENERAL EDUCATION       38742
#78                                  BIOLOGY       36757



# What are the unemployment rates?
majors[['Major', 'Unemployment_rate', 'Unemployed']].sort_index(by='Unemployed', ascending = False).head(10)
#                                     Major  Unemployment_rate  Unemployed
#161  BUSINESS MANAGEMENT AND ADMINISTRATION              0.059      147261
#158                        GENERAL BUSINESS              0.051       85626
#114                              PSYCHOLOGY              0.070       79066
#159                              ACCOUNTING              0.053       75379
#13                           COMMUNICATIONS              0.064       54390
#73          ENGLISH LANGUAGE AND LITERATURE              0.069       52248
#164        MARKETING AND MARKETING RESEARCH              0.055       51839
#132        POLITICAL SCIENCE AND GOVERNMENT              0.069       40376
#25                        GENERAL EDUCATION              0.044       38742
#78                                  BIOLOGY              0.059       36757


# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category
# What are the unemployment rates?
majors.groupby('Major_category', as_index=False).Unemployed.mean().sort_index(by='Unemployed', ascending = False).head(10)

###
#Major_category  Unemployed
#3                      Business   33415.154
#4   Communications & Journalism   25299.750
#15               Social Science   14683.333
#1                          Arts   13015.625
#9     Humanities & Liberal Arts   11942.400
#14     Psychology & Social Work   11578.444
#12          Law & Public Policy    8609.800
#6                     Education    7833.500
#5       Computers & Mathematics    7270.364
#8                        Health    6251.083


# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042
majors['sample_employment_rate'] = majors.Employed/majors.Total

majors.head(5)



# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"
majors['sample_employment_rate'] = majors.Employed/majors.Total

majors.head(5)