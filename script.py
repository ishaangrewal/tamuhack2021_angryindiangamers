import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# get csv file
df = pd.read_csv("https://raw.githubusercontent.com/ishaangrewal/tamuhack2021_angryindiangamers/main/datasets/cardio_train.csv", sep=';')

# drop id column
df = df.drop(["id"], axis=1)

# get age in terms of years
df['age'] = df['age']/365

# get x and y values
x = df.drop(["cardio"], axis=1)
y = df["cardio"]

corr = x.corr()
#sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True)


# split data
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state=0)

# regression model
rf = RandomForestRegressor(n_estimators=100, random_state=0)
rf.fit(x_train, y_train)
print("Regression Model Complete")

# predict test data
predictions = rf.predict(x_test)
print("Regression Prediction Complete")

# spit results into w/ cardio disease and w/o cardio disease
results = pd.DataFrame()
results['Actual'] = y_test
results['Prediction'] = predictions
results_0 = results[results['Actual'] == 0]
size_0 = len(results_0.index)
results_1 = results[results['Actual'] == 1]
size_1 = len(results_1.index)


# initialize subplots
fig, ((ax1), (ax2)) = plt.subplots(1, 2, figsize=(20, 10))

fig.suptitle("Distribution of Cardiovascular Disease Predictions")

# Plot 1 for patients without cardio disease
ax1.set_title("Distribution of Predictions for Patients w/o Cardiovascular Disease")
ax1.set_xlabel("Predicted Chance of Cardiovascular Disease")
ax1.set_ylabel("Relative Frequency")
ax1.set_xlim(0, 1)
counts_0, bins_0 = np.histogram(results_0["Prediction"], bins=20)
counts_0 = counts_0 / size_0
ax1.hist(bins_0[:-1], bins_0, weights=counts_0, color='green', edgecolor='black', linewidth=1.2)

# Plot 2 for patients with cardio disease
ax2.set_title("Distribuution of Predictions for Patients w/ Cardiovascular Disease")
ax2.set_xlabel("Predicted Chance of Cardiovascular Disease")
ax2.set_ylabel("Relative Frequency")
ax2.set_xlim(0, 1)
counts_1, bins_1 = np.histogram(results_1["Prediction"], bins=20)
counts_1 = counts_1 / size_1
ax2.hist(bins_1[:-1], bins=bins_1, weights=counts_1, color='red', edgecolor='black', linewidth=1.2)


plt.show()





