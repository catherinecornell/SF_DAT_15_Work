##### Part 1 #####

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import statsmodels.formula.api as smf

# 1. read in the yelp dataset
yelp = pd.read_csv('/Users/ccornell/Documents/GA/SF_DAT_15/hw/data/yelp.csv')
yelp.head()

# 2. Perform a linear regression using 
# "stars" as your response and 
# "cool", "useful", and "funny" as predictors
feature_cols = ['cool', 'useful', 'funny']
X = yelp[feature_cols]
y = yelp.stars
X_train, X_test, y_train, y_test = train_test_split(X,y)

linreg = LinearRegression()
linreg.fit(X_train, y_train)


print linreg.intercept_
print linreg.coef_

# 3. Show your MAE, R_Squared and RMSE
#mae:
y_pred=linreg.predict(X_test)
print metrics.mean_absolute_error(y_test, y_pred)
#r_squared:
metrics.r2_score(y_test, y_pred)
#rmse:
print np.sqrt(metrics.mean_squared_error(y_test, y_pred))


# 4. Use statsmodels to show your pvalues
# for each of the three predictors
# Using a .05 confidence level, 
# Should we eliminate any of the three?
lm = smf.ols(formula='stars ~ cool + useful + funny', data=yelp).fit()
print lm.pvalues
lm.conf_int()

# 5. Create a new column called "good_rating"
# this could column should be True iff stars is 4 or 5
# and False iff stars is below 4

yelp['good_rating'] = (yelp['stars'] >= 4).astype(bool)
yelp.good_rating.head(20)



# 6. Perform a Logistic Regression using 
# "good_rating" as your response and the same
# three predictors
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
feature_cols = ['cool', 'useful', 'funny']
X = yelp[feature_cols]
y = yelp.good_rating
X_train, X_test, y_train, y_test = train_test_split(X,y)
logreg.fit(X_train, y_train)
assorted_pred_class = logreg.predict(X_test)



# 7. Show your Accuracy, Sensitivity, Specificity
# and Confusion Matrix

from sklearn import metrics
preds = logreg.predict(X_test)
print metrics.confusion_matrix(y_test, assorted_pred_class)

#Accuracy    = (60+1692)/2500  == .7008
#Sensitivity = 1692/(32+1692) == .981
#Specificity =  60/(60+716)  == .0773


# 8. Perform one NEW operation of your 
# choosing to try to boost your metrics!
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
feature_cols = ['cool', 'useful', 'funny']
X = yelp[feature_cols]
y = yelp.good_rating
logreg.fit(X_train, y_train)
assorted_pred_class = logreg.predict(X_train)




##### Part 2 ######

# 1. Read in the titanic data set.

titanic = pd.read_csv('/Users/ccornell/Documents/GA/SF_DAT_15/hw/data/titanic.csv')
titanic.head()


# 4. Create a new column called "wife" that is True
# if the name of the person contains Mrs.
# AND their SibSp is at least 1

titanic.wife=[(titanic.Sex=='female') & (titanic.SibSp==1)]



# 5. What is the average age of a male and
# the average age of a female on board?
titanic.Age[titanic.Sex=='male'].mean()
#30.73
titanic.Age[titanic.Sex=='female'].mean()
#27.91


# 5. Fill in missing MALE age values with the
# average age of the remaining MALE ages
titanic.Age[titanic.Sex=='male'].fillna(value='30.73')


# 6. Fill in missing FEMALE age values with the
# average age of the remaining FEMALE ages
titanic.Age[titanic.Sex=='female'].fillna(value='27.91')



# 7. Perform a Logistic Regression using
# Survived as your response and age, wife
# as predictors
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
feature_cols = ['Age', 'wife']
X = titanic[feature_cols]
y = titanic.Survived
X_train, X_test, y_train, y_test = train_test_split(X,y)
logreg.fit(X_train, y_train)
assorted_pred_class = logreg.predict(X_test)


# 8. Show Accuracy, Sensitivity, Specificity and 
# Confusion matrix

from sklearn import metrics
preds = logreg.predict(X_test)
print metrics.confusion_matrix(y_test, assorted_pred_class)



# 9. now use ANY of your variables as predictors
# Still using survived as a response to boost metrics!
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
feature_cols = ['Fare', 'Pclass']
X = titanic[feature_cols]
y = titanic.Survived
X_train, X_test, y_train, y_test = train_test_split(X,y)
logreg.fit(X_train, y_train)
assorted_pred_class = logreg.predict(X_test)





# 10. Show Accuracy, Sensitivity, Specificity

from sklearn import metrics
preds = logreg.predict(X_test)
print metrics.confusion_matrix(y_test, assorted_pred_class)



# REMEMBER TO USE
# TRAIN TEST SPLIT AND CROSS VALIDATION
# FOR ALL METRIC EVALUATION!!!!

